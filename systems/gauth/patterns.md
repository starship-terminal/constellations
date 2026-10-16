# Gauth patterns

How Gauth's components combine to do the recurring jobs on its public pages, written from the captures of 2026-10-17 (signed out, 1440 and 390 wide). Each pattern says when Gauth uses it, the components it is built from (entries in [components.md](components.md), values in [tokens.json](tokens.json)), the layout, and the screens that show it. These are observations of what the product does, not Gauth's own guidance; where a pattern could not be seen signed out, it says so.

| Pattern | Captured | Example screen |
|---|---|---|
| [App shell and navigation](#app-shell-and-navigation) | yes | [home-light-default](screenshots/home-light-default.png) |
| [Forms and validation](#forms-and-validation) | yes, without an error message (Gauth shows none) | [signin-light-dialog](screenshots/signin-light-dialog.png) |
| [Empty, loading and error states](#empty-loading-and-error-states) | empty, one loading state, a lesson error | [academy-my-light-default](screenshots/academy-my-light-default.png) |
| [Destructive confirmation](#destructive-confirmation) | not present signed out | - |
| [Feedback after an action](#feedback-after-an-action) | yes | [lesson-science-light-quiz-answered](screenshots/lesson-science-light-quiz-answered.png) |
| [Search and filtering](#search-and-filtering) | yes, no results page | [academy-math-light-default](screenshots/academy-math-light-default.png) |
| [Data display](#data-display) | yes | [plus-light-full](screenshots/plus-light-full.png) |
| [Onboarding and first run](#onboarding-and-first-run) | yes, sign-up excluded | [home-light-promo](screenshots/home-light-promo.png) |
| [Upsell](#upsell) | yes, checkout excluded | [plus-dialog-light-default](screenshots/plus-dialog-light-default.png) |

## App shell and navigation

**When.** Every page a learner moves between: Homework, Academy, the unit pages, Insights, the plans page. Atlas and the lesson players have their own shells.

**Components.** [Sidebar](components.md#sidebar), [Sidebar item](components.md#sidebar-item) and its current states (cool and warm), [Sidebar collapse button](components.md#sidebar-collapse-button), [Gauth PLUS card](components.md#gauth-plus-card), [Top bar](components.md#top-bar), [Top bar question field](components.md#top-bar-question-field), [Upgrade button](components.md#upgrade-button), [Sign in button](components.md#sign-in-button).

**Layout.** A fixed 220px sidebar (`layout.sidebar`) at the left and a 60px top bar (`layout.header`) over the content column. The sidebar lists four destinations, a rule, App, and the PLUS card pinned to its foot; the sidebar sits over the top bar (`zIndex.sidebar` 101 over `zIndex.header` 99). On Homework and Insights the shell is white with a cool grey current item (`component.sidebar.item-current`); on Academy it takes the warm ground (`background.academy`, `#faf9f5`) and the current item turns beige (`component.sidebar.item-current-warm`). Inner pages move the question field into the top bar. Collapsing the sidebar folds it to an icon rail.

Three surfaces leave the shell:

- **Lesson players** drop it entirely: an exit cross at the top left, the lesson title, and transport controls as 32px ghost icon buttons. The math player covers the shell at `zIndex.player` (1000).
- **Atlas** has its own 56px header and 230px drawer ([Atlas top bar](components.md#atlas-top-bar), [Atlas sidebar](components.md#atlas-sidebar)).
- **At 390 wide** the sidebar becomes a drawer behind a menu button in a top bar ([Mobile top bar](components.md#mobile-top-bar)).

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-sidebar-folded](screenshots/home-light-sidebar-folded.png), [academy-science-light-default](screenshots/academy-science-light-default.png), [lesson-science-light-default](screenshots/lesson-science-light-default.png), [atlas-light-default](screenshots/atlas-light-default.png), [mobile-home-light-default](screenshots/mobile-home-light-default.png).

## Forms and validation

**When.** The few inputs a visitor meets: the Sign in dialog's email field, the question field, the Create a Course prompt, the Atlas prompt box, the Ask Tutor bar.

**Components.** [Email field](components.md#email-field), [Primary button, disabled (Sign in)](components.md#primary-button-disabled-sign-in), [Social sign-in button](components.md#social-sign-in-button), [Question field](components.md#question-field), [Course prompt field](components.md#course-prompt-field), [Atlas prompt box](components.md#atlas-prompt-box), [Send button](components.md#send-button).

**Layout.** Fields are filled, not outlined: the email field is a grey 48px box at radius 12 with a leading mail icon, and a clear button appears once something is typed. The submit action sits under or inside the field: a full-width 54px button in the Sign in dialog, a round send button inside the prompt boxes.

**Validation.** Gauth validates by holding the submit back, not by writing errors:

- The Sign in button stays disabled, in brand red at low strength (`action.primary-disabled`, `#ffccd8`) with white text, while the email field is empty or holds something that is not an address. Typing a non-address and leaving the field shows no message, no red border and no icon.
- The Atlas send button is a grey disc (`component.atlas.send` with a `text.disabled` arrow) carrying `disabled` while the box is empty, and turns near-black (`palette.atlas.toggle`) once text is typed. The Create a Course send button does the same.

Where errors appear after a submit was not seen, since nothing was submitted.

**Screens.** [signin-light-dialog](screenshots/signin-light-dialog.png), [home-light-question-focused](screenshots/home-light-question-focused.png), [academy-my-light-create-dialog](screenshots/academy-my-light-create-dialog.png); crops [signin-email-filled](components/crops/signin-email-filled.png), [signin-submit-disabled](components/crops/signin-submit-disabled.png), [send-button-disabled](components/crops/send-button-disabled.png), [send-button-enabled](components/crops/send-button-enabled.png).

## Empty, loading and error states

**Empty.** My Course, signed out, is the one empty list: a fan of three course cards, a 20px bold title, a grey line, and the dark Create button ([My Course empty state](components.md#my-course-empty-state), [Create button (empty state)](components.md#create-button-empty-state)). The empty state carries the page's one primary action rather than pointing elsewhere. The Atlas drawer's topic list is empty signed out and shows nothing in its place.

**Loading.** Gauth renders its pages on the server, so the skeletons its CSS declares (`catalog_mathSkeleton*`, `math-course-detail_detailSkeletonBanner`, loading dots in the course dialog and the lesson result page) never showed, even with the data request held back. The loading state captured is the math tutor's status line, "Explaining ...", which shimmers while the tutor narrates ([Tutor status line](components.md#tutor-status-line)). With reduced motion the shimmer, the skeleton pulse and the loading dots stop and hold still at reduced opacity ([raw/foundations.json](raw/foundations.json)).

**Error.** The error a visitor can reach is a wrong answer in a lesson. The science lesson's check-in comes back as a result card in the notes, headed "Quick check · Needs review" with a cross icon, painted in the lesson's wrong colours (`status.danger.fill`, `.border`, `.text`), with Your answer beside Correct answer and a line on why the answer missed ([Quiz result card](components.md#quiz-result-card)). The math player has an incorrect frame state with its own animation (`.shared_playerFrameIncorrect`), not reached. A page that fails to load was not seen.

**Screens.** [academy-my-light-default](screenshots/academy-my-light-default.png), [lesson-math-light-default](screenshots/lesson-math-light-default.png), [lesson-science-light-quiz-answered](screenshots/lesson-science-light-quiz-answered.png).

## Destructive confirmation

Not present signed out. A visitor has nothing to delete, leave or cancel: no course, topic, history or subscription. The one closing action, the lesson's exit cross, leaves without asking.

## Feedback after an action

**When.** After a learner answers, presses or hovers.

**What Gauth does.**

- **Inline, in place.** A lesson answer is acknowledged where the question was: the check-in turns into a result card in the notes ([Quiz result card](components.md#quiz-result-card)). No toast was seen anywhere signed out.
- **Press.** Buttons shrink instead of changing colour: `scale.press` (0.98) on the primary and Astryx buttons, `scale.press-round` (0.94) on the math player's round buttons. The dark primary keeps its hover fill while pressed (`action.primary-pressed`).
- **Hover.** Cards lift by shadow: `elevation.level-1` at rest to `elevation.level-2` on hover in `duration.fast` (160ms); story cards also rise 4px. Outlined controls darken their border (`border.strong`).
- **State change.** The current tab, sidebar item, unit and menu row are marked by a fill (`background.selected-warm`, `component.sidebar.item-current`) or a check, never by colour alone on the label.

**Screens.** [lesson-science-light-quiz-answered](screenshots/lesson-science-light-quiz-answered.png); crops [lesson-card-hover](components/crops/lesson-card-hover.png), [create-button-pressed](components/crops/create-button-pressed.png), [menu-item-selected-selected](components/crops/menu-item-selected-selected.png).

## Search and filtering

**When.** Narrowing the catalogue, finding a topic in Atlas, switching the Insights list.

**Components.** [Category tab](components.md#category-tab) and [Category tab, current](components.md#category-tab-current), [Pill tab](components.md#pill-tab) and [Pill tab, current](components.md#pill-tab-current), [Topic search field](components.md#topic-search-field), [Recommendation chip](components.md#recommendation-chip), [Show more button](components.md#show-more-button).

**Layout.** Filtering is by tabs, not by a search box: the Academy's four category tabs (36px, radius 12, the current one beige) swap the whole catalogue below, and stick to the top with Create Course as the page scrolls (`zIndex.sticky`). Insights uses pink pill tabs for News and Blog. Within a course list, Show more expands the rest of the units in place. Atlas puts a search field in its drawer for a learner's own topics (empty signed out) and offers recommendation chips under the prompt box as starting points. No results page or empty search result was seen.

**Screens.** [academy-science-light-default](screenshots/academy-science-light-default.png), [academy-math-light-show-more](screenshots/academy-math-light-show-more.png), [news-light-default](screenshots/news-light-default.png), [atlas-light-default](screenshots/atlas-light-default.png).

## Data display

**When.** Lists of courses, units, stories, articles and plan features.

**Components.** [Lesson card](components.md#lesson-card-science-labs-history-signature), [Unit card](components.md#unit-card-math-curriculum), [Story card](components.md#story-card), [Unit rail](components.md#unit-rail), [Article row](components.md#article-row), [Pagination](components.md#pagination), [Table (features by plan)](components.md#table-features-by-plan), [Table (benefits)](components.md#table-benefits).

**Layout.**

- **Card grids** for anything with a cover: three 326px columns 24 apart in the Academy (`grid.catalog-columns`, `grid.catalog-gap`), three 339px columns 32 apart in Atlas (`grid.story-columns`). At 390 the Academy turns each card into a 112px row card in one column.
- **A list beside a path** on the unit page: a 310px rail of units at the left, the topic path at the right, 32 apart (`grid.unit-columns`).
- **Rows with pagination** in the blog: image-and-text rows split by a rule, then Ant Design pagination with 36px round items, the current page filled near-black and Previous disabled on page 1.
- **Tables** only for plan comparison: a real `<table>` on `/plus` (a header row holding each plan and its button, then label, Free and PLUS cells, the PLUS column tinted cream), and a three-column benefits table in the PLUS dialog with green checks against grey dashes.

Sorting was not seen anywhere.

**Screens.** [academy-science-light-full](screenshots/academy-science-light-full.png), [unit-light-default](screenshots/unit-light-default.png), [atlas-light-full](screenshots/atlas-light-full.png), [blog-light-pagination](screenshots/blog-light-pagination.png), [plus-light-full](screenshots/plus-light-full.png).

## Onboarding and first run

**When.** A visitor's first page and first lesson.

**Components.** [Promo dialog](components.md#promo-dialog), [Enable audio dialog](components.md#enable-audio-dialog), [Audio gate](components.md#audio-gate), [Course suggestion chip](components.md#course-suggestion-chip), [Recommendation chip](components.md#recommendation-chip).

**Layout.** Every page opens with the promo dialog ("Introducing Gauth Academy"): a 600px white card at radius 24 with a serif title, a media panel and one full-width black button, dismissed by its round close button. A lesson asks for sound before it starts: the science player with a two-button dialog (Enable audio, Not now), the math player with a line of text and a Continue button over the blurred slide. Blank prompts are seeded: the Create a Course dialog offers three suggested topics and Shuffle, and Atlas shows recommendation chips under its prompt box. Sign-up itself was not captured.

**Screens.** [home-light-promo](screenshots/home-light-promo.png), [lesson-science-light-audio-dialog](screenshots/lesson-science-light-audio-dialog.png), [lesson-math-light-audio-gate](screenshots/lesson-math-light-audio-gate.png), [academy-my-light-create-dialog](screenshots/academy-my-light-create-dialog.png).

## Upsell

**When.** Gauth puts the paid plan on every shell page.

**Components.** [Upgrade button](components.md#upgrade-button), [Gauth PLUS card](components.md#gauth-plus-card), [Gauth PLUS dialog](components.md#gauth-plus-dialog), [Plan card (single choice)](components.md#plan-card-single-choice), [Plan card, selected](components.md#plan-card-selected), [Join Gauth PLUS button](components.md#join-gauth-plus-button), [Plan card (plans page)](components.md#plan-card-plans-page).

**Layout.** The upsell has its own warm palette, kept out of the learning pages: a gold gradient Upgrade pill in the top bar, a cream PLUS card at the foot of the sidebar, and a two-panel dialog with a warm gradient panel and the benefits table at the left and the plan cards at the right. The plan cards are a single-choice group with the 12-month card preselected in gold (`palette.gold`), and the one action is a dark brown Join button. The dialog sits just under Gauth's other dialogs (`zIndex.upsell` 1082 under `zIndex.dialog` 1084). Checkout was not opened.

**Screens.** [plus-dialog-light-default](screenshots/plus-dialog-light-default.png), [plus-light-default](screenshots/plus-light-default.png), [home-light-default](screenshots/home-light-default.png).
