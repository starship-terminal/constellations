# Target

Public marketing design tokens from target.com, measured 2026-11-22. This file is a copy of the tokens in [tokens.json](tokens.json). It was not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json.

## Color

| Role | Value |
|---|---|
| Page | `#ffffff` |
| Text | `#333333` |
| Muted | `#666666` |
| Accent | `#cc0000` |
| Accent hover | `#aa0000` |
| On accent | `#ffffff` |
| Surface | `#f7f7f7` |
| Border | `#888888` |
| Focus | `#151515` |
| Success | `#008300` |
| Warning | `#b85300` |
| Info | `#2758b9` |

Accent, page, text, on accent, and surface were read from computed styles. The rest are published custom properties on the homepage. Success, warning, and info had no live state on the pages that were opened. Accent hover was not held under a pointer.

## Type

Helvetica for Target is the UI face. It is named in the computed font on the homepage. The file is not in this package.

Body text is 16px, weight 400, line height 22.856px, color `#333333`.

The homepage h1 is 29px, weight 700, line height 36.25px. Its text is "Homepage" and it is visually hidden. The hero type is painted in an image.

The published type scale runs from 13px to 68px.

## Radius

Search and the footer Sign up button use a 999px pill. Sign up is 44px tall, weight 700, padding 0 12px. The published input radius is 8px. The published card radius is 16px.

## Spacing

The published space scale is a 4px step: 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 80.
