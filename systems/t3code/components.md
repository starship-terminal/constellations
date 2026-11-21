# Components

Measured from the hosted app on 22 Nov 2026. Crops were not cut. The screenshots in [screenshots/](screenshots) are the evidence.

| Component | Where | States |
|---|---|---|
| Icon button | Sidebar and top bar, 28 px, radius 8 px | Default. Hover not held |
| Footer button | Sidebar footer, 32 px | Default |
| Thread row | Sidebar, 12 px title, monogram | Default, settled |
| Switch | Settings rows | On and off in [screenshots/settings-general-dark.png](screenshots/settings-general-dark.png) |
| Select | Project order, model picker | Closed and open |
| Composer | Centred, max about 736 px | Empty and in a thread |
| Menu | Thread actions, slash commands | Open |
| Dialog | Settings, add project, Add Environment | Open. Remote link and SSH tabs in [screenshots/macos-add-environment-link-dark.png](screenshots/macos-add-environment-link-dark.png) and [screenshots/macos-add-environment-ssh-dark.png](screenshots/macos-add-environment-ssh-dark.png) |
| Project palette | New thread, Mac app | Open, scrolled to remote rows. [screenshots/macos-project-picker-dark.png](screenshots/macos-project-picker-dark.png) |
| Environment row | Settings, Environments, Mac app | Connected remote, plus a discovered machine that was not added. [screenshots/macos-settings-environments-dark.png](screenshots/macos-settings-environments-dark.png) |
| Details card | Top right of the thread | Open |

Checkbox, radio, tabs, toast, and table were not present on the pages visited. Tooltip triggers exist. The tooltip itself did not paint in the DOM capture.

## Gaps

- No element crops.
- Hover, focus-visible, pressed, and disabled were not held.
- Light theme has the draft, the thread, and Appearance only.
- General dropdowns were not opened.
- The web Environments page is the empty state. The connected list and Add Environment dialog are Mac-app pixels only.
- The project palette was not captured at the top of the list in the 2x shot. The scrolled shot is the one that shows Local beside `kai-home-server`.
