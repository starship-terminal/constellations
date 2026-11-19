# Components

Measured on the signed-out pages at 1169 by 731, `html.dark`. Crops were not
taken: the preview browser did not produce screenshot frames.

| Component | Where | Values |
|---|---|---|
| Header | Home, every page | Black fill, 1px bottom rule in the brand yellow `rgb(255, 240, 87)`, height 70px |
| Nav link | RADIO (current), MOODS (rest) | kernStandard italic 15px. Current is yellow at weight 700. Rest is `rgba(255, 240, 87, 0.5)` at weight 400. Gap 24px. Transition 300ms, cubic-bezier(0.4, 0, 0.2, 1) |
| Menu button | MENU | Yellow fill, black italic 15px weight 700, radius 30px, 69 by 24 |
| Message button | Home, under the curator | Yellow pill, padding 7px 12px, black 12px weight 700, radius 9999px, height 23px |
| Listen button | Home player | Yellow circle, 65px, radius 9999px, 150ms colour transition |
| Icon button | Like, share | Yellow circle, 40px, 2px black border, radius 9999px, opacity 0.4 |
| Track card | Home | Yellow fill, padding 16px 28px, radius 0 |
| Auth link | /login SIGN UP | Black fill, yellow text, 2px black border, 36px tall, 16px weight 700, letter-spacing 0.8px, uppercase, radius 0 |
| Auth link, secondary | /login SIGN IN | Transparent fill, black text, 2px black border, same type |
| OAuth button | Continue with Google, Continue with Apple | 48px square, 2px black border, transparent fill, radius 0. Not pressed |
| Schedule title | MIND SPRAY | kernStandard 24px / 32px weight 800, black, uppercase |
| Hour | 04 | kernStandard 36px / 36px weight 700, yellow |
| About hero | 24/7 MUSIC | kernStandard 60px / 64px weight 800, black, on a yellow section |
| Privacy title | PRIVACY NOTICE | kernStandard 36px / 36px weight 700, yellow, uppercase |
| Privacy body | notice paragraphs | kernStandard 14px / 20px weight 400, yellow |
| Curator name | Dina J | gtAlpina 28.8px / 40px weight 400, yellow |
| Clock | 01:37 | Roboto 60px / 60px weight 300, yellow at 0.3 alpha |

## Gaps

- Text field, text area, select, checkbox, radio and switch were not on the signed-out pages.
- Hover, focus-visible, pressed, disabled, loading and error were not forced. A global `:focus, :focus-visible` rule sets `outline: none` and `box-shadow: none`.
- Toast (Sonner) is in the stylesheet and was not on screen.
- Dialog, menu drawer, search and the Alexa modal were not opened.
- No component crop exists. `components/crops/` is empty for that reason.
