# Patterns

All evidence comes from Metabase's official Edumation embedding demo. The purple accent is this instance's customization.

| Pattern | Composition and use | Evidence |
|---|---|---|
| Visual query notebook | Sequential Data, Filter, Summarize sections. Aggregate and grouping fields sit side by side. Compact controls add joins and computed columns; one Visualize action follows the stages. | [Builder](screenshots/query-builder-light-desktop.png) |
| Field-first filtering | Searchable field list leads to a type-specific popover. Numeric fields use an operator selector and range inputs; Add filter stays disabled until valid input. | [Field list](screenshots/query-filter-fields-light-desktop.png), [range](screenshots/numeric-filter-light-desktop.png), [operators](screenshots/filter-operators-light-desktop.png) |
| Chart configuration | A fixed left inspector uses Data, Display and Axes tabs while the chart remains visible. These were unsaved local query settings; no dashboard configuration was changed. | [Data](screenshots/chart-data-light-desktop.png), [Display](screenshots/chart-display-light-desktop.png), [Axes upper section](screenshots/chart-axes-light-desktop.png) |
| Drill-through | Clicking a bar opens a contextual menu with underlying rows, automatic insights, copy and numeric comparisons. Following See these Courses replaces aggregation with a filtered detail table and a visible filter pill. | [Menu](screenshots/drilldown-menu-light-desktop.png), [results](screenshots/drilldown-results-light-desktop.png) |
| Dashboard filtering | A labelled filter pill opens search and checkboxes, including checked and indeterminate states. Update filter remains disabled until selection changes. | [Desktop](screenshots/dashboard-filter-light-desktop.png), [390px](screenshots/dashboard-filter-light-mobile.png) |
| Responsive dashboard | Metric cards form a row at 1440px and stack at 390px; navigation condenses to icons. Captures are viewport sections, not the whole long dashboard. | [Desktop](screenshots/dashboard-light-desktop.png), [phone](screenshots/dashboard-light-mobile.png) |
| Empty and error results | The demo naturally returned No results and chart errors alongside successful metrics. These are observed product states, not fabricated failures. | [Dashboard](screenshots/dashboard-light-desktop.png) |
| Collection browsing | A sidebar, featured model/dashboard cards and a searchable table combine navigation with filtering. | [Embedded reports](screenshots/reports-light-desktop.png), [type filter](screenshots/collection-filter-light-desktop.png) |
