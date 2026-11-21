# NotebookLM patterns

How NotebookLM's components combine for its recurring jobs, written from the 2026-10-17 capture of the signed-in web app (dark and light, 1440 and 390). Each entry says when the product uses the pattern, which components and tokens it is made of, how it is laid out, and which screenshot shows it. Token names are from [tokens.json](tokens.json); component entries are in [components.md](components.md). Where the product does something only once, the entry says so rather than generalising.

## App shell and navigation

**When.** Every page. Two shells: the home page (a notebook gallery) and the notebook workspace.

**Components.** Page header ([header](components.md#header)), header tabs ([tab](components.md#tab)), search pill ([search-pill](components.md#search-pill)), segmented control ([segmented](components.md#segmented)), icon buttons, the PRO badge and the account avatar; in a notebook, the Sources and Studio panels ([panel-sources](components.md#panel-sources), [panel-studio](components.md#panel-studio)) and the Chat column ([panel-chat](components.md#panel-chat)).

**Layout.** The header is 64px (`size.header-height`) on `bg.page` with no fill or border of its own: logo and title left; tabs (All, My notebooks, Discover, Collections) after the logo on home; search, view toggle, settings, PRO and the Google bar right. The selected tab is a tonal pill (`surface.selected`), the rest are text pills; nothing uses the accent. In a notebook, Sources (354px) and Studio sit in rounded panels (`surface.panel`, `radius.panel` 32px) with a 16px gap (`layout.panel-gutter`), and Chat sits directly on the page between them. At 390 (below `breakpoint.mobile-max`) the three panels collapse into a tab bar (Sources, Chat, Studio, [mobile-tab](components.md#mobile-tab)) under the header, and the header's text buttons become icon buttons.

**Example.** [home-dark](screenshots/home-dark.png), [notebook-dark](screenshots/notebook-dark.png), [notebook-light](screenshots/notebook-light.png), [mobile-notebook-dark-chat](screenshots/mobile-notebook-dark-chat.png), [mobile-home-dark](screenshots/mobile-home-dark.png).

## Forms and validation

**When.** Dialogs that take input: adding website URLs, the custom chat prompt, sharing.

**Components.** Outlined text area and text field ([text-area-outlined](components.md#text-area-outlined), [text-field](components.md#text-field), [text-area-custom](components.md#text-area-custom)), the field error message ([error-text](components.md#error-text)), the dialog confirm button ([button-dialog-primary](components.md#button-dialog-primary), [button-disabled](components.md#button-disabled)).

**Layout.** Fields are Material outlined fields: a 1px outline in `border.subtle` at rest, `border.field` on hover, and the same colour at 2px (`borderWidth.field-focus`) on focus, with no separate focus ring. Help text sits under the field as a bulleted list. The confirm button sits bottom right and stays disabled (`state.disabled-container`, `text.disabled-button`) until the input is valid, so the product prevents a bad submit instead of rejecting one.

**When the error appears.** On blur, not on each keystroke: typing "not a link" changed nothing until focus left the field, then the outline turned `border.error` and "URL should start with http:// or https://" appeared under it in `text.error` at 13px. Insert stayed disabled throughout. Recovery is editing the field; nothing else on the dialog changes.

**Example.** [notebook-dark-website-dialog](screenshots/notebook-dark-website-dialog.png), [notebook-dark-website-dialog-typed](screenshots/notebook-dark-website-dialog-typed.png), [notebook-dark-website-dialog-error](screenshots/notebook-dark-website-dialog-error.png), [notebook-dark-configure-chat-custom](screenshots/notebook-dark-configure-chat-custom.png) (Save disabled while the custom prompt is empty).

## Empty, loading and error states

**When.** Lists that have nothing to show, are fetching, or failed.

**Components.** The empty panel ([empty-state](components.md#empty-state)) with its outlined action, the skeleton rows ([skeleton](components.md#skeleton)), the toast ([toast](components.md#toast)).

**Layout.**
- *Empty search*: a rounded panel (`surface.empty`, `radius.lg`, 1px `border.subtle`) the width of the results, with a 48px search glyph, "No notebooks found" in `typography.headline-small`, a one-line hint in `text.secondary`, and an outlined "Clear search" button. See [search-dark-empty](screenshots/search-dark-empty.png).
- *Empty collection list*: nothing but the page title and the "New collection" accent button; no illustration or message. See [home-dark-collections-empty](screenshots/home-dark-collections-empty.png).
- *Loading*: five full-width skeleton rows (56px, `radius.xs`) with a shimmer (`duration.shimmer`), in place of the result table. See [search-dark-loading](screenshots/search-dark-loading.png).
- *Error*: a failed action reports in a toast ("Failed to copy.") rather than inline. See [notebook-dark-toast](screenshots/notebook-dark-toast.png). No page-level error state was reached.

## Destructive confirmation

**When.** Deleting a notebook (from its card menu).

**Components.** Menu ([menu](components.md#menu)), small dialog ([dialog](components.md#dialog)), scrim ([scrim](components.md#scrim)), Cancel text button and Delete tonal button ([button-confirm-delete](components.md#button-confirm-delete)).

**Layout.** A 456px dialog (`layout.dialog-width-small`, `radius.dialog` 28px, `surface.raised`, no shadow) over a 32% black scrim (`bg.scrim`). Title "Delete this notebook?" in `typography.headline-small`, one sentence saying the content will be permanently deleted, then Cancel (text) and Delete (tonal grey pill, 48px, `size.control-medium`) bottom right. Delete is not red and takes focus when the dialog opens. The menu's Delete item has the same grey icon as its neighbours.

**Example.** [home-dark-card-menu](screenshots/home-dark-card-menu.png), [home-dark-delete-confirm](screenshots/home-dark-delete-confirm.png), [home-light-delete-confirm](screenshots/home-light-delete-confirm.png).

## Feedback after an action

**When.** Copying an answer, and other one-shot actions.

**Components.** Toast ([toast](components.md#toast)).

**Layout.** A 344 x 48 snackbar centred at the bottom of the viewport, inverted against the theme (`surface.toast`: white in dark, black in light), `radius.toast` 16px, `shadow.toast`, one line of `typography.body-medium` and no action button. It overlays the composer. Success and failure use the same toast; only the wording differs.

**Example.** [notebook-dark-toast](screenshots/notebook-dark-toast.png), [notebook-light-toast](screenshots/notebook-light-toast.png).

## Search and filtering

**When.** Finding a notebook; picking which sources the chat uses.

**Components.** Search pill and expanded search field ([search-pill](components.md#search-pill), [search-field](components.md#search-field)), header tabs as filters, the source checkboxes ([checkbox](components.md#checkbox)), the Web and Fast Research menu triggers ([menu-trigger](components.md#menu-trigger)).

**Layout.** The 256px outlined search pill in the header expands in place into a 650px field when activated, replacing the tabs; typing opens a suggestion panel under it ("All search results for ..."), and Enter opens a results page titled "Results for ..." with a back arrow. Home filtering is the header tabs (All, My notebooks, ...), one selected at a time. In a notebook, every source row ends in a checkbox and the panel has a Select all checkbox; the chat composer shows how many sources are selected.

**Example.** [home-dark-search-typed](screenshots/home-dark-search-typed.png), [search-dark-empty](screenshots/search-dark-empty.png), [notebook-dark](screenshots/notebook-dark.png).

## Data display

**When.** The notebook gallery, the source list, Studio outputs.

**Components.** Notebook card ([card](components.md#card)), notebook table ([table-row](components.md#table-row), [table-header](components.md#table-header)), source rows ([list-row](components.md#list-row)), Studio output rows ([list-row-output](components.md#list-row-output)), the 390 notebook rows ([mobile-list-row](components.md#mobile-list-row)).

**Layout.** Home shows notebooks as a grid of 272 x 185 cards (`surface.card`, `radius.card` 40px, 32px padding, no border or shadow) in `layout.grid-notebooks` columns: five at 1440, three at 1024, two at 800. The segmented control switches to a table (Title, Sources, Created, Visibility, Role, Actions; 52px rows, 1px `border.divider` between rows, no zebra and no row fill). At 390 the grid becomes a list automatically. Sources are 36px rows with a type icon (`icon.source-pdf`), the title, a menu button and a checkbox; Studio outputs are two-line rows with a coloured type icon (`studio.*`), meta line in `text.secondary`, and play and menu actions.

**Example.** [home-dark](screenshots/home-dark.png), [home-dark-list](screenshots/home-dark-list.png), [home-light-list](screenshots/home-light-list.png), [notebook-dark](screenshots/notebook-dark.png), [mobile-home-dark](screenshots/mobile-home-dark.png).

## Onboarding and announcements

**When.** On the first visit after a product change; the account is past first-run onboarding, so that flow was not seen.

**Components.** Large dialog ([dialog-announcement](components.md#dialog-announcement)), Studio banner ([banner](components.md#banner)), the "New!" badge ([badge-new](components.md#badge-new)).

**Layout.** A 1000px dialog (`radius.dialog`) with the product mark, a one-line headline, a divider and three illustrated columns (picture, title in `typography.title-medium`, two lines of `text.secondary`), closed only by the X. Smaller news stays in place: a dismissible banner at the top of Studio ("New: You can now create Interactive Reports!" with a Try it tonal button) and a "New!" badge on the Reports tile.

**Example.** [notebook-dark-announcement](screenshots/notebook-dark-announcement.png), [notebook-light-announcement](screenshots/notebook-light-announcement.png), [notebook-dark](screenshots/notebook-dark.png) (banner and badge).

## Public marketing page

**When.** Signed out. `https://notebooklm.google.com` and `https://notebook.google.com/` both land on `/trynow`.

**Layout.** A wordmark header, one headline, a feature illustration, and a two-link footer. At 1440 the header shows Sign in. At 390 that control leaves the header and Get the app appears above Sign in to Gemini Notebook. Feature labels (Slide decks, Mind Maps, Audio Overviews, Video Overviews) are captions on the illustration, not links.

**Example.** [home-public-light-desktop](screenshots/home-public-light-desktop.png), [home-public-light-phone](screenshots/home-public-light-phone.png).

## Empty login wall

**When.** Sign in, from the header or the hero, before any account is chosen.

**Layout.** Google Accounts identifier step: Email or phone, Forgot email?, Create account, Next. The field was empty. Next was not clicked. Create account was not opened.

**Example.** [login-empty-light-desktop](screenshots/login-empty-light-desktop.png), [login-empty-light-phone](screenshots/login-empty-light-phone.png).
