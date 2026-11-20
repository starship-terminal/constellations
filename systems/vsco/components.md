# Components

Measured on the live preview tab at 1169×731 on 2026-11-19. The preview browser did not produce screenshot frames, so there are no crops.

| Component | Where | What was measured |
|---|---|---|
| Button, gold | Home, Try VSCO for free | 35px tall, 999px radius, #ffbc3c fill, #000000 text, 600 weight, 11.4307px, 1.14307px tracking, uppercase |
| Button, solid | Home, Explore VSCO and nav Try for free | Black fill, white text, 2px black border on the nav size, 999px radius |
| Button, outline | Home, Explore creative tools | Transparent fill, 1px #000000 border, black text |
| Button, nav outline | Home, Log in | 32px tall, 1px #d9d9d9 border, black text, 13px / 500 |
| Button, pink | Home promo bar, Learn more | 30px tall, #ff0877 fill, white text, 700 weight |
| Button, disabled | Login submit while fields were empty | 42px tall, 328px wide, #aaaaaa fill, 15px / 500, uppercase |
| Button, oauth | Login, Google and Apple | 46px tall, 2px #dddddd border, transparent fill, 100px radius |
| Link | Login, Forgot password? | Transparent, black, 15px / 500, no underline measured |
| Text field | Login identity and password | Box 40px tall, 328px wide, 4px radius, 1px #d9d9d9 resting border, 0 16px padding. Input itself is 14px / 18px |
| Field label | Login Email* | 11px / 500 / 14px, #525252 |
| Focus | Login identity after focus() | Box border became #525252. Outline stayed none |
| Badge | Plans, Best for business | #e9f8ff fill, #386584 text, 4px radius, 9.67216px / 600 |
| Badge | Plans, Most popular | #edba58 fill, #000000 text, 4px radius |
| Badge | Home, NEW | White fill, black text, 4px radius, 13.1893px / 600 |
| Card | Plans, VSCO One | #000000 fill, white text, 8.79287px radius, 17.5857px padding, 358×649 |
| Card | Plans, Pro | #ffffff fill, 1px rgba(0,0,0,0.1) border, same radius and padding |
| Nav | Home and plans | White, 88px tall, 0 40px padding, no shadow |
| Brand | Marketing nav | 44×44 link |

## Gaps

- Hover, pressed, and loading were not forced on a live control. Declared hover includes `.button.is-outline:hover` filling with `var(--black)` and `.button.is-alternate:hover` filling `#e4e4e4`.
- Checkbox, radio, switch, select, textarea, tabs, menu, tooltip, dialog, toast, avatar, and table were not opened as product UI. Cookie-center controls were present and were not measured as product components.
- An invalid email blur painted no error. Destructive confirmation was not present.
- No component crops. The preview browser returned "The browser is not producing screenshot frames."
