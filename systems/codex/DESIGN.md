# Codex public site

Hand-written from measured tokens on 2026-11-22. This file was not generated, so catalog.json was not rewritten. Take values from [tokens.json](tokens.json).

## Colour

The marketing page paints one theme.

| Role | Value | Where |
|---|---|---|
| Page | `#000000` | body |
| Text on page | `#ffffff` | body |
| Nav text | `rgba(255, 255, 255, 0.6)` | Research |
| Headline on the wash | `#000000` | h1 |
| Download fill | `#000000` | Download for macOS |
| Download text | `#ffffff` | same |
| Quiet pill | `rgba(0, 0, 0, 0.04)` | Try on web |
| Log in fill | `rgba(255, 255, 255, 0.12)` | header |
| Login wall page | `#000000` | chatgpt.com/auth/login |
| Login wall text | `#ededed` | same |
| Continue fill | `#ededed` | same |
| Continue text | `#0d0d0d` | same |

## Type

OpenAI Sans, OpenAI Sans Variable Scripts, sans-serif.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Display | 64px | 500 | 64px |
| Nav | 17px | 400 | 28px |
| Button | 14px | 500 | 14px |
| Login heading | 30px | 400 | 36px |

The login wall uses the system sans, not OpenAI Sans.

## Geometry

Download and Try on web are 40px tall, 20px horizontal padding, 40px radius. Log in is 36px tall, 40px radius. Login-wall controls are pills (`9999px`), 52px tall, on a 384px card. Header is 64px (`--spacing-header-h`).

## Motion

`--transition-duration-short` is 0.2s. `--ease-out` is `cubic-bezier(0, 0, 0.2, 1)`. Reduced motion was not measured.
