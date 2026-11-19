# Unsplash components

Measured on unsplash.com, signed out, on 2026-11-19. Values are computed styles. The preview browser did not produce screenshot frames, so this file has no crops.

## Button

Primary fill is `#111111` with white type, radius 8px, and a `rgba(0, 0, 0, 0.08) 0px 1px 1px` shadow. Small is 32px tall, 14px type, 11px inline padding. Medium is 44px, 15px type, 16px inline padding. Large is 56px, 18px type, 24px inline padding. Download on a photo page and Login on `/login` are this button.

Outline is white with a 1px `#d1d1d1` border, `#767676` type, and the same radius and shadow. Submit an image and Share use it. Hover, from the stylesheet, sets the border to `#767676`, the type to `#111111`, and the shadow to `rgba(0, 0, 0, 0.1) 0px 1px 2px`.

Secondary is `#007fff` with white type. It was measured on a specimen using the live `.secondary-Qhy_qo` class, not on a button that was already on the page.

Disabled, from `.base-WybTAX:disabled`, is `#eeeeee` fill, `#767676` type, and `cursor: not-allowed`.

Pressed was not measured. The stylesheet does not declare a separate `:active` fill for the primary button.

## Link

Log in is a text button: transparent fill, `#767676`, 14px, weight 500, radius 8px, padding `0 11px`, height 32px. Hover colour is `#111111`. The transition is `color 0.1s ease-in-out, opacity 0.1s ease-in-out`.

Topic links (Featured, Nature) are 14px, weight 500, 64px tall. Inactive is `#767676`. Active is `#111111` with an inset 2px bottom bar.

## Text field

The login email and password fields are 40px tall, radius 8px, 1px `#d1d1d1` border, padding `6px 12px`, 14px type, white fill. Focus outline is `rgb(229, 151, 0) auto 5px`. The fields were focused and not filled. The form was not submitted.

Search is a separate control: a 40px pill, radius 24px, fill `#eeeeee`, placeholder "Search photos and illustrations" in `#767676`. At 1440 the form is 706px wide. At 390 it is 366px wide.

## Select

Orientation, License, and Sort by Relevance are 32px chips, radius 8px, 1px `#eeeeee` border, 14px type, weight 500, padding `5px 8px 5px 11px`. The menus were not opened.

## Checkbox and radio

A radio specimen using `.radioButton-ewDQ_A` is 16px, 50% radius, `1.5px solid #d1d1d1`. Checked, from the stylesheet, uses an 8px `#007fff` dot. No checkbox class was on the public pages. The OneTrust checkboxes belong to the consent vendor and were not measured as product controls.

## Switch

Not present as a switch. `/plus` uses a tablist: a `#f5f5f5` track, radius 32px, padding 4px, height 42px, with a white thumb, radius 24px, height 34px, shadow `rgba(0, 0, 0, 0.08) 0px 1px 3px`. Yearly is selected. Monthly was not clicked, because the click would change the displayed price.

## Tabs

Home and search use a 64px text tab with a 2px inset bar. `/plus` uses the pill tablist above.

## Menu

At 390, the Menu button opens a white popup, 358px wide, radius 8px, shadow `rgba(0, 0, 0, 0.06) 0px 4px 8px -4px, rgba(0, 0, 0, 0.08) 0px 16px 24px -8px`. It lists Company, Product, Community, Explore, and Legal, plus Submit an image and Log in. The links were not followed.

## Tooltip

Not captured. No tooltip was open.

## Dialog

The modal class `.popup-vBZs6V` computes white, radius 8px, shadow `rgba(0, 0, 0, 0.15) 0px 8px 16px`. No product dialog was opened. Login, download, and checkout were not entered.

## Toast

Not present on the pages visited.

## Card

The Plus plan card is 450px wide, padding 32px, radius 24px, border `2px solid #eeeeee`. The Limited Launch Special pill is `#37a866` on `rgba(60, 180, 110, 0.1)`, radius 36px, padding `4px 12px`.

Explore tiles are 240 by 210, with an image radius of 8px. Home promo modules use radius 8px and `overflow: hidden`. Photo grid figures at search have square corners.

## List row

Not a separate component. Search results are a photo grid. Related tags are 28px pills, fill `#eeeeee`, type `#555555`, radius 6px, padding `4px 10px`.

## Table

Not present.

## Avatar

A photo-page avatar computed 32 by 32, radius 50%.

## Badge

The deal pill above is the badge. No other badge was measured.

## Gaps

- No screenshot crops. The preview browser returned "The browser is not producing screenshot frames".
- Hover and pressed were read from stylesheets, not from a pointer press, except focus, which was applied with `element.focus()`.
- Download was not clicked. The two photo pages that loaded were Unsplash+ photos. A free-photo download control was not isolated.
- Login was not submitted. Join was not opened.
- Get Unsplash+ was not followed into checkout.
- Dark theme was resolved on a detached `.dark` node. No signed-out page painted it.
- Checkbox, tooltip, toast, table, and a destructive confirm were not on the public pages.
