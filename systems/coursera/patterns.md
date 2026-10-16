# Coursera patterns

How Coursera's components combine to do the common jobs, one entry per pattern in [docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md#patterns). Each says when the pattern appears, which components it uses (linked to their entries in [components.md](components.md)), how it is laid out, and which screen shows it. Values come from [tokens.json](tokens.json) and the measurement files; where a pattern was not seen, the entry says so and why.

## App shell and navigation

**When.** Every page. The public catalogue and the learner pages use two different shells.

**Public shell.** A sticky 105px header (`core.zIndex.header`, 3000): a 40px dark audience strip (For Individuals, Businesses, Universities, Governments; z-index 999) over a 65px white bar with the wordmark, Explore (opens a full-width mega menu over a 20% black scrim), Degrees, a 480x44 pill search field and Log In / Join for Free at the right. Content sits in a 1440 container with 48px side padding on a 12-column grid with 32px gutters (`core.layout`). A course page adds a sticky 146px course nav once the hero scrolls away. A long footer closes every page.

**Learner shell.** A 64px top bar with the app switcher, an in-course search and icon buttons, over the grey ground (`role.background.page-learner`, `#f2f5fa`). The course home is three white 16-radius cards 16 apart with no border or shadow: a 300px sidebar (course material, grades, notes, forums, info), a 716px module column and a 360px rail (weekly target, timeline). Item pages swap the sidebar for a 360px outline panel. My Learning is a white page under a 65px header with a 1376 container split two thirds and one third.

**Phone (390).** The header drops to 65px with a hamburger, wordmark and search icon; course-like pages pin a 92px bar with Enroll for free to the bottom.

**Components.** [Global header](components.md#global-header), [Explore mega menu](components.md#explore-mega-menu), [Global search field](components.md#global-search-field), [Page shell: course home](components.md#page-shell-course-home), [Sticky nav](components.md#sticky-nav), [Footer](components.md#footer).

**Screens.** [home-light-default](screenshots/home-light-default.png), [course-light-sticky](screenshots/course-light-sticky.png), [learn-home-light-module-in-progress](screenshots/learn-home-light-module-in-progress.png), [my-learning-light-default](screenshots/my-learning-light-default.png), [mobile-course-light-default](screenshots/mobile-course-light-default.png).

## Forms and validation

**When.** The log-in dialog, the course review dialog, and the settings forms.

**Layout.** The label sits above the field at 16/20 600, with a red star for a required field. Fields are 48px tall, 8 radius, a 1px `role.border.strong` outline that turns `role.border.hover` over a blue.25 fill on hover, and the two-ring focus on keyboard focus. The submit button is full width and large (48px) in a dialog.

**When errors appear.** Only on submit: leaving the email field with "not-an-email" in it showed nothing. After Continue the dialog grows an [error notification](components.md#error-notification) between its intro and the field: `role.status.danger-fill`, 8 radius, no border, an error icon and one line ("Invalid email. Please enter email as name@email.com"). The field itself is not outlined in red and keeps `aria-invalid="false"`.

**Preventing instead of reporting.** The review dialog keeps Submit disabled until a star is chosen, and the AI coach keeps its send button disabled while the field is empty ([Chat send button](components.md#chat-send-button)), so neither can produce an error.

**Recovery.** The typed value stays in the field and focus stays in the dialog; correct it and submit again.

**Screens.** [login-light-error](screenshots/login-light-error.png); crops [text-field-error-dialog](components/crops/text-field-error-dialog.png), [rate-dialog-opened](components/crops/signed-in/rate-dialog-opened.png). The error was reached with every network request aborted, so the address was never sent.

## Empty, loading and error states

**Empty.** A search with no match ("zqxjvkwpq") does not show an empty state: the page keeps the "Results for" heading and fills the grid with fallback results ([search-light-no-match](screenshots/search-light-no-match.png)). No empty list was seen on the learner pages captured; the account has courses in progress. Not captured: an empty My Learning or an empty grades table.

**Loading.** The CDS loader (`cds-Loader`) spins a ring in 500ms (`core.duration.loader`); under reduced motion it stops spinning and pulses over 1.5s (`core.duration.loader-pulse`). The one loading screen seen was a modal on the course home ("Extending and personalizing your target dates. Your page will refresh shortly.") with the Coursera C, raised by the site when an overdue course opened; it closed before it could be copied, so only its wording is recorded. Not captured: skeletons for search results (a filter change reloads the page with results already rendered).

**Error.** Unknown URLs get a 404 page that loads without CDS: a logo bar, a large abstract illustration on `#f5f5f5`, one sentence with links back to the catalogue and search, and three helpful links ([404 page](components.md#404-page), [notfound-light-default](screenshots/notfound-light-default.png)). Field errors are covered under forms. Not captured: a failed request inside a page.

## Destructive confirmation

**What was seen.** The one destructive action on the pages captured is Delete account on Account settings, and it is an ordinary 48px secondary button, with no red danger style ([Delete account button](components.md#delete-account-button)). A plain paragraph above it says what deletion removes and that it cannot be undone, and a [warning notification](components.md#warning-notification) below it says to cancel subscriptions first. The My Learning course menu offers only Rate and Share, so there is no unenroll or remove confirmation there.

**Not captured.** The confirmation dialog itself: opening it means pressing Delete account, which this capture does not do.

## Feedback after an action

**Inline, not toasts.** No toast appeared anywhere. Copying a share link swaps the COPY button's label to "COPIED!" in place ([Share dialog](components.md#share-dialog)). Finishing an item turns its status icon into a `role.status.success-text` check and puts a "Completed" label beside Go to next item ([Reading next button (large)](components.md#reading-next-button-large)); the course timeline shows "Right on schedule!" on `role.status.success-fill`. A submitted assignment shows a result banner at the top of its page ([Assignment result banner](components.md#assignment-result-banner)).

**Screens.** [learn-reading-light-default](screenshots/learn-reading-light-default.png), [learn-assignment-light-submitted](screenshots/learn-assignment-light-submitted.png), [learn-home-light-module-in-progress](screenshots/learn-home-light-module-in-progress.png).

## Search and filtering

**When.** The header search on every public page, and the search results page.

**Layout.** The header field is a 480x44 pill with a round 36px primary submit inside its right end; typing opens a suggestion list on `elevation.level2`. The results page puts suggestion chips ("More to explore") above the heading, then a sticky bar of filter pills (Topic, Duration, Learning Product, Language, Level, AI topic pills) and a Filter & Sort button. A pill opens a 384px popover of checkboxes with counts and a View button; Filter & Sort opens a side sheet with accordions and the "Sort by" radio group (Best Match, Newest). Applied filters show as a count on Filter & Sort and a selected pill. Results are a 4-column card grid at 1440 (3 at 1024, 2 at 768, 1 at 390).

**Components.** [Global search field](components.md#global-search-field), [Search autocomplete](components.md#search-autocomplete), [Filter dropdown](components.md#filter-dropdown), [Filter popover](components.md#filter-popover), [Filter and sort side sheet](components.md#filter-and-sort-side-sheet), [Product card](components.md#product-card).

**Screens.** [search-light-default](screenshots/search-light-default.png), [search-light-filter-dropdown](screenshots/search-light-filter-dropdown.png), [search-light-chip-applied](screenshots/search-light-chip-applied.png), [search-light-filtered](screenshots/search-light-filtered.png).

## Data display

**Lists of courses.** Catalogue cards in a grid (above) or in scrolling rows of compact cards on Explore and the home page, with Next and Previous arrows. My Learning lists a programme's courses as rows inside one card, each with a meta line ("Course 2 of 9 · Not started") and an overflow menu; the current course adds a progress bar and a next-item card with Resume.

**Lists of items.** The course home lists a module's items as 60px rows 2px apart: a 20px status icon, a 16/24 title and a 14/20 grey meta line ("Video • 5 min"); the current item is tinted (`role.background.selected`) and carries Resume.

**Tables.** Grades is the one table: a rounded bordered `role=table` with a grey header row and one 68px row per graded item, in the columns Item, Status, Due, Weight and Grade ([Grades table](components.md#grades-table)).

**Not captured.** Sorting and paging. Grades has no sort control, and the first search results page (13 entries) showed no pager or load-more control after scrolling to its end, so how further results arrive was not seen.

**Screens.** [learn-grades-light-default](screenshots/learn-grades-light-default.png), [learn-home-light-module-not-started](screenshots/learn-home-light-module-not-started.png), [my-learning-light-default](screenshots/my-learning-light-default.png), [explore-light-default](screenshots/explore-light-default.png).

## Onboarding and first run

**Not captured.** The account is past onboarding, and creating an account or a second one to see the first run is out of bounds for a capture. What remains of it is the My Learning greeting with the learner's career goal and an Edit goal link, and the weekly learning target card on the course home rail.
