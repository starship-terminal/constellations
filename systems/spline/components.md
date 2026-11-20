# Components

Measured on the public site and the signed-out sign-in shell on 19 November 2026. Crops are from the headless screenshots. The preview browser did not produce frames.

| Component | State | Evidence |
|---|---|---|
| Button, primary | Default | [components/crops/button-primary-default.png](components/crops/button-primary-default.png). `#eee` on `#000`, 44px or 34px tall, radius 999px, weight 500. |
| Button, primary | Hover | Declared `#fff` fill. Not hovered in the live tab. |
| Button, secondary | Default | [components/crops/button-secondary-default.png](components/crops/button-secondary-default.png). Transparent fill, 1px `#2e2e2e` border, `#eee` type. |
| Button, secondary | Hover | Declared border `--mute`. Not hovered. |
| Button, app Next | Default and disabled | White fill, `#1a1a1a` type, 40px, radius 8px. Disabled opacity 0.5 on the company step. |
| Link | Default | [components/crops/link-nav-default.png](components/crops/link-nav-default.png). 14px Geist, `#8a8a8a`, radius 8px. |
| Text field | Default and focus | Email field on the sign-in page. Fill `#ffffff0d`, height 40px, radius 8px. Focus is a 1px white inset shadow. |
| Text area | Not captured | No public text area was opened. |
| Select | Default | Company-size select on the unsubmitted company step. Fill `#ffffff0d`, height 40px, radius 8px, placeholder `#ffffff61`. Options were not opened. |
| Checkbox | Checked | News checkbox on the name step. 16px, radius 4px, fill `#2589ff`. Unchecked was not shown. |
| Radio | Not present | The company step uses a select, not radios. |
| Switch | Not present | Billing is a segmented pill, not a switch. |
| Tabs | Selected | Yearly billing pill. [components/crops/toggle-billing-yearly.png](components/crops/toggle-billing-yearly.png). |
| Menu | Not opened | Products and Resources are menu triggers. The menu was not opened. |
| Tooltip | Not present | None on the pages measured. |
| Dialog | Not present | No dialog was opened. |
| Toast | Not present | The update card is a fixed notice, not a toast. |
| Card | Default | Popular plan uses surface `#101010`. Story links use radius 16px. |
| Badge | Default | [components/crops/badge-save-default.png](components/crops/badge-save-default.png). Fill `#bfdec4`, text `#203a26`, 11px. |
| List row | Demo only | The enterprise page shows a members table as a marketing demo. Row styles were not measured. |
| Avatar | Not measured | The members demo draws initials. Computed styles were not read. |
| Logo | Default | [components/crops/logo-wordmark.png](components/crops/logo-wordmark.png). |

## Gaps

Hover, pressed, and disabled styles of the marketing buttons are declared and were not cropped. The menu, tooltip, dialog, toast, text area, radio, and switch were not on the pages that were opened. The signed-in editor was not reached.
