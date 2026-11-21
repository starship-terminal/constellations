# Workflow components

Public marketing site only, captured 2026-11-21 from https://www.workflow.design/. The signed-in app was not entered. Crops are 2x element screenshots of controls that exist on the public pages.

| Component | States | Crop | Notes |
|---|---|---|---|
| Button | default, hover, focus-visible | [button-default](components/crops/button-default.png), [button-hover](components/crops/button-hover.png), [button-focus-visible](components/crops/button-focus-visible.png) | Header "Try now". 40px tall, 8px radius, fill `#f6f6f6`, hover `#ececec`. Pressed was forced with CDP and did not paint a distinct fill. Not captured as its own crop. |
| Link | default, hover | [link-default](components/crops/link-default.png), [link-hover](components/crops/link-hover.png) | Header "Features". Colour stays `#1a1a1a`. No underline on the expanded nav item. |
| Tabs | default, selected | [tab-default](components/crops/tab-default.png), [tab-selected](components/crops/tab-selected.png) | Home asset tabs: Live websites, Figma, Images, Videos, Presentations. |
| Text field | not present |  | `/contact` has no input, textarea, or form. It is a contact directory of links. |
| Menu | open | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png) | Phone nav drawer at 390. Desktop has no dropdown menu. |
| Dialog | demo overlay | [home-light-demo-open](screenshots/home-light-demo-open.png) | "Watch demo" overlay on the home page. |

## Not present on the public site

Icon button, text field, text area, select, checkbox, radio, switch, tooltip, toast, table, avatar, badge as a product control. The pricing page uses check marks in marketing copy, not a checkbox control.

## Gaps

- Disabled, loading and error states of the button: not shown on the public site.
- Form validation: no public form was found. Not present.
- App components (comment pin, version menu, approve button, inbox, command bar): behind `https://app.workflow.design/users/sign-in`. Not captured.
- Dark theme variants: the marketing site has no theme switch. Not present.
