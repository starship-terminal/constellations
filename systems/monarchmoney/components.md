# Components

Public marketing controls on www.monarch.com, measured 2026-11-21 in headless Chromium at 1440 x 900. The signed-in app was not entered. Crops were not cut. States that were not reached are Not captured.

| Component | What was seen | States | Evidence |
|---|---|---|---|
| Button | Header Sign up, hero "Unlock better money habits", pricing "Try Monarch free for 7 days". Pill, monarch orange `#f35b16`, white label, 36px nav height, 48px hero height, radius 9999px. | default, hover (`#e64818`) | [raw/components-computed.json](raw/components-computed.json), [screenshots/home-light-default.png](screenshots/home-light-default.png), [screenshots/home-light-cta-hover.png](screenshots/home-light-cta-hover.png) |
| Quiet button | Header Sign in. White fill, 1px `#e4e1de` border, 36px, pill. | default, focus-visible (daisy 2px gap, charcoal 4px ring) | [screenshots/home-light-signin-focus.png](screenshots/home-light-signin-focus.png) |
| Icon button | Orange square icon tiles in the Features menu. | default | [screenshots/home-light-features-menu.png](screenshots/home-light-features-menu.png) |
| Link | Nav links, footer links, "Learn more". ABC Oracle, charcoal. | default | [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Text field | Opt-out form placeholders (first name, last name, email). Not filled. Debt and mortgage calculator fields. Not filled. | default only | [screenshots/optout-light-default.png](screenshots/optout-light-default.png), [screenshots/calc-debt-light-default.png](screenshots/calc-debt-light-default.png) |
| Text area | Not present on the captured public pages. | | |
| Select | Pricing "annually" control. A click changed the label. The open menu was not in the screenshot. | default. Open menu Not captured | [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png) |
| Checkbox | Opt-out form checkbox. Not checked. | default | [screenshots/optout-light-default.png](screenshots/optout-light-default.png) |
| Radio | Not present. | | |
| Switch | Not present on the public site. Cookie toggles sit in the Osano dialog, which was hidden and not submitted. | Not captured | |
| Tabs | Budgeting page Flex / Category tabs. Professionals audience tabs. About team filters. Glossary category chips. Homepage Track/Budget/Collaborate/Plan tabs exist only below the `lg` breakpoint. | selected on budgeting, professionals, about, glossary. Homepage tabs captured on phone. | [screenshots/budgeting-light-tab-category.png](screenshots/budgeting-light-tab-category.png), [screenshots/mobile-home-light-tab-budget.png](screenshots/mobile-home-light-tab-budget.png) |
| Menu | Features mega menu. Phone Open menu drawer. Careers department menu did not open (click timed out). | open | [screenshots/home-light-features-menu.png](screenshots/home-light-features-menu.png), [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) |
| Tooltip | Not present on the captured pages. | | |
| Dialog | Cookie banner (hidden, not accepted). Professional-directory fee dialog did not open (scroll timed out). | banner recorded, fee dialog Not captured | [screenshots/home-light-banner.png](screenshots/home-light-banner.png) |
| Toast | Not present. | | |
| Card | Pricing Core and Plus cards. Features menu cards. Blog cards. | default | [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png) |
| List row | Footer link groups. FAQ rows. | default, expanded | [screenshots/tracking-light-faq-open.png](screenshots/tracking-light-faq-open.png) |
| Table | Pricing comparison is a card layout, not a data table. | not present as a table | |
| Avatar | About team photos. Published staff. | default | [screenshots/about-light-default.png](screenshots/about-light-default.png) |
| Badge | Promo strip. "What's New" sparkle is copy, not a badge component. | default | [screenshots/home-light-default.png](screenshots/home-light-default.png) |

## Gaps

- Pressed, disabled, loading, and error states were not shown on the public controls that were measured. Not captured.
- Text field focus, filled, and error states were not captured. Filling the opt-out form or the professional signup would enter profile fields. Calculator fields were left empty.
- No component crops in `components/crops/`.
- Signed-in app components (transactions, budgets, goals, settings) sit behind `https://app.monarch.com/login`. Not captured.
