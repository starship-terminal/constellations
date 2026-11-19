# Components

Public signed-out Time2book, measured 2026-11-19. Crops are in [components/crops/](components/crops/). Values are token names from [tokens.json](tokens.json).

| Component | States captured | Tokens |
|---|---|---|
| Button, primary | default, hover, focus | `component.button-primary.*`, height `size.cta` (48px) or `size.nav-control` (38px) |
| Button, secondary | default (Log in) | `component.button-secondary.bg` is `rgba(23, 23, 23, 0.05)` |
| Button, OAuth | default | same fill as secondary, radius `radius.control` (12px), height `size.auth-button` (42px) |
| Link, nav | default | `typography.nav`, colour `color.text.primary` |
| Text field | default, focus | `component.field.*`. Focus border is `color.border.focus` |
| Segmented control | Monthly selected, Yearly selected | track `rgba(23, 23, 23, 0.05)`, thumb white, shadow `shadow.segment` |
| Card | pricing plan, solution photo card | radius `radius.card` (16px), padding `spacing.24` |
| Promo bar | default | fill `color.accent.default`, text `color.text.on-accent`, 14px |
| Table | pricing comparison, default | 36 rows. Header weight 500. Cell borders were not a painted 1px on the sampled cells. |
| Logo | default | `/images/time2book-logo.svg`, 112 by 20 |

## Gaps

- Pressed, disabled, loading and error were not shown on the public pages.
- Hover on the primary pill did not change the computed fill in the crop. The class lists no hover background for that link.
- Focus on the marketing CTA used the browser outline (`oklab(0.708 0 0 / 0.5) auto 1px`). The login field focus is a 50% ink border, not a ring.
- Checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, avatar and badge were not on the signed-out pages. The cookie banner is Osano, not the product.
- Icon button (search, 36px) was in the DOM with height 0 in the first read because a video close control matched the selector. The nav search glyph is 20px. A dedicated crop was not taken.
- Dark component states were not captured. `.dark` is declared and unused on these pages.
