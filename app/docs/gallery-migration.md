# Measured gallery migration

The measured collection contains product packages with many page captures and component crops. Refero supplies separate interpreted website styles. Both retain their source IDs; their detail contracts preserve different source structures.

## Restored workflows

- `/library/[slug]` opens a measured package. Screenshots, component crops, icons and boards have independent tabs, original file identities, folder groups, tag filters, name/state search and incremental display. The viewer navigates the complete filtered set rather than switching products.
- A `media` query identifies the exact capture. Original/download/copy-link actions and saved media use stable canonical package paths. Tags come from capture metadata: the current measured dataset uses light, dark and mobile. State variants remain searchable by filename; the old gallery had no dedicated state facet.
- README and Files expose full package Markdown, JSON and allowlisted source files. Relative package links stay within bounded package/document/media routes. Hidden files, raw captures, ignored dependency trees and escaping symlinks remain inaccessible. Files above 4 MiB are excluded.
- HTML style guides run in an opaque sandbox with scripts but no same-origin privilege, network connections, form submissions or arbitrary repository file access. Captured assets resolve through a bounded guide-resource route.
- Recorded values use generated theme swatches, composed type styles/font stacks, spacing/radius scales and shadows. The original token exports and their individual evidence labels remain available; known omissions and capture provenance remain explicit.

## Data boundary

`LibraryDetail.measured` preserves the measured package manifest and structured previews. `LibraryDetail.interpreted` preserves the full canonical design-system object, source facets and authored similar references. Media retain kind, path, group, original URL, thumbnail, poster and remote fallback when available. Canonical packages and generated artifacts are read, never rewritten by the app.

## Verification

Source fixtures cover complete icon inventories beyond the former 96-icon preview, original media IDs/groups, nested screenshots, full README, structured token previews, all six Refero media kinds, canonical similar references, safe document links, traversal/symlink/private-file rejection and HTML sandbox headers. TypeScript and the app test suite run locally. Browser layout and interaction verification belong to the parent task.
