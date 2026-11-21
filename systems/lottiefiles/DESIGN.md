# LottieFiles

Generated note. `make design-md` rewrites this file once the package is in catalog.json. This capture PR does not edit catalog.json, so this file is a short stand-in so the package layout is complete.

## Overview

Public marketing site, light theme only, captured 2026-11-21. Source of truth is [tokens.json](tokens.json).

## Colors

Page `oklch(100% 0 0)`. Text `oklch(14.1% 0.005 285.823)`. Muted `oklch(55.2% 0.016 285.938)`. Primary `oklch(62.6% 0.11 185.333)`, sampled sRGB `#28aca2`. Border `oklch(92% 0.004 286.32)`.

## Typography

Display: DM Sans LF, 96px, weight 500, line-height 99.84px, letter-spacing -4.8px. Controls: Inter LF, 16px and 14px, weight 500.

## Layout

Hero button height 48px, padding 24px, radius 12px. Header control height 36px, padding 16px, radius 6px.

## Elevation & Depth

Control shadow `0px 1px 2px 0px rgba(0, 0, 0, 0.05)`.

## Shapes

12px hero radius. 6px header radius. Base `--radius` is 0.5rem.

## Components

Primary button, quiet button, nav link, search field, menus, login dialog. See [components.md](components.md).

## Do's and Don'ts

Take values from [tokens.json](tokens.json). Do not read colours off the 256-colour screenshots. Do not treat inverse tokens as a dark theme. Do not style the signed-in app from this package.
