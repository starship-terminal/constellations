# Excalidraw site tree

Mapped 2026-11-21 in the T3 preview, default profile, on the signed-in Google account. The walk started at https://excalidraw.com/, then followed the welcome link to https://app.excalidraw.com/. Private account strings were replaced in the page before each saved shot. The preview stopped producing screenshot frames on Connected apps, so pages after the API keys shot were read as text only, or not opened.

## excalidraw.com (signed-out editor, session already present)

The public editor is the existing package. This pass only recorded which control leaves it.

| Control | Opens |
|---|---|
| Welcome link "Excalidraw+" | https://app.excalidraw.com/?utm_source=excalidraw&utm_medium=app&utm_content=welcomeScreenSignedInUser. With this session it lands on `/no-workspace`. |
| Welcome "Open" | Local file picker. Not opened. |
| Welcome "Help" | Help dialog. Already in the signed-out package. Not reopened. |
| Welcome "Live collaboration..." | Collaboration dialog. Not opened (starts a session). |
| Hamburger | Main menu, same page. |
| Menu "Open" | Local file picker. Not opened. |
| Menu "Save to..." | Save dialog. Not opened. |
| Menu "Export image..." | Export dialog. Already in the signed-out package. |
| Menu "Live collaboration..." | Collaboration dialog. Not opened. |
| Menu "Command palette" | Command palette. Already captured signed out. |
| Menu "Find on canvas" | Find field. Already captured signed out. |
| Menu "Help" | Help dialog. |
| Menu "Reset the canvas" | Clears the canvas. Not pressed. |
| Menu "Excalidraw+" | https://plus.excalidraw.com/plus (marketing). Not followed. |
| Menu "GitHub" | https://github.com/excalidraw/excalidraw. External. |
| Menu "X / Follow us" | https://x.com/excalidraw. External. |
| Menu "Discord" | https://discord.gg/UexuTaE. External. |
| Menu "Sign in" | https://app.excalidraw.com/?utm_source=signin&utm_medium=app&utm_content=hamburger. Not followed. The welcome banner already said the session was signed in. |
| Menu "Preferences" | Preferences submenu, same menu. Not opened this pass. |
| Theme radios | Light, Dark, System. Light was checked. Not changed (account theme lives on the plus app). |
| Language select | In-menu language list. Not changed. |
| Canvas background | Colour picker. Not opened. |
| Shape tools, More tools, Library, Zoom, Minimap, Undo, Redo, Help | Editor chrome. Already in the signed-out package. |

## app.excalidraw.com (signed in, no workspace)

`/` redirects to `/no-workspace` when the account has no workspace. Version read from the account menu: `cde80604b`.

| Control | Opens |
|---|---|
| Logo | `/` (back to this empty state). |
| Account menu | Dropdown on the same page. |
| Account menu "New workspace" | Create-workspace flow. Not opened. Creating a workspace was not in scope. |
| Account menu "My profile" | `/account/my-profile` |
| Account menu "Preferences" | `/account/preferences` |
| Account menu "Personal MCP/API keys" | `/account/api-keys` |
| Account menu "Connected apps" | `/account/connected-apps` |
| Account menu "Discord" | External Discord. Not followed. |
| Account menu "YouTube" | External YouTube. Not followed. |
| Account menu "Support" | Support link. Not followed. |
| Theme radios | Light, Dark, System. System was checked. Not changed. |
| Language | Language submenu. Not opened. |
| Sign out | Ends the session. Not pressed. |
| Card "Create workspace" | `/workspace/create/name`. Not opened. |
| Card "User settings" | `/account/my-profile` |
| "excalidraw.com" | Public editor. |
| "support@excalidraw.com" | Copies the support address. Not pressed. |
| "Get help on Discord" | https://discord.gg/e5nJxZBZxz. External. |
| "Report issue on GitHub" | https://github.com/excalidraw/excalidraw. External. |

## Settings shell (`/account/*`)

Left nav, same on every settings page:

| Nav item | URL |
|---|---|
| Logo / account row | `/` |
| My profile | `/account/my-profile` |
| Preferences | `/account/preferences` |
| Personal MCP/API keys | `/account/api-keys` |
| Connected apps | `/account/connected-apps` |
| Export private collection | `/account/export` |
| My workspaces | `/account/my-workspaces` |
| Sign out | `/sign-out` (not followed) |
| Search settings | Filters the settings list. Not submitted. |
| ESC | Closes settings back to the app. |

### My profile (`/account/my-profile`)

| Control | What it does |
|---|---|
| Change (picture) | Upload dialog. Not opened. |
| Edit (name) | Name field. Left blank. |
| Connect provider | Provider picker. Not opened (would start OAuth). |
| GitHub chip | Linked provider, already connected. Not changed. |
| Turn on (two-factor) | Authenticator setup. Not opened. |
| Sign out | Ends this session. Not pressed. |
| Sign out all sessions | Ends every session. Not pressed. |
| Delete account | Destructive confirmation. Not pressed. |

### Preferences (`/account/preferences`)

| Control | What it shows |
|---|---|
| App theme | System, shortcut Option Shift D. Not changed. |
| Language | English. Not changed. |
| Initial app page | Dashboard. Not changed. |
| Auto-redirect from excalidraw.com | Switch, off. Not toggled. |
| Email notifications | Switch, on. Not toggled. |
| Show old fonts | Switch, off. Not toggled. |
| Open audio settings | Device picker. Not opened (would request microphone). |
| Push to talk | Switch, off. Not toggled. |

### Personal MCP/API keys (`/account/api-keys`)

Beta notice. "Learn more" goes to https://plus.excalidraw.com/docs/mcp/mcp-api-key-types. Not followed. A warning says a workspace admin must enable personal keys. No key was created. No key value was on the page.

### Connected apps (`/account/connected-apps`)

Text only, after frames died: "AI apps like ChatGPT that you connected to a workspace." Empty state: "You haven't connected any apps." No screenshot.

### Not opened

Export private collection (`/account/export`), My workspaces (`/account/my-workspaces`), create workspace (`/workspace/create/name`), plus marketing (`plus.excalidraw.com`), and every external link. A workspace list, a scene, billing, and collaboration need a workspace this account does not have.
