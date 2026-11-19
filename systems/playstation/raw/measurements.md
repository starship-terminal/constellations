# Measurements

Read with `preview_evaluate` on a T3 preview tab, 2026-11-19. Viewport: innerWidth 1169, innerHeight 731, devicePixelRatio 2, visualViewport scale 1. `color-scheme` was `normal`.

`preview_snapshot` failed once with: "The browser is not producing screenshot frames. For a desktop tab, show or restore the T3 Code window and try again." No PNG was saved.

## Marketing home (`/en-sg/`)

| Element | Reading |
|---|---|
| body | color `rgb(31, 31, 31)`, font `sst, Arial, sans-serif`, 14px, weight 400. Background transparent |
| header parent section | background `rgb(255, 255, 255)` |
| `nav.shared-nav` | 64 by 492 px, font `SST, helvetica, arial, sans-serif`, weight 500, transition `0.55s height` |
| `.shared-nav__primary-button` | 11.375px, weight 500, padding `0px 20px 0px 5px`, height 64, color `rgb(31, 31, 31)` |
| `.web-toolbar__signin-button` | background `rgb(0, 112, 204)`, color `rgb(255, 255, 255)`, radius 999px, padding `0px 6px`, 14px, weight 500, letter-spacing 0.4px, 22 by 70 px |
| `a.cta__primary` | background transparent, radius 28px, padding 2px, margin 3.5px, height 38, 14px / 21px / 400, transition `0.1s all`. Color `rgb(255, 255, 255)` on the dark hero, `rgb(0, 104, 189)` on a light plate |
| `.txt-style-large-title` | 34px / 42.5px / 300 / letter-spacing 0.1px |
| `.txt-style-medium-title` | 22px / 27.5px / 300 / 0.1px |
| `.txt-style-small-title` | 18px / 22.5px / 300 / 0.1px |
| `.txt-style-base` | 14px / 21px / 400 / 0.1px. Secondary colour `rgb(107, 107, 107)` |
| `.txt-style-secondary` | 12px / 18px / 400, color `rgb(107, 107, 107)` |
| `.txt-style-utility` | 10px / 15px / 400 |
| `.hp-hero__banner.theme--dark` | background `rgb(9, 35, 145)`, color `rgb(255, 255, 255)` |
| `footer.site-footer-v2` | background `rgb(0, 67, 156)`, color `rgb(255, 255, 255)` |

Computed custom properties at this width (media-query override of the authored `:root` rule):

| Token | Computed |
|---|---|
| `--space-1` to `--space-13` | 2, 4, 7, 10, 14, 21, 28, 35, 42, 56, 70, 112, 224 px |
| `--corner-size-0` to `--corner-size-4` | 2, 3, 6, 12, 24 px |
| `--text-1` to `--text-11` | 8, 10, 12, 14, 18, 22, 27, 34, 43, 53, 67 px |
| `--mesh-gutter` | 14px |
| `--mesh-margin` | 42px |
| `--mesh-columns` | 12 |
| `--color-1-light` | 255 255 255 |
| `--color-5-light` | 107 107 107 |
| `--color-9-light` | 213 59 0 |
| `--color-10-light` | 0 104 189 |
| `--color-17-light` | 0 112 204 |

The authored `:root` rule (before the width override) declared different steps, including `--space-2: 5px`, `--space-4: 14px`, `--space-13: 288px`, `--corner-size-0: 3px`, `--corner-size-4: 48px`. Tokens use the computed values at 1169px.

## Store (`/en-sg/pages/latest`)

| Element | Reading |
|---|---|
| body | background `rgb(255, 255, 255)`, color `rgb(54, 54, 54)`, font `sst, helvetica, arial, sans-serif`, 14px |
| active tab `.tertiary-tab__link--active` | background `rgb(235, 238, 240)`, color `rgb(0, 0, 0)`, radius 24px, padding `4px 10px`, height 29, weight 500, 2px transparent border |
| `.psw-product-tile` | 313 by 261 px, radius 0, shadow none |
| price | 14px / 19.6px, color `rgb(54, 54, 54)` |
| badge `-50%` | background `rgb(0, 0, 0)`, color `rgb(255, 255, 255)`, 12.25px, weight 700, padding 4px, radius 3px, height 23 |
| `h1.psw-sr-only` | 36.75px / 51.45px / 300 |

## Sign-in wall

| Element | Reading |
|---|---|
| `h1` | "Sign in to PlayStation", color `rgb(255, 255, 255)`, 22px, weight 300, height 28 |
| field box | border `1px solid rgb(178, 178, 178)`, radius 6px, 38 by 422 px, background transparent |
| email input | padding `6px 6px 6px 10px`, 16px, color `rgb(255, 255, 255)`. Empty |
| label | color `rgb(255, 255, 255)`, 14px, weight 400 |
| Next | background `rgb(117, 117, 117)`, color `rgb(0, 0, 0)`, radius 999px, padding `0px 10px`, height 34, weight 700. Not clicked |
| Create an Account | background `rgba(255, 255, 255, 0.14)`, border `1px solid rgba(255, 255, 255, 0.8)`, color `rgb(255, 255, 255)`, radius 999px, height 34. Not clicked |
| links | color `rgb(36, 156, 255)`, 14px |
| html, body | background transparent. No solid page fill isolated |
