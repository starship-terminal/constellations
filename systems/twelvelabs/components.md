# Components

Values come from `getComputedStyle` on 2026-11-19. Crops are absent because `preview_snapshot` returned "The browser is not producing screenshot frames".

| Component | State read | Values |
|---|---|---|
| Button, paper | Home Try Free, default | Background `#f4f3f3`, label `#1d1c1b`, radius 18px, padding 18px 24px, height 60, Milling Duplex 1mm 16px |
| Button, ghost | Home Talk to Sales, default | Background `rgba(244, 243, 243, 0)`, label `#f4f3f3`, radius 18px, padding 18px 24px, height 60, border none |
| Button, inverse | Open menu Try Free and pricing Choose Plus, default | Background `#1d1c1b`, radius 14px, padding 18px 16px, height 44 on the menu and 48 on pricing. Label colour on the dark face was not read apart from the anchor default |
| Button, auth | Login Continue, default | Background `#171717`, label `#f4f4f4`, radius 6px, padding 8px 12px, height 40, Geist 16px |
| Button, social | Login Continue with Google, default | Border `rgba(0, 0, 0, 0.24)`, text `#171717`, radius 6px, height 40. Not clicked |
| Text field | Login email, focused, filled | Border 1px `#1d1c1b`, padding 6px 8px, radius 6px, height 34, Geist 14px, box-shadow `#1d1c1b` 0 0 0 1px. Outline none |
| Link | Footer Platform Overview, default | `#1d1c1b`, Milling Duplex 1mm 16px, no underline |
| Nav | Header at 1169px | Bar 60px, background `rgba(29, 28, 27, 0.1)`, logo link 159 by 32, menu button 28 by 28. Desktop link row was not in the layout |
| Menu | Open | Panel `#f4f3f3`, rows padding 15px 0, labels 16px `#1d1c1b` |
| Badge | Home New, default | Text `#dae971`, 11px, wrapper padding 2px 7px, radius 99px. Wrapper background was transparent |
| Card | Home Jockey promo | Background `rgba(65, 64, 62, 0.6)`, radius 20px, padding 24px, inset shadows |
| Card | Login | Background `rgba(255, 255, 255, 0.6)`, radius 80px, 551 by 607, inset white shadows |
| Segment | Pricing Monthly, selected | Background `#1d1c1b`, radius 12px 0 0 12px, padding 10px 16px, height 40. Selected label computed `#f4f3f3` |
| FAQ row | Pricing, closed | Question text `#1d1c1c`, 20px / 30px. Open state not clicked |
| Cookie dialog | Osano, default | Background `#ececec`, radius 20px, padding 24px, text `#1d1c1b` 14px, buttons black face, radius 12px, padding 10px 18px |

## Gaps

- Hover, pressed, disabled, loading and error were not forced.
- Checkbox, radio, switch, select, textarea, tabs, tooltip, toast, table, avatar and list row were not on the pages read.
- The HubSpot contact form is in an iframe with reCAPTCHA. Fields were not entered, so their styles are a gap.
- Password field was visible and not filled. Its unfocused border computed as `rgba(0, 0, 0, 0.16)`.
- Dark theme was declared for six Framer tokens and was not painted. The live pages stayed on `#f4f3f3` while `prefers-color-scheme` was dark.
- Phone width 390 was not captured. The live CSS viewport was 1169 by 731.
