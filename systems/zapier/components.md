# Zapier components

Public marketing and signed-out login, measured 2026-11-19 from computed styles on [https://zapier.com/](https://zapier.com/), [https://zapier.com/pricing](https://zapier.com/pricing), [https://zapier.com/app/login](https://zapier.com/app/login) and [https://zapier.com/sign-up](https://zapier.com/sign-up). Hover, focus-visible and pressed values that were not held live come from the fetched marketing stylesheet and are labelled that way.

Screenshots were not produced. `preview_snapshot` returned "The browser is not producing screenshot frames". Crops are absent for the same reason.

## Button

Brand, ink, secondary and subtle. The nav Sign up control is a brand pill.

| Variant | Default | Hover and active | Disabled |
|---|---|---|---|
| Brand | Fill `{color.action.fill}`, label `{color.text.on-accent}`, 1px border the same colour, radius `{radius.4}`, weight 600 | Stylesheet sets fill and border to `{color.action.fill-hover}` | Fill `{color.action.disabled}`, label `{color.text.disabled}`, opacity 0.75. Seen live on the empty login Continue button |
| Ink | Fill `{color.action.ink}`, label `{color.text.on-accent}`. Pricing "Try it free" | Stylesheet hover fill `{color.action.ink-hover}` | Same disabled rule as the base button |
| Secondary | Transparent fill, 1px `{color.border.strong}`, label `{color.text.primary}`. "Start free with Google" | Stylesheet: label `{color.neutral.800}`, border `{color.border.default}` | Not seen |
| Subtle | No border, weight 400, transparent fill. Nav "Log in" | Stylesheet hover fill `{color.neutral.200}` | Not seen |
| Pill | Nav Sign up: brand colours, radius `{radius.18}`, height `{size.control-sm}` | Not held | Not seen |

Sizes. Stylesheet xsmall and small are 36px with padding 6px 12px. The home hero brand button measured 40px tall with padding 8px 16px and 16px type at innerWidth 1169. From 1024px the stylesheet raises non-xsmall buttons to 48px, padding 12px 24px, 18px type. Login SSO buttons and the pricing CTA measured 48px and 18px.

Focus-visible, from the stylesheet: outline 2px solid `{color.border.focus}`, offset 2px. Not held live.

Pressed uses the same stylesheet rule as hover. Not held.

Loading was not on any page.

## Icon button

The signup password field has a 16 by 24 "Show password" control, color rgb(110, 107, 94), Arial, padding 4px 8px. That grey is not in the marketing ramp, so it stays in the gap list. No other icon button was measured.

## Link

Nav links use the subtle button. Inline links on login ("Forgot Password?", "Sign Up") are `{color.text.link}`, 14px, underline. The Contact Sales link in the login header computed to rgb(55, 17, 52) (`{color.neutral.plum-link}`), weight 500, no underline. Cell links in the stylesheet turn `{color.text.link-hover}` on hover and focus-visible. Focus on menu links is a 1px dashed `{color.neutral.800}` outline, offset 4px.

## Text field

Login email and password, and the signup fields, share `zapier-marketing-ui-input-bLrqx3gJ`.

- Height 48px, padding 8px 12px, radius `{radius.4}`, 16px Inter, fill `{color.bg.page}`, text `{color.text.primary}`.
- Rest border `{color.border.default}`.
- The autofilled email on login and signup had border `{color.border.strong}` and shadow `{shadow.focus-input}`. That is the stylesheet `:focus` rule (`border-color #201515; box-shadow 0 0 0 1px #201515; outline none`). The browser had focused the first field.
- Hover, stylesheet only: border `{color.neutral.600}`.
- Disabled, stylesheet only: text `{color.text.disabled}`, fill `{color.neutral.200}`, opacity 0.7.
- Invalid, stylesheet only: border and shadow `{color.status.danger}`. Not shown.

## Text area

Stylesheet `.zapier-marketing-ui-textarea` is 96px tall, 16px Inter, line-height 1.5, text `{color.text.primary}`, fill `{color.bg.page}`. Not on any page visited.

## Select

A popover listbox is declared (fill `{color.bg.overlay}`, border `{color.border.default}`, radius `{radius.4}`, shadow `{shadow.popover}`, max-height 184px). Not opened.

## Checkbox

Stylesheet: 18px square, radius `{radius.2}`, 1px `{color.neutral.600}` border. Checked fill and border `{color.border.strong}`, white check via clip-path. Focus-visible outline 1.5px solid `{color.border.focus}`, offset 2px. Disabled border `{color.neutral.500}`. Invalid border `{color.status.danger}`. Not shown on the pages that were measured. OneTrust checkboxes were in the DOM at 0 height.

## Radio

Pricing "Pay monthly" / "Pay yearly" uses `zapier-marketing-ui-input-VK-U8LJi`. Computed: 18px, radius 50%, 1px border. Unchecked border `{color.neutral.600}`. Checked border `{color.border.strong}`. Stylesheet adds a 10px inner dot of `{color.border.strong}` when checked. Focus-visible outline 1.5px, then a later rule of 1px, both `{color.border.focus}`. The 1px rule wins in the stylesheet.

## Switch

No Zapier switch was on these pages. OneTrust uses a switch class inside the hidden preference center. Not measured.

## Tabs

Pricing page tabs (Platform, Agents, Chatbots). Selected: fill `{color.action.ink}`, label `{color.text.on-accent}`, height 64px, padding 0 20px, radius `{radius.8}`, 24px weight 600, `aria-selected=true`. Unselected: fill `{color.bg.page}`, label `{color.text.primary}`, 1px `{color.border.strong}` border. Hover and focus were not held. A stylesheet tab list sets `--tab-underline-color` to `#381933`, and a brand context sets it to `#ff4f00`. That underline tab was not the pricing control.

## Menu

The Products menu was already in the DOM on the home page (links to Workflows, MCP, SDK, Tables). Its open panel was not measured as a separate layer. Stylesheet menu: fill `{color.bg.overlay}`, radius `{radius.4}`, padding 4px, shadow `{shadow.menu}`, offset 4px below the trigger.

## Tooltip

Not present in the marketing stylesheet under that name, and none was opened.

## Dialog

Not opened. No scrim colour was read.

## Toast

Not present.

## Card

Home feature cards: rest fill `{color.bg.raised}`, padding 24px, radius `{radius.12}`, about 270 by 188. Active card: fill `{color.bg.selected}` and a 1px `{color.border.strong}` ring (`box-shadow: rgb(32, 21, 21) 0px 0px 0px 1px`).

Pricing plan cards: fill `{color.bg.surface}`, 1px `{color.border.default}`, padding 28px, radius 0, width 283px at innerWidth 1169. Price amount 36px / 54px, weight 500.

Login card: 1px `{color.border.subtle}`, radius `{radius.4}`, padding 32px, width 430px. No shadow.

## List row

Footer app index and nav menu links are rows of text links. A dedicated list-row component was not isolated.

## Table

Not on the pages visited.

## Avatar

Not on the signed-out pages.

## Badge

Stylesheet `.zapier-marketing-ui-badge-ioc1fBpb`: padding 4px, 12px weight 500, 1px border, radius `{radius.4}`. Not isolated on a live element. The home eyebrow is type, not a badge.

## Gaps

- No screenshots or crops. Preview frames were not produced.
- Dark theme: none of the four pages exposed a theme switch. Not captured.
- Phone width 390: not captured. Desktop plan width 1440: the live tab was 1169 by 731.
- Hover, pressed, focus-visible and invalid states were not held. Declared values are in the tables above.
- Dialog, toast, tooltip, switch, table, avatar, loading and empty states: not on these pages.
- Signed-in app: not entered.
- Signup was not submitted. It asks for a name and a password, not email only.
- SSO, Google, Facebook and Microsoft buttons were not followed.
- Scrim colour: not captured.
