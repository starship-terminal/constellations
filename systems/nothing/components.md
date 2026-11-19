# Components

Measured on the public signed-out pages on 2026-11-19. No crops: the preview browser did not produce screenshot frames.

## Button

Store marketing buttons are links with `rounded`, padding `12px 16px`, height 40px, radius 4px, NType82-Regular 16px / 22.4px, weight 400.

| State | Fill | Text | Where |
|---|---|---|---|
| Default (SHOP NOW, DISCOVER, PLAY) | `#ffffff` | `#040404` | Home and Nothing OS |
| Add to bag | `#040404` | `#ffffff` | Phone (4a) Pro. LatteraMonoLL 11px / 12.1px, padding 16px, radius 6px, height 48px |
| Hover, pressed, disabled, loading | Gap | Gap | Declared `hover:opacity-70` and `hover:bg-pure-black/80`. Not painted in this capture |

Focus is declared as a 2px `accent-yellow` outline with a 2px offset on the logo and nav links. Programmatic focus did not paint it.

Support Centre uses a different button: transparent fill, 1px `#000000` border, radius 800px, LetteraMonoLL 18px weight 300, padding `16px 20px`, height 54px.

## Link

Footer links use Ndot-Regular 40px / 40px, uppercase, `#ffffff` on `#040404`, opacity transition 100ms `cubic-bezier(0.4, 0, 0.2, 1)`.

Quiet links use `#595a5a` (`--greyscale-900`) and a 200ms opacity transition. The declared hover is opacity 0.7.

## Text field

The footer newsletter field is an email input, placeholder "Email address", fill `rgba(60, 60, 60, 0.6)`, text `#ffffff`, Geist Mono Variable 12px / 15px, uppercase, padding `8px 16px`, radius 4px, height 48px, no border. I did not submit it.

The Support Centre search field is white, NType82 18px weight 300, padding `12px 20px 12px 0`, radius 0, height 40px.

## Icon button, menu, dialog, toast, tabs

Not captured as Nothing components. The cookie notice was Didomi (Arial, 8px radius, black Agree button). I dismissed it with Disagree and close.

## Card

Category tiles (EARBUDS, HEADPHONES, PHONES, CMF) are 234 by 267 at this viewport, with a 500ms opacity transition and `motion-reduce:transition-none`. The label is Geist Mono Variable 14px, uppercase, `#595a5a`. No separate card fill was sampled.

## Gaps

- No screenshots or crops. Preview snapshot failed.
- No hover, pressed, disabled, loading, or error states.
- No text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, table, avatar, or badge from the product's own UI.
- Nav at 1169px was `display: none` (the desktop nav class is `xl:block`).
- Account login and contact-support forms were not filled.
