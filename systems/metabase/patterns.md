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

| Collection creation and validation | Unsaved form with location picker, required-name error and disabled submission. | [Form](screenshots/create-collection-light-desktop.png), [validation](screenshots/collection-validation-light-desktop.png) |
| Event composition | Empty timeline onboarding leads to an unsaved event, calendar, optional time and icon selector. | [Onboarding](screenshots/collection-events-empty-light-desktop.png), [calendar](screenshots/event-date-picker-light-desktop.png), [icons](screenshots/event-icon-picker-light-desktop.png) |
| Metric detail | About, Overview, Definition, Dimensions and History organize a metric. Menus expose duplicate and caching dialogs. | [Dimensions](screenshots/metric-dimension-settings-light-desktop.png), [history](screenshots/metric-history-light-desktop.png) |
| Theme and responsive collection | Dark preserves the collection hierarchy; phone width stacks cards and uses an overlay sidebar. Original Light preference was restored. | [Dark desktop](screenshots/reports-dark-desktop.png), [phone](screenshots/reports-dark-mobile.png), [sidebar](screenshots/reports-sidebar-dark-mobile.png) |

Full traversal remains pending; see [interactions](interactions.md).

## Model lineage and report configuration

Model information drawers separate description/source fields from History and Relationships. [Submissions relationships](screenshots/model-submissions-relationships-light-desktop.png) links a saved question and its source table; the [data-reference field catalogue](screenshots/reference-assignment-fields-light-desktop.png) distinguishes semantic and database types.

The [donut inspector](screenshots/donut-data-settings-light-desktop.png) keeps the chart visible while configuring measure, breakout and colors. [Percentage placement](screenshots/donut-percentages-both-light-desktop.png) changes the local draft, with Save remaining explicit and unsubmitted.

[Query failures](screenshots/model-students-error-light-desktop.png), [history failures](screenshots/report-history-error-light-desktop.png) and [permission denial](screenshots/report-settings-denied-light-desktop.png) have distinct messages. The [dashboard picker](screenshots/report-dashboard-search-empty-light-desktop.png) disables Select for an empty search.
