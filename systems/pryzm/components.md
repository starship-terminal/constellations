# Components

Measured on the dark public pages. Rest state only. Hover, focus-visible, pressed, disabled and error were not captured.

## Button

| Variant | Where | Fill | Label | Size | Radius |
|---|---|---|---|---|---|
| Primary | Get Pryzm Pro, Subscribe, Continue, Create account | `#e5e5e5` | `#171717` | 32px tall on marketing, 12px / 500. 44px tall on sign-in, 14px / 500 | 8px |
| Secondary | Open Flow | `#262626` | `#fafafa` | 32px, 12px / 500 | 8px |
| Outline | Browse inspiration, Share, Export | white at 4.5% | `#fafafa` | 32px, 12px / 500, 1px border `#ffffff1c` | 8px |
| Ghost | Header Open studio, header Sign in | white at 15% | `#ffffff` | 24px, padding 0 8px, 12px / 500, 1px border white at 20% | 8px |
| Text | Reset password, Sign up | none | `#fafafa`, Sign up is weight 600 | 14px / 500 or 600 | 0 |

Transition on the button class is `all 150ms cubic-bezier(0.4, 0, 0.2, 1)`.

## Segmented control

Monthly is selected: fill `#fafafa`, label `#000000`, 32px tall, padding 6px 14px, pill radius, 14px / 500. Yearly is rest: transparent fill, label `#ffffff` at 60%. The "3 months free" tag sits inside the Yearly control.

## Text field

Sign-in email and password: 383px by 44px, 8px radius, 1px border `#ffffff1c`, fill `#000000`, padding 0 12px, 14px Inter, placeholder "Email address*" and "Password*". The password field has extra right padding (40px) for the visibility icon.

Footer newsletter input (`#newsletter-footer`): 32px tall, 8px radius, 12px text, same border and black fill, placeholder "you@example.com". It was not submitted.

Lab numeric fields: 68px by 32px, 8px radius, 12px text, fill white at 4.5%, border white at about 10%.

## Checkbox

Sign up has one checkbox, 16px, unchecked, next to "Email me about new features and gallery drops." The painted box was not isolated from the native control.

## Chip

Gallery filters. Selected All: fill `#e5e5e5`, label `#171717`, 26px tall, padding 4px 12px, pill radius, 1px border `#fafafa`, 12px text. Rest chips: transparent fill, label `#ffffff` at 60%, 1px border `#ffffff1c`.

## Badge

PRO on gallery cards: 10px / 600, letter-spacing 0.25px, padding 2px 6px, height 16px, pill, white label, black at 40% fill, 1px border white at 20%.

Popular on the Pro plan: 11px / 500, padding 2px 8px, pill, fill `#141414`, label `#ffffff` at 60%, 1px border `#ffffff1c`.

## Card

Gallery card: fill `#141414`, 1px border `#ffffff1c`, 18px radius, title 14px / 600 with -0.35px letter-spacing. Width was 261px at 1169px and 210.8px in the 1440 gallery. Hover class is `-translate-y-0.5` over 300ms. Hover was not screenshotted.

Pricing card: 372px wide, 14px radius, 24px padding, 1px border `#ffffff1c`, black fill. Price is 30px / 600 with -0.75px letter-spacing.

## Sidebar item

256px sidebar, black. Item is 240px by 32px, 14px Inter, padding 8px, radius 11.2px. The active Inspiration item fills `#141414`.

## Link

Footer and about links use muted text (`#ffffff` at 60%) at 14px, with a color transition of 150ms. The Framer templates link in the about body is weight 600.

## Not present on these pages

Select (the Lab Blend control looks like a select and was not opened), textarea, radio, switch, tabs, menu, tooltip, dialog, toast, table, avatar. FAQ questions were in the homepage text and no accordion trigger was measured.
