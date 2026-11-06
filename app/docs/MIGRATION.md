# Legacy library feature migration

The migration audits `web/` as the feature inventory and uses Studio's approved Refero-derived layout. The canonical stores and old app stay unchanged. The new app reads the existing data rather than rebuilding a smaller collection from screenshots.

## Separate sources and workflows

| Area | Restored behavior |
| --- | --- |
| Gallery | 41 measured packages; platform/category/theme/font search; grid/list view and preview scrubbing |
| Captured package | 4,425 screenshots, 10,456 component crops, 1,474 icons across the corpus; grouped, searchable, filtered and paginated; original-image viewer navigates within the selected group |
| Package documentation | Full README, readable files, rendered/source Markdown, structured token previews, HTML style guides in an isolated frame, package health links |
| Styles | Separate catalog of 1,342 interpreted Refero styles, opening in the same tab with the shared sidebar; theme/type/design-style/industry/tag/video filters and ranked search |
| Style detail | Screenshot, scrolling video, detail clip, posters, full design guidance, rendered/source Markdown, CSS/Tailwind/JSON exports and related styles |
| HTML components | Three usable reconstructed HTML examples; unresolved upstream references display an unavailable state. These examples are interpreted, not measured product code |
| Bookmarks | Individual media bookmarks in SQLite, alongside reference collections and notes; saved images link back to the selected capture |
| Documents | Canonical library docs, relative links, heading anchors and document navigation |
| Scorecard | Overview, heatmap, per-package evidence, platform rubric and audit history |
| Research | Full package documents, token groups with evidence and resolved aliases, media lists, selected images and copyable handoff prompts, preserving durable history and selection controls |
| Preferences | Theme, desktop sidebar collapse, gallery layout/preview preferences, provider connection test and model discovery |
| Compatibility | Old gallery/refero routes redirect to the corresponding new workflow; old file links open the package reader |

## Personal state and unavailable data

The new app preserves its existing conversations, collections, notes and provider configuration. Its version-two SQLite migration adds saved media without replacing existing tables. Old screenshot bookmarks lived only in the old browser origin's `ds-saved` local storage array. Different ports and hosts cannot read one another's browser storage. Settings provides an explicit JSON import that matches paths against canonical recorded media and reports unmatched entries; no automatic transfer of old browser state is claimed.

Provider credentials remain server-side. Model discovery tests the saved endpoint and never returns credentials or raw provider error bodies. Live model execution requires a configured credential; no live-provider success is claimed from environment-variable presence.

Package readers reject traversal, hidden/private files, symlink escapes and overly large documents. HTML guides and component previews run in isolated frames. Missing LFS/media stays unavailable; existing mirror/CDN fallback is used for Refero previews. Research only sends bounded local raster evidence to image-capable providers.

## Deliberate exclusions

Accounts, authentication, pricing/billing and MCP plugin/onboarding are excluded at the user's request. The legacy chat drawer, browser-stored secrets and legacy CSS are not carried into the new implementation. Source-specific data is preserved even where research and collection cards share an identity contract.

## Validation

The coordinating browser pass compares the old Brilliant package to the new package, exercises screenshot filtering/navigation/saving, opens the HTML guide and library documents, inspects the scorecard, and checks Linear's separate Styles detail and video controls. Automated tests cover canonical source parity, file boundaries, HTML isolation, document links, model discovery, token/media research tools and durable database migration. Typecheck, production build, repository checks and package tests complete before commit.

Detailed inventories: [Gallery](gallery-migration.md), [Styles](styles-migration.md), [knowledge and research](workflow-migration.md).
