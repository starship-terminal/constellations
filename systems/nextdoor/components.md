# Components

Measured on the signed-out pages of nextdoor.com on 2026-11-19. Values are computed styles unless the row says declared.

## Button

The painted face is an inner `div`, not the `button`. The button itself is transparent.

| Variant | Where | Fill | Text | Height | Radius | Padding |
|---|---|---|---|---|---|---|
| Brand, large | Continue, Sign up, Join Nextdoor | `#1B8751` | `#FFFFFF` | 48px | 10000px | 8px 24px |
| Neutral, large | Log in, Continue with Google, Continue with Apple | `#F0F2F5` | `#232F46` | 48px | 10000px | 8px 24px |
| Neutral, medium | Partners, Businesses | transparent | `#232F46` | 40px | 10000px | 8px 16px |
| Brand, login submit | /login/ Log in | `#1B8751` | `#FFFFFF` | 48px | 10000px | 8px 24px, 14px type |

Weight on every measured button is 420. Focus outline on the brand face is `solid 3px #FFFFFF`. Focus outline on the neutral face is `solid 3px #232F46`. Hover is a declared 8% wash of `#232F46`, not a computed colour. Disabled was not computed.

## Link

Primary links (Privacy Policy) are 14px / 18px, weight 420, `#232F46`. Hover declares a 2px underline. Secondary footer links (About) are 14px / 18px, weight 620, `#576580`, and hover declares an underline.

## Text field

Email and password on the homepage and on /login/: height 56px, radius 12px, 16px type, weight 420, transparent fill. Rest ring `inset 0 0 0 1px #CAD3E5`. Focus ring `inset 0 0 0 2px #232F46`, matching the declared `.Textfield__w16k37c:focus` rule. Error focus is declared as `inset 0 0 0 2px var(--nd-color-staticRed)` (`#ED353B`) and was not triggered.

## Card

The signup card is white, radius 12px, padding 24px, width 400px at 1169 and 326px at 390.

## Badge

`--nd-component-badge-neutral-bg` computed to `#CAD3E5`. No badge was painted on the pages visited.

## Gaps

- Address and neighborhood verification. Not entered.
- Signup and login. Forms were not submitted.
- Dark theme. Declared, not painted.
- Hover, pressed and disabled colours. Declared or unseen.
- Text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, list row, table, avatar. Not on the public pages.
- Screenshots and crops. The preview browser returned no frames.
- Icons. Not extracted.
