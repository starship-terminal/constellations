# Components

Values are token names where a token exists. Readings are in [raw/computed.json](raw/computed.json). No crops were saved: the preview browser did not produce screenshot frames.

## Button

Marketing `.button-n` uses `{light.background.action}` and `{light.text.on-action}`, radius `{core.radius.button}`, padding `{core.spacing.button-y}` `{core.spacing.button-x}`, weight 500.

The soft button `.button-n.is-lightgreen` uses `{light.background.action-soft}` and `{light.text.primary}`. The yellow button and the form submit use `{light.background.citrus}` and `{light.text.on-citrus}`. The icon button is 3.5rem tall and turns citrus on hover, with the label switching to moss.

The backoffice primary button computed `{light.background.app-action}`, text `{light.text.app-link}`, height 48px, radius `{core.radius.app-medium}`, padding inline `{core.spacing.app-large}`, weight 600.

## Link and text button

Nav links use `{core.typography.nav}` and `{light.text.primary}`. The pricing nav link has radius `{core.radius.nav-link}` and turns `{light.background.surface}` on hover.

The backoffice "Sign up now" and "Forgot password?" controls are text buttons: transparent, `{light.text.app-link}`, 14px, weight 600, radius `{core.radius.app-small}`.

## Text field

The marketing field `.field-form_link` is 38px tall, left padding 15px, radius 0, border none, colour `{light.text.primary}`. Focus draws a 3px outline in `{light.text.primary}`.

The backoffice field is 48px tall, radius `{core.radius.app-small}`, padding inline `{core.spacing.app-medium}`, border 1px `{light.border.app}`, background `{light.background.raised}`. Focus outline is 2px `{light.border.app-focus}`, offset -1px. The label is 12px `{light.text.app-secondary}`.

## Card

`.plan-card.starter` computed background `{light.background.surface}`, radius `{core.radius.plan}`, padding 18px, 227 by 483px.

The login card computed background `{light.background.raised}`, radius `{core.radius.app-card}`, padding `{core.spacing.app-xlarge}`, width 500px, shadow `{light.shadow.app-large}`.

## Language pill

The backoffice language control is a white pill, radius `{core.radius.pill}`, height 48px, border 1px `{light.border.app}`, shadow `0px 4px 16px rgba(0, 0, 0, 0.08)`. That shadow is not a named token. The small and medium shadow tokens were resolved and not used by this control.

## Gaps

- No component crop. `preview_snapshot` did not produce frames.
- Hover, pressed, disabled and error states were not forced on live controls. Hover colours that appear above come from stylesheet rules.
- Text area, select, radio, switch, tabs, menu, tooltip, dialog, toast, table and avatar were not measured as product components.
- The signup terms checkbox was present and not measured as its own control.
- Phone width was not captured.
