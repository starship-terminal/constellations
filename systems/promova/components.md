# Promova components

Measured on the signed-out site on 2026-11-19. Crops are element screenshots from headless Chromium. The T3 preview browser returned "The browser is not producing screenshot frames", so these PNGs are the public-page fallback, not preview-browser frames.

| Component | States measured | Crop | Values |
|---|---|---|---|
| Nav bar | default | [nav-default.png](components/crops/nav-default.png) | White `#ffffff`, radius 30px, height 100px, padding 0 30px, inset 20px. Sticky. |
| Button, filled nav | default. Hover `#262626` and pressed `#404040` from stylesheet rules | [button-primary-nav-default.png](components/crops/button-primary-nav-default.png) | `#000` fill, `#fff` text, 40px height, 0 radius, 14px Nekst, uppercase |
| Button, outlined nav | default. Hover `#f5f5f5`, pressed `#e0e0e0` from stylesheet rules | [button-signup-default.png](components/crops/button-signup-default.png) | White fill, 1px `#000` border, 40px, 0 radius |
| Button, filled CTA | default. Transition `background-color 0.25s ease-in-out` | [button-primary-default.png](components/crops/button-primary-default.png) | `#000` / `#fff`, 60px height, 0 radius, 18px Nekst, often 700 |
| Button, outlined CTA | default (VISIT BLOG) | not cropped | Transparent fill, 0 computed border, 60px, letter-spacing 0.9px. The visible outline was not a CSS border |
| Button, auth submit | default | [signup-card-default.png](components/crops/signup-card-default.png) | `#000` fill, 60px, radius 10px, 18px Nekst, uppercase |
| Button, OAuth | default | same card | 50px, 1px `#000`, radius 0, Manrope 15px/700 |
| Link, nav trigger | default, opacity 0.2s ease-out | nav crop | Nekst 15px/400, transparent |
| Link, footer | default | not cropped | Manrope 18px/400, line-height 25.92px, no underline |
| Link, log in | default | signup card | Nekst 16px/500, underlined in the screenshot |
| Text field | default. Focus did not change border, outline, or shadow | signup card | 50px, radius 5px, padding 0 20px, 1px `rgba(0,0,0,0.3)`, Manrope 15px/500 |
| Text area | default on /who-we-are | not cropped | 120px height, radius 5px, padding 20px, same hairline |
| Search field | default on /blog | not cropped | Same field metrics, width 300px, placeholder "Article name, keywords" |
| FAQ row | closed and open | not cropped | Summary Nekst 24px. Open item padding 22px 20px, 1px `#000` border, answer Manrope 16px |
| Card, sign-up | default | signup card | White, radius 20px, padding 15px, width 400px, no shadow |
| Card, section | default | [home-light-default.png](screenshots/home-light-default.png) | Radius 30px at 1440, 20px at 390, width 1400 at 1440 |
| Promo modal | default, then closed | not cropped | `#dfe3ff`, radius 30px, padding 30px. Close button 36px, radius 50%, white |
| Announcement strip | default | nav crop | Yellow `#fff584` with a black "START SPEAKING" segment |
| 404 | default | not cropped | "page not found", Nekst 20px, hero `#bec8ff`, GO TO HOMEPAGE button 50px |

## Shared values

Filled actions are black on white type. Outlined nav actions are white with a 1px black border. Marketing buttons are square (`pGCWia_square_buttons`). The sign-up submit is the exception at 10px. Fields are 5px. Islands are 30px on desktop and 20px on the phone width.

## Gaps

- Hover and pressed fills for the nav buttons come from stylesheet rules, not a forced computed hover.
- Focus-visible was not painted on the email field.
- Disabled, loading, checkbox, radio, switch, select, tabs, toast, table, avatar, and badge were not on the captured signed-out pages.
- The outlined VISIT BLOG control computed a 0 border. Its visible edge is a gap.
- No dark theme was offered.
