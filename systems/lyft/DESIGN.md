# Lyft DESIGN.md

Hand-written from measured tokens in [tokens.json](tokens.json). This file was not produced by `make design-md`. The catalog was left alone, and that command rewrites catalog-backed generated files.

Captured 2026-11-21 from https://www.lyft.com/, light theme only.

## Colors

| Role | Token | Value |
|---|---|---|
| Page | light.background.primary | #fff |
| Surface | light.surface.primary | #fff |
| Raised band | light.background.secondary | #f1f0ec |
| Text | light.text.primary | #1d0c17 |
| Muted text | light.text.secondary | #1d0c17b3 |
| Accent (actions) | light.surface.interactive | #820076 |
| Accent (wordmark) | core.color.brand.lyftPink | #ff00bf |
| Link | light.text.interactive | #ac2a9e |
| Border | light.stroke.tertiary | #36220129 |
| Danger | light.text.negative | #c81534 |
| Success | light.text.positive | #197849 |
| Scrim | light.background.scrim | #1d0c174d |

## Typography

| Role | Family | Size | Weight | Line height |
|---|---|---|---|---|
| Display | RebelSansDisplay, sans-serif | 60px | 600 | 66px |
| Body | RebelSansText, sans-serif | 16px | 400 | 22px |
| Button | RebelSansText, sans-serif | 16px | 400 | 22px |

Rebel Sans is proprietary and is not in this package.

## Rounded

| Token | Value |
|---|---|
| core.radius.pill | 48px |
| core.radius.card | 16px |

## Spacing

| Token | Value |
|---|---|
| core.space.button-x | 24px |
| core.space.card-y | 24px |
| core.space.card-x | 16px |
| core.sizing.button-height | 48px |

## Elevation

Light shadows from `--core-ui-elevation-level1-light` through `level8-light`, plus `panel`. See [tokens.json](tokens.json) `core.elevation`.

## Omitted

Dark theme. The public site does not switch themes.

Motion. No duration custom properties were declared on the homepage.

Component states other than the default primary button and the empty phone field.
