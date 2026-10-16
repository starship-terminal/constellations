# Polaris patterns

This file summarises the written patterns in the archived polaris.shopify.com content at commit 3f7954ae42fabf26d63cee68c23ceebfd7ef0972 of Shopify/polaris-react-archive. It covers the `patterns/` and `patterns-legacy/` folders, the component guideline pages that carry pattern-level rules (under `components/`), the `content/error-messages.mdx` page, and a few lines from `foundations/` and `design/`. Everything is paraphrased in plain English. Where the docs say nothing about a point, the text says "Not stated in the archive docs" instead of filling the gap. A few components used by these patterns (Frame, TopBar, Navigation, ContextualSaveBar, Toast, Modal, Loading, PageActions) are marked "no longer supported" in `components/deprecated/`, with an App Bridge API named as the replacement. The same pages also exist under `components/internal-only/`, flagged as for Shopify staff only. The pattern guidance below still reflects what those pages say. All source paths are relative to the repo root.

---

## 1. App shell (Frame, TopBar, Navigation, Page header and actions, Layout)

**Example screen.** [16-app-shell](screenshots/16-app-shell.png) (desktop) and [phone/14-app-shell](screenshots/phone/14-app-shell.png) (390 px): Frame, TopBar, Navigation and Page in the live gallery. The gallery renders the published components; the screens are not Shopify admin captures.

**When to use.** Use it for every full page of an app inside the Shopify admin. It gives each page the same outer structure: a frame with top bar and side navigation, a page header with title and actions, and a body laid out in columns.

**Components.** `Frame`, `TopBar` (with its menu, user menu and search field parts), `Navigation` (with navigation sections, items, secondary actions, rollup), `Page`, `Layout`, `PageActions` (deprecated), `Card`, `AppProvider` (used to set the top bar colour).

**Layout.**
- `Frame` has no visible UI. It wraps the app and hosts the navigation, top bar, toast, contextual save bar and loading components.
- The top bar sits across the top. The navigation sits in the sidebar and moves into the top bar on small screens.
- `Page` is the outer wrapper below that: title, breadcrumbs, primary action, secondary actions, then content.
- Inside the page, `Layout` arranges sections as one column, two columns (primary about two thirds, secondary about one third), equal columns, or annotated (settings pages only).
- The docs list optional bottom-of-page actions (`PageActions`), but that component is deprecated in favour of the App Bridge Save Bar API.

**Rules.**
- Frame: put the top bar, navigation, contextual save bar, toast and loading inside it. Wrap the app in it so toasts are read out by screen readers while a modal is open.
- Top bar: do use it for search, a user menu and the brand logo. Don't use it as the global navigation. Use an SVG logo and set the background through `AppProvider`. Keep logo and menu text at a passing WCAG 2.0 contrast against that background. Keep the navigation toggle visible for small screens. Third-party apps supply their own logo.
- Top bar search placeholder: the word "Search", with no ellipsis.
- Navigation: do make each item go to a URL or trigger an action. Do group items into sections by category, with a section title. Do use a major icon for item actions and a minor icon for secondary actions. Don't put extra components such as a New badge inside navigation items. Use sentence case for items, short labels, and all caps for section titles.
- Page header: do always give a title. Do add breadcrumbs when the page has a parent, and make each breadcrumb read like the title of the page it links to. Organise the page around one primary activity and put it in the header as the primary button when it is a single action. Put the other page-level actions in the header as secondary actions. On a page for one object, add previous and next links to move between objects of the same type.
- Page title: as few words as possible, never truncated. For a list page, use the plural object name (for example "Orders").
- Action labels: lead with a verb and use verb plus noun. A bare verb is fine for a secondary action when the noun is the page's own object (for example "Import" on an orders list). Use the full verb plus noun when the verb is ambiguous, as with "Cancel". Skip words like "a" and "the".
- Page width: default width for most pages. Full width only for layouts that need it, such as wide tables. Narrow width for a page built around one unified task read top to bottom.
- Page extras: action groups for many related actions (they collapse into one action on small screens). Title metadata is for brief, non-interactive status of the whole page. A destructive secondary action has its own style. Use a tooltip action to explain why an action is disabled. Show the app icon only on pages that belong to an app. External links open in a new tab.
- Layout: use white-background sections for primary content and grey for less important secondary content. Centre the cards when there is no secondary column, so content does not stretch too wide. Group similar concepts and actions in one card. Separate cards with a full-width divider. Use equal columns only when sections have equal importance.
- Annotated layout: for settings pages, used on its own. Each section gets a title and, when the purpose is not obvious, a description of one to three sentences that does not repeat the title and may link to Help Center content.
- Bottom-of-page actions (deprecated): one primary action on the right, matching the header's primary action, and at most two secondary actions.

**Not stated in the archive docs.** Exact frame dimensions or spacing. How many items a navigation should have. Breakpoint values for when navigation moves into the top bar.

**Source:**
- polaris.shopify.com/content/components/deprecated/frame.mdx
- polaris.shopify.com/content/components/internal-only/frame.mdx
- polaris.shopify.com/content/components/internal-only/top-bar.mdx
- polaris.shopify.com/content/components/deprecated/top-bar.mdx
- polaris.shopify.com/content/components/internal-only/navigation.mdx
- polaris.shopify.com/content/components/deprecated/navigation.mdx
- polaris.shopify.com/content/components/layout-and-structure/page.mdx
- polaris.shopify.com/content/components/layout-and-structure/layout.mdx
- polaris.shopify.com/content/components/deprecated/page-actions.mdx

---

## 2. Forms and validation (FormLayout, field labels, help text, InlineError, when errors appear, ContextualSaveBar for unsaved changes)

**Example screen.** [19-states](screenshots/19-states.png), "Form with validation errors": a critical summary banner, two field errors and a separate InlineError. The gallery renders the published components; the screens are not Shopify admin captures.

**When to use.** Use it whenever a merchant enters or edits data: creating a resource, editing a resource, or changing settings.

**Components.** `Form`, `FormLayout` (default stack, field group, condensed field group), `TextField`, `InlineError`, `Banner` (critical, as a form summary), `ContextualSaveBar`, `Card`, `Page`.

**Layout.**
- `Form` wraps all inputs. `FormLayout` sits inside it and stacks fields vertically, which is the default.
- Fields are placed in a `Card`, inside a card section (see the Card layout section below). Use `FormLayout` even for a single field.
- A field group puts several fields on one row. A condensed group narrows very short inputs so more fit in a row. Groups wrap on small screens.
- Group related fields under section titles. Keep the order logical and predictable (first name before last name).
- For long or complex forms, a critical `Banner` summarising the problems goes at the top of the form.
- The `ContextualSaveBar` appears across the page once the form has unsaved changes.

**Rules.**
- Ask only for what is needed. Mark non-required fields as "Optional".
- Field labels: short (one to three words), sentence case, placed above or beside the field. Say what is expected as a noun, not a question or a sentence ("Email address", not a prompt). A standalone field with no form around it (such as a comment box) may use a call to action as its label.
- Labels are not help text. Don't use them to give instructions. Hide a label only when the purpose is clear from context, and keep it available to screen readers.
- Placeholder text: avoid it in general because of contrast, inconsistent behaviour and the text vanishing when typing starts. The exceptions are search, filter and email fields, where the placeholder should float above the cursor when the field is focused. Never put required information in a placeholder. Floating placeholders on a minimalist page (such as a login page) are allowed but should be used sparingly.
- Help text: short, and nothing essential should depend on it, since people skip it. Use it when the label alone does not explain the purpose, to give guidance, or to show a format. Don't repeat the label. For input that must follow a format (tags, dates), give an example introduced with the word "Example" and a colon. If space is tight, keep only the example. For free text, give no example. For long text or notes, say who can see the text.
- Prefix and suffix on a `TextField` suit currency symbols and units. Connected fields suit a value plus its unit.
- When errors appear: validate a field once the merchant has finished with it, not earlier. After a field already has an error, re-check as they type so the error disappears the moment it is fixed. An inline error shows as soon as input is not valid and goes away as soon as it is valid.
- Inline error wording: one sentence, in the passive voice so the merchant is not blamed, saying what is wrong and, if useful, the next step or a one-click fix. Sentence case. Place it directly by the field it describes. Use a separate `InlineError` when an error depends on a group of fields or needs a non-standard position. Tie it to the field by its id so assistive tech reads it.
- General error text: be specific, avoid the word "invalid" and other jargon, don't over-apologise, and say "we" only when Shopify caused the problem. Place the error near what needs fixing. Red marks errors that need immediate attention, yellow marks warnings or errors that are part of daily work.
- Submit errors: for long forms, summarise problems in a critical banner at the top, then move focus to that banner. Still show inline errors on each field. Move focus to the error on a failed submit, and don't move focus for background changes.
- Form submission: the form has one submit button and it is at the end. Pressing Enter in a text field submits it by default.
- Browser help: add an autocomplete attribute to common input types, and set `inputMode` so mobile shows the right keyboard. Avoid auto-focusing a field unless it will not skip more important content.
- Unsaved changes with `ContextualSaveBar`: show it whenever the page's form has unsaved changes, including while creating a new object. It saves or discards everything on the page, so avoid several independently editable forms on one page. If a section must be edited on its own, use an Edit button that opens a modal for that section. Message text is a short adjective plus noun, not a sentence: "Unsaved changes" when editing, "Unsaved" plus the resource name when creating. Action labels are verbs without nouns: "Save" and "Discard". This component is deprecated in favour of the App Bridge Contextual Save Bar API.

**Not stated in the archive docs.** How to mark required fields (only the "Optional" label is described). Whether validation runs again on submit. Any limit on form length. How to handle server-side validation timing.

**Source:**
- polaris.shopify.com/content/components/layout-and-structure/form-layout.mdx
- polaris.shopify.com/content/components/selection-and-input/form.mdx
- polaris.shopify.com/content/components/selection-and-input/text-field.mdx
- polaris.shopify.com/content/components/selection-and-input/inline-error.mdx
- polaris.shopify.com/content/patterns-legacy/text-fields.mdx
- polaris.shopify.com/content/content/error-messages.mdx
- polaris.shopify.com/content/components/feedback-indicators/banner.mdx
- polaris.shopify.com/content/components/deprecated/contextual-save-bar.mdx
- polaris.shopify.com/content/components/internal-only/contextual-save-bar.mdx
- polaris.shopify.com/content/foundations/accessibility.mdx
- polaris.shopify.com/content/patterns/card-layout/index.mdx

---

## 3. Empty, loading and error states (EmptyState, EmptySearchResult, SkeletonPage/SkeletonBodyText, Spinner, Loading bar, Banner for errors)

**Example screen.** [19-states](screenshots/19-states.png): SkeletonPage and EmptySearchResult; [11-data](screenshots/11-data.png): an empty state with one primary action; [18-app-shell-error-toast](screenshots/18-app-shell-error-toast.png): an error toast. The gallery renders the published components; the screens are not Shopify admin captures.

**When to use.** Use it when a page has nothing to show yet, when content is on its way, or when something has gone wrong.

**Components.** `EmptyState`, `SkeletonPage`, `SkeletonBodyText`, `SkeletonDisplayText`, `SkeletonTabs`, `SkeletonThumbnail`, `Spinner`, `ProgressBar`, `Loading` (page-level bar inside `Frame`, deprecated), `Banner`, `InlineError`.

### Empty states

**Layout.** `EmptyState` fills a whole page (or full content area) with an illustration, a title, a subtitle, one primary button and an optional secondary action. A variant adds subdued footer content for non-critical context or lower-key actions. A full-width layout also exists. Inside a card, modal or navigation, leave extra space under the image.

**Rules.**
- Use it only when a full page is empty. Don't use it for a small area or single element.
- Explain the benefit of the feature, and the steps to start using it. Keep it focused on a few key points, in simple language.
- Be encouraging. Never make merchants feel guilty or unsuccessful for not having used a feature yet.
- Title: action-oriented, so it pushes the merchant toward the first step. Subtitle: reads like conversation and uses articles.
- Exactly one primary button, labelled verb plus noun. Secondary actions, such as "Learn more" or "Close", follow the same wording rules.
- Illustrations are decorative and carry an empty alt attribute. The illustration guidance says an empty state illustration shows the first time a merchant opens a new area.
- A list or table with an empty state should switch smoothly from loading to zero, one or many items.

**EmptySearchResult.** Not stated in the archive docs by that name. The only related text is the resource list example "With a custom empty search result state", which says to show a custom empty state when filters or search return nothing. No wording or layout rules are given.

### Loading states

**Layout.** Page content that loads all at once shows a `SkeletonPage` with `SkeletonBodyText`, `SkeletonDisplayText` and similar pieces shaped like the final layout. Content that loads later inside a card uses skeleton pieces on their own.

**Rules.**
- Make the skeleton match the real layout and line counts. A mismatched layout confuses merchants.
- Show real content for anything static, such as a page title that never changes ("Products"). Use skeletons only for dynamic content. Never use placeholder text for content that will change, since it makes the load feel jumpy. Secondary header actions are always skeletons.
- `Spinner`: for an action that is being processed. Don't use it for a whole page load. Use it for content skeletons cannot represent, like a chart. White spinners are for small ones on buttons only. Always give it an accessibility label that states the state in few words ("Loading", "Submitting", "Processing").
- `ProgressBar`: shows how much of a task is done. Don't use it for a whole page load (use `SkeletonPage`). For short waits, use `Spinner`.
- `Loading` bar: signals a page load, an upload, or a page mutation like saving. Pair it with an aria-busy element. Deprecated in favour of the App Bridge Loading API.
- General loading principles from the legacy pattern: make it fast (cache, prefetch when intent shows, load the visible part first, limit page content, paginate); use the time well (move to the next view at once, show real content and active controls, use recognisable placeholders); stay focused (clear feedback within 100 milliseconds, real progress at about one second intervals, a stable layout, little visual noise).
- Avoid spinners as placeholders and avoid empty views with only a spinner. Use spinners only when they help.
- If a load will run past about ten seconds, set expectations and let the merchant decide whether to wait.

### Error states

**Layout.** A `Banner` goes at the top of the page under the page header, or inside the section it concerns (below that section's heading). For a single field, use `InlineError` directly below the field.

**Rules.**
- Critical banner: for problems that must be fixed at once to continue. Warning banner: for things that need attention. Both can stress merchants, so use them with care.
- Banner text: focus on one theme. Keep the body to one or two sentences that do not repeat the title and say how to fix the problem. At most one primary action.
- Critical and warning banners are announced as alerts. Don't use them for information that is not urgent. Don't move focus to a banner that appears on page load or outside the merchant's current task.
- Error message anatomy: an optional heading naming the effect of the error, a body that explains the fix and may link to help, and an optional call to action that offers a one-step fix or goes to the place to fix it.
- With several errors, list the changes needed ("To save this product, make 2 changes") instead of a count of errors.
- When there is no solution, say plainly that something went wrong and suggest a refresh.
- Full-page failure: the content guide gives sample wording for "admin unavailable" (state the page is not available, suggest checking the address or trying again, offer a Retry button). Nothing more on error pages.

**Not stated in the archive docs.** Specific rules for 404 and 500 page layouts beyond that copy sample. Retry timing. Where to place an `EmptyState` relative to filters. How long a skeleton may show before moving to an error.

**Source:**
- polaris.shopify.com/content/components/layout-and-structure/empty-state.mdx
- polaris.shopify.com/content/components/lists/resource-list.mdx
- polaris.shopify.com/content/components/tables/index-table.mdx
- polaris.shopify.com/content/design/illustrations.mdx
- polaris.shopify.com/content/components/feedback-indicators/skeleton-page.mdx
- polaris.shopify.com/content/components/feedback-indicators/skeleton-body-text.mdx
- polaris.shopify.com/content/components/feedback-indicators/skeleton-display-text.mdx
- polaris.shopify.com/content/components/feedback-indicators/skeleton-tabs.mdx
- polaris.shopify.com/content/components/feedback-indicators/skeleton-thumbnail.mdx
- polaris.shopify.com/content/components/feedback-indicators/spinner.mdx
- polaris.shopify.com/content/components/feedback-indicators/progress-bar.mdx
- polaris.shopify.com/content/components/deprecated/loading.mdx
- polaris.shopify.com/content/patterns-legacy/loading.mdx
- polaris.shopify.com/content/components/feedback-indicators/banner.mdx
- polaris.shopify.com/content/content/error-messages.mdx
- polaris.shopify.com/content/foundations/accessibility.mdx

---

## 4. Destructive confirmation (Modal with critical primary action, wording)

**Example screen.** [20-delete-confirm](screenshots/20-delete-confirm.png): a modal whose primary action is critical red, with Cancel beside it. The gallery renders the published components; the screens are not Shopify admin captures.

**When to use.** Use it when an action cannot be undone, such as deleting a record, or when a merchant would lose work (for example discarding unsaved changes).

**Components.** `Modal` (with a destructive primary action), `Button` (critical tone), `ActionList` (destructive item), `Page` (destructive secondary action).

**Layout.**
- The trigger lives on the page. A delete action is a destructive secondary action in the page header, or the last item in an action list, shown with the delete icon.
- Activating it opens a `Modal` with a short title, a short body, a primary destructive button and a plain cancel path.
- Keep to two buttons at most at the bottom (primary and secondary). Pass the opening button as the modal's activator so focus goes back to it on close.

**Rules.**
- Modals interrupt, so use them thoughtfully and sparingly. They are for confirmations and conditional changes, not for complex forms or long information.
- The modal requires a choice. It closes with the X, the Cancel button, the Escape key, or a click outside.
- Title: verb plus noun, as a question or a statement. Good: a short question such as "Delete customer?" or "Discard unsaved changes?". Don't write "Are you sure...?" or a bare "Discard?".
- Body: put the most critical fact first. A short line saying the action can't be undone is the model. Start with imperative verbs, don't use permissive "you can" wording, and use "need" rather than "must" when something is required.
- Buttons: clear, action-led labels in verb plus noun form (Save, Close, Cancel, OK are fine bare). Say what will happen, never mislabel.
- A tertiary action in a modal is only for something that needs the modal's content. It must never dismiss the modal and must never be destructive.
- Delete versus remove: delete erases the object from the system, so use the delete icon and put it at the bottom of an action list. Remove only takes an item out of a context (a product leaves a collection) and uses the x icon. Don't mix the two icons.
- Don't use critical-styled buttons often in one view, and don't put a primary critical button beside other tones and variants that clash with it.
- Accessibility: the modal uses the dialog role, labels itself from its title, moves focus in on open, keeps focus inside while open, and returns focus on close. A title is required, though it may be visually hidden.
- Modal is deprecated in favour of the App Bridge Modal API.
- Related: a toast with an "Undo" action is described elsewhere as a way to let merchants reverse a deletion (see section 5).

**Not stated in the archive docs.** Whether to ask for typed confirmation. Which actions deserve a modal versus an undo. The exact label for the cancel button of a destructive modal beyond "Cancel" being a valid dismiss control. Any rule on button order.

**Source:**
- polaris.shopify.com/content/components/deprecated/modal.mdx
- polaris.shopify.com/content/components/internal-only/modal.mdx
- polaris.shopify.com/content/patterns/common-actions/variants/overview.mdx
- polaris.shopify.com/content/components/layout-and-structure/page.mdx
- polaris.shopify.com/content/patterns/resource-details-layout/variants/default.mdx
- polaris.shopify.com/content/components/deprecated/toast.mdx

---

## 5. Feedback after an action (Toast vs Banner vs inline, durations)

**Example screen.** [17-app-shell-toast](screenshots/17-app-shell-toast.png) and [18-app-shell-error-toast](screenshots/18-app-shell-error-toast.png): toasts after Save and a failed Export; [08-feedback](screenshots/08-feedback.png): banners in each tone. The gallery renders the published components; the screens are not Shopify admin captures.

**When to use.** Use it to tell a merchant what happened after they did something: saved, copied, deleted, failed.

**Components.** `Toast` (non-blocking message at the bottom of the interface, inside `Frame`; deprecated in favour of the App Bridge Toast API), `Banner`, `InlineError`, inline icon changes (copy check mark), `Spinner`, `ProgressBar`.

**Layout.**
- Toast: appears at the bottom of the interface, disappears by itself, includes its own dismiss X.
- Banner: top of the page or section it concerns.
- Inline: next to the element that was acted on (a text field error, or a check icon replacing a copy icon).

**Which one to pick.**

| Situation | Use | Notes |
|---|---|---|
| Quick confirmation of success | Toast | Default choice for success |
| Success that arrives late, stays, or needs a next step | Banner (success tone) | Add next steps if relevant |
| Persistent condition or change | Banner | Dismissible unless critical or a required step |
| Error caused by merchant input | Inline error | Right under the field |
| Error needing action | Critical or warning Banner | See section 3 |
| Error not caused by the merchant (connection) | Toast, rarely | 3 words or fewer |
| Copy to clipboard | Check icon inline; toast if inside an action list | Copy action itself shows on hover for cursor users |
| Request received, work in progress | Spinner or ProgressBar | Show that the interface got the request |

**Rules.**
- Toast text: short and affirmative, noun plus verb, 3 words at most ("Product updated"). Not a full sentence, no "successfully", no explanation of limits.
- Toast duration: the default is 5000 milliseconds. A custom duration can be set. A toast with an action needs at least 10000 milliseconds so people have time to use it.
- Toast action: include only if the same action is reachable elsewhere on the page (Undo, Retry, Reload). Keep the label to one verb. Don't add an OK, Dismiss or Cancel action, since the X already dismisses it.
- Toast errors: still available but discouraged. Reserve for errors the merchant did not cause and that can be said in three words. For persistent errors, always prefer a banner.
- Toast access: it is announced assertively to screen readers, disappears automatically, and is hard for keyboard users and people with low vision or low dexterity to reach. Never use it for critical information that needs immediate action.
- Banners: dismissible by default. Only critical information or a required step stays pinned. Don't use a banner as the main way to reach a regular action.
- Unsuccessful completions: say what stopped the action and what the merchant can do about it, for example with a text field's validation error.
- Multiple toasts are allowed to report different actions.
- Copy: show the copy control on hover for cursor use, and confirm with a check icon after a click or tap.

**Not stated in the archive docs.** Toast screen position beyond "bottom of the interface". How many toasts may stack. Auto-dismiss time for banners (banners are dismissed by the merchant). Duration for inline copy confirmation.

**Source:**
- polaris.shopify.com/content/components/deprecated/toast.mdx
- polaris.shopify.com/content/components/internal-only/toast.mdx
- polaris.shopify.com/content/components/feedback-indicators/banner.mdx
- polaris.shopify.com/content/content/error-messages.mdx
- polaris.shopify.com/content/design/interaction-states.mdx
- polaris.shopify.com/content/patterns/common-actions/variants/overview.mdx
- polaris.shopify.com/content/components/selection-and-input/inline-error.mdx

---

## 6. Search and filtering (IndexFilters, Filters, saved views/tabs, query field)

**Example screen.** [16-app-shell](screenshots/16-app-shell.png): ResourceList with Filters, a query field, an applied "Status: Active" filter and Clear all. The gallery renders the published components; the screens are not Shopify admin captures.

**When to use.** Use it above a long list or table of resources, so merchants can narrow, search, sort, and save useful subsets as views.

**Components.** `IndexFilters`, `Filters`, `Tabs`, `ChoiceList` (as the filter input), `TextField` (query field), `Popover`, `IndexTable`, `ResourceList`, `Card`. `Legacy filters` is deprecated; `Filters` now works as a stand-alone piece, but mostly lives inside `IndexFilters`.

**Layout.**
- `IndexFilters` sits directly above an `IndexTable`, inside a card with no padding (the resource index layout shows it that way).
- It has four parts. Tabs at the top list the saved views. A search-and-filter button toggles from "View" mode to "Filter" mode and reveals the query field and filters. A sort button opens a popover with sort options and a direction choice. Filters are form inputs that include or exclude items. Action buttons give a primary Save (or "Save as" when the current view cannot be changed) and a secondary Cancel.
- The component supports configurations without filters, or without search and filters, keeping only views and sorting.

**Rules.**
- Saved views: each tab is a named subset that was filtered, sorted or searched. Merchants can switch views, edit a view's filters and search, and create, rename, duplicate or delete views.
- Tabs generally: they should hold the same kind of content (a list under different filters), only one is active at a time, merchants shouldn't need to hop between tabs for one task, and they are not primary navigation.
- Tab labels: short, usually one word, reading as if the page's noun follows the label. The orders page uses "All", "Open", "Unfulfilled", "Unpaid".
- Promote only the filters most people use, no more than two or three. Think about small screens for each filter's design and the total count. Put only filter-related content into the children slot.
- Query field label: say what is being filtered ("Filter orders"), not "Enter text here".
- Filter pills: use the filter's own value when its meaning is clear on its own ("Fulfilled"), and add a word when it would be ambiguous ("High risk", not just "High"). Group values from one category in one pill. When every value is selected, shorten the pill by cutting from the middle.
- Sorting: offer it on long lists, especially if different tasks want different orders. Sort options have a label and a direction.
- Accessibility: every control needs a label, state changes must be announced, and everything must work with a keyboard, including any custom content you add.
- Searchable pickers (legacy): show more tools as the option count grows. See "Pickers" in the extra patterns.

**Not stated in the archive docs.** Debounce timing for the query. How to word the empty results message after a search. Whether filter state belongs in the URL. A maximum number of saved views. Placeholder text for the query field beyond the label rule above.

**Source:**
- polaris.shopify.com/content/components/selection-and-input/index-filters.mdx
- polaris.shopify.com/content/components/selection-and-input/filters.mdx
- polaris.shopify.com/content/components/deprecated/legacy-filters.mdx
- polaris.shopify.com/content/components/navigation/tabs.mdx
- polaris.shopify.com/content/patterns/resource-index-layout/variants/default.mdx
- polaris.shopify.com/content/patterns-legacy/pickers.mdx

---

## 7. Data display (IndexTable vs ResourceList vs DataTable, bulk actions, sorting, pagination)

**Example screen.** [16-app-shell](screenshots/16-app-shell.png): ResourceList rows with selection and sort; [11-data](screenshots/11-data.png): a DataTable with totals; [09-navigation](screenshots/09-navigation.png): pagination. The gallery renders the published components; the screens are not Shopify admin captures.

**When to use.** Use it to show a collection of the same kind of thing.

| Need | Component | What the docs say it is for |
|---|---|---|
| Scan many objects with several columns, act on them, jump to a details page | `IndexTable` | At-a-glance view of objects of one type, with bulk actions, sorting, filtering |
| Find an object and open its details page, in a compact list | `ResourceList` (with `ResourceItem` or a custom item) | Actionable list of resources. It can look like a table but is not a data table |
| Compare and analyse structured data | `DataTable` | Static data across categories and measures. Not for an actionable list that links to details pages |

The docs give these descriptions but no formal "pick A when B" rule beyond them.

**Components.** `IndexTable` (with `IndexTable.Row` and `IndexTable.Cell`), `ResourceList`, `ResourceItem`, `DataTable`, `IndexFilters`, `Filters`, `Pagination`, `SkeletonPage`, `EmptyState`.

**Layout.**
- Title the list with the resource type. If the list shows only some items, say so ("Popular products this week").
- Above the rows: filters, sorting, bulk-action controls (see section 6). Below: the pagination.
- The components give you the controls but not the logic. You handle sort, filter and page-change events and pass new props back in.

**Rules.**
- Rows must do something when clicked: go to the details page or reveal more detail. An `IndexTable` row can hold a link marked as the primary link so a click navigates instead of selecting.
- Support sorting and filtering when the list can be long.
- Bulk actions: add them for tasks often applied to many items (such as tagging many products). Name them verb plus noun. The docs show promoted bulk actions, selection across pages, and selection with no bulk actions. Only hide bulk actions on narrow screens (below 490px, via the `condensed` option) when merchants do not depend on them, since hiding stops multi-select. Shift-click selects a range of rows.
- Pagination: the `Pagination` page says to use it for lists with more than 25 items. The `IndexTable` and `ResourceList` pages say to paginate past 50 items. These two numbers differ in the docs. Put web pagination at the bottom of the list, and disable the previous or next button at the first or last page. On iOS and Android use infinite scrolling, start loading about five items from the end, and show a spinner under the list.
- Loading: use `SkeletonPage` for the rest of the page on first load when the loading prop is on.
- Empty: use the `EmptyState` example for an index with no resources yet.
- Alignment: right-align number cells and titles in `IndexTable` and use the numeric text style. In `DataTable`, numbers are right-aligned, text is left-aligned, headers match their data, and nothing is centred.
- `DataTable` content: headers are informative, concise, sentence case, and carry the unit symbol so it is not repeated in cells. Keep decimals consistent. Include a totals row with no calculations inside it. Wrap long content rather than truncating it. Use only values that serve the purpose.
- Use real tables for tabular data, never for page layout.
- Subheaders in an `IndexTable` group rows so a whole group can be selected at once, and nested rows show hierarchy.

**Not stated in the archive docs.** A numeric limit on bulk actions. Row density rules. Which of `IndexTable` and `ResourceList` to prefer for a given page. Whether the 25 or the 50 threshold wins.

**Source:**
- polaris.shopify.com/content/components/tables/index-table.mdx
- polaris.shopify.com/content/components/tables/data-table.mdx
- polaris.shopify.com/content/components/lists/resource-list.mdx
- polaris.shopify.com/content/components/navigation/pagination.mdx
- polaris.shopify.com/content/components/selection-and-input/index-filters.mdx
- polaris.shopify.com/content/patterns/resource-index-layout/variants/default.mdx

---

## 8. Onboarding and first run (the "new features" pattern, CalloutCard, MediaCard, empty states as first run)

**Example screen.** [19-states](screenshots/19-states.png), "Onboarding callout": a CalloutCard with a primary and a secondary action. The gallery renders the published components; the screens are not Shopify admin captures.

**When to use.** Use it to introduce a feature a merchant has not tried, or to welcome them to a section that is still empty.

**Components.** `EmptyState`, `CalloutCard`, `MediaCard` (including video card and portrait video card), `VideoThumbnail`, `Badge` (informational tone, for a New badge), `Card`, `Banner` (not for this purpose).

**Layout.**
- First visit to an empty section: a full-page `EmptyState` with illustration, title, subtitle and one primary action. The illustration guidance says this is where the empty state picture is seen the first time.
- A feature or opportunity in the middle of a page: a `CalloutCard` with a title, short body, one clear action (a second one optional), an illustration and a dismiss control.
- Educational content: a `MediaCard` that pairs text with a visual (image or video), with a call to action or, if none is needed, no actions. A portrait video card suits a page where the video is the main content, such as an empty state.
- The New badge goes to the right of the label or text it marks (the `Page` header already places badges right of titles).

**Rules.**
- Highlight a feature only when all three are true: the business wants adoption, it adds substantial new value (not just a better way to do something already done), and it is worth pulling the merchant off their task. Big things qualify: whole new pages, new technology.
- Don't use New badges or pips on individual areas (Products, Orders, Customers). Different teams doing it differently creates inconsistency and visual clutter.
- A pip marks a status or a new item in a list (a new notification). Don't use it for new features.
- A New badge is short-lived. Remove it when the merchant clicks the thing it marks, 5 days after they first see it, or after 3 sessions (for example three visits to the page), whichever comes first.
- Legacy rule: never put a New badge in the admin's primary navigation. Using one in the settings navigation needs case-by-case approval from UX management.
- Use the informational `Badge` tone for the New badge.
- `CalloutCard`: state the benefit and what the feature does, give a clear call to action, aim it at merchants who benefit most, make every card dismissible, and use an illustration that supports the message.
- `MediaCard`: educate about completing tasks in the current section, don't advertise. The text must stand alone without the media. Make it dismissible, target it, give a clear call to action. Use a small visual when vertical space is limited or the card should be quieter.
- Copy for both: start sentences with imperative verbs, put the most important point first, use "need" for requirements, and keep button labels verb plus noun.
- Don't use a `Banner` for marketing or upsell. Use callout cards.
- `EmptyState` as first run: see section 3. It explains one feature before it has been used, encourages without guilt, and offers one primary step.
- Onboarding illustrations (design guidance): they frame what each setup task is for and change appearance when the task is complete.

**Not stated in the archive docs.** A setup guide, checklist or multi-step wizard pattern. How to order several callouts on one page. Any limit on how many callout or media cards show at once. Rules for dismissal memory (when a dismissed card returns).

**Source:**
- polaris.shopify.com/content/patterns/new-features/index.mdx
- polaris.shopify.com/content/patterns/new-features/variants/default.mdx
- polaris.shopify.com/content/patterns-legacy/new-badge.mdx
- polaris.shopify.com/content/components/layout-and-structure/callout-card.mdx
- polaris.shopify.com/content/components/layout-and-structure/media-card.mdx
- polaris.shopify.com/content/components/layout-and-structure/empty-state.mdx
- polaris.shopify.com/content/design/illustrations.mdx
- polaris.shopify.com/content/components/feedback-indicators/banner.mdx

---

## Extra patterns

### 9. App settings layout

**When to use.** When merchants need to find and change an app's settings.

**Components.** `BlockStack`, `Card`, `InlineGrid`, `Box` (the docs' example also uses `Page`, `Divider`, `Text`, `TextField`).

**Layout.** Two columns per group of settings. The narrow left column carries a heading and an optional short description so merchants can scan to the right group. The wider right column holds the settings of that group in a card. Groups stack vertically, with a divider between them on wider screens.

**Rules.**
- Skip the description unless it helps.
- Keep related settings together in one card.
- Stack the groups vertically down the page.

**Source:** polaris.shopify.com/content/patterns/app-settings-layout/index.mdx; polaris.shopify.com/content/patterns/app-settings-layout/variants/default.mdx; polaris.shopify.com/content/components/layout-and-structure/layout.mdx

### 10. Card layout

**When to use.** Whenever content is placed in a `Card`. A standard structure lets merchants learn where things sit.

**Components.** `Card`, `BlockStack`, `Bleed`, `FormLayout`, `ActionList`, `Button`, `Tooltip`, `IndexTable`, `ResourceList`.

**Layout.** Three parts: header, body, footer.
- Header: a card title, and often a header action.
- Body: one or more sections, each with a heading and a block such as a list, table or form layout.
- Footer: call-to-actions on the right and list actions on the left.

**Rules.**
- Titles: say the card's purpose. For a list of objects, use the object type. If the header action is icon-only, choose a title that makes clear what it edits. With several sections, pick a title that covers all of them.
- Header actions: represent the whole card (most often Edit or View). Prefer tertiary icon buttons with a tooltip. Don't put calls to action in the header (those go in the footer). Put actions for a single list item on that item. Put section actions in that section's header. Don't group header actions behind a menu by default. Avoid adding list actions in the header unless the card contains only a list. Table actions sit on the right of the header.
- Sections: group content that shares a purpose. Don't make each list item its own section. Omit the section title when there is only one section (but keep the usual title-to-content gap). Don't let a card grow so tall it is hard to scan: offer expand and collapse in the footer.
- Form layouts: wrap in a section, use one even for a single field, don't let short inputs span the full width (use a field group), and don't leave large blank areas beside choice lists.
- Footer calls to action: default to plain buttons, use primary only for the page's most important action, use an action list when there are more than two, and don't use the footer for actions that change the card's content (those belong in the header or on list items). Don't use primary for non-critical actions.
- List actions: left in the footer, for adding items or expanding and collapsing. Don't repeat the object name in the button label.
- Spacing: the default card padding is `space-400`. The deeper something is nested, the smaller its padding. Use padding inside visibly bounded containers (such as a table header) and stacks for gaps between blocks. Don't use padding to separate blocks or around invisible containers. Use `Bleed` with negative margin for optical adjustments.
- Gaps: smaller gaps mean more closely related. Use `space-100` inside a form layout item and between simple list items. Use `space-200` between header, body and footer of a single-section card, between a section heading and its content, and between items that are themselves tight stacks. Use `space-300` between form layout items. Use `space-400` between sections of a multi-section card. Never use `space-400` inside a section. Nest stacks so section titles sit with their own content instead of floating between groups.
- Alignment: align content to both left and right edges of the card, optically rather than strictly.

**Source:** polaris.shopify.com/content/patterns/card-layout/index.mdx

### 11. Common actions

**When to use.** For recurring actions (add, copy, delete, edit, more actions, pin, remove), so they look and behave the same everywhere.

**Components.** `Button` (tertiary icon buttons, secondary, primary), `ActionList`, `Tooltip`, `Toast`.

**Rules by action.**
- Add: default to the circle-plus icon. Use the plain plus icon on secondary and primary buttons. Put add after the last item of a short list, and in the header when the list of resources will be long. For a selectable-options list, put it at the bottom, outside the scrolling area. For a table, put it in the card, table or page header, not the bottom of the table. Don't add intermediate steps when creating a resource, since configuration belongs on the new page.
- Copy: tertiary icon button. Clipboard icon for text, link icon for URLs. Show on hover for cursor users. Confirm inline with a check icon, or with a "copied" toast if the copy sits in an action list.
- Delete: delete icon, at the bottom of an action list. Inline list-item delete goes on the right as a tertiary icon button, shown on hover for cursor users. Never use the x icon for delete. Don't overuse critical styling.
- Edit: edit icon on a tertiary icon button. Don't crowd many filled buttons together.
- More actions: menu horizontal icon on a secondary or tertiary icon button. Don't group actions in the card header by default.
- Pin: pin icon to pin, filled pin icon to show pinned. Keep pinned items together and make unpinning easy.
- Remove: x icon on a tertiary icon button, shown on hover. Never the delete icon.

**General rules.**
- Labels: short, verb plus noun, with the icon on the left. Use icons alone for well-known actions. Don't add words that context already supplies.
- Hierarchy: secondary or tertiary buttons by default. Primary and secondary to mark the likely action in a view. Tertiary icon buttons in list and table rows. No more than two filled buttons in a card. Actions in editors get extra emphasis from the emphasis colour role.
- Interaction: keyboard focus rings must be visible. The docs say not to show them for cursor use. Don't rely on colour alone to show something is interactive. Use disabled styling only for things that cannot be used.
- Platforms: on desktop, reveal list item actions (edit, delete, copy, remove) on hover. On mobile, design for touch placement and target size.

**Source:** polaris.shopify.com/content/patterns/common-actions/index.mdx; polaris.shopify.com/content/patterns/common-actions/variants/overview.mdx; polaris.shopify.com/content/patterns/common-actions/variants/best-practices.mdx

### 12. Date picking

**When to use.** When merchants choose a date, a range, or a preset period.

**Components and variants.**
- Single date: `TextField`, `DatePicker`, `Popover`, `Card`. Type a date or pick from a one-month calendar. Used for scheduling on a given day or memorable dates such as a birthdate.
- Date range: `DatePicker` (two months), `OptionList`, `TextField`, `Popover`, `Button`, plus `BlockStack`, `Box`, `InlineGrid`, `InlineStack`. A preset list, text inputs and a calendar together. Used for analytics time frames and multi-day events.
- Date list: `OptionList`, `Popover`, `Button`. Suggested dates for when preset choices are enough.

**Rules.**
- Single date closes on selection and takes labels that simply name the task (start date, end date, start time). It can be repeated for an end date or time.
- Date range needs an explicit confirm, because choosing a range takes several steps. Show two months so a range can cross months. Pin dates that matter to this merchant at the head of the option list. Mark unselectable dates with the disabled text colour. If someone types a date that does not exist, go back to the earlier choice.
- Date list: show a likely default range on the button. Put single dates first, then ranges from smallest to largest. The list can be adapted, for example for suggested search queries.
- Related: dates are formatted per the grammar guidelines, and timezone handling is tricky (the docs link out for tips).

**Source:** polaris.shopify.com/content/patterns/date-picking/index.mdx; polaris.shopify.com/content/patterns/date-picking/variants/single-date.mdx; polaris.shopify.com/content/patterns/date-picking/variants/date-range.mdx; polaris.shopify.com/content/patterns/date-picking/variants/date-list.mdx

### 13. Resource details layout

**When to use.** To view, edit and create one resource (a product, order, customer, discount). It pairs with the resource index layout. Using it for creation also teaches merchants how editing looks.

**Components.** `Page`, `Card`, `BlockStack`, `InlineGrid` (also `Bleed`, `Divider`, skeleton parts in the example).

**Layout.** Full-width page header with back action, title, secondary actions and previous/next pagination. Below, two columns: primary about two thirds on the left, secondary about one third on the right. Content sits in cards, with similar content in one card.

**Rules.**
- Use the default page width, not full width.
- Group similar content in a single card.
- Primary column: what defines the resource. Secondary column: status, metadata, summaries.
- Order cards by importance, top to bottom.
- In the actions menu, put page-specific actions first and typical object actions (such as delete) last.

**Source:** polaris.shopify.com/content/patterns/resource-details-layout/index.mdx; polaris.shopify.com/content/patterns/resource-details-layout/variants/default.mdx

### 14. Resource index layout

**When to use.** To overview and manage a set of resources: add, find, take action.

**Components.** `Page`, `Card`, `IndexFilters`, `IndexTable`, `Badge`, `ChoiceList`.

**Layout.** One column. Page title and page-level actions at the top. Filters, sorting and selection actions at the top of the table. Resource rows below.

**Rules.**
- Page title is the resource type.
- Resource creation is the primary action in the top right. Drop the button if creation is not offered.
- Use normal page width if the index does not need the full width.
- When the index has no resources, use the `EmptyState` component.

**Source:** polaris.shopify.com/content/patterns/resource-index-layout/index.mdx; polaris.shopify.com/content/patterns/resource-index-layout/variants/default.mdx

### 15. Pickers (legacy pattern page)

**When to use.** When merchants browse and choose from options such as locations, customer segments, or products.

**Components.** `Listbox` with `TextField` (searchable listbox), `Popover`, `Button`, `Icon`, `Sheet`, `Modal`.

**Rules.**
- Reveal features as the option count grows. With one option, show the value directly with no picker. With a few, list them all. With many, add search, filtering or sorting.
- Sort to help finding: a natural order where one exists (date, hue), alphabetical for names, recent or frequently used for items created or reused in context.
- Pin the most relevant options at the top. For navigation or filter pickers, the main option. For form input, the most used.
- Locations: hide the picker for one location. For 2 to 10, show it with "All locations" first and selected by default, then the rest alphabetically. For 11 or more, add text search, then the 5 most recently used locations, then a way to see all.
- Customer segments: pin "All customers", then the active segment, and sort by last edited. Up to 10 segments, show all. At 11 or more, add search, show the 4 most recently edited, add a "show all" action, and paginate or load more on scroll.
- Show the picker in place when picking is the main task, or in a popover or modal when it is secondary.

**Source:** polaris.shopify.com/content/patterns-legacy/pickers.mdx

---

## Where the docs say nothing (summary)

- `EmptySearchResult`: no component page. Only a resource list example name mentions a custom empty search result state.
- Destructive confirmation: no rule on typed confirmation, or on when to use undo instead of a modal.
- Search and filtering: no rules on query debounce, URL state, or the no-results message.
- Onboarding: no setup guide, checklist or wizard pattern.
- Feedback: toast position and stacking limits are not given.
- Data display: no rule choosing between `IndexTable` and `ResourceList`, and the pagination threshold appears as both 25 and 50.
- Forms: no required-field marker beyond the "Optional" label.
- Status: several shell and feedback components are marked no longer supported in these docs, so the replacement App Bridge APIs are the current route, but their usage rules are not in this archive.
