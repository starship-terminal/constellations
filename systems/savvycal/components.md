# Components

Public marketing controls measured on savvycal.com, plus the signed-out login form. Crops are 2x viewport screenshots from headless Chrome. Values come from computed styles.

| Component | State | Evidence |
|---|---|---|
| Button, primary | Default | [button-primary-default.png](components/crops/button-primary-default.png). Fill `#f54320`, label `#ffffff`, pill radius, header size 34px, padding 4px 14px, 14px weight 500. Hero size is 46px, padding 10px 20px. [button-primary-hero.png](components/crops/button-primary-hero.png) |
| Button, ghost | Default | [button-ghost-default.png](components/crops/button-ghost-default.png). Transparent fill, label olive-950, pill, padding 4px 14px, height 34px. |
| Button, secondary | Default | [button-secondary-default.png](components/crops/button-secondary-default.png). Same as ghost at hero size, height 46px, padding 10px 20px. |
| Button, neon | Default | [button-neon-default.png](components/crops/button-neon-default.png). Fill `#b9ff78`, label olive-950, pill, height 46px, padding 10px 20px. |
| Button, submit | Default | [button-submit-default.png](components/crops/button-submit-default.png). Fill `#b9ff78`, label zinc-900, 1px border the same green, pill, height 38px, padding 8px 20px, width 448px. |
| Button, OAuth | Default | [button-oauth-default.png](components/crops/button-oauth-default.png). Fill `#ffffff`, label zinc-900, radius 8px, height 48px, padding 0 20px, GT America Standard 16px weight 500. Shadow is a 1px black ring at 5% plus `0 1px 3px` and `0 1px 2px` at 10% black. |
| Button, plan outline | Default | [button-plan-basic.png](components/crops/button-plan-basic.png). Fill white at 60%, label olive-950, inset ring olive-950 at 15%, pill, height 46px. |
| Button, plan filled | Default | [button-plan-premium.png](components/crops/button-plan-premium.png). Fill `#b9ff78`, label olive-950, pill, height 46px, full card width. |
| Link, nav | Default | [link-nav-default.png](components/crops/link-nav-default.png). 14px weight 500, olive-950, no underline. |
| Link, nav | Hover | [link-nav-hover.png](components/crops/link-nav-hover.png). Computed color `rgb(245, 67, 32)`. |
| Link, underline | Default | [link-underline-default.png](components/crops/link-underline-default.png). 14px weight 500, zinc-900, underline, radius 4px. |
| Text field | Default | [field-email-default.png](components/crops/field-email-default.png). Transparent computed fill, 1px border zinc-950 at 10%, radius 8px, height 36px, padding 5px 11px, 14px. |
| Text field | Focus | [field-email-focus.png](components/crops/field-email-focus.png). Painted ring sampled as `#00c951`. Forced focus computed a blue shadow that did not match the crop. |
| Checkbox | Checked | [checkbox-default.png](components/crops/checkbox-default.png). 24px, radius 6px, fill zinc-900 at 10%, inset ring the same. Arrived `aria-checked=true`. |
| Checkbox | Unchecked | [checkbox-unchecked.png](components/crops/checkbox-unchecked.png). Same box, check removed after a local click. Not submitted. |
| Tabs | Annual selected | [tabs-billing-annual.png](components/crops/tabs-billing-annual.png). Fill olive-950, label white, pill, padding 6px 16px, 14px weight 500. Monthly is transparent with olive-950 type. |
| Badge | Verified | Fill emerald-50, text emerald-700, pill, 10px weight 500, padding 0 6px, height 16px. No crop. |

Hover and pressed on the orange and neon pills did not change the computed fill. The classes declare `hover:bg-[#e03a18]` and `hover:bg-[#a8f560]`. Disabled and loading were not on the pages.

## Gaps

- Icon button, text area, select, radio, switch, menu, tooltip, dialog, toast, avatar, and table were not measured as product controls.
- The home and `/demo` calendars are public demos. They are not the signed-in scheduler.
- Signup was not opened. Login is email plus Google, Microsoft, and Fastmail. Those OAuth buttons were not pressed.
- Password reset was screenshotted and not submitted.
- Dark calendar tokens exist under `html.dark` and were not captured as a marketing theme.
