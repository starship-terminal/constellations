# Components

Inventory of the signed-out controls that were measured on 2026-11-19. Crops are missing because the preview browser did not produce screenshot frames and headless Chromium was blocked with HTTP 403.

| Component | State | Evidence |
|---|---|---|
| Button, Get started | default | [raw/css-vars.json](raw/css-vars.json) `homeGetStarted`: 44px tall, padding 12px 16px, radius 1600px painted, `#1C1B1B` on `#FCFCFC` text, The Future 14/19.6 weight 500 |
| Button, Log in (marketing) | default | Same file `homeLogIn`: 44 by 72, translucent off-white fill, `#1C1B1B` text |
| Button, Register now | default | Same file `registerNow`: 64 by 160, padding 20px 32px, `#FCFCFC` fill, `#1C1B1B` text, 16/22.4 weight 500 |
| Button, Log in (app) | default | Same file `loginSubmit`: 54 by 380, padding 0 20px, radius 1000px, `#F2F2F2` fill, `#0A0A0A` text, shadow `0 1.5px 3px #0000000f` |
| Button, Log in with a passkey | default, not clicked | Same file `loginPasskey`: 54 by 380, `#5C5C5C` fill, white text |
| Link | default | Footer link 18/25.2, padding 6px 12px, radius 12px. Login wordmark link `#9E9EFF` |
| Text field, hero email | empty | 64 by 320, 1px `#94908D` border, radius 100px, transparent fill, 18px The Future |
| Text field, login email | empty | Wrapper 52 by 380, fill `rgba(255,255,255,0.08)`, 1px `rgba(255,255,255,0.1)` border, radius 12px. Label 14px weight 700 at 50% white |
| Nav item | closed | Chequing button, padding 6px 12px, radius 12px, 14px weight 500, height 32px |

## Gaps

- Hover, focus-visible, pressed, disabled, loading, and error were not forced. Focus colour tokens exist (`--ws-color-focus-ring-primary` `#1C1B1B`, login `--states-border-focus` `#FFFFFF`) and were not seen painted on a focused control.
- Checkbox, radio, switch, select, text area, tabs, tooltip, toast, table, avatar, and badge were not on the pages that were opened.
- No element crop exists. `components/crops/` is empty.
