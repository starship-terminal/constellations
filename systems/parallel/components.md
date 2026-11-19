# Components

Measured on useparallel.com, signed out, 2026-11-19. Desktop shots are 1440×900. Crops are from those shots.

| Component | State | Value | Crop |
|---|---|---|---|
| Button, primary | default | Fill rgb(31, 31, 31), label rgb(255, 255, 255), 14px/500 Inter, radius 12px, height 43px, padding 12px 20px | [button-primary-default.png](components/crops/button-primary-default.png) |
| Button, LinkedIn | default | Fill rgb(255, 255, 255), border 1px rgb(230, 230, 230), label rgb(41, 41, 41), radius 12px, height 43px | [button-secondary-default.png](components/crops/button-secondary-default.png) |
| Button, trial | default | Gradient rgb(239, 110, 7) to rgb(255, 183, 125), label rgb(255, 255, 255), 19px/500, radius 12px, height 61px | [button-trial-default.png](components/crops/button-trial-default.png) |
| Button, nav | default | Sign up fill rgba(255, 255, 255, 0.12), label rgba(255, 255, 255, 0.88), radius 10px, height 40px. Try free fill rgb(31, 31, 31), label rgb(255, 255, 255) | [button-nav-default.png](components/crops/button-nav-default.png) |
| Text field | default | Fill rgb(244, 243, 241), text rgb(15, 15, 15), 16px Inter, tracking -0.32px, radius 12px, height 41px, padding 10px 12px | [text-field-default.png](components/crops/text-field-default.png) |
| Text field | focus | Border rgb(15, 15, 15) 1px. Outline style none | not cropped |
| Text field | error | Message "Password must be at least 8 characters long", rgb(239, 7, 7), 14px Inter. Triggered with `not-an-email` and a one-character password. Not submitted | not cropped |
| Search | default | Field container rgb(253, 253, 253), radius 15px, height 66px. Arrow 38px, gradient rgb(239, 110, 7) to rgb(255, 183, 125) | [search-default.png](components/crops/search-default.png) |
| Chip | default | Fill rgba(255, 255, 255, 0.1), border 1px rgba(255, 255, 255, 0.3), label rgb(255, 255, 255), 14px/500, radius 9999px, height 36px, padding 10px 16px | [search-default.png](components/crops/search-default.png) |
| Card | default | Fill rgb(255, 255, 255), border 1px rgb(230, 230, 230), radius 32px, padding 32px 24px, 472×532 | [card-default.png](components/crops/card-default.png) |
| Link | default | "Create new account" and "Sign in" on the auth cards. Colour rgb(5, 5, 5), 14px/500, underline on the account link | [card-default.png](components/crops/card-default.png) |
| Nav | default | Logo plus Explore, Talent, Employers, Sign in, Sign up over the homepage photo | [nav-default.png](components/crops/nav-default.png) |

## Gaps

- Hover, pressed, disabled, loading, and selected were not held. The jobs "Jobs" tab was filled white and "Companies" was not. That is the only selected state read.
- Checkbox, radio, switch, select, textarea, tabs, menu, tooltip, dialog, toast, table, avatar, and badge were not on the signed-out pages that were opened.
- The homepage Explore control is a button. Its menu was not opened.
- Signup has no email field. The only action is LinkedIn. That button was not clicked.
- Focus painted a 1px black border and `outline-style: none`. A focus ring was not visible.
- Declared `--shadow-primary` (8px 8px 0 #0f0f0f) was not on the captured controls.
