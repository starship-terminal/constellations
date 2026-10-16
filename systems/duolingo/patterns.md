# Duolingo: patterns

How Duolingo puts its components together for the eight patterns in [docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md). Written from the captures in [screenshots/](screenshots) (2026-09-25, and the 2026-10-17 refresh for onboarding, empty and no-results search, the lesson report form, the friend-streak dialog and the 1000px and 390px layouts). Token names are from [tokens.json](tokens.json); component specs are in [components/core.md](components/core.md) and [components/product.md](components/product.md). Each pattern ends with what was not captured.

## App shell and navigation

Three widths, one structure ([core.layout.columns](tokens.json)).

| Width | Shell | Screenshot |
| --- | --- | --- |
| 1160px and up | Fixed 256px sidebar on the left (logo, eight uppercase nav items, a promo card), a centred row of at most 1056px with the main column and a 368px sticky right rail (stat bar, Super, league and quest cards), 48px between them | [learn-light-default](screenshots/learn-light-default.png) |
| 700 to 1159px | The sidebar collapses to 88px of icons; the main column and rail stay | [learn-light-tablet](screenshots/learn-light-tablet.png) |
| Below 700px | A 58px top bar with the stats, one column, an 82px bottom tab bar with six 32px icons | [learn-light-phone](screenshots/learn-light-phone.png), [learn-dark-phone](screenshots/learn-dark-phone.png), [quests-dark-phone](screenshots/quests-dark-phone.png) |

The current destination is the only coloured nav item: `surface.selected` fill, a 2px `border.selected` outline and `text.link` label ([learn-light-default](screenshots/learn-light-default.png)). Surfaces are separated by 2px `border.default` rules, never by shadow. The lesson player drops the shell entirely: a top bar with quit, settings and a progress bar, the challenge, and a footer band that carries the verdict ([lesson-light-challenge-default](screenshots/lesson-light-challenge-default.png)).

Not captured: the 88px sidebar's MORE flyout and any keyboard navigation of the shell beyond Tab ([components/focus.md](components/focus.md)).

## Forms and validation

Settings forms are a single column of labelled 3D fields: a bold label (heading-small), a `surface.subtle` field with a 2px `border.default` border and 12px radius, and one filled SAVE CHANGES button that stays disabled (`surface.disabled` face, `text.disabled` label) until something changes ([settings-profile-light-default](screenshots/settings-profile-light-default.png)). Focus turns the field border `border.focus`; nothing else moves ([components/focus.md](components/focus.md)). Toggles sit on the right of each row, choices are radio cards, and the theme is a native select behind a 3D face ([settings-account-light-default](screenshots/settings-account-light-default.png)).

Short forms inside a flow are checkbox lists with one submit: the lesson report form lists six native checkboxes (20px, 2px `border.default`, 5px radius; checked turns the border and tick `border.focus`) and its SUBMIT button is disabled until one is ticked ([lesson-light-report-form-checked](screenshots/lesson-light-report-form-checked.png), [lesson-dark-report-form](screenshots/lesson-dark-report-form.png), [lesson-dark-report-form-checked](screenshots/lesson-dark-report-form-checked.png)).

Not captured: a validation error on screen. Errors appear only after a submit, which this capture does not do. The error styling is in the CSS: the field border and a helper line turn `accent.danger.lip` (fire-ant) with a circle-exclamation icon ([components/core.md](components/core.md#text-input-incl-password-with-eye-toggle-clearable)).

## Empty, loading and error states

| State | What Duolingo shows | Screenshot |
| --- | --- | --- |
| Empty (nothing searched yet) | A large group illustration, one centred line of `text.secondary` copy, and a side card offering another route (Invite friends) | [user-search-light-empty](screenshots/user-search-light-empty.png) |
| Empty (no results) | Duo in a detective costume and "Sorry, we didn't find any matching learners. Try searching again." in `text.secondary`, 19px, centred under it | [user-search-light-no-results](screenshots/user-search-light-no-results.png), [user-search-dark-no-results](screenshots/user-search-dark-no-results.png) |
| Loading | A full-page white screen with Duo and LOADING... in bold uppercase `text.disabled`, fading in; in-app route changes leave the main column blank until the page arrives | [onboarding-light-loading](screenshots/onboarding-light-loading.png) |
| Error | Error 404: crying Duo on the left, a title and two lines of `text.secondary` copy with inline links, no buttons | [error-404-light-default](screenshots/error-404-light-default.png) |

Every state leads with a mascot illustration; none uses an icon-only empty state or a spinner. Under reduced motion the loader's dots keep only an opacity change (`core.duration.reducedMotion`).

Not captured: a network or server error inside the app, and skeleton screens (none appeared).

## Destructive confirmation

Two forms, both with one danger action. Removing a course opens a bottom sheet over a dimmed page (`background.scrim`): Duo, a bold question naming the course, a warning line, an outline CANCEL and a filled red REMOVE (`accent.danger.face` with its `accent.danger.lip`) ([settings-courses-light-remove-confirm](screenshots/settings-courses-light-remove-confirm.png), [settings-courses-dark-remove-confirm](screenshots/settings-courses-dark-remove-confirm.png)). Quitting a lesson opens a centred dialog (`surface.overlay`) where the safe action is the filled button (KEEP LEARNING) and the destructive one is red text (END SESSION) ([lesson-light-quit-modal](screenshots/lesson-light-quit-modal.png)). The row action that starts the course removal is red uppercase text with no frame.

Not captured: the delete-account flow (left alone on purpose).

## Feedback after an action

The lesson footer is the feedback surface. After CHECK the whole band turns `feedback.correct.background` or `feedback.incorrect.background`, a round badge and a title appear in the verdict colour, TOO EASY / TOO DIFFICULT / REPORT links take the same colour, and CONTINUE turns green or red ([lesson-light-feedback-correct](screenshots/lesson-light-feedback-correct.png), [lesson-dark-feedback-incorrect](screenshots/lesson-dark-feedback-incorrect.png)). Streaks, XP and league moves get full-screen celebration screens with a mascot ([lesson-dark-streak-celebration](screenshots/lesson-dark-streak-celebration.png), [lesson-dark-complete](screenshots/lesson-dark-complete.png)). Small confirmations swap a label in place ("Copy link" becomes "Copied").

Not captured: a toast. None appeared in either capture; the app's CSS has no toast or snackbar class the capture could find.

## Search and filtering

Friend search is a full-width `surface.subtle` field (63px, 2px `border.default`, 12px radius) with a search icon and a clear button, submitted with Enter. Results are a bordered list of rows with an avatar, the name and a filled FOLLOW pill ([user-search-light-results](screenshots/user-search-light-results.png)); no results and nothing-yet are the two empty states above. The search field does not change its border on focus.

Not captured: filtering. The free web app has no filter controls on the screens visited.

## Data display

Lists, not tables. The leaderboard is a ranked list of 64px rows (rank, avatar, name, XP) where the learner's own row is filled `gamification.league.currentUserRow` and the promotion and demotion zones are marked by colour ([leaderboard-light-default](screenshots/leaderboard-light-default.png)). Quests are cards of rows with a progress bar (`dataViz.progress.*`) and a chest ([quests-light-default](screenshots/quests-light-default.png)); profile statistics are 2px-bordered tiles in a two-column grid ([profile-light-scrolled](screenshots/profile-light-scrolled.png)).

Not present: tables and charts.

## Onboarding

Captured on 2026-10-17 from a fresh logged-out browser (headless, no account), through "Get started" on www.duolingo.com, in both themes at 1440 and 390 ([tools/capture/onboarding.mjs](tools/capture/onboarding.mjs), readings in [raw/2026-10/onboarding/](raw/2026-10/onboarding)).

1. **Course picker** ("I want to learn..."): a grid of flag cards with learner counts. It stays light in both themes ([onboarding-light-course-picker](screenshots/onboarding-light-course-picker.png), [onboarding-dark-course-picker](screenshots/onboarding-dark-course-picker.png)).
2. **Loading**: Duo and LOADING... ([onboarding-light-loading](screenshots/onboarding-light-loading.png)).
3. **Intro**: Duo alone with a speech bubble ("Hi there! I'm Duo!") and one CONTINUE button in the footer ([onboarding-light-intro](screenshots/onboarding-light-intro.png), [onboarding-dark-intro](screenshots/onboarding-dark-intro.png)).
4. **Questions**, one per screen with a progress bar along the top and Duo asking in a speech bubble: how you heard about Duolingo (two-column choice cards with icons), why you are learning, how much you know (single-column rows with signal-bar icons), a daily goal (minutes per day with a label: Casual, Regular, Serious, Intense), and where to start (two large cards). CONTINUE is disabled (`surface.disabled`) until a choice is made; a picked card takes the selected style (`surface.selected`, `border.selected`, `text.selected`) ([onboarding-light-source](screenshots/onboarding-light-source.png), [onboarding-light-source-selected](screenshots/onboarding-light-source-selected.png), [onboarding-light-motivation](screenshots/onboarding-light-motivation.png), [onboarding-light-level](screenshots/onboarding-light-level.png), [onboarding-light-goal](screenshots/onboarding-light-goal.png), [onboarding-light-goal-selected](screenshots/onboarding-light-goal-selected.png), [onboarding-light-start-choice](screenshots/onboarding-light-start-choice.png); dark and `-phone` versions of each).

The flow asks for nothing personal before the first lesson. Not captured: the first lesson and the profile and sign-up steps after it (they ask for an age, a name and an email).
