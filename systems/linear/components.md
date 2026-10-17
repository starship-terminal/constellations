# Linear components

The component inventory and the interaction states of Linear's signed-in app. The app components were measured on 2026-10-17 in dark and light from redacted copies of the signed-in pages ([README.md](README.md#how-the-app-values-were-read) says how): crops are in [components/crops/](components/crops), values for every crop in [raw/measurements.md](raw/measurements.md) and [raw/components-computed.json](raw/components-computed.json). The SVG redraws in [components/](components) are from the first capture (2026-09-23) and are reconstructions; [components/manifest.json](components/manifest.json) lists them. States that could not be reached are named per component in the README's [Coverage](README.md#coverage) table.

## Component inventory and evidence

| Family | Measured (2026-10-17) | Redrawn (2026-09-23) |
| --- | --- | --- |
| Buttons | primary, primary small, secondary, destructive, icon, property chip | primary states, secondary, ghost, danger, icon, web CTA |
| Links | inline link, breadcrumb | none |
| Inputs | text field (and read-only), search field, text area (description editor), select (trigger, open list, option), switch on and off, checkbox geometry | field states, checkbox, switch |
| Navigation | view tab (pill), sidebar item | selected sidebar row, pill tabs |
| Overlays | menu with highlighted option, tooltip with keyboard keys, dialog and scrim, toast | status menu, tooltip, toast |
| Lists and tables | board card, board column header, sub-issue row, projects table row, members table header, row and group header | issue row, board card |
| Display | avatar, Admin badge, label chip, keyboard key, presence dot, project health labels | label badge, avatar, shortcut |
| Shell | inset main panel, page header, empty state | empty state, composer, properties, date picker |

## Buttons, fields and interaction states

Measured in both themes (crops in `components/crops/`, values in `raw/measurements.md`):

- **Focus-visible** is a 1px solid outline in the focus colour, drawn in plain CSS. Its offset depends on the control: 2px outside buttons, 0 on icon buttons, 1px on links, -1px inside fields and tabs.
- **Hover** lightens the fill one step (accent #5E6AD2 to #6975E2 in dark; in light the accent darkens, #6D78D5 to #5E6AC1). Transitions are 0.15s ease on border, background, colour and opacity.
- **Pressed** (:active) equals hover on every button measured.
- **Selected** tabs and sidebar items take a filled pill one step above the control fill.
- **Disabled** never appeared: the composer's Create issue button stays enabled with an empty title.
- Motion variables: `--speed-quickTransition` 100ms, `--speed-highlightFadeOut` 150ms, `--speed-regularTransition` 250ms, `--speed-slowTransition` 350ms, `--speed-highlightFadeIn` 0ms; easings `--ease-out-quad`, `--ease-out-cubic` and others. 14 rules respond to `prefers-reduced-motion: reduce`.

The public site's primary actions are pale filled pills with dark text, 32px high, 13px at weight 510; the embedded demo's icon buttons use a 2% white fill and an inset 1px line at 5% white.
