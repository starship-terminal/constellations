# Components

The sunset page rendered one control. Everything else on the checklist was absent.

## Export link

The only interactive element is an `<a href="/exports/me">` with the visible label "Export". It is a button-styled link, not a `<button>`.

| State | Reading |
|---|---|
| Default, dark (loaded) | Background `rgb(255, 255, 255)`, text `rgb(0, 0, 0)`, 14px, weight 600, line-height 20px, radius 12px, padding 8px 12px, height 36px, gap 6px, border width 0, shadow none. |
| Default, light (class toggle) | Background `rgb(0, 0, 0)`, text `rgb(255, 255, 255)`. Radius, padding and height unchanged. |
| Focus | `a.focus()` then `getComputedStyle`. Outline `rgba(0, 0, 0, 0) solid 2px`, offset 2px. The class `focus-visible:outline-none` suppresses the ring. |
| Hover | Not computed. The class `hover:bg-token-bg-inverse/80` maps to the stylesheet rule `background-color: rgb(var(--bg-inverse) / .8)`. |
| Disabled | Not rendered. The class names `data-[disabled=true]:bg-token-bg-secondary` and `data-[disabled=true]:text-token-text-primary/30`. |

Token names: `dark.color.control.button-background`, `dark.color.control.button-text`, `dark.component.button.radius`, `dark.component.button.padding`, `dark.component.button.height`. The light set has the same component metrics and the inverted colours.

## Copy

`main p` with classes `text-base text-token-text-secondary`. Dark colour `rgba(255, 255, 255, 0.6)`. Light colour `rgba(25, 25, 25, 0.5)`. Size 16px, weight 400, line-height 24px. Width 448px, height 48px.

## Gaps

| Component | Status |
|---|---|
| Button hover, pressed, disabled, loading | Not captured. One link, resting and focused only. |
| Icon button | Not present. |
| Text field, text area, select | Not present. No signup form. |
| Checkbox, radio, switch | Not present. |
| Tabs, menu, tooltip, dialog, toast | Not present. Toast custom properties exist in a Sonner block in the stylesheet and were not painted. |
| Card, list row, table, avatar, badge | Not present. |
| Crops | Not captured. No screenshot frames, so `components/crops/` is empty. |
