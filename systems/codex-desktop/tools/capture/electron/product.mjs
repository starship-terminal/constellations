// PRODUCT (adapt): everything in this file is Codex 26.1013's (the Codex desktop app for macOS, OpenAI;
// the installed bundle is `Codex 2.app`, a second-account copy of ChatGPT.app's Electron build).
// Another Electron app replaces it whole and keeps cdp.mjs, vars.mjs, utilities.mjs, shots.mjs and run.mjs.
//
// A shot is { name, window, state?, reveal(h), parts, force?, hover?, focus?, after?(h), optional?, optionalParts? }:
//   name    screenshot file name, `{page}-{state}` (the theme folder is added by shots.mjs)
//   window  a key of WINDOWS
//   reveal  async ({ page, cdp, ...helpers }) => {} : clicks, keys and hovers that show the state.
//           Look, don't act: open and close, type and clear, never submit or send.
//   parts   { component: selector | [selector, nth] | (page) => Locator }: each is measured
//           (computed style) and its box recorded for crops, as `{component}-{state}`
//   force   { component: ['hover' | 'focus' | 'focus-visible' | 'active'] }: pseudo-classes forced through CDP
//   after   async (h) => {} : undo what reveal did (clear typed text, close a menu)
//
// Codex is one window: a navigation rail, a sidebar (Projects, Recents), the main pane (the new-chat
// composer, a chat, or a page such as Plugins or Settings) and an optional right panel of tabs (browser,
// files, terminal). It is React with Tailwind CSS 4 and OpenAI's own component kit (CSS-module classes such
// as _Button_eg66f_2 with data-variant, data-color and data-size). Three CDP pages share the title
// "ChatGPT" (the main window, the avatar overlay and a detached window), so the window is picked by URL.
// The capture works only in the project it created, design-capture, on the empty folder
// ~/.design-systems/harness-scratch/codex; it never opens the owner's chats, projects or environments.

export const NAME = 'Codex';
export const WINDOWS = { main: { url: /^app:\/\/-\/index\.html$/ } };
// Scopes vars.mjs resolves custom properties on, besides html and body.
export const SCOPES = { main: ['html'] };
export const PROJECT = 'design-capture';

// ---- navigation helpers (selectors are Codex's own data attributes, roles and aria-labels, never account text)
const wait = (page, ms = 600) => page.waitForTimeout(ms);
// A shot that clicks a Delete control only to show its confirmation must see that confirmation before it goes
// on. If none opens, the click may have deleted something: the whole capture stops (shots.mjs reads `abort`).
async function confirmOpened(page, what) {
  const dialog = page.locator('[role=alertdialog], [role=dialog]').filter({ visible: true }).filter({ has: page.locator('button', { hasText: /^Cancel$/ }) });
  if (await dialog.last().waitFor({ state: 'visible', timeout: 3000 }).then(() => true, () => false)) return;
  throw Object.assign(new Error(`no confirmation dialog after ${what}: check that nothing was deleted`), { abort: true });
}
const vis = (page, sel) => page.locator(sel).filter({ visible: true }).first();
const OPEN = '[role=menu]:visible, [role=dialog]:visible, [role=listbox]:visible, [data-composer-overlay-floating-ui]:visible';
export async function closeAll(page) {
  for (let i = 0; i < 4 && await page.locator(OPEN).first().isVisible().catch(() => false); i++) {
    await page.keyboard.press('Escape'); await wait(page, 300);
  }
}
const rail = dest => `nav[data-app-navigation-rail] button[data-sidebar-destination="builtin:${dest}"]`;
const SIDEBAR = 'nav[aria-label=Home]';
const editor = '[data-codex-composer=true]';
const composerText = page => page.locator(editor).filter({ visible: true }).first().evaluate(e => e.innerText.replace(/​/g, '').trim()).catch(() => '');
async function clearComposer(page) {
  await closeAll(page);
  for (let i = 0; i < 5 && await composerText(page); i++) {
    await page.locator(editor).filter({ visible: true }).first().click();
    await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); await wait(page, 400);
  }
  if (await composerText(page)) throw new Error('composer could not be emptied');
}
// Toggles a click can flip (the activity view, the tab strip): put them back as they were.
async function untoggle(page) {
  const act = page.locator(`${SIDEBAR} button[aria-pressed=true]`).filter({ hasText: '' });
  for (const b of await act.all()) if (/activity/i.test(await b.getAttribute('aria-label') || '')) { await b.click(); await wait(page, 600); }
  const tabs = page.locator('button[data-app-shell-workspace-layout-toggle=main][aria-pressed=true]');
  if (await tabs.count()) { await tabs.first().click(); await wait(page, 800); }
}
// The empty new-chat page of the capture's project: rail Home, settings closed, sidebar shown.
export async function home({ page }) {
  await closeAll(page);
  await page.locator(rail('home')).click(); await wait(page, 1000);
  await untoggle(page);
  if (await vis(page, 'button[aria-label="Show sidebar"]').isVisible().catch(() => false)) { await vis(page, 'button[aria-label="Show sidebar"]').click(); await wait(page, 700); }
  const chip = vis(page, 'button[aria-label^="Change project"]');
  if (!((await chip.getAttribute('aria-label').catch(() => '')) || '').endsWith(PROJECT)) await selectProject(page);
  await page.mouse.move(1300, 300); await wait(page, 300);
}
async function selectProject(page) {
  await vis(page, 'button[aria-label^="Change project"]').click(); await wait(page, 700);
  await page.locator('[role=dialog] [role=option], [role=dialog] [role=listbox] > *').filter({ hasText: new RegExp(`^${PROJECT}$`) }).first().click(); await wait(page, 800);
}
export async function reset(h) { return home(h); }
async function settings({ page }, slug) {
  await closeAll(page);
  if (!(await page.locator('button[data-settings-panel-slug]').first().isVisible().catch(() => false))) {
    await page.locator('button[aria-label="Open profile menu"]').click(); await wait(page, 700);
    await page.getByRole('menuitem', { name: /Settings/ }).filter({ hasNotText: 'Workspace' }).click(); await wait(page, 1500);
  }
  if (slug) { const b = page.locator(`button[data-settings-panel-slug="${slug}"]`); await b.scrollIntoViewIfNeeded(); await b.click(); await wait(page, 1500); }
  await page.mouse.move(1300, 30);
}
async function scrollMain(page, dy) { await page.mouse.move(1100, 500); await page.mouse.wheel(0, dy); await wait(page, 900); }

// Codex's buttons style :hover and :active directly, and draw their own focus-visible ring, so no state needs help.
export async function prepareState() {}

// A fingerprint of what a capture must never change: theme, model and effort, permissions, the
// activity and tab toggles, the sidebar's projects and chats, and the composer's draft.
export async function guard(h) {
  const { page } = h;
  await home(h);
  return JSON.stringify(await page.evaluate(sel => {
    const q = s => document.querySelector(s);
    return {
      theme: document.documentElement.dataset.theme,
      model: q('button[data-codex-intelligence-trigger]')?.getAttribute('data-selected-reasoning-effort') + ' ' + (q('button[data-codex-intelligence-trigger]')?.textContent || ''),
      perms: q('button[aria-label="Change permissions"]')?.innerText.trim(),
      workIn: q('button[aria-label="Work in"]')?.innerText.trim(),
      activity: q('button[aria-label="View activity"]')?.getAttribute('aria-pressed') || 'false',
      tabs: q('button[data-app-shell-workspace-layout-toggle=main]')?.getAttribute('aria-label'),
      projects: [...document.querySelectorAll('[data-app-action-sidebar-project-label]')].map(e => e.getAttribute('data-app-action-sidebar-project-label')).join('/'),
      pinned: [...document.querySelectorAll('[data-app-action-sidebar-thread-pinned=true]')].length,
      draft: (q(sel)?.innerText || '').replace(/​/g, '').trim(),
    };
  }, editor));
}

// The theme is Codex's own setting (Settings > Appearance > Mode: System, Light or Dark); System follows
// Electron's native theme, not an emulated prefers-color-scheme. Returns the label it replaced.
export const THEME_LABELS = { light: 'Light', dark: 'Dark', system: 'System' };
export async function setTheme(h, label) {
  const { page } = h;
  await settings(h, 'appearance');
  const radios = page.locator('[role=radiogroup][aria-label=Theme] input');
  const before = await radios.evaluateAll(es => es.find(e => e.checked)?.getAttribute('aria-label'));
  if (before !== label) { await page.locator(`[role=radiogroup][aria-label=Theme] label:has(input[aria-label="${label}"])`).click(); await wait(page, 2000); }
  await home(h);
  return before;
}

// ---- the shot list
const M = 'main';
const nth = (sel, i) => [sel, i];
const S = {
  rail: 'nav[data-app-navigation-rail]',
  railSelected: `nav[data-app-navigation-rail] button[aria-current=page]`,
  railButton: rail('automations'),
  sidebar: SIDEBAR,
  modeButton: 'button[aria-label^="Switch mode"]',
  iconButton: `${SIDEBAR} button[aria-label="Search"]`,
  activity: `${SIDEBAR} button[aria-label="View activity"]`,
  newChat: page => page.locator(`${SIDEBAR} button`).filter({ hasText: /^New chat$/ }).first(),
  sectionTitle: page => page.locator('[data-app-action-sidebar-section-toggle]').filter({ hasText: 'Projects' }).first(),
  projectRow: '[data-app-action-sidebar-project-row][data-app-action-sidebar-project-label="downloads"]',
  projectRowSelected: `[data-app-action-sidebar-project-row][data-app-action-sidebar-project-label="${PROJECT}"]`,
  threadRow: '[data-app-action-sidebar-thread-id][data-app-action-sidebar-thread-active=false]',
  // The composer's layout root paints nothing; its body is the visible box.
  composer: '[data-composer-surface-variant] [data-composer-body]',
  editor,
  utilityBar: '[data-composer-utility-bar-scroll-area]',
  projectChip: 'button[aria-label^="Change project"]',
  workIn: 'button[aria-label="Work in"]',
  add: 'button[aria-label="Add files and more"]',
  perms: 'button[aria-label="Change permissions"]',
  hooks: 'button[aria-label="Review hooks"]',
  model: 'button[data-codex-intelligence-trigger]',
  dictate: 'button[aria-label="Dictate"]',
  voice: 'button[aria-label="Start new voice chat"]',
  homeIcon: '[data-testid=home-icon]',
  homeHeading: page => page.getByText(/^What should we work on/).filter({ visible: true }).first(),
  profile: 'button[aria-label="Open profile menu"]',
  update: 'button[aria-label="Update available"]',
  hideSidebar: 'button[aria-label="Hide sidebar"]',
  menu: '[role=menu]',
  tooltip: '[role=tooltip]',
  popover: '[data-radix-popper-content-wrapper] [role=dialog]',
  // settings
  settingsNav: page => page.locator('button[data-settings-panel-slug=import]').first(),
  settingsNavSelected: 'button[data-settings-panel-slug][aria-current=page]',
  settingsSearch: '[data-sidebar-header-search]',
  settingsSearchInput: '#settings-search',
  pageTitle: 'main h1',
  sectionHeading: page => page.locator('main h2, main h3, main [role=heading]').filter({ visible: true }).first().or(page.locator('main').getByText('Permissions', { exact: true })).first(),
  settingsRow: page => page.locator('main div[class*="@container/settings-row"]').filter({ visible: true }).nth(1),
  settingsCard: page => page.locator('main div[class*="@container/settings-row"]').filter({ visible: true }).first().locator('xpath=..'),
  switchOn: 'main button[role=switch][aria-checked=true]:not([disabled])',
  switchOff: 'main button[role=switch][aria-checked=false]:not([disabled])',
  switchDisabled: 'main button[role=switch][disabled]',
  select: page => page.locator('main div[class*="@container/settings-row"] button[aria-haspopup=menu]').filter({ visible: true }).first(),
  buttonSecondary: page => page.locator('main div[class*="@container/settings-row"] button').filter({ hasText: /^(Change|View|Manage|Review|Reset|Open System Settings)$/ }).filter({ visible: true }).first(),
};
const mainButton = re => page => page.locator('main button').filter({ hasText: re }).filter({ visible: true }).first();
const lastMenu = page => page.locator(S.menu).filter({ visible: true }).last();
const ROW = '[role=menuitem]:not([aria-disabled=true]), [role=menuitemradio], [role=menuitemcheckbox]';
const menuParts = { menu: lastMenu, 'menu-row': page => lastMenu(page).locator(ROW).filter({ visible: true }).first() };
const openMenu = sel => async ({ page }) => { await vis(page, sel).click(); await wait(page, 900); };
const typed = async ({ page }) => { await clearComposer(page); await page.locator(editor).filter({ visible: true }).first().click(); await wait(page, 300); await page.keyboard.type('Draft text, never sent'); await wait(page, 500); };
const openSearch = async ({ page }) => { await vis(page, S.iconButton).click(); await wait(page, 1000); };
const palette = '[role=dialog]:has([role=listbox])';
// The palette dialog is a transparent shell; cmdk's root inside it is the visible box.
const paletteBox = `${palette} [cmdk-root]`;
const goRail = dest => async ({ page }) => { await page.locator(rail(dest)).click(); await wait(page, 2200); await page.mouse.move(1300, 30); };
// The composer's add menu and other composer overlays float in a [data-composer-overlay-floating-ui] shell.
const overlay = '[data-composer-overlay-floating-ui]';
const projectActions = async ({ page }) => {
  await page.locator(S.projectRowSelected).hover(); await wait(page, 400);
  await page.locator(`button[aria-label="Project actions for ${PROJECT}"]`).click({ force: true }); await wait(page, 900);
};

// One shot per part and state: `{page}-{part}-{state}`, measured as `{part}-{state}`.
function states(groups) {
  const out = [];
  for (const [pageName, window, reveal, parts, kinds] of groups)
    for (const [part, spec] of Object.entries(parts))
      for (const kind of kinds)
        out.push({ name: `${pageName}-${part}-${kind}`, window, state: kind, reveal, parts: { [part]: spec },
          ...(kind === 'hover' ? { hover: part } : kind === 'focus-visible' ? { focus: part } : { force: { [part]: ['hover', 'active'] }, hover: part }) });
  return out;
}

const SETTINGS_PANES = ['general-settings', 'import', 'profile', 'appearance', 'account', 'archived-chats', 'voice', 'storage', 'agent', 'personalization',
  'pets', 'keyboard-shortcuts', 'usage', 'data-controls', 'plugins-settings', 'passwords', 'computer-use', 'appshots', 'browser-use', 'cloud-computer',
  'hooks-settings', 'connections', 'codex-cloud', 'code-review', 'git-settings', 'worktrees'];

export const SHOTS = [
  { name: 'home-default', window: M, reveal: async () => {},
    parts: { rail: S.rail, 'rail-button-selected': S.railSelected, 'rail-button': S.railButton, sidebar: S.sidebar, 'mode-button': S.modeButton,
      'icon-button': S.iconButton, 'new-chat-row': S.newChat, 'section-title': S.sectionTitle, 'project-row': S.projectRow,
      'project-row-selected': S.projectRowSelected, 'thread-row': S.threadRow, composer: S.composer, 'composer-editor': S.editor,
      'utility-bar': S.utilityBar, 'project-chip': S.projectChip, 'work-in-chip': S.workIn, 'composer-tool': S.add, 'permissions-button': S.perms,
      'hooks-button': S.hooks, 'model-button': S.model, 'dictate-button': S.dictate, 'voice-button': S.voice, 'home-icon': S.homeIcon,
      'home-heading': S.homeHeading, avatar: S.profile, 'update-button': S.update, 'sidebar-toggle': S.hideSidebar },
    optionalParts: ['update-button', 'hooks-button'] },
  { name: 'home-composer-typed', state: 'filled', window: M, reveal: typed,
    parts: { composer: S.composer, 'composer-editor': S.editor, 'send-button': page => page.locator(`${S.composer} button[type=submit], ${S.composer} button[aria-label*="Send" i]`).filter({ visible: true }).first() },
    optionalParts: ['send-button'], after: async ({ page }) => clearComposer(page) },
  { name: 'add-menu', window: M, reveal: openMenu(S.add),
    parts: { 'composer-menu': page => page.locator(`${overlay} div.overflow-hidden`).filter({ visible: true }).first(),
      'composer-menu-row': page => page.locator(`${overlay} button[data-list-navigation-item]`).filter({ visible: true }).nth(1),
      'composer-menu-row-active': page => page.locator(`${overlay} button[data-list-navigation-item]`).filter({ visible: true }).first() } },
  { name: 'permissions-menu', window: M, reveal: openMenu(S.perms), parts: menuParts },
  { name: 'model-menu', window: M, reveal: openMenu(S.model), parts: { ...menuParts, slider: page => lastMenu(page).locator('[role=slider]').first() }, optionalParts: ['slider'] },
  { name: 'model-submenu', window: M, optional: true,
    reveal: async h => { await openMenu(S.model)(h); const t = lastMenu(h.page).locator('[aria-haspopup]').filter({ visible: true }).first(); await t.hover(); await wait(h.page, 1000); },
    parts: { submenu: lastMenu } },
  { name: 'work-in-menu', window: M, reveal: openMenu(S.workIn), parts: menuParts },
  { name: 'project-popover', window: M, reveal: openMenu(S.projectChip),
    parts: { popover: page => page.locator('[role=dialog]').filter({ visible: true }).last(), 'popover-search': page => page.locator('[role=dialog] input').filter({ visible: true }).last(),
      option: page => page.locator('[role=dialog] [role=listbox] [role=option]').filter({ visible: true }).nth(1) },
    optionalParts: ['option'] },
  { name: 'mode-menu', window: M, reveal: openMenu(S.modeButton), parts: menuParts },
  { name: 'profile-menu', window: M, reveal: openMenu(S.profile), parts: { ...menuParts, 'menu-separator': '[role=menu] [role=separator]' }, optionalParts: ['menu-separator'] },
  { name: 'profile-submenu', window: M,
    reveal: async h => { await openMenu(S.profile)(h); await h.page.getByRole('menuitem', { name: /^Help/ }).hover(); await wait(h.page, 1000); },
    parts: { submenu: lastMenu } },
  { name: 'explore-popover', window: M, reveal: openMenu('nav[data-app-navigation-rail] button[data-slot=popover-trigger]'),
    parts: { popover: page => page.locator('[role=dialog]').filter({ visible: true }).last() } },
  { name: 'project-actions-menu', window: M, reveal: projectActions, parts: { ...menuParts, 'menu-separator': '[role=menu] [role=separator]' }, optionalParts: ['menu-separator'] },
  { name: 'project-options-menu', window: M,
    reveal: async ({ page }) => { await S.sectionTitle(page).hover(); await wait(page, 300); await page.locator('button[aria-label="Project sidebar options"]').click({ force: true }); await wait(page, 900); },
    parts: menuParts },
  { name: 'project-options-submenu', window: M, optional: true,
    reveal: async ({ page }) => { await S.sectionTitle(page).hover(); await wait(page, 300); await page.locator('button[aria-label="Project sidebar options"]').click({ force: true }); await wait(page, 900);
      await lastMenu(page).locator('[aria-haspopup]').first().hover(); await wait(page, 1000); },
    parts: { submenu: lastMenu, 'menu-radio-row': page => lastMenu(page).locator('[role=menuitemradio], [role=menuitemcheckbox]').first() }, optionalParts: ['menu-radio-row'] },
  // Remove project on the capture's own project: the confirmation is opened and cancelled.
  { name: 'remove-project-dialog', window: M,
    reveal: async h => { await projectActions(h); await h.page.getByRole('menuitem', { name: 'Remove project' }).click(); await wait(h.page, 1000); },
    parts: { dialog: page => page.locator('[role=dialog], [role=alertdialog]').filter({ visible: true }).last(),
      'button-danger': page => page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Remove/ }).filter({ visible: true }).last(),
      'button-ghost': page => page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Cancel$/ }).filter({ visible: true }).last() },
    after: async ({ page }) => { await page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Cancel$/ }).last().click().catch(() => {}); await wait(page, 600); } },
  { name: 'create-project-dialog', window: M,
    reveal: async ({ page }) => { await S.sectionTitle(page).hover(); await wait(page, 300); await page.locator('button[aria-label="Add new project"]').click({ force: true }); await wait(page, 1200); },
    parts: { dialog: page => page.locator('[role=dialog]').filter({ visible: true }).last(), 'dialog-title': page => page.locator('[role=dialog] h2').filter({ visible: true }).last(),
      'text-field-focused': page => page.locator('[role=dialog] input').filter({ visible: true }).first().locator('xpath=..'),
      'button-primary': page => page.locator('[role=dialog]').getByRole('button', { name: 'Create project', exact: true }),
      'button-ghost': page => page.locator('[role=dialog]').getByRole('button', { name: 'Cancel', exact: true }),
      'dialog-close': page => page.locator('[role=dialog] button').filter({ hasText: 'Close dialog' }).filter({ visible: true }).last() },
    optionalParts: ['dialog-title', 'dialog-close'],
    after: async ({ page }) => { await page.locator('[role=dialog]').getByRole('button', { name: 'Cancel', exact: true }).click().catch(() => {}); await wait(page, 600); } },
  { name: 'hooks-dialog', window: M, reveal: openMenu(S.hooks),
    parts: { dialog: page => page.locator('[role=dialog]').filter({ visible: true }).last() }, optional: true },
  { name: 'search-palette', window: M, reveal: openSearch,
    parts: { palette: paletteBox, 'palette-input': `${palette} input`, 'palette-row-selected': `${palette} [role=option][aria-selected=true]`,
      'palette-row': nth(`${palette} [role=option][aria-selected=false]`, 0), 'palette-heading': page => page.locator(`${palette} [role=presentation], ${palette} [cmdk-group-heading]`).filter({ hasText: /^Chats$/ }).first(), kbd: page => page.locator(`${palette} kbd`).first() },
    optionalParts: ['palette-heading', 'kbd'] },
  { name: 'search-palette-empty', window: M, state: 'empty', reveal: async h => { await openSearch(h); await h.page.keyboard.type('zzqxv'); await wait(h.page, 1200); },
    parts: { palette: paletteBox } },
  { name: 'tooltip', window: M, state: 'hover', reveal: async ({ page }) => { await vis(page, S.iconButton).hover(); await wait(page, 1600); },
    parts: { tooltip: S.tooltip, 'icon-button': S.iconButton } },
  { name: 'sidebar-collapsed', window: M, reveal: async ({ page }) => { await vis(page, S.hideSidebar).click(); await wait(page, 1000); await page.mouse.move(1300, 300); },
    parts: { 'sidebar-toggle': 'button[aria-label="Show sidebar"]' },
    after: async ({ page }) => { await vis(page, 'button[aria-label="Show sidebar"]').click().catch(() => {}); await wait(page, 800); } },
  // Rail pages
  { name: 'space', window: M, reveal: goRail('space'), parts: {} },
  { name: 'scheduled', window: M, reveal: goRail('automations'), parts: { 'page-title': page => page.locator('main h1, main h2').filter({ visible: true }).first() }, optionalParts: ['page-title'] },
  { name: 'plugins', window: M, reveal: goRail('customize'),
    parts: { 'page-title': page => page.locator('main h1, main h2').filter({ visible: true }).first(), tab: page => page.locator('main [role=tab][aria-selected=false]').filter({ visible: true }).first(),
      'tab-selected': 'main [role=tab][aria-selected=true]', card: page => page.locator('main a, main [role=button], main button').filter({ has: page.locator('img') }).filter({ visible: true }).nth(1) },
    optionalParts: ['page-title', 'tab', 'tab-selected', 'card'] },
  { name: 'code-review', window: M, reveal: goRail('pull-requests'), parts: {} },
  // Settings, every pane
  ...SETTINGS_PANES.map(slug => ({ name: `settings-${slug}`, window: M, reveal: async h => settings(h, slug), parts: {}, optional: true })),
  { name: 'settings-general', window: M, reveal: async h => settings(h, 'general-settings'),
    parts: { 'settings-nav': S.settingsNav, 'settings-nav-selected': S.settingsNavSelected, 'settings-search': S.settingsSearch, 'page-title': S.pageTitle,
      'section-title': S.sectionHeading, 'settings-card': S.settingsCard, 'settings-row': S.settingsRow, 'switch-on': S.switchOn, 'switch-off': S.switchOff,
      'switch-disabled': S.switchDisabled, 'switch-track-on': `${S.switchOn} > span`, 'switch-track-off': `${S.switchOff} > span`, select: S.select, 'button-secondary': S.buttonSecondary, link: page => page.locator('main a').filter({ visible: true }).first() },
    optionalParts: ['switch-disabled', 'link'] },
  { name: 'settings-general-scrolled', window: M, reveal: async h => { await settings(h, 'general-settings'); await scrollMain(h.page, 900); }, parts: {} },
  // The default file open destination select is Codex's "open in" list of editors and terminals.
  { name: 'settings-open-in-menu', window: M,
    reveal: async h => { await settings(h, 'general-settings'); await S.select(h.page).click(); await wait(h.page, 900); },
    parts: { ...menuParts, 'menu-row-checked': page => lastMenu(page).locator('[role=menuitemradio][aria-checked=true], [role=menuitemcheckbox][aria-checked=true]').first() },
    optionalParts: ['menu-row-checked'] },
  { name: 'settings-appearance', window: M, reveal: async h => settings(h, 'appearance'),
    parts: { radio: '[role=radiogroup][aria-label=Theme] label:has(input:not(:checked))', 'radio-selected': '[role=radiogroup][aria-label=Theme] label:has(input:checked)',
      'radio-thumb': '[role=radiogroup][aria-label=Theme] label:has(input:not(:checked)) > span', 'radio-thumb-selected': '[role=radiogroup][aria-label=Theme] label:has(input:checked) > span',
      'color-field': page => page.locator('main input[type=text]').filter({ visible: true }).first().locator('xpath=..'),
      'theme-select': 'main button[aria-label$="code theme"]', 'text-button': mainButton(/^Reset to default$/) },
    optionalParts: ['color-field', 'text-button'] },
  { name: 'settings-theme-menu', window: M, reveal: async h => { await settings(h, 'appearance'); await vis(h.page, 'main button[aria-label$="code theme"]').click(); await wait(h.page, 1000); },
    parts: { popover: page => page.locator('[role=menu], [role=listbox], [role=dialog]').filter({ visible: true }).last() } },
  { name: 'settings-search', window: M, state: 'filled',
    reveal: async h => { await settings(h, 'general-settings'); await h.page.locator(S.settingsSearchInput).click(); await h.page.keyboard.type('theme'); await wait(h.page, 1200); },
    parts: { 'settings-search': S.settingsSearch },
    after: async ({ page }) => { await page.locator(S.settingsSearchInput).click().catch(() => {}); await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); } },
  { name: 'settings-shortcuts', window: M, reveal: async h => settings(h, 'keyboard-shortcuts'),
    parts: { kbd: page => page.locator('main kbd').filter({ visible: true }).first(), 'search-field': page => page.locator('main input').filter({ visible: true }).first().locator('xpath=..') },
    optionalParts: ['kbd', 'search-field'] },
  { name: 'settings-archived', window: M, reveal: async h => settings(h, 'archived-chats'),
    parts: { 'list-row': page => page.locator('main button').filter({ hasText: /^Unarchive$/ }).first().locator('xpath=../..'), 'button-secondary-sm': mainButton(/^Unarchive$/),
      'button-danger-text': page => page.locator('main').getByRole('button', { name: 'Delete all' }).first() },
    optionalParts: ['list-row', 'button-danger-text'] },
  // Delete all archived chats: the confirmation is opened and cancelled.
  { name: 'delete-archived-dialog', window: M, optional: true,
    reveal: async h => { await settings(h, 'archived-chats'); await h.page.locator('main').getByRole('button', { name: 'Delete all' }).first().click(); await confirmOpened(h.page, 'Delete all archived chats'); await wait(h.page, 1000); },
    parts: { dialog: page => page.locator('[role=dialog], [role=alertdialog]').filter({ visible: true }).last(),
      'button-danger': page => page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Delete/ }).filter({ visible: true }).last(),
      'button-ghost': page => page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Cancel$/ }).filter({ visible: true }).last() },
    after: async ({ page }) => { await page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Cancel$/ }).last().click().catch(() => {}); await wait(page, 600); } },
  { name: 'settings-usage', window: M, reveal: async h => settings(h, 'usage'),
    parts: { progress: page => page.locator('main [role=progressbar]').first() }, optionalParts: ['progress'] },

  // ---- states, one part per shot: hover with the real pointer, focus-visible with real keyboard focus,
  // pressed with :hover and :active forced through CDP over the part.
  ...states([
    ['home', M, async () => {}, { 'icon-button': S.iconButton, 'new-chat-row': S.newChat, 'project-row': S.projectRow, 'thread-row': S.threadRow,
      'rail-button': S.railButton, 'project-chip': S.projectChip, 'composer-tool': S.add, 'permissions-button': S.perms, 'model-button': S.model, 'voice-button': S.voice },
      ['hover', 'focus-visible', 'pressed']],
    ['settings', M, async h => settings(h, 'general-settings'), { 'settings-nav': S.settingsNav, 'switch-off': S.switchOff, select: S.select, 'button-secondary': S.buttonSecondary },
      ['hover', 'focus-visible', 'pressed']],
    ['settings', M, async h => settings(h, 'general-settings'), { 'settings-search-input': S.settingsSearchInput }, ['hover', 'focus-visible']],
    ['palette', M, openSearch, { 'palette-row': nth(`${palette} [role=option][aria-selected=false]`, 1) }, ['hover']],
    ['menu', M, openMenu(S.profile), { 'menu-row': page => lastMenu(page).locator(ROW).filter({ visible: true }).nth(3) }, ['hover']],
  ]),
];

// ---- after the test run: the capture's own chat (the newest chat under the design-capture project).
// File mentions are never clicked: Codex would open hello.txt in the owner's default editor.
const openChat = async ({ page }) => {
  await page.locator(`[role=listitem][aria-label="${PROJECT}"] [data-app-action-sidebar-thread-id]`).first().click(); await wait(page, 2500);
  await page.mouse.move(1300, 700); await wait(page, 300);
};
const CONVERSATION = {
  'user-message': '[data-user-message-bubble]',
  'worked-row': page => page.locator('main button').filter({ hasText: /^Worked for/ }).first(),
  'assistant-message': '[data-local-conversation-final-assistant] [data-markdown-text-style=assistant-message]',
  'inline-code': '[data-markdown-copy=inline-code]',
  'file-mention': '[data-appearance=inline-mention]',
  'message-action': 'main button[aria-label=Copy]',
  'summary-panel': '[data-summary-panel-variant]',
  'context-usage': 'span[aria-label^="Context usage"]',
  composer: S.composer,
};
const tabsClose = async ({ page }) => {
  for (let i = 0; i < 4; i++) { const c = page.locator('button[data-app-shell-tab-close-button]').filter({ visible: true }); if (!(await c.count())) break; await c.last().click(); await wait(page, 700); }
  await untoggle(page);
};
const newTab = async h => { await openChat(h); await h.page.locator('button[aria-label="New tab"][data-app-shell-workspace-layout-toggle]').click(); await wait(h.page, 1500); await h.page.mouse.move(700, 700); };
export const AFTER_RUN = ['conversation', 'conversation-expanded', 'conversation-user-hover', 'chat-actions-menu', 'chat-actions-submenu', 'message-more-menu',
  'tabs-new', 'tabs-terminal', 'conversation-thread-row-selected-hover', 'conversation-worked-row-hover', 'conversation-worked-row-focus-visible', 'conversation-message-action-hover'];
SHOTS.push(
  { name: 'conversation', window: M, reveal: openChat,
    parts: { ...CONVERSATION, 'thread-title': page => page.locator('header, [data-app-shell-header-slot]').getByText(/files/i).first(),
      'thread-row-selected': '[data-app-action-sidebar-thread-active=true]', 'header-icon-button': 'button[aria-label="Chat actions"]',
      'header-toggle-pressed': 'button[aria-label="Toggle pinned summary"][aria-pressed=true]' },
    optionalParts: ['thread-title', 'header-toggle-pressed', 'context-usage', 'file-mention', 'inline-code'] },
  { name: 'conversation-expanded', window: M,
    reveal: async h => { await openChat(h); for (let i = 0; i < 4; i++) { const b = h.page.locator('main button[aria-expanded=false]').filter({ hasText: /^Worked for/ }).filter({ visible: true }).first(); if (!(await b.count())) break; await b.click(); await wait(h.page, 900); } await h.page.mouse.move(1300, 700); },
    parts: { 'worked-row-expanded': page => page.locator('main button[aria-expanded=true]').filter({ hasText: /^Worked for/ }).first(),
      'tool-row': page => page.locator('main').getByText(/^(Listed files|Created|Edited|Ran)/).first(), 'assistant-message': CONVERSATION['assistant-message'] },
    optionalParts: ['tool-row'] },
  { name: 'conversation-user-hover', window: M, state: 'hover', reveal: openChat, hover: 'user-message',
    parts: { 'user-message': '[data-user-message-bubble]', 'message-action-user': 'main button[aria-label="Copy message"]' }, optionalParts: ['message-action-user'] },
  { name: 'chat-actions-menu', window: M, reveal: async h => { await openChat(h); await openMenu('button[aria-label="Chat actions"]')(h); },
    parts: { ...menuParts, kbd: page => lastMenu(page).locator('kbd, [data-menu-item-shortcut]').first(), 'menu-separator': '[role=menu] [role=separator]' }, optionalParts: ['kbd', 'menu-separator'] },
  { name: 'chat-actions-submenu', window: M, optional: true,
    reveal: async h => { await openChat(h); await openMenu('button[aria-label="Chat actions"]')(h); await lastMenu(h.page).locator('[aria-haspopup]').filter({ hasText: 'Copy' }).first().hover(); await wait(h.page, 1000); },
    parts: { submenu: lastMenu } },
  { name: 'message-more-menu', window: M, reveal: async h => { await openChat(h); await h.page.locator('main button[aria-label="More actions"]').last().click(); await wait(h.page, 900); },
    parts: menuParts },
  // The right panel's tab strip: a new tab (browser start page with Files, Terminal and New page), then a
  // terminal in the scratch folder. Both tabs are closed and the strip hidden again afterwards.
  { name: 'tabs-new', window: M, reveal: newTab,
    parts: { tab: page => page.locator('[role=tab]').filter({ visible: true }).first(), 'url-field': page => page.locator('input[placeholder="Search or enter a URL"]').filter({ visible: true }).first(),
      'tool-card': page => page.getByText('Files', { exact: true }).filter({ visible: true }).first().locator('xpath=ancestor::*[self::button or @role="button"][1]'), 'tab-close': 'button[data-app-shell-tab-close-button]' },
    optionalParts: ['tab', 'url-field', 'tool-card'], after: tabsClose },
  { name: 'tabs-terminal', window: M, optional: true,
    reveal: async h => { await newTab(h); await h.page.getByText('Terminal', { exact: true }).filter({ visible: true }).first().click(); await wait(h.page, 3000); await h.page.mouse.move(700, 700); },
    parts: { terminal: page => page.locator('.xterm, [class*=terminal i]').filter({ visible: true }).first() }, after: tabsClose },
  ...states([
    ['conversation', M, openChat, { 'thread-row-selected': '[data-app-action-sidebar-thread-active=true]', 'message-action': 'main button[aria-label=Copy]' }, ['hover']],
    ['conversation', M, openChat, { 'worked-row': CONVERSATION['worked-row'] }, ['hover', 'focus-visible']],
  ]),
);

// ---- an agent run, taken by run.mjs. The owner approved (2026-10-25) harmless test prompts in a fresh
// local chat on the empty folder ~/.design-systems/harness-scratch/codex, approving only actions inside it.
export const SCRATCH = 'harness-scratch/codex';
async function sendPrompt({ page }, text) {
  await page.locator(editor).filter({ visible: true }).last().click();
  await page.keyboard.type(text, { delay: 10 }); await wait(page, 300);
  await page.keyboard.press('Enter'); await wait(page, 1500);
}
const approveButton = page => page.locator('main button:visible').filter({ hasText: /^(Approve|Allow|Run|Yes|Accept)\b/ }).last();
const rejectButton = page => page.locator('main button:visible').filter({ hasText: /^(Deny|Reject|Decline|No|Skip)\b/ }).last();
export const RUN = {
  window: 'main',
  async start(h) {
    await home(h);
    const chip = await vis(h.page, S.projectChip).getAttribute('aria-label');
    if (!chip.endsWith(PROJECT)) throw new Error('composer is not on the capture project: ' + chip);
    if ((await vis(h.page, S.workIn).innerText()).trim() !== 'This computer') throw new Error('composer is not on This computer');
  },
  // Called after the steps, and also when one failed or timed out: stop a run this script left going and
  // wait for the agent to go idle, so nothing keeps working after the capture exits.
  async finish(h) {
    const { page } = h;
    await closeAll(page);
    const stop = page.locator('button[aria-label*="Stop" i]:visible');
    for (let i = 0; i < 30 && await stop.count(); i++) {
      if (i === 0) await stop.first().click().catch(() => {});
      await wait(page, 1000);
    }
    if (await stop.count()) throw new Error('the agent is still running after Stop');
  },
  async state({ page }) {
    if (await approveButton(page).count()) return 'approval';
    const stop = page.locator('button[aria-label*="Stop" i]:visible, button[aria-label*="Interrupt" i]:visible, button[aria-label*="Cancel" i]:visible');
    return (await stop.count()) ? 'running' : 'done';
  },
  async reject({ page }) { await rejectButton(page).click().catch(() => {}); await wait(page, 800); },
  steps: [
    { name: 'list-files', send: h => sendPrompt(h, 'List the files in this folder.') },
    { name: 'create-file', send: h => sendPrompt(h, 'Create hello.txt here with one line: hello from the design capture') },
  ],
  parts: { ...CONVERSATION, 'stop-button': 'button[aria-label*="Stop" i]', thinking: page => page.locator('main').getByText(/^Thinking/).first() },
};
