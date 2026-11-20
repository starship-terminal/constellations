# Components

Public controls measured on runey.app and runey.app/auth on 19 November 2026. Values are token names. The crops are 2x PNGs of the live controls.

| Component | States seen | Crop | Values |
|---|---|---|---|
| Button, primary | default, hover | [button-primary.png](components/crops/button-primary.png), [button-primary-hover.png](components/crops/button-primary-hover.png) | Face is a vertical gradient from `core.color.primary-light` to `core.color.primary`. Label `core.color.on-primary`, `core.typography.button`, height `core.spacing.11`, padding inline `core.spacing.8`, radius `core.radius.pill`. Shadow `core.shadow.primary`. Hover raises the filter to brightness(1.06) and uses `core.shadow.primary-hover`. |
| Button, secondary | default | [button-secondary.png](components/crops/button-secondary.png) | Face `core.color.page`, text `core.color.foreground`, 1px `core.color.border`, same height and radius as the primary. |
| Button, ghost | default | [button-ghost.png](components/crops/button-ghost.png) | Transparent face, text `core.color.foreground`, no border. Request demo. |
| Button, Google | default | [button-google.png](components/crops/button-google.png) | Face `core.color.google`, text `core.color.foreground`, 1px `core.color.border`, weight 500, height `core.spacing.11`. |
| Button, sign in | default | [button-signin.png](components/crops/button-signin.png) | Same gradient as the primary, full width of the form (356px at 1169). |
| Link, nav | default | [link-nav.png](components/crops/link-nav.png) | `core.typography.nav`, colour `core.color.muted`, padding `core.spacing.2` `core.spacing.4`, radius pill. Hover class is `hover:text-foreground` and `hover:bg-foreground/5`. The hover fill was not measured. |
| Chip | selected, default | [chip-selected.png](components/crops/chip-selected.png), [chip-default.png](components/crops/chip-default.png) | Selected face `core.color.foreground`, label `core.color.on-foreground`. Default face `core.color.card`, label `core.color.chip-text`, border `core.color.border-soft`. `core.typography.chip`, height 32px. |
| Billing toggle | yearly selected | [billing-toggle.png](components/crops/billing-toggle.png) | Track `core.color.wash`, padding `core.spacing.1`, radius pill. Selected segment matches the selected chip, plus `core.shadow.sm`. |
| Text field | empty, focus | [field-email.png](components/crops/field-email.png), [field-email-focus.png](components/crops/field-email-focus.png), [field-password.png](components/crops/field-password.png) | Face `core.color.field`, border 1px `core.color.border`, radius pill, height `core.spacing.11`, padding `core.spacing.3` `core.spacing.4`, type 14px. Focus ring `core.shadow.focus`. Placeholder colour was not read separately from the muted token. |
| Plan card | default | [card-plan.png](components/crops/card-plan.png) | Face `core.color.card`, border `core.color.border-soft`, radius `core.radius.card`, padding `core.spacing.8`. Name `core.typography.plan-name`. Price `core.typography.price`. |
| Quote card | default | [card-quote.png](components/crops/card-quote.png) | Face `core.color.card`, radius `core.radius.quote`, padding `core.spacing.9`, shadow `core.shadow.sm`. |
| FAQ | closed, open | [faq-closed.png](components/crops/faq-closed.png), [faq-open.png](components/crops/faq-open.png) | Face `core.color.card`, border `core.color.border-faint`, radius `core.radius.faq`, padding `core.spacing.5` `core.spacing.6`. |
| Auth card | sign in | [card-auth.png](components/crops/card-auth.png) | Face `core.color.auth-card`, radius `core.radius.card`, padding `core.spacing.10`, shadow `core.shadow.card`. Outer frame is `core.color.auth-frame` with radius `core.radius.quote`. |
| Cookie card | default | [home-light-cookie.png](../screenshots/home-light-cookie.png) | Face `core.color.card`, radius `core.radius.card`, padding `core.spacing.6`, shadow `core.shadow.cookie`. Accept all uses the primary gradient at 32px height and 12px type. Reject all uses the secondary face. |

## Gaps

- Pressed, disabled, loading and error were not on the page. The primary class declares `active:brightness-[0.96]` and `disabled:opacity-50`. Those were not computed.
- No checkbox, radio, switch, select, text area, toast, table, avatar or badge was on the public pages.
- The nav hover fill (`hover:bg-foreground/5`) was not measured.
- Tooltip, menu and dialog beyond the cookie card were not opened. Features is a button that opens a menu. That menu was not captured.
- The signed-in app shell, sidebar, invoices, projects and dashboard were not entered.
- Dark theme controls were not painted. The `.dark` custom properties are in [tokens.json](tokens.json) under `dark` and labelled declared.
