# Luma patterns

How the components in [components.md](components.md) combine into Luma's screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots).

## App shell and navigation

A floating glass tab bar holds three tabs: Home, Discover and Chat. The selected tab sits in a pill darker than
the bar in both themes and its label takes the ink (`color.surface.selected`, `color.text.tabSelected`); a red count
marks unread chats. There is no bar fill at the top. Tab roots open with the account avatar, a 22 pt bold title
(or the Luma wordmark on Home) and a glass capsule of actions at the top right; pushed pages float a round glass
back button and centre a 17 pt title. Content scrolls under both and blurs under the header
([02-home-scrolled](screenshots/dark/02-home-scrolled-header-blur-picked.png)). See
[01-home](screenshots/dark/01-home-your-events-calendars.png), [09-discover](screenshots/dark/09-discover-popular-category-chips.png)
and [28-chat-list](screenshots/dark/28-chat-list-unread-dot.png).

The app has two page backgrounds. Full-bleed pages (Home, Discover, Chat, search, Your Events, Notifications, a
category or calendar page) sit on `color.bg.page`, pure black or pure white. Settings and its pushed pages sit on
`color.bg.grouped` with rows in cards (`color.surface.card`); in dark the two backgrounds are the same black, in
light the grouped page is a pale grey under white cards ([23-settings light](screenshots/light/23-settings-root-grouped-rows.png)).

Event pages and the Create Event sheet are the exception: they take their background, buttons and fields from the
event's cover image, in both themes, so a light-theme event page is as dark as a dark one when the cover is dark
([05-event-page light](screenshots/light/05-event-page-cover-tinted-actions.png),
[18-create-event](screenshots/dark/18-create-event-form-cover-tinted.png),
[18-create-event light](screenshots/light/18-create-event-form-cover-tinted.png)). The Create Event cover is random,
so dark shows an orange sheet and light a purple one. `color.coverExample` holds one reading of each; derive the
tint from the cover instead.

Layers, bottom to top: page, card, glass controls (tab bar, nav buttons, chips, the segmented control, the
composer), then menus and sheets, which are glass too. No shadows are drawn.

## Lists and data display

The event row is the core list item: an 80 pt square cover with an 8 pt corner, then the host line (12 pt
grey), the title (17 pt medium, up to two lines on a 22 pt line) and meta lines (15 pt grey, with clock and pin
icons). A pill at the top right gives the price in green or the state (Sold Out red, Near Capacity amber, Waitlist
Open blue), each a faint wash of its label colour. An Invited badge straddles the cover's lower edge in purple.
Rows group under date sections, the date in the ink and '/ weekday' in `color.text.tertiary`; hairlines start at
the row text. See [31-your-events](screenshots/dark/31-your-events-segmented-upcoming-soldout-badge.png),
[03-home-picked](screenshots/dark/03-home-picked-date-sections.png) and
[13-search-typed](screenshots/dark/13-search-typed-results-waitlist-badge.png).

Horizontal rails show calendars (80 pt tiles), cities (photo cards with the name over the image) and featured
calendars ([01-home](screenshots/dark/01-home-your-events-calendars.png),
[10-discover](screenshots/dark/10-discover-cities-featured-calendars.png)). The map shows events as stacks of cover
thumbnails with a name and a '+N more' count ([16-map](screenshots/dark/16-discover-map-event-clusters.png)).

Chat rows show the event cover, a bold title, a one-line preview and a grey date, with a red dot for unread
([28-chat-list](screenshots/dark/28-chat-list-unread-dot.png)). Notifications put an avatar with a small role badge
before a sentence with bold names and a grey age, and the event cover after it
([17-notifications](screenshots/dark/17-notifications-list-unread-tint.png)).

## Forms and validation

Create Event is a cover-tinted sheet: a large cover with an image button, a bold Event Name field, a Start and End
group, Choose Location and Add Description rows, then Ticketing and Options sections with a switch and pop-up values
(Free, Public, Unlimited). The check at the top right is a faint glass circle until a name is typed and the ink
once one is ([19](screenshots/dark/19-create-event-ticketing-options-switch-popups.png),
[20](screenshots/dark/20-create-event-name-typed-confirm-enabled.png)). Edit Profile uses capsule fields with a grey
label on the left, a rounded Bio area and a list of social handle rows
([27-edit-profile](screenshots/dark/27-edit-profile-fields-social-handles.png)). Settings values that are choices
open pop-up menus, shown by an up-down chevron after the value
([25-notification-settings](screenshots/dark/25-notification-settings-banner-popup-values.png)). No validation
error was captured.

## Empty, loading and error states

Not captured. Search matches loosely, so even nonsense text returned events; the chat list loaded before the
capture ran; cutting the network ends the mirroring session. The closest is the Push Notifications Disabled banner,
a card with a title, an explanation and a link to the system settings
([25](screenshots/dark/25-notification-settings-banner-popup-values.png)).

## Destructive actions

Destructive choices are red: Report Event inside the event's More menu, Unfollow as the one item in the Following
menu, and Delete Account as a red row on its own card under a footnote
([08](screenshots/dark/08-event-more-menu-destructive-item.png), [22](screenshots/dark/22-following-menu-destructive-unfollow.png),
[26](screenshots/dark/26-account-settings-destructive-row.png)). None was tapped, so the confirmations they lead to
were not captured.

## Feedback

Unread counts on the Chat tab, red unread dots in chat rows, the bell's red dot on Home, Invited badges, status
pills on events, the send button turning blue once there is text
([30](screenshots/dark/30-chat-composer-typed-send-enabled.png)) and the Create Event check turning to the ink. No
toast was seen.

## Search and filtering

Search opens with a glass field beside the back button, two glass filter chips (Near you, Any Date) and a Recently
viewed list with a clear button ([12](screenshots/dark/12-search-focused-filter-chips-recent.png)). Near you opens a
pop-up menu ([15](screenshots/dark/15-location-filter-popup-menu.png)); Any Date opens the Date Range sheet with a
month calendar and a Confirm button ([14](screenshots/dark/14-date-range-sheet-calendar-confirm.png)). Your Events
filters with a segmented control (Upcoming, Past) and a pull-down menu of RSVP states with icons
([31](screenshots/dark/31-your-events-segmented-upcoming-soldout-badge.png),
[32](screenshots/dark/32-your-events-segmented-past.png), [33](screenshots/dark/33-your-events-filter-menu-icons.png)).
Picked for You switches between Nearby and Around the World with a pop-up
([04](screenshots/dark/04-nearby-popup-menu.png)). Discover browses by outlined category chips and city cards
([09](screenshots/dark/09-discover-popular-category-chips.png)).

## Onboarding

Not captured: the account was already signed in.
