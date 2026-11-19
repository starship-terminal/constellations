# Components

Measured on the public signed-out surfaces on 2026-11-19, at 1440 by 900. Crops are in [components/crops/](components/crops/). Values are token names from [tokens.json](tokens.json).

## Button

The marketing primary is white on ink, 32px tall, 13px semibold, radius `core.radius.button`.

| State | Fill | Text | Evidence |
|---|---|---|---|
| default | `dark.color.button-primary` | `dark.color.button-primary-text` | [button-primary-default.png](components/crops/button-primary-default.png) |
| hover | `dark.color.button-primary-hover` | `dark.color.button-primary-text` | [button-primary-hover.png](components/crops/button-primary-hover.png) |
| focus-visible | same as hover, plus outline `dark.color.focus` | | computed on `.mwm-product-start` |

The secondary action, "Open MWM Console", uses `dark.color.nav-hover` at 10% white. Hover did not change the fill. Crop: [button-secondary-default.png](components/crops/button-secondary-default.png).

The pricing call to action is the same white fill at 44px and 16px semibold. Crop: [plan-cta-default.png](components/crops/plan-cta-default.png).

Console's "Sign In" uses `#f2f2f2` and lightens to white on hover. That fill is not a marketing token. See [console-sign-in-dark-email.png](screenshots/console-sign-in-dark-email.png).

## Nav item

13px regular, padding 0 12px, height 32px, radius 8px. Resting fill is transparent. Hover and the open Products item use `dark.color.nav-hover`. Focus-visible adds the `dark.color.focus` outline. Crops: [nav-item-default.png](components/crops/nav-item-default.png), [nav-item-hover.png](components/crops/nav-item-hover.png).

## Badge

"MOST POPULAR" is `dark.color.orange` on white text, 14px bold, padding 5px 10px, radius `core.radius.pill`. Crop: [badge-default.png](components/crops/badge-default.png).

The plan tier pill ("PRO") is `dark.color.chip` with `dark.color.muted` text.

## Text field

The home prompt field is a borderless textarea, 16px, letter-spacing -0.32px, inside the prompt card. Crop: [text-field-default.png](components/crops/text-field-default.png).

Console's email field is 16px on `dark.color.surface`, 1px `dark.color.control` border, radius `core.radius.field`, height 43px. Focus sets the border and a 2px outline to `dark.console.focus-ring`. The field was typed into and cleared. It was not submitted.

## Prompt card

`.mwm-prompt` is `dark.color.surface`, 1px `dark.color.prompt-border`, radius `core.radius.card`, shadow `core.shadow.prompt`. Crop: [prompt-default.png](components/crops/prompt-default.png).

Chips inside it are 40px tall, radius 8px, fill `dark.color.chip`, 14px medium. Crop: [chip-default.png](components/crops/chip-default.png). Focus-visible draws a 2px ring at 18% white.

## Icon button

The prompt's add and voice buttons are 40px squares, radius 8px, fill `dark.color.chip`. Crop: [icon-button-default.png](components/crops/icon-button-default.png).

## Menu

The Products menu opens from the nav chevron. The open trigger uses `dark.color.nav-hover`. The panel itself is a full-width sheet under the top bar. Shot: [home-dark-products-menu.png](screenshots/home-dark-products-menu.png). The menu links were not followed.

## FAQ

A pricing question is a full-width button, 72px tall, 14px, with a hairline under it. Opening one reveals the answer and flips the chevron. Shot: [pricing-dark-faq-open.png](screenshots/pricing-dark-faq-open.png).

## Link

`.mwm-build-link` is 18px, letter-spacing -0.54px, white, with a trailing arrow. No underline at rest.

## Card

`.mwm-number-card` is `dark.color.page`, 1px `dark.color.card-border`, radius `core.radius.card`, about 313 by 340. The plan price well is `dark.color.surface`, radius 8px, padding 0 18px.

## Gaps

- Checkbox, radio, switch, select, tabs, tooltip, toast, table, avatar and list row do not appear on the captured public pages.
- The console password field and the "Forgot password?" control were visible. Forgot password was not opened.
- Create's provider buttons were measured and hovered. None was clicked.
- Disabled, loading, error and pressed states were not shown by these pages.
- The marketing site has no light theme. A `light` set exists in tokens.json and is empty.
