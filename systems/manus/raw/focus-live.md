# Keyboard focus, checked live (2026-10-17)

The measured copies said 39 of 64 focusable components show no change on keyboard focus. To rule out
a fault of the static copies, focus was checked in the signed-in app itself, in the built-in browser
pane at 1440 x 900, dark theme, on the home page.

Method: `document.activeElement.blur()`, then one Tab key press at a time from the browser's own
keyboard input, reading the focused element after each press with `getComputedStyle` and
`matches(':focus-visible')`. Element text was masked before it was read out.

| Stop | Element | :focus-visible | Outline | Box shadow | Background |
|---|---|---|---|---|---|
| 1 | button (sidebar header) | true | none | transparent layers only | rgb(36, 36, 36) |
| 2 | div | true | none | none | transparent |
| 3 | button | true | none | none | transparent |
| 4 | button | true | 1px rgba(255, 255, 255, 0.06) (its resting hairline, unchanged by focus) | none | transparent |
| 5 | button (with a label) | true | 1px rgba(255, 255, 255, 0.06) (resting hairline) | none | transparent |
| 6 | div role=region (scroll area) | true | none | none | transparent |
| 7 | div role=button (nav section header) | true | none | none | rgb(31, 31, 31), the sidebar fill |
| 8 | div role=button (nav section header) | true | none | none | rgb(31, 31, 31) |

Every stop matched `:focus-visible` and none drew an outline or a ring; the first changed its fill.
So the measured result is the product's behaviour, not a capture fault: Manus suppresses the
browser outline on most controls and draws a ring only where a component asks for one (fields,
outlined buttons, cards with `focus-visible:outline-*` or `ring-*` classes, listed in
`css-rules.json` under `focusVisible`).
