# Components

Public IFTTT controls, measured on ifttt.ai on 2026-11-21. Crops were not cut: the full pages in [screenshots/](screenshots/) are the evidence. Values are token names from [tokens.json](tokens.json).

| Component | Where | States read |
|---|---|---|
| Button, primary | Home "Start building", login submit, header "Get started" | default #111 fill, white text, 64px radius, 101px tall on the hero. Hover is opacity 0.8. Active and focus-visible use #111 at 0.6. Disabled keeps the fill and drops to opacity 0.3 (stylesheet, not a live disabled control). |
| Button, outlined | Header "Log in", plan "Get started", service "Share" | 54px tall, pill, ink or white text, inset or hover scrim `#111` at 0.05. |
| Button, on colour | Service page "Copy" and "Back" over the coloured hero | White text on ink, or white text on a transparent face with a white hover scrim. |
| Icon button | Phone menu, 48px, and the search icon | Default only. No separate hover colour. |
| Link | Header Explore and Plans | Ink, 20px, weight 700. No underline in the header. Footer links are underlined on the login page. |
| Text field | Login username, password, header search, forgot-password email | 55px, 16px radius, 2px border. Username border is ink. Password border is ink at 0.1 until focus. Not typed. |
| Text area | Home "Describe what you'd like to build" | Visible on the home hero. Values not read as their own token. Submitting it opens the signup wall. |
| Select | Not present | No public select was found. |
| Checkbox | Not present | |
| Radio | Stylesheet has `.form input[type=radio]:checked+label:after` in ink. No public radio was on the captured pages. | Not captured as a state. |
| Switch | Plans "Show yearly prices" | 48x32, 16px radius, `#01b6ff` when yearly is on. |
| Tabs | Home featured tabs (Popular, Business, and the rest). MCP client tabs. Explore All / Applets / Services / Stories are links, not tabs. | Selected tab is an ink pill with white text, 8px radius, 48px tall. |
| Menu | Phone hamburger drawer | Explore, Plans, Log in, Get started. Desktop has no dropdown menu. |
| Tooltip | Plans "About Credits" | role=tooltip. Credits text was read during the site-tree probe. |
| Dialog | Service Share | "Share this using the options below" with Copy and a close control. |
| Toast | Not present | |
| Card | Plan cards, applet cards, testimonial cards | Plan cards are paper with a hairline. The recommended plan has an ink frame. Testimonial cards are clover `#0dd14e` and fuchsia `#ff3cec`, 24px radius. |
| List row | Service ingredient rows, docs nav | Observed on the service and docs pages. |
| Table | Not present | The plans comparison is a card row, not a table. |
| Avatar | Testimonial photo | 48px circle. Published marketing photo, not an account. |
| Badge | "SAVE 30%", "RECOMMENDED", credit pills, testimonial badge | Credit pill is a light outline. SAVE 30% uses clover. Testimonial badge is white on the card colour, 14px, weight 700, uppercase. |

## Shared values

Ink `#111111` does text, the primary button, and the strong border. Paper `#ffffff` is the page. The only hues that are not ink are the wordmark orange `#ff5e19`, the plans switch blue `#01b6ff`, clover `#0dd14e`, fuchsia `#ff3cec`, and the fieldset red `#d4545c`. Buttons are pills. Fields are 16px. Cards are 24px.

## Gaps

- Text area, select, checkbox, radio, toast, and table were not present as live public controls, or were only a stylesheet rule.
- Disabled, loading, and error states were not shown. No form was submitted, so validation error is not captured.
- Pressed was read from the stylesheet (`:active` background `#11111199`), not held on a live button, because holding the hero button navigates to signup.
- Focus ring is 2px ink on some logo links. Primary buttons use a background change, not a ring. Several computed focus outlines came back `none`.
- Dark theme is not present.
