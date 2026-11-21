# PamPam components

Public marketing site and published maps, captured 2026-11-21, signed out. Crops are 2x element screenshots. Values are token names. A state that was not reached is listed under Gaps.

## Button

Primary plan action. Fill `light.accent.default`, text `light.text.onAccent`, border `light.border.accent`, radius `core.radius.control.button` (12px), height `core.size.button` (64px), shadow `core.shadow.button`.

| State | Crop |
|---|---|
| default | [button-primary-default.png](components/crops/button-primary-default.png) |
| hover | [button-primary-hover.png](components/crops/button-primary-hover.png) |
| focus-visible | not captured. Keyboard focus was not landed on the div control |
| pressed | not captured |
| disabled | not present as a disabled attribute. The print wizard's Next control paints grey until a place is chosen; that state was not measured |

Quiet plan action. Fill `light.background.quiet`, text `light.text.disabled`, hairline `light.border.default`.

| State | Crop |
|---|---|
| default | [button-quiet-default.png](components/crops/button-quiet-default.png) |

Make map. Black fill, white label, about 40px tall. Clicking it opens the login dialog. Google was not clicked.

| State | Crop |
|---|---|
| default | [button-make-map-default.png](components/crops/button-make-map-default.png) |

## Link

Nav link. Colour `light.text.muted`, 16px / 24px, weight 550, padding 8px 12px. Hover on Pricing did not change the computed colour.

| State | Crop |
|---|---|
| default | [link-nav-default.png](components/crops/link-nav-default.png) |
| hover | [link-nav-hover.png](components/crops/link-nav-hover.png) |
| focus-visible | not captured as a crop. Computed outline on the Pricing link was `rgb(0, 95, 204) auto 1px`, the browser default (`light.focus.ring`) |

## Text field

Explore search. Placeholder "Search map". Height about 36px, pill radius. Typed "park" and did not submit.

| State | Crop |
|---|---|
| default | [text-field-search-default.png](components/crops/text-field-search-default.png) |
| filled | [text-field-search-filled.png](components/crops/text-field-search-filled.png) |

The print wizard field ("Neighborhood, district, or business area") is a second field. It was not filled.

## Menu

Solutions menu. White panel, 6px radius, shadow `core.shadow.menu`. Items are 40px, colour `light.text.menu`.

| State | Crop |
|---|---|
| open | [menu-solutions-default.png](components/crops/menu-solutions-default.png) |
| item hover | [menu-item-hover.png](components/crops/menu-item-hover.png) |

Products opens the same kind of menu. See [home-light-products-menu.png](screenshots/home-light-products-menu.png).

## Dialog

Login dialog from Make map. White panel, about 375px wide. One action: Login with Google. Not clicked. Close control returns to the page.

| State | Crop |
|---|---|
| default | [dialog-login-default.png](components/crops/dialog-login-default.png) |

Page form of the same wall: [login-light-default.png](screenshots/login-light-default.png).

## Card

Pricing plan card. Fill `light.background.surface`, radius 16px, padding 24px. The crop is the full Free column, not a tight card.

| State | Crop |
|---|---|
| default | [card-plan-default.png](components/crops/card-plan-default.png) |

## Switch

Pricing "Pay monthly / Pay yearly" is a pill toggle on [pricing-light-default.png](screenshots/pricing-light-default.png). A yearly state was on screen. The monthly state was clicked and the URL stayed `/pricing`. No crop of the pill was saved.

## Not present on the public surface

Text area, select, checkbox, radio, tabs, tooltip, toast, table, avatar, badge. Icon buttons exist (zoom +/−, dialog close, prompt star) and were not cropped. FAQ rows expand on the home page; the open state was not cropped.

## Gaps

- Signed-in map editor, account, billing and onboarding stop at Google sign-in.
- Hover and pressed colours of the primary button were not re-read from CSS. The hover crop exists; a colour change is not claimed.
- Focus-visible crops were not saved. The one computed focus outline is the browser default.
- Disabled, loading and error states of fields were not reached. No form was submitted.
- Dark theme is not present. The stylesheet has no `data-theme` and no `prefers-color-scheme` rule.
- 242 geo template pages and most blog posts share the marketing shell. One of each family was captured.
- Filter on a published map was not opened.
- The list-row crop missed the card and was deleted.
