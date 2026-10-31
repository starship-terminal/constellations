# Live capture procedure

Use the owner-selected visible Codex in-app browser. The owner signs in. Open existing organization/project pages; never resume a project or run SQL without separate authority. Open one popup at a time, wait until visibly settled, and save a viewport screenshot plus computed styles from the same state.

The capture used read-only `tab.playwright.evaluate`: `getComputedStyle` on body and visible buttons, anchors, inputs, headings, comboboxes, dialogs and menus; record colour, background, border, radius, font family/size/weight/line-height, padding, gap, shadow, dimensions and transitions. Store tag, role, label, disabled/expanded attributes and bounding rectangle. Custom-property enumeration is partial; do not call it complete. Record innerWidth, innerHeight, devicePixelRatio, visualViewport, timestamp, safe URL and theme classes. Raw unfiltered outputs stay outside Git.

Read screenshot format from decoded bytes, not the filename. Convert accepted JPEG screenshots to PNG and quantize with Pillow. Full-page attempts with missing lazy content or shifted fixed navigation are rejected. Review every screenshot, then select crop coordinates from native PNGs and put them in crops.json. Never use DPR alone to compute crop boxes.

Original scratch root: ~/.design-systems/supabase. No raw DOM, cookies or proprietary fonts were stored in this package. Owner profile is permitted. Scan all text and images using the current repository policy before committing.

Light appearance was authorized, captured on desktop/mobile project lists and the status filter, then restored to System. app-restored-system-theme is verification. Reset temporary viewport overrides afterwards.
