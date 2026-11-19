# Components

Signed-out marketing controls measured on [https://webflow.com/](https://webflow.com/) and [https://webflow.com/pricing](https://webflow.com/pricing), 2026-11-19. Values are token names. Computed numbers are in [tokens.json](tokens.json).

## Button

Primary. `a.btn`, label Start for free and Get started. Background `{light.background.accent}`, text `{light.text.on-accent}`, radius `{core.radius.button}`, padding `{core.spacing.button-y}` `{core.spacing.button-x}`, height `{core.size.button-height}`, type `{core.typography.button}`. Hover background `{light.background.accent-hover}` and shadow `{dark.elevation.button-hover}`. Focus ring `{light.focus.ring}` at `{core.focus.width}` offset `{core.focus.offset}`.

![Primary button](components/crops/button-primary-dark.png)

Secondary. Talk to Sales, dark page. Background `{dark.background.raised}`, text `{dark.text.primary}`, same radius and padding. No border.

Inverse. `a.btn.cc-dark`, label Compare all Site plans, light page. Background `{light.background.inverse}`, text `{light.text.on-inverse}`. In dark the same class computed to white with `{dark.text.primary}` ink. That flip was read on a node with height 0, so it is recorded as a gap in the dark inverse button crop.

Text button. Read story, transparent background, no radius, no padding.

## Link

Nav link. Log in and Contact Sales. Type `{core.typography.nav}`, colour `{light.text.primary}` or `{dark.text.primary}`, no underline, no background. Padding `{core.spacing.nav-y}` on top.

Footer link. Colour `{light.text.secondary}` in light, size 16px, weight 400, no underline.

## Text field

Home Marketo email field, placeholder Work Email. Background `{dark.background.surface}` in dark, text `{dark.text.primary}`, border 1px `{dark.border.strong}`, radius `{core.radius.input}`, padding 24px, font 16px / 24px / 400. Transition 200ms on border-colour and background. The field was not typed in and not submitted. No error state.

## Switch

Yearly/monthly pricing toggle. Track `.toggle-label` is `{core.size.toggle}` by 24px, radius `{core.radius.pill}`, background `{light.background.accent}`. Knob is the `::before`, 21px, white, radius 50%, translated 18px on the yearly side. The yearly label reads "Yearly (Save up to 40%)".

## Badge

NEW pill. `.pill.cc-category`. Background `{light.background.inverse}`, text `{light.text.on-inverse}`, radius `{core.radius.button}`, padding 3.2px 6px 2.4px, type `{core.typography.caption}`.

![NEW pill](components/crops/pill-new-light.png)

## Card

Site plan card. `.pricing-card` border 1px `{light.border.stroke}`, radius 0 on the inner card. The shell `.pricing-card-component` has radius `{core.radius.card}`. Team variant background `{light.background.surface}`. Enterprise band `.pricing-card-lg` background `{light.background.inverse}`, text `{light.text.on-inverse}`, radius `{core.radius.card}`, padding 32px 144px 32px 32px.

![Pricing card](components/crops/pricing-card-light.png)

## Wordmark

Header SVG, 124 by 24 at 1440. The mark is `#146EF5`. The word is `currentColor`.

![Wordmark](components/crops/wordmark-dark.png)

## Gaps

- Login, signup, and account fields were not reached. /login is a PerimeterX hold page.
- Cookie dialog colours were not computed. Later loads did not show the dialog.
- Open nav menus, tooltips, toasts, tables, avatars, checkboxes, radios, and text areas were not on the loaded pages.
- Disabled, pressed, loading, and error states were not shown.
- The dark inverse button was read on a node with no height.
