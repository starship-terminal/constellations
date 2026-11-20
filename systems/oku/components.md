# Oku components

Measured on the public signed-out pages of oku.club on 2026-11-19, from computed styles. The preview browser did not produce screenshot frames, so there are no crops.

## Button

The header Join control is the filled action. On the dark paint it is olive `#E0E1E4` text on `#131314`, Inter 14/500, 40px tall, padding 0 24px, radius 8px, shadow `rgba(0, 0, 0, 0.25) 0px 4px 4px -5px`. Sign in beside it is a quiet button: page fill, olive text, same size and radius.

Join for free on the homepage is a quieter fill, blueberry-10 `#242426`, blueberry-100 text, 15/500, 54px tall. At 390px it is 46px tall and 14px type. Subscribe on pricing is an outline: transparent fill, 1px inset ring at 22% olive, 40px tall, full card width.

Hover, pressed, disabled and loading were not measured. Focus on Join computed `outline: none`. The stylesheet sets `:focus { outline: none }`.

## Icon button

Explore carousel controls are 32px circles, page fill, olive text. The phone menu button is 22 by 40, transparent, olive, with a 24px stroked icon. Shelf actions on a book page are 92 by 50, radius 8px, page fill, 1px inset ring plus the lift shadow, and a 28px filled glyph.

## Link

Nav links are Inter 16/400, line-height 24px, blueberry-100, no underline. Inline links in captions use the surrounding muted colour and no underline. Book cards report a link colour of `rgb(158, 158, 255)` in dark and `rgb(0, 0, 238)` in light. The light value is the browser default, not a declared token.

## Text field

Sign-in, join and reset share one field: 368 by 46, radius 8px, 1px blueberry-20 border, page fill, blueberry-100 text and placeholder, padding 0 16px, Inter 14/400. Labels are Inter 14/400, blueberry-80, line-height 25.2px.

## Text area, select, checkbox, radio

Not present on the measured public pages.

## Switch

The pricing billing control is a checkbox plus a label. The label is 42 by 27, radius 27px, blueberry-10 in the rule and olive when yearly is checked. The knob is a 21px circle, 3px from the top and left, milk fill, transition 300ms `cubic-bezier(0.23, 1, 0.32, 1)`. Active scales the knob on X to 1.1. The unchecked position rule was not in the accessible stylesheets.

## Tabs

Book Info, Reviews and Highlights are links. Selected: blueberry-100, 15px, padding 16px 0, 3px bottom border in blueberry-100. Idle: blueberry-50, transparent 3px bottom border.

## Menu

The phone drawer is a nav, absolute, page fill, padding 24px, full viewport. Links are Fabric Serif 36/400, line-height 54px, blueberry-100. No desktop menu was opened.

## Tooltip, dialog, toast

Not shown. Toastify custom properties are on `:root` (info `#3498db`, success `#07bc0c`, warning `#f1c40f`, error `#e74c3c`) and no toast was on screen. A Nolt feedback widget declares `#fd6a65` and was not opened.

## Card

Book cards on explore are 388 by 410, radius 8px. Dark fill is the page colour. Light fill is white with a 1px blueberry-10 border. Covers are 154 by 252, radius 3px, no shadow.

Pricing cards are 368px wide, padding 40px, radius 8px. Free is blueberry-5 `#1C1C1D`. Premium is badge-premium-13 `#1F241F`. Supporter is badge-supporter-13 `#292328`.

## List row

The homepage activity list is links with no card chrome. Names and times were not copied into tokens. Collection chips on a book page use radius 6px and padding 8px.

## Table

Not present.

## Avatar

User marks appear on the activity list. Size and radius were not isolated from the list link.

## Badge

Save ribbons on pricing are 12px, weight 700, white, on a 50px box. The "Save 50%!" note is Inter 12/400, badge-premium-100 `#6F9965`. Premium and supporter names are serif labels, not pills.

## Gaps

- No hover, pressed, disabled, loading or error state was held.
- Focus is removed by a global outline rule.
- Text area, select, checkbox, radio, tooltip, dialog, toast, table and avatar were not measured as components.
- Light theme was measured on explore only. Pricing cards, fields and the homepage were not remeasured in light.
- No screenshots or crops. The preview browser returned "The browser is not producing screenshot frames".
