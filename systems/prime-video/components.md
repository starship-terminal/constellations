# Components

Measured on the signed-out marketing page and the Amazon sign-in wall it redirects to. No crops: the preview browser did not produce screenshot frames.

## Button

The trial CTA is an inline-flex link. Background `#ffffff`, text `#00050d`, 18px Ember at weight 500, line-height 22px, padding 8px 18px, height 60px, radius 8px. Transition 200ms `cubic-bezier(0.25, 1, 0.5, 1)` on transform, background-color, color and outline. `--fable-button-primary-height-min` is 60px and `--fable-button-primary-padding-vertical` is 8px, which matches. Hover, pressed and disabled were not read.

## Nav link and Join Prime

Nav links are 14px Ember at weight 500, letter-spacing 0.49px, padding 0 12px, height 38px, radius 8px, colour `#ffffff` on a transparent background. Join Prime uses the same box with background `rgba(26, 152, 255, 0.8)`. Focus outline on a nav link was `#f1f1f1` solid 2px, offset -2px. The first focusable control used `#e59700` auto 5px, offset -2px.

## Link

Footer links are 15px Ember, colour `#79b8f3`, line-height 19px, no underline. Amazon sign-in links are Arial 14px (legal row 12px), colour `#2162a1`.

## Text field

Present only on the Amazon wall. `#ap_email` is 32px tall, padding 5px 11px, radius 8px, background `#ffffff`, text `#0f1111`. Focused border is 1px `#2162a1`. The unfocused password border was 1px `#888c8c`. Nothing was typed.

## Card

Amazon `.a-box` is 350px wide, background `#ffffff`, border 1px `#d5d9d9`, radius 8px. Inner padding is 20px 26px. No shadow.

## Heading

Marketing h1 uses the heading-800 class: 36px / 40px / 700 Ember, white, on a 529px column. Amazon's "Sign in" heading is 20px / 28px / 400 Arial.

## Footer

Background `#222222`, text `#8197a4`, 15px / 19px, padding 24px.

## Gaps

| Component | Why it is missing |
|---|---|
| Icon button, text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, list row, table, avatar, badge | Not rendered on the signed-out marketing page or the sign-in wall. Dialog radius (24px) and toast radius (8px) exist as custom properties only. |
| Hover, pressed, disabled, loading, error | Not triggered. Entering the email field and submitting would start account creation. |
| Crops | Preview browser returned no screenshot frames. |
| Icons | Search, caret and category SVGs were in the nav. Their path data was not extracted, and the wordmark is a raster PNG. |
