# Components

Signed-out Twitch, 2026-11-21. Values are computed styles and custom properties from headless Playwright at 1440 by 900, device pixel ratio 2, unless a row says otherwise.

## Button

Primary Sign Up is a pill. Fill `#9147ff`, text `#ffffff`, height 32, weight 600, radius `9000px`. Hover computed `#772ce8`. Mouse-down computed `#5c16c5`.

![Sign Up](components/crops/button-primary-default.png)

Secondary Log In uses `rgba(83, 83, 95, 0.38)` in dark and the same 32px pill. Light secondary token is `rgba(173, 173, 184, 0.22)`. The community banner paints a white Sign Up with black text.

![Log In](components/crops/button-secondary-default.png)

Disabled Continue on the login dialog is `rgba(83, 83, 95, 0.55)`, `disabled` true, until the field is valid. The field was not filled.

## Icon button

The search submit sits on the right of the search field, 36px tall, fill `rgba(83, 83, 95, 0.38)` in dark. The focused field grows a purple ring around the pair. See [screenshots/home-dark-search.png](screenshots/home-dark-search.png).

## Link

"Use phone number instead" and "Trouble logging in?" use the link colour: `#bf94ff` in dark, `#5c16c5` in light. The selected directory tab uses the same purple. Link hover was not held. The dark hover token is `#a970ff`.

## Text field

Search is 36px tall, fill `#18181b` in dark, radius `8px 0 0 8px`. The signup email field is 32px tall, 488px wide, radius 8px, with an inset 1px ring `rgba(222, 222, 227, 0.95)`. Focus replaces that ring with a 2px `#a970ff` outer and inset shadow. The login field is 36px tall and 488px wide. In light its fill is `#ffffff` and the focus ring is `#772ce8`. No text was typed.

![Email focus](components/crops/field-email-default.png)

![Search](components/crops/search-default.png)

## Text area

Not present on the signed-out pages.

## Select

Directory sort is a pill button, "Recommended For You". The open menu has two rows: Recommended For You (selected) and Viewers (High to Low). Neither was chosen. See [screenshots/directory-dark-sort.png](screenshots/directory-dark-sort.png).

Language on a category page opens a checkbox list (English, Bahasa Indonesia, and further names) with Clear all. No box was checked. See [screenshots/category-dark-language.png](screenshots/category-dark-language.png).

## Checkbox

Present in the language menu. Unchecked. The check mark colour was not isolated.

## Radio

Not present on the signed-out pages.

## Switch

The user menu has a Dark Theme switch, `role="switch"`, `data-a-target="tw-toggle"`. Off is light (`aria-checked="false"`, class `tw-root--theme-light`). On is dark. It was toggled for the readings and left on dark for the dark shots.

Labeled Content has a Hide Labeled Content switch. It was photographed on and not changed. See [screenshots/home-dark-labeled.png](screenshots/home-dark-labeled.png).

## Tabs

Directory uses Categories and Live Channels. The selected tab is the link purple. Category pages use Live Channels, Videos, and Clips. See [screenshots/directory-dark-default.png](screenshots/directory-dark-default.png).

## Menu

More Options is the header ellipsis. It lists General links (About, Blog, Download Apps, Turbo) and Help & Legal. See [screenshots/home-dark-more.png](screenshots/home-dark-more.png) and [site-tree.md](site-tree.md).

The user menu lists Language, Dark Theme, Labeled Content, and Log In. Log In opens the login wall. See [screenshots/home-dark-user-menu.png](screenshots/home-dark-user-menu.png).

## Tooltip

Not opened. `--color-background-tooltip` is `#ffffff` in dark and `#1f1f23` in light. Those values were not confirmed on a painted tip.

## Dialog

Log In and Sign Up are centered panels on a scrim, form width 488. Title is Roobert 24px / 500. The signup panel also offers phone signup and Google, Amazon, and Apple. None of those were followed. See [screenshots/login-dark-default.png](screenshots/login-dark-default.png) and [screenshots/signup-dark-dialog.png](screenshots/signup-dark-dialog.png).

`--color-background-modal` (`#15052e` in dark) does not match the painted grey panel.

## Toast

Not present.

## Card

Live cards are 16:9 thumbs with a red LIVE badge, a viewer count, a title, an avatar, a name, and pill tags. Category cards are square art with a title and a viewer count.

![Live card](components/crops/card-live-default.png)

![Category card](components/crops/card-category-default.png)

## List row

The left rail is a channel row: avatar, name, category, red viewer count. See [components/crops/sidebar-default.png](components/crops/sidebar-default.png).

## Table

Not present.

## Avatar

Circular, on channel rows and live cards. See [components/crops/card-channel-default.png](components/crops/card-channel-default.png).

## Badge

LIVE is `#eb0400`, white text, 4px radius, 12px type. A red count badge sits on the Prime offers icon. Tags are grey pills.

## Gaps

- Signed-in chat, settings, and following were not opened.
- A submitted validation error was not produced.
- Tooltip, radio, text area, toast, and table were not on these pages.
- Light hover and pressed were not held.
- Reduced motion was not probed.
