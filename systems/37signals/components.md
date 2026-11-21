# Components

Public controls on 37signals.com, 2026-11-21. Crops are 1x cuts from the raw captures, then quantised.

| Component | State | Evidence |
|---|---|---|
| Link | Default, desktop nav | [link-nav-default.png](components/crops/link-nav-default.png). White, Lab Grotesque, weight 700, no underline until hover or focus |
| List row | Signal index | [list-row-signal-default.png](components/crops/list-row-signal-default.png). Number plus title, one link |
| Button | Quiet, on theme | [button-quiet-default.png](components/crops/button-quiet-default.png). White pill, theme-coloured label, radius 1.3em, height 36px |
| Button | Theme fill | [button-signup-default.png](components/crops/button-signup-default.png). `.button--theme`. Fill is the page colour, label is white |
| Text field | Empty | [text-field-email-empty.png](components/crops/text-field-email-empty.png). Lab Grotesque Mono, placeholder only, not typed |
| Signup panel | Empty | [signup-form-empty.png](components/crops/signup-form-empty.png) |

Not present on the public site: icon button, text area, select, radio, switch, tabs, tooltip, dialog, toast, avatar, badge, checkbox as a visible control. The nav checkbox is `display: none`.

Hover on a desktop nav link adds an underline. The jobs Sign up button did not change colour on hover in one reading (the page theme had already been randomised to a different swatch, so that shot was discarded). Focus on the email field computed no outline and no shadow.
