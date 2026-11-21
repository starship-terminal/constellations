# Measurements

Read on 2026-11-21 from https://digg.com/ in headless Chromium, viewport 1440 x 900, devicePixelRatio 1. Dark readings used `<html class="... dark">` after the theme cycle button. Phone layout was photographed at 390 x 844, devicePixelRatio 2, and not re-measured for tokens.

Full dumps stay in `~/.design-systems/digg/readings/` (`vars-light.json`, `vars-dark.json`, `colors-computed.json`, `components.json`). They are not committed.

## Semantic colours

Canvas samples of computed `var(--name)`. Alpha is 1 unless noted.

| Role | Light | Dark | Authored |
|---|---|---|---|
| background | #fdfdff | #161617 | hex on `:root, .light` and `.dark` |
| foreground | #161617 | #fdfdff | hex |
| card | #ffffff | #1c1c1f | dark authored `#1c1c1f` |
| popover | #ffffff | #27272c | dark authored `#27272c` |
| primary | #1c66eb | #1c66eb | `var(--blue-500)` |
| secondary | #f0f0f5 | #252525 | dark authored `#242424`. Sample differed by one step. Token keeps `#242424`. |
| muted-foreground | #151517 at 0.702 | #fefeff at 0.702 | dark authored `#fdfdffb3` |
| border | #000000 at 0.078 | #ffffff at 0.078 | dark authored `#ffffff14` |
| ring | #ababbf | #1c66eb | dark aliases `--blue-500` |
| destructive | #cc434d | #cc434d | `var(--red-600)` |
| success | #6aa15a | #6aa15a | sampled `--green-500` |
| sidebar | #f8f8fb | #0f0f10 | dark authored `#0f0f10` |
| brand-text | #1c66eb | #6ba4ff | dark aliases `--blue-300` |

## Components (light, home or login)

| Control | Height | Radius | Font | Fill |
|---|---|---|---|---|
| Sign up | 40px | 26px | 14px / 500 | #1c66eb |
| Log in | 40px | 26px | 14px / 500 | #f0f0f5 |
| Feed View trigger | 36px | 26px | 14px / 400 | translucent secondary |
| Email field | 36px | 8px | 14px / 400 | transparent |
| Continue | 36px | full | 14px / 500 | #1c66eb |
| digg it | 44px | 999px | 14px / 500 | page |
| Sidebar link | 40px | full | 14px / 600 | selected uses secondary |
| Source avatar | 24px | full | | |
| Post item | 142px tall in one reading | 18px | 14px | transparent, hover secondary |

## Layout

`innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 1, `visualViewport.scale` 1. Aside x 0, width 255, height 900. Main x 256, width 1184.

## Motion

Sign up computed `transition: 0.15s cubic-bezier(0.4, 0, 0.2, 1)`. Declared `--default-transition-duration: .15s`, `--ease-out: cubic-bezier(0, 0, .2, 1)`, `--ease-in-out: cubic-bezier(.4, 0, .2, 1)`.

## Not captured

Pressed, disabled, loading, error, overlay, scrim, green ramp steps other than 500, reduced-motion durations, story headline size, focus ring pixel width.
