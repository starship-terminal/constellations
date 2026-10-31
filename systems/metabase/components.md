# Components

Observed live in the official Edumation demo, light theme. Crops use native screenshot pixels, not inferred CSS rectangles. Each crop was visually checked. No 2x upsampling: these are 1x captures.

| Component / state | Screenshot | Crop | Token group |
|---|---|---|---|
| Primary button, default | [query-builder-light-desktop.png](screenshots/query-builder-light-desktop.png) | ![Primary button, default](components/crops/primary-default.png) | light.component.primary |
| Range popover, focused input and disabled submit | [numeric-filter-light-desktop.png](screenshots/numeric-filter-light-desktop.png) | ![Range popover, focused input and disabled submit](components/crops/range-disabled.png) | light.component.inputFocused; light.component.disabled; light.component.popover |
| Field menu with search focus | [query-filter-fields-light-desktop.png](screenshots/query-filter-fields-light-desktop.png) | ![Field menu with search focus](components/crops/filter-fields.png) | light.component.popover |
| Numeric operators menu | [filter-operators-light-desktop.png](screenshots/filter-operators-light-desktop.png) | ![Numeric operators menu](components/crops/filter-operators.png) | light.component.popover |
| Grouping field menu | [grouping-fields-light-desktop.png](screenshots/grouping-fields-light-desktop.png) | ![Grouping field menu](components/crops/grouping-menu.png) | light.component.popover |
| Aggregation menu | [aggregation-light-desktop.png](screenshots/aggregation-light-desktop.png) | ![Aggregation menu](components/crops/aggregation-menu.png) | light.component.popover |
| Visualization choices, table selected | [chart-chooser-light-desktop.png](screenshots/chart-chooser-light-desktop.png) | ![Visualization choices, table selected](components/crops/chart-types.png) | light.accent.default |
| Tabs and switches off | [chart-display-light-desktop.png](screenshots/chart-display-light-desktop.png) | ![Tabs and switches off](components/crops/chart-tabs.png) | light.accent.default |
| Axis inputs, switch on, disabled scale | [chart-axes-light-desktop.png](screenshots/chart-axes-light-desktop.png) | ![Axis inputs, switch on, disabled scale](components/crops/chart-inputs.png) | light.component.input |
| Drill-through action menu | [drilldown-menu-light-desktop.png](screenshots/drilldown-menu-light-desktop.png) | ![Drill-through action menu](components/crops/drill-menu.png) | light.component.popover |
| Metric card | [dashboard-light-desktop.png](screenshots/dashboard-light-desktop.png) | ![Metric card](components/crops/metric-card.png) | light.component.card; core.typography.metric |
| No-results card | [dashboard-light-desktop.png](screenshots/dashboard-light-desktop.png) | ![No-results card](components/crops/empty-card.png) | light.component.card |
| Chart error card | [dashboard-light-desktop.png](screenshots/dashboard-light-desktop.png) | ![Chart error card](components/crops/error-card.png) | light.component.card |
| Multi-select, checked, unchecked, indeterminate | [dashboard-filter-light-desktop.png](screenshots/dashboard-filter-light-desktop.png) | ![Multi-select, checked, unchecked, indeterminate](components/crops/dashboard-multiselect.png) | light.component.popover |
| Checkbox list with disabled options | [collection-filter-light-desktop.png](screenshots/collection-filter-light-desktop.png) | ![Checkbox list with disabled options](components/crops/collection-filter.png) | light.component.popover |
| Filtered table and filter pill | [drilldown-results-light-desktop.png](screenshots/drilldown-results-light-desktop.png) | ![Filtered table and filter pill](components/crops/table-results.png) | light.text.primary |

## Gaps

No live dark theme, persistent pressed state, toast, radio selection or destructive dialog. Hover is incidental and not independently measured. Numeric fields show automatic focus; this does not establish keyboard focus-visible parity. Switches are observed on/off but their track CSS was not tokenised. Chart axes screenshot shows the upper scroll section only. Source CSS enumeration is partial, so missing variables are not proof of absent product tokens. No brand assets are licensed for reuse.
