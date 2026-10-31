# Components

Use `light.component.*` or `dark.component.*` in [tokens.json](tokens.json): primaryButton and toolbarButton separate `.container` geometry/chrome from `.label` visible text. iconButton and sidebar expose containers only; tableLabel exposes the visible Google label. No inherited wrapper typography is presented as visible label typography. `core.type.table` holds the table label size, line height and tracking. These are component-specific readings, not a complete shared scale.

| Component | Evidence | Captured states |
|---|---|---|
| Button / icon button / link | [Toolbar](components/crops/light-toolbar.png) | Default, selected navigation; other states not systematically measured |
| Text field / textarea | [Create](screenshots/company-create-light.png), [Description](screenshots/onboarding-company-description.png) | Default, prefilled; no validation error |
| Select / checkbox | [Columns](screenshots/companies-view-settings-light.png) | Select open, unchecked table selection |
| Radio / switch | [Appearance](screenshots/appearance-light.png), [Call choice](screenshots/onboarding-call-intelligence-disabled.png) | Selected and unselected |
| Tabs | [Overview](screenshots/company-record-overview.png), [Notes](screenshots/company-notes-empty.png) | Selected and empty content |
| Menu / tooltip / dialog | [View menu](screenshots/companies-view-picker.png), [Tooltip](screenshots/companies-dark-scoped.png), [Sort](screenshots/companies-sort-light.png) | Open, dismissed after capture |
| Table / list row / avatar / badge / card | [Table](components/crops/light-table.png), [Record](screenshots/company-record-overview-light.png) | Populated and default |
| Toast | Not captured | No suitable non-mutating trigger |

All screenshot-only states are **Observed**; do not infer measured token specifications from their pixels. Keyboard focus-visible, pressed, error and loading coverage is incomplete. Create forms were closed without submitting; no saved filter/sort/view edits were made.
