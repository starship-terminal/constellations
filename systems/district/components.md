# Components

Public District, signed out, 2026-11-21. Values are token names from [tokens.json](tokens.json). Crops were not cut: the screenshots in [screenshots/](screenshots) are the evidence.

## Button

Header Login is a 40px pill (`core.radius.pill`), 13px semibold, text `light.color.control.loginText`, border `light.color.control.loginBorder`, hover fill `light.color.control.loginHover`. See [home-light-default.png](screenshots/home-light-default.png).

Dialog Continue, empty, is 48px, radius 12px, fill `light.color.control.disabledFill`, label `light.color.control.disabledText`. See [home-light-login-wall.png](screenshots/home-light-login-wall.png).

Contact "Send message" uses the brand purple fill. See [contact-light-default.png](screenshots/contact-light-default.png).

## Icon button

Carousel next control on artist rows. Login dialog close. Gallery next. See [home-light-default.png](screenshots/home-light-default.png) and [event-light-gallery.png](screenshots/event-light-gallery.png).

## Link

Primary nav. Selected item is `light.color.control.navSelected` with a 3px underline. Unselected is `light.color.text.primary`. Footer links are quiet text.

## Text field

Search is a pill shell in the header. Login phone field is 48px, radius 12px, border grey-400. Contact fields are grey filled. Nothing was typed. See [contact-light-default.png](screenshots/contact-light-default.png).

## Text area

Contact "How can we help?". Not filled.

## Select

Search scope listbox (All, Events). Location dialog city list. See [home-light-search-scope.png](screenshots/home-light-search-scope.png) and [home-light-location.png](screenshots/home-light-location.png).

## Checkbox

Not present on the captured public pages.

## Radio

Contact category tiles (Dining, Movies, Events, Other). Not selected.

## Switch

Not present. OTP channel is two pills, not a switch. SMS selected fill is `light.color.control.selectedFill`.

## Tabs

Primary nav behaves as tabs (For you, Events). Policies sidebar groups expand. See [policies-light-nav-open.png](screenshots/policies-light-nav-open.png).

## Menu

Search results listbox. Location dialog. Events filter dialog. See [home-light-search.png](screenshots/home-light-search.png) and [events-light-filters.png](screenshots/events-light-filters.png).

## Tooltip

Not observed.

## Dialog

Login wall and location picker. Dialog fill is white, radius 16px, shadow `0 25px 50px -12px rgba(0,0,0,0.25)`. See [home-light-login-wall.png](screenshots/home-light-login-wall.png).

## Toast

Not observed. No action was submitted.

## Card

Event posters with 16px top radius. Artist circles. Dining rows. See [events-light-default.png](screenshots/events-light-default.png) and [dining-light-default.png](screenshots/dining-light-default.png).

## List row

Corporate announcement rows. City list in the location dialog. Policy sidebar links.

## Table

Not present.

## Avatar

Circular artist photos, about 190px on desktop.

## Badge

Not a separate component. Date lines on event cards use a muted gold computed colour, not tokenised.

## Gaps

Pressed, focus-visible, loading, and error states were not held. Disabled is the empty Continue button only. Dark theme is declared in CSS and not shown. Signed-in components were not reached.
