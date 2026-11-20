# Measurements

Read 2026-11-19 from the T3 preview tab `https://sg.trip.com/`, then `/hotels/`, `/pages/support/`, and `/account/signin`. No Cloudflare challenge on those loads. devicePixelRatio 2. visualViewport scale 1.

## Viewport

| Pass | innerWidth | innerHeight | Page |
|---|---|---|---|
| Token dump | 1169 | 731 | home |
| Resize | 1440 | 900 | home |

The resize request was 1440 by 900. The reported viewport after resize was 1280 by 800, then `innerWidth` read back as 1440 and `innerHeight` as 900. The CSS values are the ones labelled here.

## Computed controls

| Element | Width | Height | Background | Text | Font | Radius | Other |
|---|---|---|---|---|---|---|---|
| `.mc-lhd-header-content` | 1440 | 66 | `#fff` | | 400 16px Trip Geom | 0 | |
| `.mc-lhd-logo` | 133 | 32 | transparent | `#121826` | | 0 | |
| `.mc-lhd-login-btn` | 112 | 34 | `#2c61fe` | `#fff` | 500 14px/18px | 4px | padding 8px |
| `.mc-srh-box.experiment-e` | 1096 at 1440, 825 at 1169 | 260 | `#fff` | | | 16px | shadow rgba(7,20,60,.16) 0 0 4px, rgba(7,20,60,.12) 0 8px 32px |
| Search `button.tripui-online-btn-large` | 106 | 48 | `#2c61fe` | `#fff` | 700 16px/24px | 4px | padding 0 16px |
| Active tab label | 144 | 21 | transparent | `#2c61fe` | 500 14px/21px | 0 | |
| Destination input | 267 at 1440 | 48 | transparent | `#121826` | 700 16px | 0 | placeholder Where to? |
| Field row `.z5SApYdkQdnm44Bv3aS2` | 1050 | 66 | transparent | | | 4px | border 1px rgb(218,223,230) |
| `.slogan-desc` | | 48 | transparent | `#fff` | 700 40px/48px | | |
| `footer.mc-ft` | | 546 at 1440 | rgb(245,247,250) | `#121826` | | | |
| Hotels `h1` | 140 | 48 | transparent | `#fff` | 700 48px/48px | | |
| Hotels body | 1169 | | rgb(246,247,250) | | | | |
| Hotel card | 264 | 371 | `#fff` | | | 8px | border 1px #d4d7de, shadow 0 2px 6px rgba(0,0,0,.08) |
| Support banner | 1169 | 316 | rgb(4,124,136) | | | | |
| Support `h1` | 410 | 68 | transparent | `#fff` | 700 48px/68px | | |
| FAQ chip | | 42 | rgb(245,247,250) | `#121826` | 400 14px/18px | 4px | padding 12px 16px |
| Email input | 378 | 56 | `#fff` | `#121826` | 700 16px/22px | 4px | rest border 1px #d4d7de; focused border rgb(44,97,254) |
| Continue with email | 378 | 56 | rgb(206,210,217) | `#fff` | 700 18px/24px | 4px | disabled |
| Continue with Google | 378 | 56 | rgb(66,133,244) | `#fff` | | 4px | |
| Continue with Apple | 378 | 58 | `#fff` | `#000` | | 4px | border 1px #d4d7de |

## Stylesheet hover rules

| Selector | Declaration |
|---|---|
| `.tripui-online-btn-solid-primary:hover:not(:disabled)` | background-color rgb(41, 83, 214) |
| `.mc-lhd-login-btn:hover` | background-color rgb(44, 89, 229) |
| `.experiment-e .mc-srh-box__tab-item:hover .mc-srh-box__tab-name` | color var(--smtcColorTextBrand, #2c61fe) |

## Fonts

Computed on `html`: `"Trip Geom", "system-ui", -apple-system, Roboto, Helvetica, Arial, sans-serif` at 16px. `@font-face` for Trip Geom at weights 400, 500, 700. `theme-color` meta is `#FFFFFF`.

## Screenshot status

`preview_snapshot` failed twice with: The browser is not producing screenshot frames. A headless Chromium navigation to https://www.trip.com/ returned 200 and landed on https://verify.trip.com/static/tripVerify.html. That frame was deleted and not copied into this package.
