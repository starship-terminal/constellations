# Letterboxd

Public signed-out site, captured 2026-11-21 from https://letterboxd.com. One dark field. Values come from custom properties resolved on `:root` at 1440 x 900. This file was written by hand because `catalog.json` was left alone and `make design-md` would rewrite the catalog. Prefer [tokens.json](tokens.json) when the two disagree.

## Colour

| Role | Value | Token |
|---|---|---|
| page | #14181c | light.page |
| surface | #283038 | light.surface |
| text | #99aabb | light.text |
| muted | #8899aa | light.muted |
| heading | #ffffff | light.heading |
| link | #ddeeff | light.link |
| link hover | #40bcf4 | light.link-hover |
| border | #445566 | light.border |
| accent | #00e054 | light.accent |
| accent surface | #00ac1c | light.accent-surface |
| accent hover | #00c030 | light.accent-hover |
| accent pressed | #009926 | light.accent-pressed |
| blue | #40bcf4 | light.blue |
| orange | #ff8000 | light.orange |
| danger | #c40f00 | light.danger |
| focus | #209ce4 | light.focus |
| on accent | #ffffff | light.on-accent |

## Type

Sans: GraphikWeb, then system-ui. Display: TiemposHeadlineWeb, then Georgia. Body serif: TiemposTextWeb, then Georgia.

| Role | Size |
|---|---|
| heading-1 | 32px |
| heading-2 | 27px |
| heading-3 | 22px |
| heading-4 | 18px |
| body-large | 17px |
| body-medium | 15px |
| body-small | 13px |
| body-meta | 12px |
| label | 13px |

Nav links compute 13px, weight 700, letter-spacing 1px, uppercase.

## Space

4px, 6px, 8px, 10px, 12px, 16px, 20px, 24px, 32px, 48px, 64px. Content gutter is 20px. Page gutter is 24px.

## Radius

1px, 2px, 3px poster, 4px, 6px, 8px. Search field computes 15px.

## Motion

150ms dropdown fade, 333ms short, 500ms medium, 1000ms long, 2000ms extra long. Easings: out-expo, out-back, in-back. See tokens.json.

## Layout

Desktop captures are 1440 x 900. Phone captures are 390 x 844 at 2x.
