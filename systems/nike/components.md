# Nike components

Public signed-out surfaces on nike.com/sg, 2026-11-19. Crops are 2x except the product card, which is 1x. Nothing was added to a bag.

## Button

Add to Bag is the primary control. Computed fill `#111111`, label `#ffffff`, height 60px, padding 18px 24px, radius 30px, Helvetica Now Text Medium 16px / 500. Hover fill computed `#707072`, which matches `--podium-cds-button-color-bg-primary-hover`. The button was not clicked.

![Add to Bag](components/crops/button-add-default.png)

![Add to Bag hover](components/crops/button-add-hover.png)

Shop and Explore on the home hero are white pills: fill `#ffffff`, text `#111111`, height 36px, padding 6px 16px, radius 30px. They sit on the photograph, so a rest crop would include the photo. The home screenshot shows them.

Favourite is a second 60px pill, transparent fill, `#111111` label, radius 30px. No border was computed on the button element.

![Favourite](components/crops/button-secondary-default.png)

## Icon button

The header search, heart, and bag are 36px icon buttons. The search button opens the field. Heart and bag were not activated. Bag is empty chrome, not a checkout.

## Link

Join Us and Sign In are 16px Helvetica Now Text Medium, `#111111`, no underline at rest. Shop Now in the promo strip is 12px and underlined. Sign In was not followed into an account.

![Join Us](components/crops/link-join-default.png)

## Text field

Header search is `#f5f5f5`, height 36px, radius 24px, Helvetica Now Text Medium 16px. Expanded width on desktop computed 808px. Focus outline computed as `none`.

![Search](components/crops/search-default.png)

Help search ("What can we help you with?") is a 56px field, radius 8px on the input. Computed `border-width` on the input and its wrappers was `0px`. The grey outline visible in the help screenshot is not in those computed styles. Recorded as a gap.

![Help field](components/crops/field-help-default.png)

## Text area

Not present on the public pages opened.

## Select

Sort By is a text control on the listing. Its open menu was not captured.

## Checkbox, radio, switch

Not present on the public pages opened. Size is a grid of chips, not a radio control in the reading.

## Tabs

Not present.

## Menu

Hovering Men opens a white panel, height 417px, shadow `none`, with Featured, Shoes, and the rest of the department list.

![Men menu](screenshots/home-light-menu.png)

## Tooltip

Not captured.

## Dialog

Closed video dialogs are mounted in the home DOM ("This is a modal window."). No dialog was opened. Cookie banner was not present.

## Toast

Not present.

## Card

Product tiles on Men's Shoes are square photographs (348px at 1440) on a light grey field, radius 0px, with the name in `#111111`, the subtitle in `#707072`, and the price in `#111111` at 16px / 500. Just In is `#d33918`.

![Product card](components/crops/product-card-default.png)

## List row

Store rows on Find a Nike Store: name in black, address in grey, status "Closed" in red. The addresses are Nike's published store addresses.

## Table

Not present.

## Avatar

Not present. Signed out.

## Badge

Just In and Available in SNKRS are text, not a filled chip. Just In computed `#d33918` (`--pds-color-text-badge`).

## Size chip

Available size: 48px tall, radius 4px, 1px border `#cacacb`, text `#111111`. Unavailable: fill `#f5f5f5`, text `#9e9ea0`, same border. Selecting US M 9 did not change the computed background of the text node. The selected border, if any, was not read off the chip wrapper. Add to Bag stayed unclicked.

![Size](components/crops/size-default.png)

## Gaps

- Dark theme: `color-scheme` computed `normal`. No theme toggle on the public storefront.
- Pressed, loading, and error states of Add to Bag: not captured. The control was not clicked.
- Focus ring on buttons: `--podium-cds-color-focus-ring` is `#1151FF`. A live focus-visible ring was not captured.
- Help field border: visible in the screenshot, computed border width 0. Not tokenised from a computed border.
- Sign-in form: `/sg/register` redirected to accounts.nike.com and returned Access Denied (Akamai). No fields measured. The denial screenshot is not in the package.
- Checkout, bag contents, member account: not entered.
