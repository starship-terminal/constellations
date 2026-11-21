# Cofounder components

Public marketing site and the signed-out login wall, measured on 2026-11-21. States that need a click on Google, GitHub or Email were not taken.

| Component | States captured | Where |
|---|---|---|
| Link (nav) | default, focus-visible | header on [screenshots/home-light-default.png](screenshots/home-light-default.png). Focus outline `#005fcc` 1px auto. |
| Button (header CTA) | default | white pill, 41px, 8px radius, text `#171717`. Opens the login wall. Crop: [components/crops/nav-cta-default.png](components/crops/nav-cta-default.png). |
| Button (Copy Setup Prompt) | default, focus-visible | transparent fill, white text, 8px radius. Focus outline 2px solid white. |
| Button (capability row) | default, hover, focus-visible | 47px, 10px radius, translucent white fill. Hover becomes `#ffffff`. Opens a dialog. |
| Dialog | opened | capability details. 16px radius, translucent `#f7f7f3` fill. [screenshots/home-light-capability-dialog.png](screenshots/home-light-capability-dialog.png). |
| Menu | opened (phone) | [screenshots/mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png). |
| Accordion (FAQ) | default, expanded | pricing page. Row height 68px. [screenshots/pricing-light-faq-open.png](screenshots/pricing-light-faq-open.png). |
| Tabs | pressed | home workflow and tool tabs. `aria-pressed` flips. No colour change was isolated. |
| Button (login) | default, hover, focus (Google only, not clicked) | three stacked buttons. Google is a dark pill. GitHub and Email are light pills. No email field. |
| Card | observed | resource cards and chapter cards. Values not isolated per card. |

## Not present on the public surface

Text field, text area, select, checkbox, radio, switch, toast, table, avatar, badge. The login wall has no field until "Continue with Email", which was not opened.

## Not captured

| Item | Reason |
|---|---|
| Pressed state of identity buttons | Clicking Google, GitHub or Email was refused. |
| Email step | The button was not clicked. |
| Signed-in app controls | Behind the login wall. |
| Dark theme on the marketing site | Not painted. Docs expose a dark switch. That tree was not measured. |
| Tooltip, toast | None appeared. Copy Setup Prompt showed no toast. |
