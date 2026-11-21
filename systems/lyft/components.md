# Components

Public marketing controls only. Values are token names from [tokens.json](tokens.json). Crops were not cut. The full screenshots show the control.

## Button

Primary. "Get a ride" in the header. Background `light.surface.interactive` (`#820076`), text `light.text.primary-inverse`, height `core.sizing.button-height` (48px), radius `core.radius.pill` (48px), padding `core.space.button-x`. Font Rebel Sans Text 16/22 weight 400.

Shown in [screenshots/home-light-default.png](screenshots/home-light-default.png).

Hover computed style did not change. Pressed was not held. Disabled and loading were not on the page.

Secondary outline. "Schedule for later" on the cities page, white fill, dark stroke, pill radius. Observed in [screenshots/cities-light-default.png](screenshots/cities-light-default.png). Values not read off that control.

## Link

Header "Log in" is Rebel Sans Text 16, colour `light.text.primary`, no underline. Shown in [screenshots/home-light-default.png](screenshots/home-light-default.png).

Inline legal links on the homepage are `light.text.interactive` (`#ac2a9e`).

## Text field

Login phone field, empty, with a country chip and placeholder "Phone number". Shown in [screenshots/login-light-default.png](screenshots/login-light-default.png). Focused, still empty, in [screenshots/login-light-phone-focused.png](screenshots/login-light-phone-focused.png). No focus ring was visible. Nothing was typed.

Driver apply field, empty, placeholder "Mobile Phone Number". Shown in [screenshots/signup-light-default.png](screenshots/signup-light-default.png).

Search fields on cities and help are empty. Not submitted.

## Checkbox

"Keep me signed in" on the login wall, unchecked. Not toggled. [screenshots/login-light-default.png](screenshots/login-light-default.png).

## Card

Ride-type cards. White surface, 16px radius, 24px 16px padding. Standard expands to a raised card with "Request Standard". [screenshots/home-light-ride-standard.png](screenshots/home-light-ride-standard.png). "Request Standard" was not clicked.

## Menu

No desktop flyout opened on hover of Rider, Driver, or Business. The phone drawer is the menu. [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Dialog

Help center region dialog ("You're viewing the Lyft US Help Center") was on screen and hidden before the kept shot. Select region was not pressed. The consent toast was hidden the same way.

## Not present on the public pages

Text area, select (the country control on cities is a native-looking dropdown and was not opened), radio, switch, tabs, tooltip, toast (consent only), table, avatar, badge, icon button beyond carousel arrows.

## Gaps

Signed-in controls, validation errors, loading, and disabled states were not reached. The capture stopped at the empty login and driver-apply walls.
