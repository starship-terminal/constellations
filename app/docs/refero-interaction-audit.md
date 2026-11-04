# Refero interaction audit, 2026-11-04

This pass compares the signed-in original, the earlier standalone mockup, and the new app in real browsers. It covers distinct page templates and interaction states, with representative records for different media availability. It does not claim to have opened every record in the upstream catalog.

Excluded by the owner: authentication/accounts, pricing/upgrade flows, and MCP. Original logos and proprietary fonts remain reference material; Studio uses its own mark, Lucide, and the documented system sans/Georgia substitutes.

## Research and home

| Control or state       | Original observation                                                                               | Clone outcome                                                                                                                         |
| ---------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Prompt category tabs   | Popular, Inspiration, Onboarding, Workflows replace the suggestions                                | Clicked tabs and suggestion; retained keyboard tab navigation                                                                         |
| Research tips          | Coach above composer, dismissible                                                                  | Dismiss/reopen checked                                                                                                                |
| Research/web/iOS modes | Separate research and app-search modes                                                             | Preserved; app searches use local captured data                                                                                       |
| Home below the fold    | Page Types, Flows, UX Patterns, UI Elements, Sites, each with chips and More navigation            | Added captured-screen browse rows and retained Sites. Rows explicitly search captured names/tags; no inferred labels or ordered flows |
| Saved research         | Search groups remain visible, card grids, query labels, See all and Show More; narrative follows   | Candidate results now render expanded, six initially, with Show more/less and source-aware destinations                               |
| Mixed-source results   | Separate original product surfaces                                                                 | Package and Styles destinations retained separately; a combined result cannot silently drop Styles                                    |
| Result inspection      | Click a result to inspect it, dismiss to return                                                    | Existing inspector retained with pin/exclude/save                                                                                     |
| Follow-up              | Compact fixed composer and suggested follow-up prompts                                             | Added prompt chips; stop/retry/export remain available                                                                                |
| History                | Conversation navigation in left rail                                                               | Fixed hidden older history and added restore access for archived conversations                                                        |
| Submit motion          | Captured eight sequential transition frames (295–442ms per screenshot) before upstream daily limit | Existing streamed state/stop/error path preserved; result insertion uses reduced-motion-aware transition                              |

The original returned its daily research limit during the new prompt test. No upgrade or further model requests were made there. Existing history supplied the completed-response reference. Frame capture is a timing sample, not a high-frame-rate recording.

## Catalog, Styles, and collections

See the companion live-audit records for exact clicked controls, evidence, and implemented behavior. Individual screenshot search uses the recorded package media inventory, not the style snapshot. Styles retain the canonical 1,342-record snapshot and its separate document/video data.

## Data-backed limits

- The local corpus has no upstream popularity/trending rankings. The app exposes actual name and capture-date sorting, not invented scores.
- The local corpus does not provide Refero's full screen taxonomy or ordered flow memberships. Filename/tag searches are labelled as searches; independently captured images are not presented as an ordered flow.
- Current original catalog counts and records differ from the older local snapshot. This UI work does not refresh or overwrite captured evidence.
- New AI completion parity requires a configured model; the app's missing-provider state preserves the user's prompt and supports retry.

## Evidence

Browser screenshots and transition frames are stored outside the repository under the session's `full-audit/` directory, split into `styles/`, `catalog/`, and `research/`. The private captured token package `systems/refero-design` supplies semantic palette, radii, and motion values; the app's existing accessibility adjustments remain in place.

## Final validation

The production build passed. All 108 application tests, TypeScript, formatting, `make check`, and `make test` passed. A separate temporary database and production server rendered an explicitly labelled research fixture with real library records; Show more/less (six/eight cards), follow-up selection, pinning, inspection, and archive/restore passed without modifying personal research history. At 1280px the original research grid measured two 399px columns with a 36px gap; the final clone measured two 398px columns with the same gap.

Screenshots-to-boards now have a versioned personal-database migration, independent of package associations and flat bookmarks. API tests cover identity validation, collection isolation, persistence, and export links. Existing user board contents and test bookmarks were restored after live checks.
