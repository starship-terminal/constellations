# Components

Public signed-out Skiff, measured 2026-11-19. Crops are from the 1440 captures. Values are token names. States that were not on the page are gaps.

## Nav pill

The floating bar at the top of every measured page. Background `{light.background.nav}`, text `{light.text.on-nav}`, radius `{core.radius.nav}`, padding `{core.spacing.4}`, border 1 px `{light.border.nav}`, shadow `{core.shadow.nav}`. The mark tile is 36 px, `{light.accent.default}`, radius `{core.radius.mark}`. Labels are `{core.typography.body-small}`.

![Nav pill](components/crops/nav-pill-default.png)

The Product and Resources menus were not opened.

## Notice card

The home page card. Background `{light.background.surface}`, radius `{core.radius.raised}`, border 1 px / 2 px `{light.border.stroke}`, padding 140 px 160 px at 1440. The heading is `{core.typography.display}`. The second line is `{light.accent.default}`. Body copy is `{core.typography.body}` in `{light.text.secondary}`.

![Notice](components/crops/notice-card-default.png)

## Migrate link

Orange text, `{core.typography.body}`, colour `{light.accent.default}`, no underline at rest. Hover colour `{light.accent.hover}` is declared (`.hover:text-orange-600`) and was not observed.

![Migrate link](components/crops/link-migrate-default.png)

## Report form

Empty fields. Background `{light.component.field.bg}`, text `{light.component.field.text}`, radius `{light.component.field.radius}`, padding 8 px 12 px, inset shadow `{core.shadow.inset}`. The submit button is `{light.component.button-primary.bg}`, label `{light.component.button-primary.text}`, radius `{light.component.button-primary.radius}`, padding 8 px 16 px. The form was not submitted.

![Report form](components/crops/form-report-default.png)

## Badge

The DEFAULT chip on the Mail domain demo. Background `{light.component.badge.bg}`, text `{light.component.badge.text}`, radius `{light.component.badge.radius}`, padding 2 px 5 px, mono 13 px, uppercase. UNVERIFIED uses the overlay fill and `{light.text.muted}`.

![Badge](components/crops/badge-default.png)

## Marketing demo

The Mail page paints an inbox mock, feature cards and a dark code panel. These are public demos, not the app. The code panel background is `{light.background.code}`, radius `{core.radius.nav}`.

![Inbox demo](components/crops/demo-inbox-default.png)

![Code panel](components/crops/code-panel-default.png)

## Footer

Column labels are `{core.typography.label}` in `{light.text.secondary}`, uppercase. Links are `{core.typography.footer-link}` in `{light.text.footer}`.

![Footer](components/crops/footer-default.png)

## Gaps

- Hover, focus-visible, pressed, disabled, loading and error states of the button, fields and links were not captured. Focus ring colour `#0b79af` is declared on inputs and was not observed.
- Product and Resources menus, select, checkbox, radio, switch, tabs, tooltip, dialog, toast and table were not on the measured pages as real controls.
- The signed-in Mail, Pages, Drive and Calendar apps were not entered. The product shut down.
- Changelog and privacy-policy footer links redirected to the home notice with a fragment. Those documents were not captured.
- Terms of service and acceptable use policy point at app.skiff.com document URLs. They were not opened.
- Dark theme was not painted.
- A reduced-motion pass was not run. The only authored reduce rule found is Sonner's toast reset.
