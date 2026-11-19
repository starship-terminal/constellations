# Components

The 404 page at [https://tome.app/](https://tome.app/) on 2026-11-19. Token names point at [tokens.json](tokens.json).

## Heading

The page title, "This page doesn't exist".

| State | Crop | Values |
|---|---|---|
| default | [components/crops/error-heading-default.png](components/crops/error-heading-default.png) | `core.typography.heading` on `dark.text.primary` (light: `light.text.primary`). Letter-spacing -0.96px. No radius, no shadow |

## Body copy

"It may have been moved, removed, or never existed." `core.typography.body` in `dark.text.copy` (`#ffffff`). In light, copy and primary are the same `#171717`. Margin-top `core.spacing.8`. No separate crop: it sits under the heading in [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png).

## Status line

"404 DEPLOYMENT_NOT_FOUND", uppercase, `core.typography.meta` in `dark.text.secondary`. The request id under it uses the same style without the uppercase transform. Gap `core.spacing.4`.

## Primary button

A "Go back" button is in the DOM with the `hidden` attribute, so it is not painted. Computed values, not a crop: height `core.size.control-height`, padding `0 12px`, radius `core.radius.control`, background `dark.background.action`, text `dark.text.on-action`, type `core.typography.button`. The stylesheet sets hover to `dark.background.action-hover` and active to `scale(0.98)`. Those states were not shown.

## Secondary link

"View documentation", an anchor to the host's deployment-not-found docs. Uppercase mono, `core.typography.meta`, colour `dark.text.secondary`.

| State | Crop | Values |
|---|---|---|
| default | [components/crops/secondary-link-default.png](components/crops/secondary-link-default.png) | colour `dark.text.secondary`, no underline, transition colour 150ms |
| focus-visible | [components/crops/secondary-link-focus.png](components/crops/secondary-link-focus.png) | outline `dark.border.focus` 2px solid, offset 2px, radius 6px |
| hover | not cropped | stylesheet sets colour to `dark.text.primary` |

The sibling "Copy debug prompt" button uses the same secondary style. It was focused in the preview browser and drew the same 2px `#0070f3` outline. It was not clicked, so the copied state was not captured.

## Separator

A 6×10.39px mark between the two footer actions, colour `dark.border.divider`. Not extracted as its own SVG.

## Gaps

No text field, text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, card, list row, table, avatar, or badge. No product icon, wordmark, or illustration. The primary button's hover, active, and disabled states were not shown because the control is hidden.
