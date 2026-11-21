# Measurements

Read on https://calendly.com/ on 2026-11-21, signed out, headless Chromium, viewport 1440×900, devicePixelRatio 1.

| Element | Reading |
|---|---|
| body font | Geist, system-ui, -apple-system, Segoe UI, Roboto, sans-serif |
| body size | 16px |
| body color | rgb(0, 0, 0) computed; token `--color-text-primary` is #071a31 |
| body background | rgb(252, 251, 248) which is `--color-magnolia` / `--color-surface-bg-primary` |
| header height | 68px (`--header-height`) |
| header background | rgb(252, 251, 248) |
| primary CTA | "Get started for free": background #071a31, text #fcfbf8, radius 16px, padding 12px 16px, font 14px / 400, height 48px |
| mobile header | `--header-height-mobile` 56px |
| breakpoints | `--breakpoint-ui-tb` 768px, `--breakpoint-ui-sdsk` 1024px, `--breakpoint-ui-dsk` 1280px |
| focus border | `--color-action-focus-border` #6bb1ff |

Font faces declared: Geist (variable, woff2), Calendly Sans (variable), Wulkan Text (400, 500, 600, roman and italic). Proprietary. Not committed.

Custom properties: 423 non-Tailwind names resolved on `:root`. The token file keeps the Calendly semantic set (color, spacing, radius, type, shadow, ease, breakpoints). Tailwind's stock hue palette was left out. See [css-vars.json](css-vars.json).
