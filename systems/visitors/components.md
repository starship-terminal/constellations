# Components

Captured from the public homepage and the login page on 2026-11-21, signed out. Values are computed styles where a row says so, otherwise Observed. Crops were not cut: the preview stopped producing frames before a crop pass.

| Component | States seen | Evidence |
|---|---|---|
| Button, primary | Default. Background `#918df6` on the hero, `#9580ff` on the nav Register pill. White text, 500, pill radius, 44px hero / 32px nav | Computed on `/` |
| Button, quiet | Default. `rgba(0,0,0,0.03)` fill, `#666` text, pill, 44px | Computed on See demo and the Google / GitHub buttons |
| Button, disabled | Continue with email. Fill `#dad9fc`, white text, `cursor: not-allowed` | Computed on `/login` |
| Link | Register on the login card is `#2c78fc`, 14px, no underline | Computed on `/login` |
| Text field | Email, focused. Fill `#f5f5f5`, radius 12px, 40px tall, 2px `#918df6` outline plus a `#dad9fc` ring | Computed on `/login`. Empty, not submitted |
| Menu | Features menu, four cards, 218×116, radius 16px, tinted fills | Computed and [screenshots/home-light-features-menu.png](screenshots/home-light-features-menu.png) |
| Badge | NEW pill, sky at 8% fill, `#2c78fc` text, 32px | Computed on `/` |
| Card | Feature cards and the pricing card | Observed on the homepage tiles. Not measured after the frame stop |
| FAQ row | Closed. 44px, 16px/500, `#181925` | Computed on the first FAQ button |
| Segment | Monthly / Yearly pills, 32px | Computed, default only |
| Nav | Dark pill, fill `#14141f`, radius 24px, shadow-1 | Computed on `header` |

Not present on the pages that rendered: text area, select, checkbox, radio, switch, tabs (the hero demo tabs are buttons, not a tab widget that was measured), tooltip, dialog, toast, table, avatar, icon button as its own control.

Not captured: hover, pressed, loading, error, and a validation error. The email field was left empty, so Continue stayed disabled. Focus-visible was the email field's default focus, not a keyboard pass. Dark theme was not applied.
