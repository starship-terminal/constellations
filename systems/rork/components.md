# Components

Public signed-out controls on rork.com, measured 19 November 2026. Values are token names. The crops are 2x.

## Button

Sign in, in the header. White pill, black label, 36px tall, padding `0 16px`, 14px medium.

| State | Crop | Fill | Text |
|---|---|---|---|
| Default | [button-primary-default.png](components/crops/button-primary-default.png) | `{dark.action.primary}` | `{dark.text.inverse}` |
| Hover | Same control, not a separate crop | `{dark.action.primary-hover}` | `{dark.text.inverse}` |
| Focus | Keyboard focus on the same control | `{dark.action.primary}` | ring `{dark.focus.ring}` at 2px |

Continue, Get Started, and Upgrade are the same white fill at radius `{core.radius.lg}` and 40px tall. [button-continue-default.png](components/crops/button-continue-default.png), [button-plan-default.png](components/crops/button-plan-default.png).

Pressed, disabled, and loading were not on screen.

## Link

Nav links are 16px, colour `{dark.text.secondary}`. App is a text gradient from `{dark.accent.gold-start}` to `{dark.accent.gold-end}`. Contact us is 12px, underlined, white at 40%.

## Text field

The email step field is 40px tall, radius `{core.radius.lg}`, padding `4px 12px`, border `{dark.border.subtle}`, fill white at 3%. Placeholder "Email address". [text-field-email-default.png](components/crops/text-field-email-default.png).

Focus draws a 1px `{dark.focus.ring}` ring. No error state was shown, because the form was not submitted.

The home composer is a contenteditable inside a `{dark.surface.card}` shell, radius `{core.radius.composer}`, 768 by 112. [text-field-composer-default.png](components/crops/text-field-composer-default.png).

## Chip

iPhone is selected: white 14px medium text, transparent fill, pill radius. Android is `{dark.text.muted}`. [chip-selected-default.png](components/crops/chip-selected-default.png).

## Dialog

The sign-in card is 448px wide, radius `{core.radius.dialog}`, fill `{dark.surface.raised}`, border `{dark.border.default}`, backdrop blur 24px. Overlay is `{dark.surface.overlay}`. [dialog-email-default.png](components/crops/dialog-email-default.png).

The pricing dialog is 1024 by 733, same radius and fill.

## Card

Free and Pro cards are 314px wide, radius `{core.radius.card}`, padding 20px, fill `{dark.surface.wash}`. Rork Max uses a left-to-right gradient from `{dark.accent.max-start}` to `{dark.accent.max-end}`. [card-max-default.png](components/crops/card-max-default.png).

Blog cards are 360 by 437, radius 16px, fill `#171717` at 60%, border `{dark.border.hairline}`.

## Accordion

FAQ questions are 14px medium, padding `16px 0`, full width of an 830px column. Opening one did not change the button's computed colour. [accordion-default.png](components/crops/accordion-default.png).

## Gaps

- Select, checkbox, radio, switch, tooltip, toast, table, avatar, and list row were not on these pages.
- The Products and Resources menus did not stay open long enough to measure.
- The 6-digit code step was not requested.
- Pressed, disabled, and loading were not shown.
- No light theme painted.
