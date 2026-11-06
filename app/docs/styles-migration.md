# Styles migration parity

Styles is the Refero corpus. Measured package screenshots belong to the separate
library. The Styles index requests `source=refero` and also enforces that source
before filtering. Legacy source/platform query parameters cannot merge the stores.

The new style views preserve the approved 80px header and equal-width detail panes.
On narrow screens, the detail panes stack and controls wrap.

## Restored behavior

- Index: theme (including mixed), product type, design style, industry, secondary
  tags, and video facets. Facet counts, source-host search, ranked facet matches,
  search prompts, `/` focus, URL state, saved facet preferences, and progressive
  card loading. Cards retain tagline, icon, facet labels and delayed hover videos.
- Detail: screenshot, scrolling video, detail clip, poster and detail still;
  controlled playback, appropriate video posters, local/remote image/video fallback,
  image lightbox and source/Refero links. Favicon remains a separate identity asset.
- Documents: rendered and source DESIGN.md, GFM tables, CSS/JSON syntax colors,
  wrapping, raw-content copy and downloads. Existing export bytes remain unchanged.
- Design details: color groups/roles, complete typography specifications and type
  scale specimens, spacing base unit/density, radius, elevation/philosophy,
  do/don't guidance, component descriptions, surfaces, imagery, layout, custom notes
  and upstream similar-brand explanations. Font samples use installed font files.

## Reconstructed HTML availability

The 2026-10-20 snapshot contains 165 nonempty component `html` fields in 55 styles.
Only three fields contain markup (basement-studio, samara and partiful). The other
162 are unresolved upstream RSC references such as `$1e`; the UI reports those as
unavailable and does not pretend they are HTML.

Actual markup has preview, source, copy and download actions. The preview uses an
iframe with an empty sandbox token list and restrictive CSP: no scripts, forms,
network connections or parent access. Inline styles and HTTPS/data images/fonts
are allowed for presentation. Every preview is labelled a Refero reconstruction.
The old local Refero UI never exposed component HTML, so this is an additional
capability rather than a claim of previous UI parity.

## Verification

`pnpm test -- tests/styles-data.test.ts` checks corpus separation, independent
facets, mixed themes, source-domain search, ranking and unresolved-HTML detection.
The app typecheck covers the new detail and media contract. Root task owns browser
verification of desktop, mobile, manual videos, document controls and lightboxes.
