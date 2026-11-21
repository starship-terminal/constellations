# Components

Public controls measured on 2026-11-21. Crops are in [components/crops/](components/crops/). Values are token names. Raw computed styles are in [raw/readings.json](raw/readings.json).

## Button

The marketing call to action is `#homepage-weave-cta`. Fill is `linear-gradient(270deg, {color.gradientStart}, {color.gradientEnd})`. Text is `{color.ink}`. Radius `{radius.lg}`. Height 60px. Type is Source Sans 3, 16px, weight 600, uppercase. Hover did not change the computed gradient or shadow. Focus was not separately cropped.

REQUEST DEMO is a quiet button: transparent fill, 1px `{color.muted}` border, `{radius.lg}`, height 50px, white text.

The Forge Log in button is `{color.cobalt}` with white text, `{radius.md}`, height 32px. It was not pressed.

## Link

Docs and Pricing use `{color.accent}`, Source Sans 3, 20px. LOG IN and SIGN UP are uppercase Source Sans 3 at 16px, letter-spacing 0.96px. SIGN UP hover colour is `{color.amber}`. Keyboard focus draws a 1px `{color.focus}` outline.

LOG IN and SIGN UP open the Forge wall. They were not followed from the measured state.

## Text field

Contact Us fields are 42px tall, `{radius.sm}`, background `{color.field}`, border `{color.fieldBorder}`, white text. Placeholders seen: First Name, Last Name, Phone, Company, Work Email, Comments. The form was not filled and not submitted.

The Forge Email field is 32px tall, `{radius.md}`, white fill, border `{color.forgeBorder}`. It was left empty.

## Select

Contact Us shows Select Country and Interested In. They were not opened.

## Text area

Contact Us has a Comments box. It was left empty.

## Menu

Header menus open on hover. Weave, Solutions, Enterprise, and Resources are in [screenshots/](screenshots/). The phone nav was not opened. See [site-tree.md](site-tree.md).

## Dialog

The homepage announcement is a public dialog: "Your Weights & Biases sign-in now lives in CoreWeave Forge." Close dismisses it. Sign in to CoreWeave Forge is a login wall and was not followed.

## Card

Pricing shows Personal ($0/mo) and Advanced Enterprise (Custom plan) cards. GET STARTED on Personal points at the signup wall and was not followed.

## Badge

The announcement uses an ANNOUNCEMENT label. No separate badge component was measured.

## Gaps

Icon button, checkbox, radio, switch, tabs, tooltip, toast, list row, table, avatar: not captured as interactive components. The brand guide has a tab row (Personality, Logo, Color, Typeface). Those tabs were not activated. Status colours (success, warning, danger, info) were not found as roles on the public pages. Disabled, loading, pressed, and error states were not reached without submitting a form.
