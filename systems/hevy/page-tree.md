# Hevy page tree

Every screen, tab, sheet, menu, dialog and toast reachable in Hevy 3.1.16 (free account), and whether it has been explored.

| Mark | Meaning |
|---|---|
| `[x]` | Opened, scrolled to the bottom, every child listed below it |
| `[~]` | Opened but not yet scrolled to the bottom or not all children opened |
| `[ ]` | Not opened yet |
| `[action]` | Button that changes your account or posts something. Listed, not pressed. |
| `[external]` | Leaves Hevy (another app, the App Store, a website, an iOS system sheet's targets). Listed, not opened. |
| `[same as X]` | Opens a page already in the tree |
| `[infinite]` | Endless feed of the same card. Scrolled several screens, no new card types. |

Capture files are in [screenshots/light/](screenshots/light/), [screenshots/dark/](screenshots/dark/) and [screenshots/pages/](screenshots/pages/). `t*` files are from the tree pass.

## Tree

- [x] Home tab
  - [x] Feed: Home (Following) [infinite] ([01-home.png](screenshots/light/01-home.png), [d17-home.png](screenshots/dark/d17-home.png))
    - [x] Feed switcher menu (popover: Home (Following), Discover) ([t01](screenshots/pages/t01-home-feed-switcher-menu.png))
      - [x] Discover feed [infinite] ([t02](screenshots/pages/t02-discover-feed.png), [t21 trainer tag variant](screenshots/pages/t21-discover-post-trainer-tag.png))
        - [action] + Follow
        - [x] Post (Workout Detail), below
    - [x] Post card
      - [x] Author row → Other user profile, below
      - [x] Post body / "See N more exercises" [same as Post (Workout Detail)]
      - [action] Like
      - [x] Comment icon → Comments, below
      - [x] Share icon → iOS share sheet, below
    - [x] Suggested Athletes carousel
      - [action] Follow
      - [action] Dismiss (x)
      - [x] Athlete card → Other user profile, below
      - [x] Invite a friend → Invite Friends, below
    - [x] Post (Workout Detail) ([t03 top](screenshots/pages/t03-post-detail-top.png), [t05 actions row](screenshots/pages/t05-post-detail-actions-row.png), [t04 bottom](screenshots/pages/t04-post-detail-bottom.png), [p03](screenshots/pages/p03-workout-detail.png))
      - [x] Image carousel with page dots (second image not reachable: swiping doesn't work through iPhone Mirroring)
      - [x] Muscle Split bar chart, "Show N more" expands in place
      - [x] Exercise rows → Exercise detail [same as Exercise detail under Workout]
      - [x] Personal record badges under sets
      - [x] Likes count → Likes list ([t07](screenshots/pages/t07-likes-list.png)), scrolled to end
        - [action] Follow
        - [x] Row → Other user profile
      - [x] Comments ([t06](screenshots/pages/t06-comments-empty.png)): empty state, emoji quick-reply bar, comment field with send
        - [action] Emoji quick replies, comment field, send
        - [x] Likes count [same as Likes list]
      - [x] Share → iOS share sheet ([t10](screenshots/pages/t10-post-share-sheet.png))
        - [external] Contacts, AirDrop, Telegram, WeChat, Reminders, Copy, Quick Note, Save to Files, more
      - [x] "..." menu sheet ([t11](screenshots/pages/t11-post-menu-sheet.png))
        - [action] Save as Routine
        - [action] Copy Workout
        - [action] Report Workout
    - [x] Other user profile
      - [x] Private state ([t08](screenshots/pages/t08-other-profile-private.png)): Follow, lock notice
      - [x] Public state ([t12 top](screenshots/pages/t12-other-profile-public-top.png), [t13 mid](screenshots/pages/t13-other-profile-public-mid.png)): bio, weekly hours bar chart, Compare, routines carousel, workout feed [infinite]
        - [action] Follow
        - [external] Bio link
        - [x] Share icon [same as iOS share sheet]
        - [x] "..." menu sheet ([t09](screenshots/pages/t09-user-menu-report-block.png))
          - [action] Report User
          - [action] Block User
        - [x] Routine card [same as Routine detail]
        - [x] Compare → Comparison ([t14 top](screenshots/pages/t14-compare-top.png), [t20 stats](screenshots/pages/t20-compare-stats-mid.png), [t15 bottom](screenshots/pages/t15-compare-bottom.png))
          - [x] Period dropdown → sheet with Pro-locked options ([t17](screenshots/pages/t17-period-sheet-pro-locked.png))
            - [x] Pro-locked option → Contextual paywall ([t18](screenshots/pages/t18-paywall-contextual.png))
              - [action] Plan cards, Subscribe
              - [x] Not now / close
          - [x] "?" help → Info dialog with Okay ([t19](screenshots/pages/t19-info-dialog.png))
          - [x] Exercise in common → Exercise comparison ([t16](screenshots/pages/t16-compare-exercise.png)), fits one screen
            - [x] Exercise row [same as Exercise detail]
  - [x] Search ([p01](screenshots/pages/p01-search.png))
    - [x] Search tab: suggested athletes
      - [action] Follow, dismiss (x)
      - [x] Invite a friend → Invite Friends, below
      - [x] Typed query → Results with verified badge and clear (x) ([t26](screenshots/pages/t26-search-results-verified.png))
      - [x] Typed query, nothing found → No-results state with Invite button ([t27](screenshots/pages/t27-search-no-results.png))
        - [external] Invite (opens share)
    - [x] Contacts tab
      - [x] Loading spinner ([t24](screenshots/pages/t24-contacts-loading-spinner.png))
      - [x] Empty state ([t25](screenshots/pages/t25-contacts-empty.png))
  - [x] Invite Friends ([t22](screenshots/pages/t22-invite-friends.png))
    - [external] WhatsApp, Messenger, Facebook, Messages, Share More
    - [x] Copy Link → Alert "Link added to clipboard" with Ok ([t23](screenshots/pages/t23-copy-link-alert.png))
    - [action] Connect with Contacts (triggers the iOS contacts permission prompt)
  - [x] Notifications ([p02](screenshots/pages/p02-notifications-empty.png)): empty state, fits one screen
- [x] Workout tab ([02](screenshots/light/02-workout.png), [d10](screenshots/dark/d10-workout.png))
  - [x] Title dropdown → menu: Workout, Trainer ([t49](screenshots/pages/t49-workout-mode-menu.png))
    - [x] Trainer mode ([t50](screenshots/pages/t50-trainer-mode-tab.png))
      - [x] Start with Hevy Trainer [same as Trainer questionnaire]
      - [x] Build my own workouts → back to Workout mode
  - [x] PRO badge → Generic paywall [same as Paywall under Settings]
  - [x] Start Empty Workout → Log Workout (see Log Workout below)
  - [x] New folder icon → "Create New Folder" dialog with text field ([t51](screenshots/pages/t51-new-folder-dialog-input.png))
    - [action] Save
    - [x] Cancel
  - [x] New Routine → Routine editor ([07](screenshots/light/07-new-routine-empty.png), [10](screenshots/light/10-routine-editor.png), [p14](screenshots/pages/p14-create-exercise-form.png))
  - [x] Explore (below)
  - [action] Tip banner close (x)
  - [x] My Routines collapse/expand ([t55](screenshots/pages/t55-my-routines-collapsed.png))
  - [action] Long-press to reorder routines
  - [x] Routine card
    - [action] Start Routine (starts a workout; covered via a throwaway workout)
    - [x] "..." → Routine card menu ([t52](screenshots/pages/t52-routine-card-menu.png))
      - [x] Share Routine [same as iOS share sheet]
      - [action] Duplicate Routine
      - [x] Edit Routine ([t53](screenshots/pages/t53-edit-routine.png))
        - [x] REPS ▾ → Repetition Options sheet ([t54](screenshots/pages/t54-repetition-options-sheet.png))
        - [action] Update
        - [x] Cancel
      - [action] Delete Routine
    - [x] Card body → Routine detail ([p04](screenshots/pages/p04-routine-detail.png), [t56 chips](screenshots/pages/t56-routine-detail-chip-reps.png), [t57 bottom](screenshots/pages/t57-routine-detail-bottom.png))
      - [x] Volume / Reps / Duration chips
      - [x] Edit Routine link [same as Edit Routine]
      - [x] Share icon [same as iOS share sheet]
      - [x] "..." → Action sheet ([p05](screenshots/pages/p05-action-sheet.png)): Duplicate [action], Edit [same], Delete [action]
      - [x] Exercise name → Exercise detail, below
  - [x] Exercise detail
    - [x] Summary tab ([p06](screenshots/pages/p06-exercise-summary.png), [t58 bottom](screenshots/pages/t58-exercise-summary-bottom-records.png))
      - [x] Hero animation with pause button
      - [x] "Last 3 months" → Period sheet with Pro-locked options [same as Comparison period sheet]
      - [x] Metric chips (Heaviest Weight, One Rep Max, Best Set)
      - [x] Personal Records "?" → Info dialog [same pattern as Comparison info dialog]
      - [x] Set Records expand ([t59](screenshots/pages/t59-exercise-set-records-expanded.png))
    - [x] History tab ([p07](screenshots/pages/p07-exercise-history.png)): long list of session cards [infinite]
      - [x] Session header → Own workout detail ([t65](screenshots/pages/t65-own-workout-detail.png))
        - [x] "..." → Own workout menu ([t66](screenshots/pages/t66-own-workout-menu.png))
          - [action] Save as Routine, Copy Workout, Delete Workout
          - [x] Edit Workout ([t67](screenshots/pages/t67-edit-workout-form.png), [t71 bottom](screenshots/pages/t71-edit-workout-bottom.png)): photo/video area, description, Date, Gym, Visibility
            - [x] Visibility sheet ([t68](screenshots/pages/t68-visibility-sheet.png))
            - [x] Gym → iOS location prompt (you chose Allow Once, not captured) → Gym picker ([t69](screenshots/pages/t69-gym-picker.png), nearby gyms blurred)
            - [x] Date → Date and time wheel sheet ([t70](screenshots/pages/t70-date-time-wheel-sheet.png))
            - [external] Add a photo / video (iOS photo picker)
            - [action] Save
            - [x] Cancel (no prompt when nothing changed)
    - [x] How to tab ([p08](screenshots/pages/p08-exercise-howto.png))
    - [x] Leaderboard tab ([p09](screenshots/pages/p09-exercise-leaderboard.png), [t73 bottom](screenshots/pages/t73-leaderboard-bottom-sticky-you.png)): your row pinned at the bottom
      - [x] "?" → Info dialog [same pattern]
      - [x] Share → Leaderboard share card ([t72](screenshots/pages/t72-share-card-leaderboard.png))
      - [x] Invite a Friend [same as Invite Friends]
    - [x] How to tab bottom ([t74](screenshots/pages/t74-howto-bottom.png))
    - [x] "..." → Exercise menu ([t60](screenshots/pages/t60-exercise-menu.png))
      - [x] Weight Units sheet ([t61](screenshots/pages/t61-exercise-weight-units-sheet.png))
      - [action] Duplicate Exercise
    - [x] Share → Share card composer ([t62](screenshots/pages/t62-share-card-composer.png))
      - [x] Background → "Pick a background" sheet ([t63](screenshots/pages/t63-share-pick-background.png)), Light card ([t64](screenshots/pages/t64-share-card-light.png))
      - [external] Stories, More
      - [action] Download (saves an image to your phone)
  - [x] Explore ([12](screenshots/light/12-explore.png), [d16](screenshots/dark/d16-explore.png), [t30 bottom](screenshots/pages/t30-explore-bottom-routine-categories.png))
    - [x] Filters sheet ([t28](screenshots/pages/t28-explore-filters-sheet.png))
    - [x] Level sheet ([p23](screenshots/pages/p23-level-sheet.png)), Goal sheet ([t29](screenshots/pages/t29-goal-sheet.png)), Equipment sheet (same layout)
    - [x] Program card → Program detail ([p22](screenshots/pages/p22-program-detail.png), [t34 bottom](screenshots/pages/t34-program-detail-bottom.png))
      - [action] Save Program
      - [x] Share icon [same as iOS share sheet]
    - [x] Show all 26 programs (expands in place)
    - [x] Trainer → Trainer intro ([t35](screenshots/pages/t35-trainer-intro.png))
      - [x] Get Started → Questionnaire, 10 steps ([t36](screenshots/pages/t36-trainer-q1-radio.png) to [t47](screenshots/pages/t47-trainer-q10-bottom.png)): radio rows, ruler picker, wheel picker, "Recommended" tag, muscle focus, gym type, equipment checkboxes
        - [action] "Please accept our health terms and policy" → Accept and Continue ([t48](screenshots/pages/t48-trainer-after-continue.png))
      - [x] Cancel
    - [x] Routine category tile → Category page ([t31](screenshots/pages/t31-routine-category-top.png), [t32 bottom](screenshots/pages/t32-routine-category-bottom.png))
      - [action] Save Routine
      - [x] "see more" expands description in place
      - [x] "..." → Sheet with Share Routine ([t33](screenshots/pages/t33-routine-share-sheet-menu.png)) [same as iOS share sheet]
- [x] Log Workout (in-progress workout, tested with throwaway workouts that were all discarded)
  - [x] Empty state ([14](screenshots/light/14-empty-workout.png), [d11](screenshots/dark/d11-empty-workout.png))
  - [x] Collapse arrow → Minimised in-progress bar ([05](screenshots/light/05-workout-in-progress-bar.png))
    - [x] Trash → Discard dialog ([06](screenshots/light/06-discard-dialog.png), [d15](screenshots/dark/d15-discard-dialog.png))
  - [x] Clock icon → Clock sheet: Timer ([p20](screenshots/pages/p20-clock-timer-ring.png)), Stopwatch ([p21](screenshots/pages/p21-clock-stopwatch.png))
  - [x] Finish
    - [x] No exercises → Alert "Add an exercise" ([t75](screenshots/pages/t75-finish-validation-alert.png))
    - [x] No set values → Alert "Your workout has no set values" ([t82](screenshots/pages/t82-finish-no-set-values-alert.png))
    - [x] With a ticked set → Save Workout ([t83](screenshots/pages/t83-save-workout-tooltip.png)) with tooltip "Tap to select your gym"
      - [action] Save
      - [x] Date → Date and time wheel sheet [same as t70]
      - [x] Gym → Gym picker ([t69](screenshots/pages/t69-gym-picker.png), nearby gyms blurred)
      - [x] Visibility sheet [same as t68]
      - [x] Sync With ([t84](screenshots/pages/t84-sync-with-switches.png))
      - [external] Add a photo / video (iOS photo picker)
      - [x] Discard Workout → confirm dialog → discarded
  - [x] Body figures → Muscle Distribution sheet, empty state ([t77](screenshots/pages/t77-muscle-distribution-sheet-empty.png))
    - [x] Start Adding Exercises [same as Exercise picker]
  - [x] Settings button → Workout Settings modal (same rows as Settings > Workouts, plus Apple Watch)
    - [x] Apple Watch ([t76](screenshots/pages/t76-apple-watch-searching.png))
      - [external] Troubleshooting Instructions
  - [x] Add Exercise → Exercise picker ([08](screenshots/light/08-exercise-picker.png), [09](screenshots/light/09-exercise-picker-selected.png), [d12](screenshots/dark/d12-exercise-picker-selected.png))
    - [x] Equipment / Muscle filter sheets ([p10](screenshots/pages/p10-filter-sheet-equipment.png) to [p13](screenshots/pages/p13-filter-sheet-muscles.png))
    - [x] Create → Create Exercise ([p14](screenshots/pages/p14-create-exercise-form.png)), Exercise Type list ([p15](screenshots/pages/p15-exercise-type-list-tags.png))
    - [x] "i" → Exercise detail with pinned "Add exercise" ([t78](screenshots/pages/t78-exercise-detail-from-picker.png))
  - [x] Exercise block ([03](screenshots/light/03-log-workout.png), [d13](screenshots/dark/d13-log-workout.png))
    - [x] Exercise name → Exercise detail
    - [x] Rest Timer → Wheel picker sheet ([p18](screenshots/pages/p18-rest-timer-wheel-picker.png))
    - [x] "⇔ KG" header → Weight Input explainer sheet ([t79](screenshots/pages/t79-weight-input-explainer-sheet.png))
    - [x] Set number → Set type sheet ([p16](screenshots/pages/p16-set-type-sheet.png), [p17](screenshots/pages/p17-set-types-in-table.png))
    - [x] Weight / reps input focus ([16](screenshots/light/16-keyboard-input.png), [d14](screenshots/dark/d14-sets-completed-timer-focus.png))
    - [x] Tick set → Completed row + Rest timer bar ([15](screenshots/light/15-sets-completed-rest-timer.png))
    - [x] "..." → Exercise menu sheet ([p19](screenshots/pages/p19-exercise-menu-sheet.png))
      - [x] Reorder Exercises ([t80](screenshots/pages/t80-reorder-exercises.png))
      - [x] Replace Exercise [same as Exercise picker]
      - [x] Add To Superset → Superset sheet, empty state ([t81](screenshots/pages/t81-superset-sheet-empty.png))
      - [x] Remove Exercise (removes immediately, no confirmation)
    - [x] Add Set (adds a row in place)
    - [action] Notes field
- [x] Profile tab ([11](screenshots/light/11-profile.png), [d07](screenshots/dark/d07-profile.png))
  - [x] Edit (pencil) → Edit Profile ([p27](screenshots/pages/p27-edit-profile-form.png), private values blurred)
    - [action] Done, Change Picture, field edits
  - [x] Share → iOS share sheet [same, contacts not captured]
  - [x] Settings (gear) → Settings, below
  - [x] Workouts count → scrolls to your workouts feed
  - [x] Followers ([t85](screenshots/pages/t85-followers-list.png), [t86 bottom](screenshots/pages/t86-followers-bottom-follow-states.png)): Contacts synced row, Following/Follow buttons
    - [x] See → Contacts empty state [same as t25]
    - [action] Follow, Following (unfollow), remove (x)
    - [x] Row → Other user profile [same]
  - [x] Following ([t87](screenshots/pages/t87-following-list.png)): same layout
  - [x] "Last 3 months" → Period sheet with Pro-locked options [same]
  - [x] Duration / Volume / Reps chips
  - [x] Your workouts feed [infinite]
    - [x] Post with inline comment preview and "Add a comment" ([t88](screenshots/pages/t88-own-post-inline-comment.png))
    - [x] Comments with a real comment and Reply ([t89](screenshots/pages/t89-comments-with-reply.png))
      - [action] Reply, like comment, comment field
    - [x] "..." → Own post menu ([t90](screenshots/pages/t90-own-post-feed-menu.png))
      - [x] Share Workout → Workout share composer ([t91](screenshots/pages/t91-share-workout-template-1.png))
        - [x] Send to → sheet with ChatGPT, Claude ([t92](screenshots/pages/t92-share-send-to-sheet.png)); both [external]
        - [x] Workout Link → Toast "Link Copied" ([t93](screenshots/pages/t93-toast-link-copied.png))
        - [x] Background [same as t63]
        - [external] Stories, More
        - [action] Download
        - [blocked] Templates 2 to 8 (swipe only, iPhone Mirroring can't swipe)
      - [action] Save as Routine, Copy Workout, Delete Workout
      - [x] Edit Workout [same as Edit Workout form]
  - [x] Statistics ([d08](screenshots/dark/d08-statistics.png), [t94 bottom](screenshots/pages/t94-statistics-bottom.png))
    - [x] "?" → Info dialog without title ([t104](screenshots/pages/t104-info-dialog-no-title.png))
    - [x] Body graph → Body distribution [same as below]
    - [x] Set count per muscle group (PRO) → Contextual paywall "Advanced Statistics" ([t95](screenshots/pages/t95-paywall-advanced-stats.png))
    - [x] Muscle distribution (Chart) ([d09](screenshots/dark/d09-muscle-distribution-chart.png))
    - [x] Muscle distribution (Body) ([t96](screenshots/pages/t96-body-distribution.png), [t97 bottom](screenshots/pages/t97-body-distribution-bottom.png)): week switcher, muscle table
    - [x] Main exercises: period dropdown, "No data yet" ([t99](screenshots/pages/t99-main-exercises-empty.png)). Hevy crashed once on opening this, then loaded on retry.
    - [x] Leaderboard Exercises ([t100](screenshots/pages/t100-leaderboard-exercises.png)) → Exercise leaderboard [same]
    - [x] Monthly Report ([t101 top](screenshots/pages/t101-monthly-report-top.png), [t102 bottom](screenshots/pages/t102-monthly-report-bottom.png)): 12-month bar chart, chips, summary grid, calendar, radar
      - [x] Share → Monthly share card ([t103](screenshots/pages/t103-share-card-monthly.png))
  - [x] Exercises ([p26](screenshots/pages/p26-exercise-library.png)) [same as Exercise picker layout]
  - [x] Measures ([p25](screenshots/pages/p25-measurements.png))
    - [x] "+" → Log Measurements form ([t111](screenshots/pages/t111-log-measurements-form.png), [t112 bottom](screenshots/pages/t112-log-measurements-bottom-locked.png)), Pro-locked fields
      - [x] Locked field → Upsell bottom sheet ([t113](screenshots/pages/t113-upsell-bottom-sheet.png))
      - [external] Add Picture (iOS photo picker)
      - [action] Save
    - [x] History row → same Log Measurements form, prefilled
  - [x] Calendar ([p24](screenshots/pages/p24-calendar-month.png), [t110 workout days](screenshots/pages/t110-calendar-month-workout-days.png))
    - [x] Month ▾ → View sheet ([t105](screenshots/pages/t105-calendar-view-sheet.png))
      - [x] Year heatmap ([t106](screenshots/pages/t106-calendar-year-heatmap.png))
      - [x] Multi-year heatmap ([t107](screenshots/pages/t107-calendar-multiyear-heatmap.png))
    - [x] Filter icon → First Weekday ([t108](screenshots/pages/t108-first-weekday.png))
    - [x] Share → Calendar share card ([t109](screenshots/pages/t109-share-card-calendar.png))
    - [x] Streak / rest days pill → Info dialog [same]
    - [x] Workout day → Own workout detail [same]
- [x] Settings ([13](screenshots/light/13-settings.png), [d02 top](screenshots/dark/d02-settings-top.png), [d03 mid](screenshots/dark/d03-settings-mid.png), [t128 bottom](screenshots/pages/t128-settings-bottom-social-logout.png))
  - [x] Unlock → Generic paywall ([p28](screenshots/pages/p28-paywall.png))
    - [action] Plan cards, Subscribe
    - [x] Not now / close
  - [x] Account
    - [x] Profile [same as Edit Profile]
      - [x] Sex → single-choice sheet (not captured, shows your answer)
      - [x] Birthday → date wheel [same pattern]
      - [x] Private data "?" → Info dialog [same pattern]
    - [x] Account → Account Settings ([t114](screenshots/pages/t114-account-settings.png))
      - [x] Change Username ([t115](screenshots/pages/t115-change-username-form.png))
      - [x] Change Email ([t116](screenshots/pages/t116-change-email-form.png), email blurred)
      - [x] Update Password ([t117](screenshots/pages/t117-update-password-form.png))
      - [action] Update (all three), Delete Account
    - [x] Manage Subscription ([t118](screenshots/pages/t118-manage-subscription.png), [t119 bottom](screenshots/pages/t119-manage-subscription-bottom.png))
      - [x] More information → Generic paywall [same]
      - [action] Plan offer cards, Restore Purchases
      - [external] Privacy Policy, Terms & Conditions, Contact us (mail)
    - [x] Notifications ([d05](screenshots/dark/d05-notifications-switches.png), [t123 bottom](screenshots/pages/t123-notifications-bottom.png))
      - [action] Every switch
  - [x] Preferences
    - [x] Workouts → Workout Settings ([17](screenshots/light/17-workout-settings-toggles.png), [t122 bottom](screenshots/pages/t122-workout-settings-bottom.png))
      - [x] Sounds ([p30](screenshots/pages/p30-sounds-value-rows.png)), its value rows open single-choice lists [same pattern]
      - [x] Default Rest Timer → Wheel picker sheet [same as p18]
      - [x] First day of the week → First Weekday [same as t108]
      - [x] Previous Workout Values ([t120](screenshots/pages/t120-previous-values-choice.png))
      - [x] Warm-up Calculator (PRO) → Contextual paywall ([t121](screenshots/pages/t121-paywall-warmup-calculator.png))
      - [x] Warm-up Sets (one switch with helper text)
      - [action] Switches: Keep Awake, Plate Calculator, RPE Tracking, Smart Superset Scrolling, Inline Timer, Live PR Notification
    - [x] Privacy & Social ([d06](screenshots/dark/d06-privacy-switches-off.png))
      - [x] Default Workout Visibility ([t124](screenshots/pages/t124-default-visibility-page.png))
      - [action] Private Profile, Hide Suggested Users switches
    - [x] Units ([d04](screenshots/dark/d04-units-segmented.png))
    - [x] Language ([p29](screenshots/pages/p29-language-single-choice.png))
    - [x] Apple Health ([p31](screenshots/pages/p31-apple-health-connect.png))
      - [action] Connect
    - [x] Apple Watch [same as t76]
    - [x] Integrations ([p32](screenshots/pages/p32-integrations-connected-states.png))
      - [action] Connect, Disconnect
    - [x] Theme ([d01](screenshots/dark/d01-theme-setting.png))
    - [x] Export & Import Data
      - [x] Export Data ([t126](screenshots/pages/t126-export-data.png))
        - [action] Export Workouts, Export Measurements
      - [x] Import Data ([t125](screenshots/pages/t125-import-data.png))
        - [external] Import Strong CSV (Files picker)
  - [x] Guides
    - [x] Getting Started Guide ([p33](screenshots/pages/p33-guide-article.png))
    - [x] Routine Help ([t127](screenshots/pages/t127-routine-help-guide.png))
  - [x] Help
    - [x] Frequently Asked Questions ([p34](screenshots/pages/p34-faq-card-list.png))
      - [x] Article → Web view, loading ([t130](screenshots/pages/t130-faq-article-webview-loading.png)) then loaded ([t131](screenshots/pages/t131-faq-article-webview.png)); help-centre content, light theme
    - [external] Contact Us, Review Hevy on the App Store, Become an Affiliate, Careers
    - [x] About ([p35](screenshots/pages/p35-about.png))
      - [external] Instagram, Facebook, Twitter, email, Privacy Policy, Terms, Acknowledgements
  - [x] Hevy Coach → "What best describes you?" survey ([t129](screenshots/pages/t129-coach-survey.png))
    - [action] The three answers
  - [external] Follow us icons (Instagram, YouTube, TikTok, Facebook, Reddit, X)
  - [action] Logout

## Leaves that are not explored, and why

| Leaf | Reason |
|---|---|
| Every `[action]` | Pressing it changes your account, posts something, or saves data |
| Every `[external]` | Leaves Hevy |
| Trainer "Accept and Continue" | Accepting health terms needs your explicit OK |
| Connect with Contacts | Triggers the iOS contacts permission prompt |
| Share card templates 2 to 8, post image carousel page 2 | Swipe only. iPhone Mirroring can't send swipes. |
| Long-press menus (reorder routines, comment long-press) | iPhone Mirroring can't send long-presses |
| Software keyboard | iPhone Mirroring hides it |
| Network error state | Turning off the phone's connection would also cut Mirroring |

## Notes from the pass

- Hevy crashed once, on opening Statistics > Main exercises. It loaded fine on retry.
- The only real toast in the app so far is "Link Copied" ([t93](screenshots/pages/t93-toast-link-copied.png)). Copy Link on Invite Friends uses an alert instead.
- Loading states seen: spinner ([t24](screenshots/pages/t24-contacts-loading-spinner.png)), skeleton placeholders ([t98](screenshots/pages/t98-skeleton-loading-suggested.png)), web view spinner ([t130](screenshots/pages/t130-faq-article-webview-loading.png)).
- Validation errors seen: "Add an exercise" ([t75](screenshots/pages/t75-finish-validation-alert.png)), "Your workout has no set values" ([t82](screenshots/pages/t82-finish-no-set-values-alert.png)).
