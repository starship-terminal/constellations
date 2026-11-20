# Components

Measured on the public marketing site on 2026-11-19. Values are token names. The computed readings are in [raw/components-computed.json](raw/components-computed.json).

`preview_snapshot` returned "The browser is not producing screenshot frames." Crops were not invented. The Gaps section records that.

## Button

The enquire Submit control is `light.component.button-primary.bg` (`#26232a`) with white text, a 2px radius, 48px height and 16px inline padding. The listing Check Availability control is `light.component.button-brand.bg` (`#c84908`), 40px tall, same radius and padding. The home search control is a 40px square of `light.accent` (`#ff8065`) with a 0px radius, sitting in the search bar. The header Inquire Now control is a 40px frame with a 1px white border and 12px inline padding, not a fill. View all photos is white with a 1px `light.border.field` border, 40px tall, 2px radius, Akkurat 700.

Hover was declared as `hover:border-neutral-500` on field shells and `group-hover:border-black` on the Inquire Now frame. A pointer hover was not painted, because the screenshot path failed and a synthetic mouseover did not change the computed border. Focus on the search Garden chip painted a 2px `light.focus` (`#0066cc`) box-shadow.

## Link

Header links are Akkurat 400 at 14px/20px. On the home hero they computed to white. On the listing page, under the solid white header, Inquire Now computed to `rgb(0, 0, 0)`. Destination breadcrumbs used `light.accent` for Home. Links transition colour, background and border over `core.motion.duration.default` with `core.motion.easing.standard`.

## Text field

The enquire field shell is a 70px column: 12px 16px padding, 1px `light.border.field`, 2px radius, transparent background. The label is `core.typography.label` in `light.text.primary`. The input is `core.typography.body` in `light.text.primary`. Placeholder copy uses the `placeholder:text-neutral-400` class. The input node itself computed an 8px radius. The shell is the painted edge.

The phone field is on this form. It was not filled. See Gaps.

## Text area

The enquire notes field is 96px of text inside a 122px shell with the same border, radius and padding as the text field. Akkurat 16px/24px.

## Select

Country on the enquire form and Guests, Bedrooms and Bathrooms on search are custom buttons, not native selects. The search ones are 50px tall, 12px 16px padding, 1px `light.border.field`, 2px radius. The open menu was not captured.

## Checkbox

Two enquire checkboxes computed to 24 by 24 px with `appearance: auto`. They were not toggled. The marketing copy on the second checkbox offers SMS. That box was not checked.

## Radio, switch

Not present on the pages measured. The OneTrust preference centre mounts a switch. It was not opened and not measured as a product control.

## Tabs

Journal category links (Stories, Guides, Trending) are text links, not a tab widget. On the journal sheet they computed to AkkuratStd-Regular 16px/20px in `rgb(50, 50, 50)`. A coral category bar (`rgb(254, 127, 99)`) was in the DOM at height 0.

## Menu

The desktop header shows Destinations, List Your Home and Inspiration as links. Destinations and Inspiration have empty hrefs and are disclosure controls. They were not opened. At 390px the header shows a 40px Open menu button and hides the link row. The menu overlay was not opened.

## Tooltip, dialog, toast

Not opened. A cookie banner from OneTrust was on every page. It was hidden in the DOM for measurement. Accept was not clicked.

## Card

Home listing cards are image links. The title is `core.typography.card-title`, italic, `light.text.primary`. The image filled the link box (568 by 377 px on the home page at 1440). Card radius computed to 0.

## List row

Search results were not scrolled into a measured row. The result count heading computed to Akkurat 16px/24px, `light.text.primary`.

## Table

Not present.

## Avatar

Host portraits appear on list-your-home. They were not cropped.

## Badge

Listing type labels (EXCLUSIVE, HOUSE) are 12px/16px Akkurat 700, uppercase. Exclusive uses `light.accent`. House uses `light.text.muted`. The journal `#TRENDING` chip is `light.brand.400` (`#fe7f63`) with white text, 5px 10px padding, 2px radius, 0.6px letter-spacing. That coral is one step lighter than the search button.

## Gaps

- No component crops. The preview browser did not produce screenshot frames.
- Hover, pressed, disabled, loading and error states were not painted.
- The enquire form was not submitted, so validation and error styles are a gap.
- Phone, country and postal fields were not filled.
- Menus, the date popover, the guest popover and the filter dialog were not opened.
- Checkbox, radio and switch product states are a gap. The native checkbox size is recorded. Its checked colour is not.
- Dark theme: no `prefers-color-scheme` rule was declared on the marketing sheets.
