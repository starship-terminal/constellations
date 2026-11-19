# Components

Values are computed styles from savee.com on 2026-11-19, CSS viewport 1169 by 731. No crops. `preview_snapshot` returned "The browser is not producing screenshot frames".

## Button

Primary, light. "Join for free" in the nav is `#0a0a0a` on `#fdfdfd` text, pill radius (`16777200px`), padding `16px 20px`, height 46, 14px medium, letter-spacing `-0.14px`. The hero copy is the same colours at height 56, padding `20px 40px`, 16px medium.

Primary, dark. On FAQ, contact and team the same control flips: background `#fdfdfd`, text `#0e0e0e`. "Contact us" and "Create your team" are height 56.

Secondary. "See plans" is `#dadada` with `#464646` text, height 56, padding `20px 40px`, weight 400.

Ghost. "Log in" on the light nav is transparent, `#404040` text, height 46, padding `16px 20px`, weight 400.

Outline. "Get Portfolio" and "Create team" are transparent with a `2px` inset ring of `#c4c4c4`, height 44, padding `14px 32px`, weight 400.

Social. "Continue with Google" and "Continue with Apple" share a transparent face, `#0a0a0a` text, and a `1.25px` ring of `#c4c4c4`. Height 44, padding `14px 32px`, pill. They were not clicked.

Disabled. Empty "Continue" on login has opacity `0.6`, cursor `default`, `aria-disabled="true"`. Filling the email field sets opacity `1` and cursor `pointer`. The field was cleared again. The form was not submitted.

Hover, focus-visible and pressed were not shown. The class string names `focus-visible:outline-2` with `outline-offset-2` and `outline-ring`. Ring token under light is `#5f5f5f`.

## Link

Nav links on home are 16px, weight 500, `#404040`, letter-spacing `-0.16px`, no underline. Footer links are `#464646`. "Terms of Service" and "Privacy Policy" sit under the login form. Dark nav links on FAQ compute `oklab(0.994 0 0 / 0.6)` at weight 550.

## Text field

Login, https://savee.com/login/. One field, `#login-email`, placeholder "Email or username", type text, width 328, height 49, padding `12px 0`, radius 0, transparent background, `#0a0a0a` text and caret, `1px solid #0a0a0a` bottom border. Placeholder is `#a3a3a3`. Focus outline is `none`. The field was filled with kaichen@agentmail.to and then cleared. Continue was not clicked.

Contact, https://savee.com/contact/, dark. Name and email inputs are `#1e1e1e`, radius 14px, padding `12px 16px`, height 46, width 320, weight 500, color `#a3a3a3`. Focus draws `rgb(229, 229, 229) 0 0 0 2px`. Placeholder on the message field is `#404040`. The form was not submitted. A Google reCAPTCHA iframe is on the page.

## Text area

Contact message field: same face as the contact inputs, height 128, placeholder "Describe your question or issue. We'll suggest relevant help articles as you type...". Not filled.

## Select, checkbox, radio, switch

Not present on the pages opened.

## Tabs

Pricing billing control on https://savee.com/upgrade/?source=nav_bar. The wrap is `#e4e4e4`, pill, padding 4px, height 48. "Yearly, save 25%" is selected: `#323232` background, `#e4e4e4` text, height 40, padding `10px 20px`, 14px weight 500. "Monthly" is transparent with `#5f5f5f` text. Monthly was not clicked, so the monthly prices were not read.

## Menu

Not present as an open menu. Nav is a fixed bar, not a dropdown.

## Tooltip

On https://savee.com/team/create/ a tooltip reading "Download Savee for iOS" is in the DOM at opacity 0. Face `#fdfdfd`, text `#0e0e0e`, radius 8px, padding `4px 8px`, 11px. It was not hovered, because screenshot frames were already failing and hover would not be evidenced.

## Dialog, toast

Not opened. Login has no error toast because the form was not submitted. Contact was not submitted.

## Card

Save tile: `#e4e4e4` (`--color-muted` / `--color-card`), radius 16px, height 320. Widths vary (214 to 257 on features). Class includes `transition-[translate,box-shadow] duration-150`.

Plan card: background `#fdfdfd`, radius 24px, padding 32px, 352 by 482. Popular (Pro) shadow is `rgba(0, 0, 0, 0.25) 0px 25px 50px -12px`. Portfolio and Team use `rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px`.

## List row, table

FAQ is a 3-column grid (`gap-x-20 gap-y-24`, 1103px wide at this viewport), not a table. Questions are 30px medium `#fdfdfd` on the dark FAQ page. The first answer, after a click, is 21px weight 500, `#a3a3a3`, line-height 25.2px.

## Avatar, badge

"Popular" is a pill badge: `#0a0a0a` background, `#fdfdfd` text, padding `4px 10px`, 13px medium. No avatar component was measured. Review buttons name people. Those names stay in the live page and are not copied here as specimens.

## Icon button

"Close" on the floating home player is 26 by 26, transparent, `#5f5f5f`, pill. "Show another save" tiles on login use radius 8px.

## Gaps

- Hover, focus-visible and pressed were not shown.
- No screenshots or crops. Preview frames failed.
- Signed-in library, boards and search were not entered.
- Google, Apple and the magic-link submit were not used.
- No card was entered. Pricing CTAs were not clicked.
- Contact was not submitted. reCAPTCHA was not solved.
- Phone 390 and desktop 1440 were not applied. Live width was 1169.
- Dark theme on the marketing home was not switched. FAQ, contact and team shipped `theme-dark` on their own.
- `prefers-reduced-motion` was not emulated.
