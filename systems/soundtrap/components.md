# Components

Inventory of what the public signed-out pages actually showed on 2026-11-19. Values are token names. Readings are in [raw/components-computed.json](../raw/components-computed.json).

The preview browser did not produce screenshot frames, so this package has no crops.

| Component | Where | States read | Gap |
|---|---|---|---|
| Button | Marketing pill "Get started" and "Get started for free"; login "Log in" | Default. Hover and pressed declared, not forced | Hover, pressed, disabled, loading |
| Icon button | "Open navigation menu" at 390 on pricing, 24 by 24 | Default | Hover, focus |
| Link | Nav items, "Forgot your password?", "Sign up" | Default | Hover underline motion not timed |
| Text field | Login email and password | Default, focus-visible | Error, disabled |
| Text area | Not on these pages | | Not present |
| Select | Language summary on the home footer, 180 by 44, radius 8px | Closed | Open menu not opened |
| Checkbox | Only inside the closed OneTrust preference center | | Not captured: vendor cookie UI, not product chrome |
| Radio | Not on these pages | | Not present |
| Switch | Not on these pages. OneTrust has switches in a closed panel | | Not present on product chrome |
| Tabs | Pricing Individual / Education, 21px weight 700 | Selected and unselected colour | Hover not forced |
| Menu | Phone nav button exists. Menu was not opened | | Not captured |
| Tooltip | Not shown | | Not present |
| Dialog | OneTrust preference center was in the DOM and display none | | Not captured. Product dialog shadow tokens were declared |
| Toast | Not shown | | Not present |
| Card | Pricing plan cards, radius 8px, four set colours | Default | Hover not forced |
| List row | Footer link groups | Default colour only | |
| Table | Pricing comparison rows | Text only | Header chrome not separated from the page |
| Avatar | Not shown | | Not present |
| Badge | Not shown | | Not present |

## Shared values

Focus on the email field is a 2px white ring and a 4px `#3c95ff` ring (`core.palette.focus`). Login fields use `light.component.field-radius` (8px) and `light.background.tinted`. Marketing pills use `light.component.button-pill-radius` (9999px).

## Gaps

- No screenshots or crops. The preview browser returned "The browser is not producing screenshot frames."
- Hover, pressed, disabled, loading, and error were not forced.
- Signed-in studio chrome was not entered.
- OAuth buttons were measured and not followed.
- Warning and announcement colours are utility names with no declaration found.
