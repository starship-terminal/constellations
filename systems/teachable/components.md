# Components

Public marketing controls, plus the signed-out Teachable Accounts sign-in form. Values are computed styles. Crops are from the 1440 viewport screenshots.

| Component | States | Crop | Values |
|---|---|---|---|
| Button, primary | default | [button-primary-default.png](components/crops/button-primary-default.png) | `light.component.button.*`. Fill `#e6ff32`, text `#000000`, 1px black border, radius `900px`, padding `14.9666px 22.4499px`, height `48px`, Peridot 600 / `14.9666px`. Hover did not change background, border, or shadow. |
| Button, black | default | home screenshot | `light.color.action.black` / `blackText`. Same pill radius. "Explore demo". |
| Button, outline on nav | default | [button-outline-nav-default.png](components/crops/button-outline-nav-default.png) | Transparent fill, 1px white border, white text, radius `900px`. "Contact sales". |
| Button, plan | default, featured | [card-plan-featured.png](components/crops/card-plan-featured.png) | Idle: white fill, `#1c4774` text and border. Featured: `#1c4774` fill and white text. Radius `900px`. |
| Link, nav | default, hover | [link-login-default.png](components/crops/link-login-default.png) | Creator login is underlined at rest and loses the underline on hover. Menu links gain an underline on hover. White, weight 600, `14.9666px`. |
| Tabs, billing | idle, selected | [tabs-billing-default.png](components/crops/tabs-billing-default.png) | Pill tabs. Selected is black fill and white text. Idle is transparent with a 1px black border and `#222222` text. Yearly is the selected tab on first load and carries a "22% OFF" label. |
| Card, plan | default, featured | [card-plan-default.png](components/crops/card-plan-default.png), [card-plan-featured.png](components/crops/card-plan-featured.png) | Featured Builder card has a `2px solid #1c4774` border and radius `8.98px`. Title `29.9333px` / 600. Price `52.3832px` / 700. |
| Text field | default, focus | accounts sign-in, no crop | Email input: white, `1px solid #4a4e6d`, radius `5px`, height `40px`, padding `8px 32px 8px 16px`. Focus kept that border and drew no outline. Password border is `#e2e2e9`. |
| Button, login | default | accounts sign-in, no crop | `light.component.loginButton.*`. Fill `#e6ff32`, text `#212338`, radius `4px`, height `38px`, width `420px`. |
| Nav | default | [nav-default.png](components/crops/nav-default.png) | Black bar, height `79px` at 1440. At 390 the bar is `59px` and a `20px` menu button is visible. |
| Link, footer | default | home screenshot, below the fold | `#a0a0a0`, `17.2116px`, weight 400, no underline. |

## Gaps

- Checkbox, radio, switch, select, textarea, toast, dialog, tooltip, table, avatar, and badge were not on the signed-out pages that loaded. The "22% OFF" label is text inside the selected tab, not a separate badge component with its own fill.
- Icon button: the stories slider buttons are `45px` black circles. Their hover was not measured.
- Menu: the Products and Resources dropdowns were not opened as a stable overlay.
- FAQ accordion: a click on "Can I cancel my account at any time?" did not expand a panel in the headless session.
- Disabled, pressed, loading, and error states were not shown. The accounts form was not submitted.
- Focus-visible on marketing controls was not visible after one Tab. Accounts email focus did not add an outline.
- Dark theme: the public site and the signed-out accounts page have no theme control.
- Login screenshots: the preview browser did not produce frames, and a headless session was not started against the login host.
