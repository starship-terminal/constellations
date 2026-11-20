# Components

Measured on the public Visitors pages on 2026-11-19. Values are the computed styles in [tokens.json](tokens.json). Crops were not cut; the screenshots are the evidence.

## Button

Primary action is a pill. "Start 14 day free trial" is 44px tall, fill `#918df6`, white label, 16px weight 500, padding 0 20px. Hover drops opacity to 0.9 and does not change the fill. Header "Register" is the same pill at 32px with fill `#9580ff`.

Quiet actions use `rgba(0, 0, 0, 0.03)` and body ink `#666666`. "See demo", "Google" and "GitHub" are this treatment. "Continue with email" is the primary pill in the disabled fill `#dad9fc`, white label, `cursor: not-allowed`, until an email is present. It was not clicked.

See [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/login-light-default.png](screenshots/login-light-default.png).

## Text field

`/login` and `/register` have one field, placeholder "Email address". Fill `#f5f5f5`, text `#181925`, 16px weight 500, 40px tall, 12px radius, padding 0 16px. Focus outline is 2px `#918df6` with a 2px `#dad9fc` ring. See [screenshots/login-light-field-focus.png](screenshots/login-light-field-focus.png).

## Link

Docs body links are `#2c78fc` and underlined (`a.text-sky-4`). Header links are `#bbbcc3`, 14px weight 500, with a hover class `hover:text-fg-4` that was not the resting colour. Keyboard focus on the header Login link drew no outline.

## Menu

The Features control opens a dark panel of four cards: Revenue `rgba(51, 199, 88, 0.16)`, Realtime `rgba(145, 141, 246, 0.16)`, Performance `rgba(255, 166, 0, 0.16)`, Profiles `rgba(214, 64, 159, 0.16)`. Each card is 218 by 116, radius 16px, padding 16px 12px. See [screenshots/home-light-features-menu.png](screenshots/home-light-features-menu.png). The popover container's own fill was not isolated; the screenshot is the evidence for the dark panel.

## Card

The pricing block is a 984 by 502 grid, radius 16px, fill `rgba(0, 0, 0, 0.03)`. The event count "10K" is 48px `#918df6`. The price "9" is 24px `#181925`. The slider thumb is a 32px white circle with the `--shadow-3` shadow. See [screenshots/home-light-pricing.png](screenshots/home-light-pricing.png).

## Badge

The homepage "NEW" chip is a pill, fill `rgba(44, 120, 252, 0.08)`, text `#2c78fc`, 14px weight 500. Docs method badges: GET is 12px `#33c758` on `rgba(51, 199, 88, 0.08)`, radius 4px.

## List row

The public demo at `/s/godly.website` shows page and source rows, metric labels, and a delta in green or red. It is a public stats page, not the signed-in product. See [screenshots/demo-light-default.png](screenshots/demo-light-default.png).

## Gaps

- Text area, select, checkbox, radio, switch: not on the captured public pages.
- Tabs: the demo has Top / Entered / Exited and Referrer / Links / Campaign as text buttons. Selected and unselected fills were not measured as a tab component.
- Tooltip, dialog, toast: not opened. No cookie dialog appeared.
- Table: not present on the marketing pages. The demo list is not a table.
- Avatar: a small mark sits in the homepage product demo. It was not measured as a component.
- Icon button: the mobile header has a menu glyph. It was not opened, so the drawer is a gap.
- Loading and error on a form: not triggered. Continue stays disabled until an email is entered, and the form was not submitted because a Turnstile widget is on the page.
- Pressed and focus-visible on the primary button: focus-visible ring classes exist (`focus-visible:outline-blue-500` on Monthly). A keyboard focus on the trial button did not paint an outline in the headless page.
