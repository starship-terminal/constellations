# Components

Public controls measured on me.sh and app.me.sh on 2026-11-21. Crops are in [components/crops/](components/crops). A state that was not driven is listed as not captured.

| Component | States captured | Notes |
|---|---|---|
| Logo link | default | Header mark, links to `/` |
| Nav menu button | default, opened | Releases, Resources, Company. Opens a `role="menu"` panel |
| Sign in link | default, hover | Opens `https://app.me.sh/login?signin` |
| Get started | default | Header outline button. Opens `https://app.me.sh/login` |
| Plan card | default | Pricing cards. Team card carries the orange border |
| Billing toggle | selected | Pay monthly / Pay annually. In-page only |
| Search field | default, focused, filled | Integrations catalog. Typing filters the list. Not submitted |
| Login email | default | Sign-in wall. Not filled |
| Identity buttons | default | Apple, Google, SSO. Not clicked |
| Filter chip | selected | Home feed demo chips. In-page only |
| Mobile menu toggle | opened | A `div.y0DxmG_toggle`, not a button. Opens the same three menus |

Not present on the public pages: checkbox, radio, switch, tabs, tooltip, toast, table, textarea, select.

Not captured: pressed, disabled, loading, error, and focus-visible rings. The marketing sheets declare no focus token, and the kit's forced-pseudo pass was not run.
