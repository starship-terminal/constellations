# Measurements

Read 2026-11-19 from the public signed-out site. `https://www.vevo.com/` redirects to `https://www.hq.vevo.com/`. No Cloudflare challenge. No account, phone, or card.

Viewport used for the token readings: `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 2, `visualViewport.scale` 1. Phone readings: 390 by 844, same ratio.

The preview browser opened the page and returned computed styles, then failed both snapshot attempts with "The browser is not producing screenshot frames". Screenshots were taken with headless Playwright on the same public marketing URLs after they loaded without a challenge.

## Colour

| Role | Value | Where |
|---|---|---|
| Page | `rgb(255, 255, 255)` | `--wst-color-fill-background-primary` |
| Secondary surface | `rgb(227, 227, 227)` | `--wst-color-fill-background-secondary` |
| Ink section | `rgb(0, 0, 0)` | hero, originals, newsroom, footer fills |
| Crimson section | `rgb(161, 0, 46)` | By the numbers |
| Slate section | `rgb(121, 128, 148)` | Vevo For Artists |
| Sand section | `rgb(206, 199, 174)` | Watch More Music |
| Action / cookie bar | `rgb(23, 75, 235)` | `--wst-color-action`, `--cookie-banner-primary-color` |
| Text | `rgb(0, 0, 0)` | `--wst-color-text-primary` |
| Muted | `rgb(79, 79, 79)` | `--wst-color-text-secondary` |
| Inverse text | `rgb(255, 255, 255)` | hero `h1`, nav label |
| Current menu item | `rgb(149, 7, 255)` | phone menu Home |
| Pill default | white fill, black label, radius 24px, height 46px | `a.wixui-button` About Us |
| Pill hover | `rgb(2, 2, 2)` fill, `rgb(253, 253, 253)` label, 0.4s ease | forced `:hover` |
| Skip focus | 2px `rgb(17, 109, 255)` | `#SKIP_TO_CONTENT_BTN` after Tab |

`prefers-color-scheme: dark` did not change `--wst-color-text-primary` or `--wst-color-fill-background-primary`. One theme.

## Type

The display face is a Wix-hosted family, `wfont_08392a_c1f9747dda3c4c4889c5132122c1d70a`. Declared sizes scale with the viewport.

| Role | Declared | Computed at 1440 |
|---|---|---|
| Display `--font_0` | 88px / 1.4em | 166.3px, line-height 157.985px, letter-spacing -1.663px, white |
| Heading `--font_2` | 72px / 1.4em | 81.6px, letter-spacing -0.816px |
| Stat figures | same family | 74.5px / 74.5px, letter-spacing -0.745px |
| Body `--font_7` | 18px / 1.4em | 22.2px / 26.64px on the sand section |
| Caption `--font_9` | 14px / 1.4em | 15.1px / 16.61px, white |
| Nav label | | 14px / 21px, padding 0 10px, white |
| Button label | | 16px / 22.4px, black |
| Phone menu item | | 22px, white; current `rgb(149, 7, 255)` |

## Geometry

Desktop header 77px. Phone header 49px. Content inset 30px at 1440, 21px at 390. Cookie bar 68px tall, blue, Decline and Accept 32px tall with 16px horizontal padding and square corners. Logo 62 by 15 CSS px, fill `#ffffff`.

## Not on the page

No text field, text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, table, or avatar. No signed-out video player: `/watch` and a video path redirect to `/originals`. No disabled, pressed, loading, or error control. No dark theme.
