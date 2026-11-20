# Promova components

Public marketing surface, measured 2026-11-21 from computed styles. Crops were not cut. The screenshots in [screenshots/](screenshots/) show the components in place.

| Component | Where | States read |
|---|---|---|
| Hero title | [home-light-default](screenshots/home-light-default.png) | default: Nekst 70px / 700, ink on transparent |
| Nav bar | same | default: white, 30px radius, 100px tall, 1400px wide |
| Nav menu button | same | default: Nekst 15px / 400, transparent |
| Primary button (GET STARTED) | same, hover in [home-light-cta-hover](screenshots/home-light-cta-hover.png) | default black fill, white label, 40px, square corners. Hover fill #262626 |
| Secondary button (SIGN UP) | same | white fill, 1px ink border, 40px, square corners |
| Hero button (TRY NOW) | same | black fill, Nekst 18px / 700, 60px tall, 340px wide, square corners |
| Languages menu | [home-light-menu-languages](screenshots/home-light-menu-languages.png) | open. Panel paint was not isolated (the wrapper computed transparent) |
| Courses, Why Promova, Resources menus | matching `home-light-menu-*` shots | open |
| Language card | homepage, below the hero | white, 20px radius, 20px padding, 92px tall |
| FAQ search field | [faq-light-default](screenshots/faq-light-default.png) | default and focus-visible screenshot. Field itself is transparent, 18px Manrope. Not filled |
| FAQ search button | same | black, 60px, Nekst 18px |
| FAQ topic card | same | white, 20px radius, no shadow |
| Phone drawer | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png) | open. Links, store badges, SIGN UP, GET STARTED |
| Onboarding language row | [onboarding-light-wall](screenshots/onboarding-light-wall.png) | visible, not chosen. Branch stopped |
| Sign-up wall | [signup-light-wall](screenshots/signup-light-wall.png) | header only. No email form rendered |

## Shared values

Ink `#000000` on white panels. The page frame is black. The hero panel is lilac `#bec8ff` with a 30px radius. FAQ page fill is pink `#f5a0d2`. Buttons are square. Cards and panels are rounded. No measured shadow on the nav, hero, cards or buttons.

## Gaps

- Icon button, text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, table, avatar, badge: not present on the captured public pages, or not isolated.
- Text field: the FAQ search and the contact form exist. The contact form was not filled and not submitted. Its computed field styles were not read.
- Focus-visible, pressed, disabled, loading, error: not captured. Keyboard focus was not held on a control that changed paint. Pressed was not sampled.
- Menu panel fill, radius and shadow: not captured. The dropdown wrapper computed as transparent.
- Dark theme: not present.
