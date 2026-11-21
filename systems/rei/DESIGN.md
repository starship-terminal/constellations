# DESIGN.md

Hand copy of the measured homepage tokens. `make design-md` was not run. That command rewrites DESIGN.md from a catalog.json entry, and this pass does not edit catalog.json.

## Colors

| Role | Value | From |
|---|---|---|
| page | `#ffffff` | body background |
| surface | `#f4f2ed` | header `.gnav`, `--cdr-color-background-primary` |
| header | `#292929` | header `.unav` |
| text | `#000000` | body color |
| muted | `#4b4a48` | category and price |
| accent | `#c7370f` | promo bar and Shop the sale |
| on-accent | `#ffffff` | Shop the sale type |
| border | `#958e83` | search inset ring |
| link | `#406eb5` | product title |

## Typography

| Style | Family | Size | Weight | Line height |
|---|---|---|---|---|
| body | Graphik, Helvetica Neue, sans-serif | 16px | 400 | 24px |
| utility | Graphik | 14px | 400 | 20px |
| word | Stuart, Georgia, serif | 24px | 600 | 30px |
| section | Stuart | 32px | 500 | 40px |
| button | Graphik | 16px | 500 | 22px |

## Rounded

Controls use 4px.

## Spacing

Utility bar 40px. Main bar 128px. Search 46px. Primary button 38px. The page also ships fluid `--cdr-space-scale-*` clamps. Those were not copied as a fixed scale.

## Components

Shop the sale: background `#c7370f`, text `#ffffff`, radius 4px, height 38px.
