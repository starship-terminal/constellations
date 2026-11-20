# Components

Public marketing controls measured on runway.com, plus the signed-out login form measured in the T3 preview browser. Crops are 2x viewport screenshots from headless Chrome. The preview browser stopped producing screenshot frames before a login shot could be saved, so the login controls have values and no crop.

| Component | State | Evidence |
|---|---|---|
| Button, primary | Default | [button-primary-default.png](components/crops/button-primary-default.png). Fill `#262626`, label `#ffffff`, radius 6px, height 32px, padding 6px 10px, 14px weight 600. |
| Button, secondary | Default | [button-secondary-default.png](components/crops/button-secondary-default.png). Fill `#eef1f5`, label `#1a1a1a`, same size as primary. |
| Button, inverse | Default | [button-inverse-default.png](components/crops/button-inverse-default.png). Fill `#f7f7f7`, label `#0c0c0c`, radius 8px, height 40px, padding 8px 12px, 16px. |
| Button, ghost on banner | Default | [button-ghost-default.png](components/crops/button-ghost-default.png). Fill `rgba(247, 247, 247, 0.05)`, 1px outline `rgba(255, 255, 255, 0.75)`, radius 4px, height 28px. |
| Button, plan outline | Default | [button-plan-default.png](components/crops/button-plan-default.png). Transparent fill, 1px border `#0c0c0c`, radius 9999px, height 36px. |
| Button, plan filled | Default | [button-plan-selected.png](components/crops/button-plan-selected.png). Fill `#0c0c0c`, label `#ffffff`, radius 9999px, height 36px. |
| Button, accent | Default | [button-accent-default.png](components/crops/button-accent-default.png). Fill `rgb(44, 34, 250)`, label white, radius 9999px, height 34px. |
| Link, nav | Default | [link-nav-default.png](components/crops/link-nav-default.png). 16px weight 500, `#0c0c0c`, no underline. |
| Text field | Default | Sign-in email and password. White fill, 1px `#dfdfe4`, radius 8px, height 50px, padding 8px 12px, width 360px. No crop. |
| Switch | Yearly on | Pricing toggle track `#0c0c0c`, 40 by 24px, radius 9999px, padding 2px. Thumb colour was not read. No crop. |
| Tabs | Individual selected | Pill fill `#0c0c0c`, label white, height 36px, padding 0 16px, radius 9999px. Unselected label `#0c0c0c` on transparent. |

Hover, pressed, focus-visible, disabled, and loading were not captured. The buttons declare `hover:bg-black`, `active:bg-[#595959]`, and `focus-visible:ring-2 focus-visible:ring-blue-500`. Calling `focus()` did not apply `:focus-visible`, so the ring colour is a class name, not a computed ring.

## Gaps

- Icon button, text area, checkbox, radio, menu, tooltip, dialog, toast, avatar, badge, and table were not on the pages that painted.
- The enterprise page has a sales form (name, email, company, title, phone, two selects). Fields computed transparent fill, border `rgba(102, 110, 122, 0.4)`, padding 8px 14px, height 41px. The form was not submitted and has no error state.
- Login has no screenshot. Preview frames stopped before `preview_snapshot` could save one.
