# Components

Public marketing site only. States were read from computed styles on 2026-11-21. The signed-in dashboard was not entered.

| Component | States seen | Evidence |
|---|---|---|
| Button (Get Started) | default, hover, focus-visible | [raw/cta-states.json](raw/cta-states.json). Orange fill `#f35820`, hover `#bd400f`, 32px tall, 6px radius, focus ring 2px white plus 4px orange |
| Button (Contact Sales) | default | White face, orange text `#f35b22`, same 32px height |
| Link | default | Header Login and footer links. Orange on the secondary button, black on nav labels |
| Text field | default, unfilled | Contact sales, newsletter, bot-directory search. Not submitted |
| Switch | default, toggled | Homepage "I'm a developer". Toggled and restored. No submit |
| Menu | open | Product, Use Cases, Resources, Prompt, phone sheet |
| Tabs / volume buttons | default | Pricing 20K, 100K, 200K, 500K, 1M+ |
| Search | open | Docs search dialog. Bot directory search focused, empty |
| Dialog | open | Login wall, recorded and not submitted |
| Card | default | Product menu cards, pricing cards |
| Badge | default | "New" on the homepage banner |
| Icon button | default | Copy, chat launcher, mobile menu, close |
| Text area, select, checkbox, radio, tooltip, toast, table, avatar, list row | not captured as a full state set | Some appear inside pages (pricing table, blog rows). No dedicated state pass |

## Gaps

Pressed and disabled button states were not held. Loading and error states were not provoked. Form validation was not triggered, because no form was submitted. Signed-in components are Not captured.
