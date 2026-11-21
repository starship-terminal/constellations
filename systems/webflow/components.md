# Webflow components

Public marketing site at [https://webflow.com/](https://webflow.com/), captured 2026-11-21, signed out. Values are computed styles and CSS custom properties. Crops, where present, are in [components/crops/](components/crops). The designer and dashboard were not opened.

## Button

Primary actions are blue `#146ef5` with white text, radius `0.25rem` (`--_components---button--border-radius`), font weight 500, font size 1rem. "Get started", "Start for free", and "Contact Sales" use this fill. "Talk to Sales" is a quiet button: gray surface, dark text, same radius. Hover was captured on the header CTA ([screenshots/home-light-cta-hover.png](screenshots/home-light-cta-hover.png)). Pressed, disabled, and loading were not shown on the public pages.

## Icon button

The phone header uses one control, `aria-label="menu"`, class `.w-nav-button`. Open, it becomes a close mark. See [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). The story dialog uses a blue square close button.

## Link

Nav links are dark text on white (white text in dark mode), no underline. "Pricing" is a link to `/pricing`. Footer links repeat the same treatment. Focus-visible was requested in the measure pass. A failed focus is Not captured.

## Text field

The login wall shows "Email address or username" and "Password". The contact-sales page shows an email field. Neither was typed into and neither form was submitted. Input radius is `0.25rem` (`--_components---input--border-radius`). Input font size is 1rem, weight 400.

## Text area

Not captured as a painted control. The contact-sales page was opened and not filled. If no textarea resolved in the measure pass, this row stays Not captured.

## Select

Pricing exposes `<select>` elements for bandwidth and locales. They were not submitted. A computed reading is in [raw/components-computed.json](raw/components-computed.json) when the selector resolved.

## Checkbox

Not present as a labelled public control on the captured pages. The billing control is a switch, below.

## Radio

Not present on the captured public pages.

## Switch

Pricing has a Monthly / Yearly toggle, an `input` named `toggle`. Yearly is the default painted state ("Yearly (Save up to 40%)"). See [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png) and [screenshots/pricing-light-billing-toggle.png](screenshots/pricing-light-billing-toggle.png).

## Tabs

Not present as a tablist on the captured pages. The homepage role switcher (Marketer, Designer, Developer, Agency) is a menu, not tabs.

## Menu

Platform, Solutions, and Resources are buttons with `aria-haspopup="true"` and `aria-controls` of `dropdown_content_0`, `dropdown_content_1`, and `dropdown_content_2`. Open, the panel is a light gray surface with a four-column link list and two blue promo cards. See [screenshots/home-light-platform-menu.png](screenshots/home-light-platform-menu.png). The phone menu is a full-screen sheet from `.w-nav-button`. Appearance (Light mode, Dark mode, Auto) sits in the desktop menu chrome.

## Tooltip

Not captured. No tooltip was held open.

## Dialog

Homepage cards open a full-viewport dialog (`.modal-dialog_home`) with a story, a close button, and a "Read the story" link. See [screenshots/home-light-dialog.png](screenshots/home-light-dialog.png). A two-factor dialog is mounted in the DOM and was not opened. The cookie card is a consent dialog. Accept all and Reject all were never clicked. A later paint covered the card on some viewport shots. On the homepage and the login wall that cover also cut a rectangle out of content beside the card.

## Toast

Not present on the captured pages.

## Card

Plan cards on `/pricing` and story cards on the homepage. Card radius token is `0.5rem` (`--_components---card--border-radius`). Plan cards use a light gray surface in light mode.

## List row

The phone menu rows (Platform, Source, Solutions, Resources, Enterprise, Pricing) are the public list rows. Desktop menus use the same links in columns.

## Table

Not present on the captured pages. Pricing is a card grid, not a table.

## Avatar

Customer-story portraits appear in the homepage cards and in the login-page livestream panel. They are published marketing photos, not an account avatar. No signed-in avatar was reached.

## Badge

"NEW" sits beside Campaigns in the Platform menu and beside Premium and Team on pricing. It is a small dark label.

## Gaps

- Designer, dashboard, CMS editor, and billing are behind login. Not captured.
- Signup is a press-and-hold bot wall. Not solved. Not captured past the wall.
- Phone login and phone signup returned HTTP 403 bot walls. Desktop login showed the form. Password was not submitted. Continue with Google was not clicked.
- Disabled, loading, and error states of buttons and fields were not on the public pages.
- Checkbox, radio, tabs, tooltip, toast, and table were not present on the captured public pages.
- Hover and focus colours that the measure script missed are Not captured, not guessed. The primary button crop missed: "Get started" was not a visible locator when measure ran. The badge crop missed. The phone menu overlay was reported hidden in the measure pass even though a later screenshot shows it open.
- Cookie consent was not dismissed by a click. Some screenshots still show the card. Homepage and login shots that were painted over have a rectangular bite where the card sat.
