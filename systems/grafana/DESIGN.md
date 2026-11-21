# Grafana

Public marketing design tokens from grafana.com, measured 2026-11-22. This file is a copy of the light theme in [tokens.json](tokens.json). It was not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json.

## Color

| Role | Value |
|---|---|
| Page | `#f4f4f6` |
| Surface | `#ffffff` |
| Text | `#000000` |
| Muted | `#67677e` |
| Border | `#aeaebc` |
| Accent | `#1b55f5` |
| Accent hover | `#1440e1` |
| On accent | `#ffffff` |
| Link | `#1b55f5` |
| Link hover | `#1734b6` |
| Brand | `#f04306` |
| Success | `#17b26a` |
| Danger | `#d92d20` |
| Warning | `#ff8200` |

## Type

Inter is the UI face. Poppins is the display face. Both are named in CSS custom properties on the live page. The files are not in this package.

Display heading on the homepage is Poppins 60px, weight 600, line height 75px, letter spacing -1.5px.

## Radius and motion

Control radius is 8px. Panel radius token is 16px. Default transition is 150ms, `cubic-bezier(0, 0, 0.2, 1)`. Spacing unit is 4px. Content width token is 1280px.
