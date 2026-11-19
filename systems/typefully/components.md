# Components

Values are token names. Computed numbers are in [raw/components-computed.json](raw/components-computed.json). Crops are from the light marketing page.

## Button

Nav Sign up is `action.accent` on `text.on-accent`, radius `radius.lg`, height `size.nav-button`, type `typography.button-compact`. Log in is a ghost button in `text.muted` with a 0.5px border.

![Log in and Sign up](components/crops/button-nav-default.png)

Continue and the Business Get started button are the same accent fill, height `size.control`, type `typography.button`. Continue uses `radius.xl` (12px). The pricing primary uses `radius.lg` (9.6px).

![Continue](components/crops/button-primary-default.png)

OAuth pills (Google, X/Twitter, LinkedIn, Email) are height `size.oauth` (40px) and `radius.pill`. Light fill is white with `border.default`. Dark fill is `component.button-secondary-bg` (`#282B31`).

Hover, pressed, disabled and loading were not forced. Disabled is declared as opacity 0.5.

## Text field

The email field is white, 32px tall, padding 8px 12px, radius `radius.lg`, border `border.hairline`. Focus adds a 4px accent-at-20% shadow. Placeholder is `your@email.com`. The field was not submitted.

![Email field](components/crops/text-field-default.png)

## Dialog

The email dialog is a 450 by 330 card, padding 32px, radius `radius.big`, shadow `rgba(0, 0, 0, 0.08) 0px 6px 16px -2px, rgba(0, 0, 0, 0.1) 0px 16px 80px -8px`. The scrim is black at 20% in light.

![Email dialog](components/crops/dialog-email-default.png)

## Switch

The yearly billing control is a 24 by 16 pill, on fill `action.accent`, thumb 12px white. Off was not captured.

## Card

Feature cards are `component.card-bg` with a 1px `component.card-border` and `radius.xl`. Plan cards are white in light (surface in dark), 0.5px `border.default`, padding 20px, radius 12px.

## Link

Header and footer links are `typography.nav`, colour `text.primary`, no underline. Tweet handles in the demo use `text.link` and the twitter face.

## Gaps

- Icon button, select, checkbox, radio, tabs, menu, tooltip, toast, table, avatar and badge were not measured as product controls. The product demo shows avatars and chips. Those are demo content.
- Hover, pressed, disabled, loading and error were not forced.
- The dark email field and dark dialog were not opened.
- Inline SVGs were not extracted.
