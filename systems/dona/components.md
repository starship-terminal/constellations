# Components

Public marketing site only, signed out, 2026-11-21. Values are `getComputedStyle` or the styled-components theme object in [raw/readings.json](raw/readings.json).

| Component | Where | States captured | Notes |
|---|---|---|---|
| Text button, quiet | Header Login, Watch video | default | 36px header / 52px hero, radius 32px, fill `#eceff2`, text `#19191b`, weight 500 |
| Text button, primary | Try for free | default | 52px, fill `#008ffd`, text `#ffffff`, shadow `0 2px 4px rgba(12,20,66,.1), 0 10px 40px rgba(12,20,66,.06)` |
| Text button, ink | Join our newsletter | default | 52px, fill `#19191b`, text `#ffffff`. Not submitted. |
| Ghost button | Header About | default | transparent, 14px/500, padding 6px 20px |
| Link | Footer Terms, Privacy | default | ink, 16px |
| Icon link | Footer Twitter | default | 40px hit area. Not followed. |
| Text field | Newsletter email | empty | placeholder "Enter your email". Not typed. |
| Dialog | Watch video | open | scrim `rgba(191, 195, 200, 0.8)`, inner radius 11px, YouTube iframe. [home-light-video](screenshots/home-light-video.png) |
| Cookie bar | every page until Accept | visible, then hidden for shots | Accept not clicked |
| Login card | app.dona.ai/login | empty fields | login wall. Not submitted. |

Not present: text area, select, checkbox, radio, switch, tabs, menu, tooltip, toast, table, avatar, badge, live list row.

Hover, focus-visible, pressed, disabled, loading, and error were not captured as crops.
