# Endless components

Public site only, measured 2026-11-21. Crops are in [components/crops](components/crops). Values are token names from [tokens.json](tokens.json).

| Component | States seen | Where |
|---|---|---|
| Button, filled | default, hover, focus-visible | Header "Sign up for free". `component.button`. |
| Button, quiet | default | Header "Sign in". Muted text, no fill. |
| Link | default | Nav and MCP banner. Muted or ink, no underline. |
| Text field | default, focus | Sign-in email. Focus paints an accent halo. |
| Text area | default, focus | Home composer. Empty. Not submitted. |
| Select | gated | Model chip opens a sign-up dialog, not a list. |
| Tabs | default, selected | Pricing Monthly / Annual. Blog All / Guides / Customer stories. Docs sidebar groups. |
| Menu | open | Industries hover menu. Phone Menu sheet. |
| Dialog | open, gated | "Unlock more features" from the model chip. |
| Card | default | Pricing plan cards. Model cards. Blog cards. |
| Badge | default | "Ideogram 4.6 is now available" pill. |
| List row | default | Docs sidebar rows. Footer link columns. |

## Gaps

Checkbox, radio, switch, tooltip, toast, table, avatar, and a destructive confirmation were not present on the public pages that were opened.

Disabled, loading, and error states were not shown. The contact form and every sign-in control were left unsubmitted, so validation was not captured.

The signed-in app (chat, canvas, settings) is behind the sign-in stop.
