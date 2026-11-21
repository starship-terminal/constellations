# Components

Public signed-out controls on epidemicsound.com, measured 2026-11-21 at 1440. Crops are in [components/crops/](components/crops/).

| Component | States | Where |
|---|---|---|
| Button, primary | default, hover, focus-visible | Header "Create free account". 44px, 16px horizontal padding, pill, black fill, white Inter 14/600. Hover fill #272727. Focus outline 2px white. [button-primary-default](components/crops/button-primary-default.png) |
| Button, secondary | default, hover | "Contact sales". 56px, grey-blue 12% fill, black text, Inter 16/600, pill. [button-secondary-default](components/crops/button-secondary-default.png) |
| Button, plan | default | "Get 30 days free" on pricing. 56px, black pill. Links to checkout, which was not opened. [button-plan-default](components/crops/button-plan-default.png) |
| Nav button | default, open | Music and the other header menus. 44px, transparent, pill. Open state fills the pill. [nav-button-open](components/crops/nav-button-open.png) |
| Menu | open | Header dropdown `#top-nav-panel-music`. White panel over the page. [menu-music](components/crops/menu-music.png) |
| Segment | default, selected | Individuals and Businesses on pricing. [segment-individuals](components/crops/segment-individuals.png) |
| Switch | on | Billing period on pricing. 40 by 24, black, pill. [switch-on](components/crops/switch-on.png) |
| Link | default | Footer links, black at 60% opacity, Inter 16/500. |
| Search field | default | `/music/` field, 56px, translucent fill. Text was typed and not submitted. |
| Card | default | Pricing plan cards, white on the off-white page. |

## Gaps

Text area, select, checkbox, radio, tabs, tooltip, dialog (other than the hidden cookie banner), toast, table, avatar, and badge were not present as public controls on the pages that were measured.

Disabled, loading, error, and pressed states were not captured. Pressed was not held. No form was submitted, so validation error is not captured.

Login and signup fields sit behind `/login/` and `/oauth_registration/`. Those branches were stopped.
