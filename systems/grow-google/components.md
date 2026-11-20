# Components

Public Grow with Google pages, 2026-11-21. Two shells: APAC Glue (`/intl/en_sg/`) and the US Brightspot marketing shell (`/certificates` and the rest of the US tree). Values are token names. Crops were not cut: the full screenshots are the evidence.

## Button

Primary pill, height 50px, radius 48px, label 16px weight 500.

| Shell | Default | Hover | Focus |
|---|---|---|---|
| APAC | Ink fill `{color.grey.900}`, white label. "View all tools", "About Grow with Google". | Not separately measured on the ink pill. | Keyboard focus paints a 2px `{color.blue.600}` box-shadow. |
| US | Fill `#3186ff` (`light.accent.default`), white label. "Learn more", "Enroll now". | Text stays `#3186ff` on a 4% blue wash (`light.accent.hoverWash`) for the outline variant. The filled pill hover did not change colour in the reading. | Outline 2px, offset 1px, on the outline variant. |

Pressed, disabled and loading were not present.

## Link

APAC links are `{color.blue.600}` (`#1a73e8`). US body links are `#336ef3` (computed, not a Glue ramp step). Nav links are grey-900, 16px, weight 500, radius 4px, height 48px. The current APAC item draws a blue underline.

## Icon button

The US mobile drawer toggle and the carousel previous/next controls. No separate icon-button token. The Google wordmark is brand artwork and is not extracted.

## Text field, text area, select, checkbox, radio, switch

Not present on the captured public pages. Partner and government forms exist at `/partnerapply` and `/government-form` and were not filled (captcha fields present, empty).

## Tabs

APAC stories: three buttons labelled "Selected tab 1 of 3" through "3 of 3". US certificates: a pill row (Overview, Professional Certificates, Path to jobs, AI training, FAQs). Selected state is the APAC tab's own label; a second visual selected style was not measured.

## Menu

US desktop: hovering "Career Certificates" opens a three-column panel (Foundational, Advanced, Courses) with a soft shadow and a large bottom radius. See [screenshots/us-certificates-light-nav-career.png](screenshots/us-certificates-light-nav-career.png). Phone: a drawer over a dark scrim. See [screenshots/mobile-us-certificates-light-nav-open.png](screenshots/mobile-us-certificates-light-nav-open.png) and [screenshots/mobile-apac-home-light-nav-open.png](screenshots/mobile-apac-home-light-nav-open.png).

## Tooltip, dialog, toast

Not present. The cookie control is a button labelled "Cookies management controls" and was not opened into a measured dialog.

## Card

APAC tool cards are white, radius 8px, with a blue link. US certificate cards sit on a `#eff2f7` raised ground. See [screenshots/apac-tools-light-default.png](screenshots/apac-tools-light-default.png).

## List row, table, avatar, badge

Not present as components. Story pages use editorial cards, not a table. No avatar control. No badge component was measured.

## Gaps

- No signed-in surface. No account control on either shell.
- No dark theme. `prefers-color-scheme: dark` left the body white on `#202124`.
- Desktop US nav is hover, not a button click. The first click attempt timed out because the visible link has no accessible name match on the hidden duplicate.
- Forms with captcha were not filled, so validation, error and success states are not captured.
- Component crops were not cut. Screenshots are the evidence.
