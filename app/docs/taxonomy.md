# Categorisation vocabulary

Use the in-app **Categorisation guide** (`/taxonomy`) when adding websites,
iOS apps or screenshots. `/api/taxonomy` exports the same dated vocabulary as
JSON. The original labels and group boundaries come from Refero's visible
filters, with their source URLs retained in
[src/data](../src/data/). This is a vocabulary snapshot, not a live sync.

## Choosing labels

- Assign the product's category from its platform's category group.
- For each screenshot, choose its page/screen type, then the visible UI
  elements and UX patterns supported by that capture.
- Assign a flow label only to an observed sequence of screens. One screenshot
  cannot establish an ordered flow.
- Keep web and iOS group identities even when their labels overlap. A label
  such as Search describes a different dimension in a flow and in a UI element.
- Leave an uncertain classification empty. Membership in the vocabulary does
  not establish that a label describes an asset.

Styles currently exposes rotating free-text search suggestions, not a public
exhaustive style-tag directory. Those entries are marked `search-preset` and
are excluded from classification validation. The existing snapshot's
`product_type`, `design_style` and `tags` were produced by our classifier;
retain their local provenance instead of claiming Refero supplied them.

## Contract for future importers

Use `groupsForTaxonomy(contentType)` from
[src/contracts/taxonomy.ts](../src/contracts/taxonomy.ts) to offer the appropriate
groups. Validate proposed exact labels using
`validateTaxonomyLabels(groupId, labels)`. Unknown groups, unknown labels, and
search-preset groups are rejected. Term IDs are namespaced by group; source
labels are preserved. An ID is ours, not an upstream Refero database ID.

When implementing an importer that saves assignments, record the content
identity, group and term IDs, taxonomy capture date, assignment source
(`source-provided`, `human-reviewed`, or `model-suggested`), and evidence for
the assignment. Keep model suggestions pending until reviewed. Do not silently
map old tags, overwrite package evidence, or treat a search query as a verified
classification. The current bookmark importer only imports asset identities;
this change does not add a classification write path.

The Screens API's `taxonomy` field continues to describe actual corpus
classifications. It stays empty until classifications have been recorded.
The guide vocabulary must never populate that field just because the terms
exist upstream. Current gallery and style filters continue to use recorded
local metadata.

## Refresh

Inspect each platform's directory categories and the complete expanded search
filter groups in the original site. Preserve exact labels and subgroups, record
source URL and capture date, and state any coverage limits. Update the JSON
snapshots, review the diff for additions/removals/renames, then run the taxonomy
tests and application checks. Do not regenerate IDs from translated labels or
remove terms that saved assignments still reference without a migration.
