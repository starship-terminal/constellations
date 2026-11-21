# Components

Public components measured on https://theorg.com/ on 2026-11-21, signed out. Crops are in [components/crops/](components/crops). Values are computed styles, named against tokens where the colour matches.

| Component | States | Where |
|---|---|---|
| Sign up (nav) | default, hover, focus-visible, pressed | Home header. Blue pill, white label, 32px tall. Pressed is CDP `:active`. |
| Log in | default, hover, focus-visible, pressed | Home header. Transparent, dark label, faint fill on hover. |
| Pricing link | default, hover, focus-visible, pressed | Home header. |
| Start for free | default, hover, focus-visible, pressed | Home hero. Near-black pill, 48px tall, light label. |
| Learn more | default, hover, focus-visible, pressed | Home hero. White pill beside the black CTA. |
| Platform trigger | default, hover, focus-visible, pressed | Opens the Platform dialog. |
| Platform menu link | default, hover, focus-visible, pressed | "For Companies" row inside the open dialog. |
| Hero title | default | "TRANSPARENCY STARTS HERE". |
| Get started | default, hover, focus-visible, pressed | Pricing plan card. Same black pill family as the hero CTA. |
| Monthly billing label | default, hover, focus-visible, pressed | Pricing toggle label. The selected Yearly chip is in the pricing screenshot. |
| Industry search | default, focus-visible | `/explore/industries`. Nothing was typed. |
| Teams tab | default, hover, focus-visible, pressed | `/org/five-blocks`. |
| Avatar | default | 48px image on the org chart. |
| Letter link | default, hover, focus-visible, pressed | Companies A–Z index. Colour matches `--primary-100`. |
| Footer About | default, hover, focus-visible, pressed | Footer column link. |

## Gaps

- Text area, select, checkbox, radio, switch, tooltip, toast, table: not present on the captured public pages.
- Dialog: the Platform and Enrich menus are dialogs and are in the screenshots. A destructive confirmation was not present.
- Contact sales form: present on pricing, not screenshotted and not measured, because it asks for a name, company, and work email.
- Login and signup fields: present, not measured. The branch stops at the wall.
- Disabled, loading, and error states: not shown on the public pages that were captured.
- Info colour: declared custom properties resolve empty. Not captured.
- Focus ring colour: the measured controls did not paint a distinct outline. Not captured.
