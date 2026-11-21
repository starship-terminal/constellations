# Portrait components

Values are computed styles from portrait.so on 2026-11-21, viewport 1440 by 900, unless a row says 2026-11-19. Crops are in [components/crops/](components/crops). A state that was not on the public page is a gap.

## Button

Primary face (Create your Portrait on `/pages`, Apply for early access on `/wallet`): inner span background `#2c2c2c` (`gray.700`), text white, height 44px, padding 0 20px, pill radius, font-weight 540, stacked shadow at 3% black. The outer button is transparent. See [button-primary-default.png](components/crops/button-primary-default.png).

Sign up: white inner face, text `#2c2c2c`, height 36px in the header, inner face 30px. The ring is `linear-gradient(90deg, rgb(38, 192, 255), rgb(230, 0, 194) 20%, rgb(255, 73, 78) 40%, rgb(255, 161, 62) 60%, rgb(255, 200, 55) 80%, rgb(0, 204, 61))`. See [button-signup-default.png](components/crops/button-signup-default.png).

Log in: transparent face, text `#585858`, height 36px, padding 0 16px, pill, weight 540, 14px. Focused outline was `1px none rgb(0, 95, 204)`: no ring was painted. See [button-login-default.png](components/crops/button-login-default.png).

Points "Sign up or log in": dark pill, not clicked. See [button-points-default.png](components/crops/button-points-default.png).

Editor Login: white pill on the signed-out wall. Not clicked. See [button-editor-login-default.png](components/crops/button-editor-login-default.png).

Disabled, loading, pressed, and a live hover were not captured on this pass.

## Link

Footer links (Pages and the rest) computed 16px, color `#797979`. The wallet announcement is a pill link. See [link-wallet-pill-default.png](components/crops/link-wallet-pill-default.png).

## Text field

Homepage username field: input height 78px, padding `0 140px 0 210px`, font 36px, color `#1b1b1b`, placeholder "username", empty. The email field from 2026-11-19 was not opened. Sign in with email was not clicked.

## Text area, select, checkbox, radio, switch

Not present on the public pages or the empty Sign in dialog.

## Tabs

Points page: Dashboard is the selected tab. Leaderboard is labelled "(soon)" and was not a second measured control. See [screenshots/points-light-default.png](screenshots/points-light-default.png).

## Menu

Desktop Menu (`aria-label="Menu"`) stayed `aria-expanded="false"` after a click at 1440. At 390 it opens a drawer with Home and Introducing Portrait Wallet. See [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). The 2026-11-19 editor account menu was not re-opened.

## Dialog

Log in and Sign up open one dialog, 420 by 277 px, white, radius 16 px, text `#202020`. Buttons: Close, Sign in with Portrait Wallet, Sign in with email, Sign in with other wallet. None of the three sign-in buttons were clicked. No email field was on screen. See [dialog-signin-default.png](components/crops/dialog-signin-default.png).

## Card, badge, avatar

New badge: background `#dff3ff`, text `#084e72`, 12px, weight 600, height 24px, pill, padding 0 10px. See [badge-new-default.png](components/crops/badge-new-default.png). Blog cards are on [screenshots/blog-light-default.png](screenshots/blog-light-default.png). Editor avatar was not re-measured.

## Tooltip, toast, table, list row

Not present.

## Empty states

`/pricing`, `/plus`, and `/signup` render "Uh oh / This user does not exist." with Go to home. See [screenshots/missing-light-default.png](screenshots/missing-light-default.png). `/editor` renders "You are not logged in" and a Login button that was not clicked. See [screenshots/editor-light-wall.png](screenshots/editor-light-wall.png).
