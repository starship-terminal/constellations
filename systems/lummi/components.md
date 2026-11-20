# Lummi components

Public controls measured signed out on https://www.lummi.ai/ on 2026-11-21, at 1440x900. Crops are in [components/crops/](components/crops). The site tree is [site-tree.md](site-tree.md).

| Component | States captured | Gap |
|---|---|---|
| Button (Try Pro for free) | default, hover | pressed, disabled, loading not held |
| Nav link (Illustrations) | default, hover | focus-visible not separately cropped |
| Text field (search) | default, focus | filled left empty on purpose; no submit |
| Overflow menu | open | |
| Tools menu | open | |
| Pro dialog | open | trial CTA is a login wall; not followed |
| Icon button | observed on cards (download) | download did not open a dialog; not cropped as a successful state |
| Checkbox, radio, switch, select, textarea, tabs, tooltip, toast, table, avatar, badge | not captured as interactive states | not present as public form controls on the captured pages, or only inside the login wall |
| Link | observed in nav and overflow | same type as nav link |

Login, signup, Google, and Stripe checkout were not entered. See [site-tree.md](site-tree.md).
