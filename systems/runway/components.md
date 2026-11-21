# Components

Public Runway controls, measured on 2026-11-21 from runway.com and docs.dev.runwayml.com, signed out. Crops are in [components/crops/](components/crops). Values are token names from [tokens.json](tokens.json).

| Component | States | Where | Values |
|---|---|---|---|
| Button (nav CTA) | default, hover | Header Try Runway | `core.color.cta` face, white text, `core.radius.sm`, 32px tall, 14px / 600. Hover face is black. |
| Button (quiet) | default, hover | Login, Enterprise Sales | `core.color.quiet` face, `core.color.off-black` text. Hover `core.color.quiet-hover`. |
| Button (hero) | default | Hero "Try Runway for free" | `core.color.hero-button` face, `core.color.ink` text, 8px radius, 40px tall. Hover class is `hover:bg-white`; the hover style was not held (the open menu covered the control). |
| Button (plan) | default, hover | Pricing "Start Free" | Transparent at rest, pill radius. Hover fills `core.color.ink` with white text. |
| Button (submit) | default, hover | Enterprise contact | Same face as the nav CTA. Not clicked. |
| Link (nav) | default, hover | Pricing | 16px / 500, `core.color.ink`, transparent. Hover colour did not change. |
| Menu trigger | default, hover, open | Creative and the other five header items | Resting `core.color.menu-muted`. Hover and open go to ink. Open is a hover mega menu, shot in [screenshots/home-light-menu-creative.png](screenshots/home-light-menu-creative.png). |
| Menu link | default | Creative menu | `hover:bg-black/5` in the class. A held hover crop was not taken. |
| Text field | default, focus-visible | Enterprise contact first name | 16px, 41px tall, 14px horizontal padding. Focus crop in components/crops. Not filled. |
| Text area | default | Enterprise contact message | 16px, 3px radius. Not filled. |
| Select | default | Enterprise contact company size | Native select, 16px, 3px radius. Not changed. |
| Checkbox | default | Enterprise contact products | 16px box. Not checked. |
| Tabs | selected | Pricing Monthly / Yearly, and API | Shot in [screenshots/pricing-light-yearly.png](screenshots/pricing-light-yearly.png) and [screenshots/pricing-light-api.png](screenshots/pricing-light-api.png). |
| Language menu | open | ENGLISH | [screenshots/home-light-language.png](screenshots/home-light-language.png). Not switched. |
| Mobile menu | open | Menu button at 390 | [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). |
| Code block | default | docs.dev.runwayml.com | `core.color.code-bg` / `core.color.code-fg`, 14.4px monospace. |
| Hero title | default | Home | 56px / 400 desktop, 36px at 390, white on the media. |

## Shared values

Marketing type is `abcNormal` at 400, 500 and 600. Header buttons are 32px with a 6px radius. The page is white. The filled action is `#262626`, not the declared blue. The blue (`#2c22fa`) is a declared interactive token on the developer stylesheets.

## Gaps

| Checklist item | Status |
|---|---|
| Icon button | Not present as a labelled control on the marketing header. The mobile close mark is an X in the menu shot. |
| Radio | Not present on the captured public pages. |
| Switch | Not present. The billing control is a pair of buttons. |
| Tooltip | Not captured. None stayed open long enough to read. |
| Dialog | Cookie Settings is a OneTrust dialog. Hidden, never opened. |
| Toast | Not present on the captured pages. |
| Card | Observed on product and news pages. No separate crop. |
| List row | Observed in the mobile menu and the news index. |
| Table | Not present on the captured marketing pages. |
| Avatar | Not present. |
| Badge | Observed as the "New" mark in the Creative menu. Not measured. |
| Disabled, loading, error | Not present on the public pages that were opened. The enterprise form was not submitted, so its error state is not captured. |
| Focus-visible on buttons | Not captured as a computed outline. The hero CTA class names `focus-visible:ring-2 focus-visible:ring-blue-500`. |
| Pressed | A pointerdown reading was taken. It did not change the nav CTA fill. Held pressed is not captured. |
| Dark theme | Not present as a public toggle. |
