# Component readings

Computed 2026-11-19. Viewport of the reading tab: 1169×731, devicePixelRatio 2.

| Control | Page | Background | Text | Radius | Height | Padding | Border |
|---|---|---|---|---|---|---|---|
| Join (Button_color-shadow) | / | rgb(25, 25, 25) | rgb(255, 255, 255) | 12px | 48px | 1px 20px | 1px solid rgb(25, 25, 25) |
| Load More (Button_color-white) | / | rgb(255, 255, 255) | rgb(0, 0, 0) | 12px | 48px | 1px 30px | 1px solid rgb(237, 237, 237) |
| Free download (Button_color-alien) | /photo/4057078 | rgb(84, 202, 132) | rgb(255, 255, 255) | 12px 0 0 12px | 48px | 0 20px 0 24px | 1px solid rgb(84, 202, 132) |
| Log in submit (alien) | /login/ | rgb(84, 202, 132) | rgb(255, 255, 255) | 12px | 48px | 1px 30px | 1px solid rgb(84, 202, 132) |
| Google button | /join/ | rgb(255, 255, 255) | rgb(101, 111, 107) | 12px | 48px | 1px 6px | 1px solid rgb(237, 237, 237) |
| Tab active (Home) | / | rgb(0, 0, 0) | rgb(255, 255, 255) | 30px | 48px | 0 20px | none |
| Tab inactive | / | transparent | rgb(57, 57, 57) | 30px | 48px | 0 20px | none |
| Search container | / | rgb(247, 247, 247) | rgb(0, 0, 0) | 12px | 72px | 12px | none |
| Search input | / | transparent | rgb(0, 0, 0) | 0 | 48px | 1px 2px | none |
| Text field (join) | /join/ | rgb(255, 255, 255) | rgb(57, 57, 57) | 10px | 48px | 4px 16px | none, border-color rgb(57, 57, 57) |
| Search term pill | /search/nature/ | transparent | link blue | 180px | 48px | 8px 8px 8px 5px | 1px solid rgb(237, 237, 237) |
| Media card | / | transparent | | 12px | 425 | 0 | none |
| Cookie Reject All | / | rgb(25, 25, 25) | rgb(255, 255, 255) | 12px | 40px | 8px 30px | 1px solid |
| Continue without Accepting | / | transparent | rgb(74, 74, 74) | 2px | 17px | 0 | none |

Button transition, computed on a Button_button: background-color 0.1s, border ease-in-out, transform 0.1s, box-shadow 0.005s, border-color 0.25s.

Declared hover and focus, not forced live:

- Button_color-shadow :hover and :focus-visible background is var(--color-greyscale-900) (#393939).
- Button_color-alien :focus-visible background is var(--color-alien-dark) (#32ac64).
- Disabled shadow button background is var(--color-greyscale-600) (#cdcdcd).
- Navbar focus-visible outline is 2px solid var(--color-greyscale-300).
- clickable:focus-visible sets outline none and a 4% black wash.

Reduced motion, declared: shimmer text animation is removed, and BottomSheet backdrop and panel transition-duration is 0.01ms. The live page's matchMedia('(prefers-reduced-motion: reduce)') was false. A full motion-probe pass was not run.
