# Contra components

Public signed-out components measured on contra.com on 19 November 2026. The signed-in app was not opened.

| Component | State | Evidence | Values |
|---|---|---|---|
| Button, primary | Default, hover, focus | [button-primary-default.png](components/crops/button-primary-default.png) | 48px tall, 24px radius, padding 0 24px, gap 8px, fill `{background.action}` `#222834`, label `{text.on-action}`, 1px border the same colour. Hover left the fill unchanged. Focus outline 2px solid `{border.focus}`, offset 2px |
| Button, outline | Default, hover, focus | [button-outline-default.png](components/crops/button-outline-default.png) | 48px tall, 24px radius, padding 0 24px, white fill, 1px border `{border.stroke}` `#373f51`, label the same. Hover left the fill unchanged. Focus outline matched the primary button |
| Button, prompt | Default | [home-light-default.png](screenshots/home-light-default.png) | Let's go, 36px tall, radius 999px, padding 0 16px 0 12px, fill `{background.action-soft}` `#1c212b`, 14px weight 500 |
| Button, disabled submit | Empty login | [login-light-default.png](screenshots/login-light-default.png) | 48px tall, 24px radius, fill `{background.disabled}` `#f2f4f7`, label `{text.disabled}` `#d0d4dc`. Shown because the email field was empty. Nothing was typed |
| Link, nav | Default, hover | [home-light-default.png](screenshots/home-light-default.png) | Payments, 16px weight 600, colour `{text.primary}`, no underline. Hover colour `{text.link-hover}` `#1d212a`, still no underline |
| Chip, suggestion | Default | [home-light-default.png](screenshots/home-light-default.png) | 38px tall, radius 100px, padding 8px 14px, white fill, 1px border `{border.subtle}` `#e5e7eb`, label `{text.secondary}` 14px weight 400 |
| Chip, role | Default | [home-light-default.png](screenshots/home-light-default.png) | 40px tall, radius 32px, padding 8px 16px, transparent fill, label `{text.muted}` |
| Tab | Default, selected | [home-light-default.png](screenshots/home-light-default.png) | Projects was transparent with `{text.primary}`-adjacent `#222834`. People fill `{background.selected}` `#f5f6f9`, label `#4a5264`, 42px tall, 8px radius, padding 0 16px, 19px weight 500 |
| Text area, prompt | Default | [home-light-default.png](screenshots/home-light-default.png) | Placeholder "How can I help you?", 16px, colour `#222834`, transparent fill, 0 border on the textarea itself. The rounded shell is the parent, not a separate measured node |
| Text field, email | Default | [login-light-default.png](screenshots/login-light-default.png) | 56px tall, 485px wide, radius 12px, padding 0 16px, 1px border `{border.field}`, white fill, placeholder name@work-email.com. Nothing typed |
| Text field, name | Default | Computed style on `/sign-up` | First name 234 by 56px, 12px radius, 1px border `{border.field}`. Last name same size, border `{border.subtle}`. Nothing typed. No screenshot kept, because a Cloudflare Turnstile widget was on the page |
| Card, topic | Default | [home-light-default.png](screenshots/home-light-default.png) | 320 by 168px, radius 16px, photo fill. Text on the card was white |
| Card, auth | Default | [login-light-default.png](screenshots/login-light-default.png) | White card on `{background.canvas}` `#f5f6f9`. Corner radius was not a single computed node |

## Gaps

- Button pressed, loading: not held. The empty login submit is the only disabled-looking control that painted.
- Button hover colour: computed background stayed `#222834` on Sign up and white on Post a job. No hover fill was measured.
- Text area chrome: the prompt box's radius sits on a parent. The textarea itself measured radius 0 and border 0.
- Select, checkbox, radio, switch, menu, tooltip, dialog, toast, table, badge: not present on the pages that loaded. PRO and MAX labels appear on profile cards further down the home page and were not isolated.
- Avatar: profile photos are on the home page. They are other people's pictures, so no crop was cut.
- Signup form: first name, last name, and email are on the page, plus a Cloudflare Turnstile widget. Nothing was entered. No screenshot was kept.
- Google continue: the button was measured (48px, radius 24px, fill `#222834`). It was not clicked. That path is company SSO.
- Dark theme: `prefers-color-scheme: dark` left the home page white. `--rollout-*` resolved to a dark pair on the same page and is not a live theme.
- Icons: the site icon is [icon.png](icon.png). Inline nav SVGs were not extracted. `icons/` is a catalog gap.
