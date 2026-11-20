# Measured-system category migration

The app's category assignments live in SQLite. [system-categories.json](../src/data/system-categories.json) supplies the one-time migration seed. The seed covers 219 of the 460 measured systems in the canonical [catalog](../../catalog.json), using the exact category labels captured in [Refero's catalog taxonomy](../src/data/refero-catalog-taxonomy.json). Each assignment records its reference ID, platform category group, labels and the local evidence used to choose them. New packages may add a row here as they land; the seed is add-only (see Validation).

## Scope and storage

These assignments initialize the app's category overlay. They do not alter canonical package categories, tags, tokens, capture provenance or generated package documents. The app's SQLite overlay can hold subsequent categorization edits independently of the captured library.

The source adapter identifies measured packages as `systems:<slug>`. Native mobile packages use `ios-categories`; web and desktop packages use `web-categories`. Desktop remains the package's original platform: using Refero's web vocabulary does not relabel a desktop capture as a web capture.

| Package platform | Assigned category group | Packages |
| --- | --- | ---: |
| Web | `web-categories` | 191 |
| Desktop | `web-categories` | 13 |
| Mobile | `ios-categories` | 15 |
| Total | | 219 |

There are 331 label assignments across these packages. Each package has one to three relevant categories. Labels classify the product and captured workflows, rather than visual mood, UI components or every feature a product might provide.

The separate 1,342-style Refero snapshot keeps its existing style categories. Refero's Web and iOS product categories and its Styles vocabulary describe different datasets, so this migration does not reinterpret the style snapshot.

## Choices that need interpretation

| Package | Categories | Evidence and choice |
| --- | --- | --- |
| ResearchRabbit | Reference | The [capture](../../systems/researchrabbit/README.md) records literature search, citation graphs, collections and citation copying. Its former `ai-research` label does not establish a captured AI interaction. |
| TokenTracker | Development Tools | The [capture](../../systems/tokentracker/README.md) records a local CLI dashboard for token usage, sessions, limits and skills. Usage cost display alone does not make it a Finance product. |
| Polaris | Development Tools | The [package](../../systems/polaris/README.md) is a published React component and token archive. It does not contain a captured merchant application or marketplace. |
| Grab | Food Delivery, Travel & Booking | The [capture](../../systems/grab/README.md) records GrabFood and ride booking. The iOS vocabulary has no Transport category; Travel & Booking is the closest category for the captured ride flow. |
| GitHub Mobile | Collaboration Tools, Project Management | The [capture](../../systems/github-ios/README.md) records issues, pull requests, code review and notifications. The iOS vocabulary has no Development Tools category, so these labels cover collaboration and tracking. |
| Substack | Magazines & Newspapers, Social Networking | The [capture](../../systems/substack/README.md) records newsletter reading and publishing, notes, follows, activity and chat. Magazines & Newspapers is the closest publication category. |
| Arc Search | Utility | The [capture](../../systems/arcsearch/README.md) records browser navigation, searching, tabs and history. Utility covers the browser without assuming a captured AI feature. |
| Cursor iOS | AI Tool | The [catalog](../../catalog.json) describes the coding-agent client. The iOS vocabulary lacks Development Tools, so AI Tool stands alone. |
| Luma | Scheduling Tools, Social Networking | The [capture](../../systems/luma-ios/README.md) records event creation, calendars, follows and chat. The iOS vocabulary lacks Events; these categories cover its scheduling and community workflows. |
| Grok Bot desktop | AI Tool | The [capture](../../systems/grokbot-desktop/README.md) describes a messenger for AI agents. General agent chat alone does not establish a developer workflow. |
| Raycast | Productivity | The [catalog](../../catalog.json) describes the launcher and command palette, and records an ended AI trial. The captured core workflow supports Productivity. |
| Refero | Inspiration Board, Reference | The [capture](../../systems/refero-design/README.md) records screenshot discovery, style galleries and documentation. These categories match the captured content without inferring AI behavior from its old `ai-research` label. |
| Airbnb | Travel & Booking, Marketplace | The [catalog](../../catalog.json) describes a public travel marketplace: stay search, listing cards and wishlist. The legacy `travel` category maps to Travel & Booking. |
| Awwwards | Inspiration Board, Reference | The catalog's `directory` category has no Refero equivalent; a curated awards gallery is closest to inspiration and reference material. |
| B150 | Social Networking | The legacy `media` bucket held this builders' network; no consumption-media label fits a community product. |
| Butter | Design & Media Editing | The legacy `media` bucket held this video editor; it is a creator tool, not a streaming product. |

Notion's mobile and desktop captures explicitly include Notion AI alongside docs, notes and databases, so both receive AI Tool and Productivity. Desktop coding-agent products receive AI Tool and Development Tools when their catalog description explicitly identifies coding, repositories, terminals, files or agent development work.

## Validation

`categorySeedGaps` in [categories.ts](../src/contracts/categories.ts) checks the seed against the catalog, and `make check` and the Research app tests run it. The seed is add-only: a package may have no row yet, but a row the previous seed had may not disappear, a row whose package is gone fails, and every mobile row must use `ios-categories` while every web or desktop row uses `web-categories`. Every category label must appear in its declared taxonomy group, and an empty label list is invalid.

A package with no seed row keeps its catalog `category` in the app, lists under the gallery's Uncategorised filter, and still matches its old category link (`?category=productivity`).

The initial mapping was checked against the catalog and captured taxonomy of the time: 88 packages covered, no missing or duplicate IDs, no unknown labels, and no platform-group mismatches. Every row includes its own reason, including the choices above, so future edits can inspect the evidence without reconstructing this migration.
