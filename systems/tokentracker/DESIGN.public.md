# Token Tracker public site

Hand-written from measurements taken on 2026-11-22 at `https://www.tokentracker.cc/`. This file is not generated. `make design-md` still owns [DESIGN.md](DESIGN.md), which describes the local dashboard tokens. Do not treat this file as that export.

Values below were read in headless Chromium at 1440 × 900, `color-scheme: dark`. Custom properties come from the site CSS bundle (`/assets/__vite-browser-external-pKm_FufX.css`) and from `getComputedStyle` on the painted page. Screenshots are 256-colour PNGs. Read colours from this file, not from the screenshots.

## Colour

| Role | Value | Where |
|---|---|---|
| Page | `#050507` | `--lv3-bg`, computed on the homepage shell |
| Text | `#fafafa` | computed `rgb(250, 250, 250)` on that shell (`text-oai-white`) |
| Muted nav | `#a3a3a3` | computed `rgb(163, 163, 163)` on the Cloud link |
| Ink on white button | `#0a0a0a` | computed on "Download for macOS" |
| White button | `#ffffff` | computed on that link |
| Marketing accent | `#8a7aff` | `--lv3-accent` |
| Marketing accent, soft | `#b8b3ff` | `--lv3-accent-soft`, used in the "AI TOKEN" gradient |
| Brand green | `#059669` | `--brand-primary` in `:root` |
| Brand green, light | `#10b981` | `--brand-500` |
| Warning | `#f59e0b` | `--oai-warning` |
| Danger | `#ef4444` | `--oai-error` |
| Login button fill | `#171717` | computed `rgb(23, 23, 23)` on "Continue with GitHub" |
| Login button border | `#404040` | computed `rgb(64, 64, 64)`, 1px |
| Login button text | `#ffffff` | computed on that button |

The homepage paints the violet accent. The green brand ramp is declared in `:root` and is the local dashboard's money colour. It is not the hero accent on this marketing page.

The bundle also declares a green-tinted `--oai-gray-*` ramp (`#f6f9f6` through `#050605`). The painted nav muted colour is plain `#a3a3a3`, not `--oai-gray-400` (`#95a395`).

## Type

The painted shell computes to `"OpenAI Sans", -apple-system, system-ui, "Segoe UI", Roboto, Oxygen, Ubuntu, sans-serif`. The bundle does not ship an OpenAI Sans face. Its `@font-face` rules are Geist Mono. On this machine the hero rendered the fallback sans.

| Role | Size | Weight | Line height | Tracking |
|---|---|---|---|---|
| Hero "TRACK EVERY AI TOKEN" | 52px | 600 | 56.16px | -1.3px |
| Hero accent word "AI TOKEN" | 52px | 700 | 56.16px | -1.3px |
| Nav link | 14px | 500 | 20px | normal |
| Primary download | 14px | 600 | 20px | normal |
| Install command | 14px | 500 | 20px | normal, SF Mono stack |

The install command computes to `"SF Mono", SFMono-Regular, ui-monospace, Menlo, Monaco, Consolas, monospace`.

## Controls

| Control | Height | Radius | Fill |
|---|---|---|---|
| Download for macOS | 44px | 9999px | `#ffffff`, text `#0a0a0a` |
| Continue with GitHub | 40px | 12px | `#171717`, 1px `#404040` border, 14px / 500 |
| Cloud nav link | 40px | 0 | transparent, text `#a3a3a3` |

Declared radii in `:root`: `--radius-sm` 4px, `--radius-md` 8px, `--radius-lg` 12px, `--radius-xl` 16px, `--radius-full` 9999px.

## Widths

Desktop shots are 1440 × 900 CSS pixels at 1x. Phone shots are 390 × 844 CSS pixels at 2x (780 × 1688 PNG pixels). The homepage full shot is 1440 × 7436. The phone homepage full shot is 780 × 12616.
