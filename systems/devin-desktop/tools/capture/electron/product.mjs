// PRODUCT (adapt): everything in this file is Devin 3.11.216's (Devin Desktop, built on Windsurf).
// Another Electron app replaces it whole and keeps cdp.mjs, vars.mjs, shots.mjs and run.mjs as they are.
//
// A shot is { name, window, state?, reveal(h), parts, force?, after?(h) }:
//   name    screenshot file name, `{page}-{state}` (the theme folder is added by shots.mjs)
//   window  a key of WINDOWS
//   reveal  async ({ page, cdp, ...helpers }) => {} : clicks, keys and hovers that show the state.
//           Look, don't act: open and close, type and clear, never submit or send.
//   parts   { component: selector | [selector, nth] | (page) => Locator }: each is measured
//           (computed style) and its box recorded for crops, as `{component}-{state}`
//   force   { component: ['hover' | 'focus' | 'focus-visible' | 'active'] }: pseudo-classes forced
//           through CDP on that part before the screenshot (no pointer moves)
//   after   async (h) => {} : undo what reveal did (clear typed text, close a menu)
//
// Devin Desktop is one VS Code workbench per window with two views: the Agents view (the Devin web
// app, React + Tailwind + Base UI, mounted in the workbench as .devin-app-root) and the IDE view (the
// workbench itself, Windsurf's). Every shot runs in a window the capture opened on the empty scratch
// folder ~/.design-systems/harness-scratch/devin (`devin-desktop --new-window <folder>`), never in the
// owner's own windows; its title ends in the folder name, `devin`.

export const NAME = 'Devin';
// Its title is `<page> devin` in the Agents view, `devin` or `devin — <file>` in the IDE view.
const SCRATCH_WINDOW = /(^|\s)devin($| —)/;
export const WINDOWS = { agents: SCRATCH_WINDOW, ide: SCRATCH_WINDOW };
// Scopes vars.mjs resolves custom properties on, besides html and body.
export const SCOPES = { agents: ['.devin-app-root'], ide: ['.monaco-workbench'] };

// ---- navigation helpers (selectors are Devin's own data-slot names, roles and aria-labels, never account text)
const wait = (page, ms = 600) => page.waitForTimeout(ms);
const btn = (page, label) => page.locator(`button[aria-label="${label}"]:visible, a[aria-label="${label}"]:visible`).first();
const sidebar = '[data-slot=sidebar]';
const navLink = label => `${sidebar} [data-slot=sidebar-menu-button] > a[aria-label="${label}"]`;
const navRow = label => `${sidebar} [data-slot=sidebar-menu-button]:has(> a[aria-label="${label}"])`;
const settingsNav = (page, label) => page.locator('[data-slot=sidebar-menu-button]').filter({ hasText: new RegExp(`^${label}$`) }).filter({ visible: true }).first();
const OPEN = '[role=menu]:visible, [role=dialog]:visible, [role=listbox]:visible, [role=tooltip]:visible, [role=alertdialog]:visible';

export async function closeAll(page) {
  for (let i = 0; i < 4 && await page.locator(OPEN).first().isVisible().catch(() => false); i++) {
    await page.keyboard.press('Escape'); await wait(page, 300);
  }
}
// The view switch is the "Agents" or "IDE" menu button at the top left; the Agents view is the one
// whose session sidebar is on screen.
// Its label stacks both names and hides one, so its text content is "AgentsIDE" or "IDEAgents".
const viewSwitch = page => page.locator('button[aria-haspopup=menu]').filter({ hasText: /^(AgentsIDE|IDEAgents)$/ }).filter({ visible: true }).first();
async function setView(page, view) {   // 'Agents' | 'IDE'
  const now = (await page.locator('.monaco-workbench.desktop-shell-active').count()) ? 'Agents' : 'IDE';
  if (now === view) return;
  await viewSwitch(page).click(); await wait(page, 500);
  await page.locator('[role=menuitemradio]').filter({ hasText: `${view} view` }).click(); await wait(page, 1500);
}
// The empty New session page: Agents view, sidebar shown, settings closed, Cloud chosen.
export async function home({ page }) {
  await closeAll(page);
  await setView(page, 'Agents');
  const back = settingsNav(page, 'Back to app');
  if (await back.isVisible().catch(() => false)) { await back.click(); await wait(page, 900); }
  if (await btn(page, 'Expand sidebar').isVisible().catch(() => false)) { await btn(page, 'Expand sidebar').click(); await wait(page); }
  await page.locator(navLink('New session')).click(); await wait(page, 800);
  const cloud = page.locator('button[aria-pressed]').filter({ hasText: /^Cloud$/ }).first();
  if (await cloud.getAttribute('aria-pressed').catch(() => 'true') === 'false') { await cloud.click(); await wait(page, 500); }
  await page.mouse.move(700, 880);
}
async function ide({ page }) {
  await closeAll(page);
  await setView(page, 'IDE');
  await page.keyboard.press('Escape'); await wait(page, 300);
}
// Called before every shot: close any toast left on screen, then bring the window back to a known screen.
export async function reset(h, win) { await closeToasts(h.page); return win === 'agents' ? home(h) : ide(h); }
// Called by shots.mjs right before each screenshot: a toast that appeared during the reveal fails
// the shot (closing it here would move the pointer off a hover state). Shots that show a toast on
// purpose set keepToasts.
export async function beforeShoot({ page }, shot) {
  if (!shot.keepToasts && await toastsOnScreen(page)) throw new Error('a notification toast is on screen');
}
async function settings({ page }, pane) {
  await page.locator('[data-slot=sidebar-footer] [aria-label=Settings]').first().click(); await wait(page, 1200);
  if (pane) { await settingsNav(page, pane).click(); await wait(page, 1200); }
}
const editor = '[role=textbox][aria-label=Prompt]';
// The composer is a Slate editor; Select All and Delete empties it, repeated until it shows its
// placeholder again (an unsent draft would otherwise come back on the next visit).
const promptText = page => page.locator(editor).filter({ visible: true }).first()
  .evaluate(e => e.querySelector('[data-slate-placeholder]') ? '' : e.innerText.replace(/\uFEFF/g, '').trim()).catch(() => '');
async function clearPrompt(page) {
  await closeAll(page);
  for (let i = 0; i < 5 && await promptText(page); i++) {
    await page.locator(editor).filter({ visible: true }).first().click();
    await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); await wait(page, 400);
  }
  if (await promptText(page)) throw new Error('composer could not be emptied');
  await page.keyboard.press('Escape');
}
// The workbench's notification toasts (bottom right, over both views). An error toast stays until
// it is closed, and its close button only shows while the pointer is over it, so each one is
// hovered and closed (Escape if the button does not show). Throws if one is still on screen.
const TOAST = '.notifications-toasts .notification-toast';
const toastsOnScreen = page => page.locator(TOAST).filter({ visible: true }).count();
async function closeToasts(page) {
  for (let i = 0; i < 6 && await toastsOnScreen(page); i++) {
    const t = page.locator(TOAST).filter({ visible: true }).first();
    await t.hover().catch(() => {}); await wait(page, 300);
    const x = t.locator('.codicon-notifications-clear').first();
    if (await x.isVisible().catch(() => false)) await x.click().catch(() => {}); else await page.keyboard.press('Escape');
    await wait(page, 600);
  }
  if (await toastsOnScreen(page)) throw new Error('a notification toast could not be dismissed');
}
async function scrollMain(page, dy) { await page.mouse.move(1000, 500); await page.mouse.wheel(0, dy); await wait(page, 800); }

// What a state needs besides the pointer or keyboard, in this product. Called with on=true before
// the screenshot and on=false after. Devin's controls are Base UI: a press shows through the
// `data-pressed` attribute Base UI sets on pointer down (`data-[pressed]:bg-tint-secondary`), not
// through :active, so pressed shots set that attribute on the part while :active is forced. The
// README says so. Hover is a real pointer (Tailwind hover: and can-hover: variants), and focus-visible
// is real keyboard focus; Devin draws its own focus ring (`.focus-ring`), so nothing is added there.
export async function prepareState(page, selector, states, on) {
  if (!states.includes('active')) return;
  await page.locator(selector).first().evaluate((e, on) => on ? e.setAttribute('data-pressed', '') : e.removeAttribute('data-pressed'), on);
}

// A fingerprint of the account state a capture must never change: the composer's mode and
// capability, and the sidebar's session titles in order. shots.mjs takes it before and after every
// shot and stops when it differs.
export async function guard(h, win) {
  if (win !== 'agents') return '';
  const { page } = h;
  await home(h);
  const mode = await btn(page, 'Switch mode').innerText().catch(() => '?');
  const cap = await capability(page).innerText().catch(() => '?');
  const rows = await page.locator(`${sidebar} [data-slot=sidebar-menu-button] > a[href*="/sessions/"]`).evaluateAll(as => as.map(a => a.getAttribute('aria-label')));
  return `${mode} | ${cap} | draft: ${await promptText(page)} | ${rows.join(' / ')}`;
}
const capability = page => page.locator('button[aria-haspopup=menu]:visible').filter({ hasText: /^(Fusion|Ultra|Normal|Lite|SWE-2)$/ }).first();

// The theme is Devin's own setting (Settings > Preferences > Appearance > Theme: Light, Dark or
// System); it does not follow an emulated prefers-color-scheme. Returns the label it replaced.
export const THEME_LABELS = { light: 'Light', dark: 'Dark' };
export async function setTheme(h, label) {
  const { page } = h;
  await home(h); await settings(h, 'Preferences');
  const trigger = page.locator('button[role=combobox]').filter({ hasText: /^(Light|Dark|System)$/ }).first();
  const before = (await trigger.innerText()).trim();
  if (before !== label) {
    await trigger.click(); await wait(page, 500);
    await page.locator('[role=option]:visible').filter({ hasText: new RegExp(`^${label}$`) }).first().click(); await wait(page, 2000);
  }
  await home(h);
  return before;
}

// ---- the shot list. Selectors are Devin's data-slot names, roles, aria-labels and fixed UI labels.
const A = 'agents', I = 'ide';
const nth = (sel, i) => [sel, i];
const S = {
  sidebar,
  navRow: navRow('Automations'),
  navRowSelected: `${sidebar} [data-slot=sidebar-menu-button]:has(> a[aria-current=page])`,
  sessionRow: `${sidebar} [data-slot=sidebar-menu-button]:has(> a[href*="/sessions/"])`,
  groupLabel: '[data-slot=sidebar-group-label]',
  iconButton: `${sidebar} button[aria-label="Search"]`,
  inbox: `${sidebar} button[aria-label="Notifications"]`,
  identity: '[data-slot=sidebar-footer-identity]',
  avatar: page => page.locator('[data-slot=sidebar-footer-identity] img').first().locator('xpath=..'),
  footer: '[data-slot=sidebar-footer]',
  trigger: '[data-slot=sidebar-trigger]',
  unreadDot: `${sidebar} [data-color-dot]`,
  prBadge: `${sidebar} [aria-label*="merged pull request"]`,
  segmented: '[role=group][data-orientation=horizontal]:has(> button[aria-pressed])',
  segmentSelected: '[role=group] > button[aria-pressed=true]',
  segment: '[role=group] > button[aria-pressed=false]',
  // The same segmented control filters lists (Automations' categories).
  chip: '.bg-bg-page [role=group][data-orientation=horizontal] > button[aria-pressed=false]',
  chipSelected: '.bg-bg-page [role=group][data-orientation=horizontal] > button[aria-pressed=true]',
  composer: `div.cursor-text:has(${editor})`,
  editor,
  attach: 'button[aria-label="Attach or mention"]',
  commands: 'button[aria-label="Commands and skills"]',
  config: 'button[aria-label="Configuration"]',
  mode: 'button[aria-label="Switch mode"]',
  capability,
  voice: 'button[aria-label="Record voice prompt"]',
  call: 'button[aria-label="Start voice call"]',
  send: 'button[aria-label="Send"]',
  sendMore: 'button[aria-label="More send options"]',
  viewSwitch,
  menu: '[role=menu]',
  menuRow: nth('[role=menu] [role=menuitem]', 0),
  menuSep: '[role=menu] [role=separator]',
  submenuTrigger: '[role=menu] [role=menuitem][aria-haspopup]',
  tooltip: '[role=tooltip]',
  palette: '[role=dialog][aria-label="Command palette"]',
  switchOn: '[role=switch][aria-checked=true]',
  switchOff: '[role=switch][aria-checked=false]',
  checkbox: '[role=checkbox]',
  select: 'button[role=combobox]',
  settingsSearch: '[data-slot=input-group]:has(input[placeholder^="Search settings"])',
  settingsSearchInput: 'input[placeholder^="Search settings"]',
  settingsCard: 'div.bg-bg-elevated.rounded-\\[10px\\]',
  settingsRow: page => page.locator('div.bg-bg-elevated.rounded-\\[10px\\] > div').filter({ visible: true }).first(),
  pageTitle: 'h2',
  sectionTitle: 'h3',
};
const settingsNavRow = (label) => page => settingsNav(page, label);
const dialogButton = re => page => page.locator('.monaco-dialog-box .monaco-button').filter({ hasText: re }).first();
const textButton = (re, scope = '') => page => page.locator(`${scope} button, ${scope} a, ${scope} [role=button]`.trim()).filter({ hasText: re }).filter({ visible: true }).first();

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
const openMenu = sel => async ({ page }) => { await page.locator(sel).filter({ visible: true }).first().click(); await wait(page, 800); };
const typed = async ({ page }) => { await clearPrompt(page); await page.locator(editor).click(); await wait(page, 400); await page.keyboard.type('Draft text, never sent'); await wait(page, 500); };
const openPalette = async ({ page }) => { await vis(page, S.iconButton).click(); await wait(page, 900); };
const goNav = label => async ({ page }) => { await page.locator(navLink(label)).click(); await wait(page, 2000); };
const goMore = label => async ({ page }) => {
  await page.locator(`${sidebar} button[aria-label="More"]`).first().click(); await wait(page, 600);
  await page.locator(`nav[data-open] a[aria-label="${label}"]`).first().click(); await wait(page, 2200);
};
const ROW = '[role=menuitem]:not([aria-disabled=true]), [role=menuitemradio], [role=menuitemcheckbox]';
const lastMenu = page => page.locator(S.menu).filter({ visible: true }).last();
const menuParts = { menu: lastMenu, 'menu-row': page => lastMenu(page).locator(ROW).filter({ visible: true }).first() };
const menuTitle = { 'menu-section-title': page => lastMenu(page).locator('[role=presentation].text-12').filter({ visible: true }).first() };
const vis = (page, sel) => page.locator(sel).filter({ visible: true }).first();
const rightClickSession = async ({ page }) => { await page.locator(S.sessionRow).nth(1).click({ button: 'right' }); await wait(page, 800); };

export const SHOTS = [
  { name: 'home-default', window: A, reveal: async () => {},
    parts: { sidebar: S.sidebar, 'sidebar-row': S.navRow, 'sidebar-row-selected': S.navRowSelected, 'session-row': S.sessionRow,
      'sidebar-group-label': S.groupLabel, 'icon-button': S.iconButton, 'sidebar-footer': S.footer, identity: S.identity, avatar: S.avatar,
      'unread-dot': S.unreadDot, 'pr-badge': S.prBadge, segmented: S.segmented, 'segment-selected': S.segmentSelected, segment: S.segment,
      composer: S.composer, 'composer-editor': S.editor, 'composer-tool': S.attach, 'mode-button': S.mode, 'capability-button': S.capability,
      'voice-button': S.voice, 'send-button': S.send, 'send-more': S.sendMore, 'view-switch': S.viewSwitch, 'sidebar-trigger': S.trigger },
    optionalParts: ['unread-dot', 'pr-badge'] },
  // Before the scratch folder is trusted, choosing Local asks to trust it (a dialog, cancelled here)
  // and then shows a warning banner; after, it shows the local agent's composer (home-local-trusted).
  { name: 'trust-dialog', window: A, optional: true,
    reveal: async ({ page }) => { await page.locator(S.segment).filter({ hasText: /^Local$/ }).click(); await wait(page, 1500); },
    // The trust dialog is the workbench's own (.monaco-dialog-box), drawn over the Agents view.
    parts: { dialog: '.monaco-dialog-box', 'button-primary': dialogButton(/^Trust Workspace & Continue$/),
      'button-secondary': dialogButton(/^Cancel$/), 'dialog-close': '.monaco-dialog-box .codicon-dialog-close', 'dialog-link': '.monaco-dialog-box a[data-href]' },
    optionalParts: ['dialog-link'],
    after: async ({ page }) => { await dialogButton(/^Cancel$/)(page).click().catch(() => {}); await wait(page, 600);
      await page.locator('button[aria-pressed]').filter({ hasText: /^Cloud$/ }).first().click().catch(() => {}); await wait(page, 500); } },
  { name: 'home-local', window: A, optional: true,
    reveal: async ({ page }) => { await page.locator(S.segment).filter({ hasText: /^Local$/ }).click(); await wait(page, 1500);
      if (await dialogButton(/^Cancel$/)(page).isVisible().catch(() => false)) { await dialogButton(/^Cancel$/)(page).click(); await wait(page, 800); } },
    parts: { 'segment-selected': S.segmentSelected,
      'banner-warning': page => page.getByText('Trust workspace', { exact: true }).locator('xpath=ancestor::div[contains(@class,"rounded")][1]'),
      'text-button-warning': page => page.getByText('Trust workspace', { exact: true }) },
    after: async ({ page }) => { await page.locator('button[aria-pressed]').filter({ hasText: /^Cloud$/ }).first().click().catch(() => {}); await wait(page, 500); } },
  { name: 'home-composer-typed', window: A, state: 'filled', reveal: typed,
    parts: { composer: S.composer, 'composer-editor': S.editor, 'send-button': S.send, 'send-more': S.sendMore },
    after: async ({ page }) => clearPrompt(page) },
  { name: 'send-menu', window: A,
    reveal: async h => { await typed(h); await h.page.locator(S.sendMore).click(); await wait(h.page, 800); },
    parts: menuParts, after: async ({ page }) => clearPrompt(page) },
  { name: 'attach-menu', window: A, reveal: openMenu(S.attach),
    parts: { ...menuParts, 'menu-separator': S.menuSep, 'menu-submenu-trigger': S.submenuTrigger } },
  { name: 'attach-submenu', window: A,
    reveal: async h => { await openMenu(S.attach)(h); await h.page.locator(S.submenuTrigger).first().hover(); await wait(h.page, 1000); },
    parts: { submenu: page => page.locator(S.menu).filter({ visible: true }).last() } },
  { name: 'commands-menu', window: A, reveal: openMenu(S.commands),
    parts: { 'command-list': '[role=listbox]', 'command-option': nth('[role=listbox] [role=option]', 0), tooltip: S.tooltip },
    optionalParts: ['tooltip'], after: async ({ page }) => clearPrompt(page) },
  { name: 'config-menu', window: A, reveal: openMenu(S.config), parts: menuParts },
  { name: 'mode-menu', window: A, reveal: openMenu(S.mode), parts: { ...menuParts, ...menuTitle }, optionalParts: ['menu-section-title'] },
  { name: 'capability-menu', window: A, reveal: async h => { await S.capability(h.page).click(); await wait(h.page, 800); }, parts: { ...menuParts, ...menuTitle }, optionalParts: ['menu-section-title'] },
  { name: 'view-menu', window: A, reveal: async h => { await S.viewSwitch(h.page).click(); await wait(h.page, 800); },
    parts: { 'view-menu': '[role=menu]:has([role=menuitemradio])', 'menu-radio-row': nth('[role=menuitemradio]', 0) } },
  { name: 'search-palette', window: A, reveal: openPalette,
    parts: { palette: S.palette, 'palette-input': page => page.locator(S.palette).locator('div:has(> [cmdk-input])').first(), 'palette-row': nth(`${S.palette} [cmdk-item][aria-selected=false]`, 0),
      'palette-row-selected': `${S.palette} [cmdk-item][aria-selected=true]`, 'palette-heading': `${S.palette} [cmdk-group-heading]`, kbd: `${S.palette} kbd` } },
  { name: 'search-palette-empty', window: A, state: 'empty',
    reveal: async h => { await openPalette(h); await h.page.keyboard.type('zzqxv'); await wait(h.page, 1000); },
    parts: { palette: S.palette } },
  { name: 'notifications', window: A, reveal: async ({ page }) => { await page.locator(S.inbox).click(); await wait(page, 1500); },
    parts: { 'notifications-panel': page => page.getByText('Notifications', { exact: true }).filter({ visible: true }).last().locator('xpath=ancestor::div[contains(@class,"flex-col")][2]'),
      'tab-selected': '[role=tab][aria-selected=true]:visible', tab: '[role=tab][aria-selected=false]:visible',
      'notification-row': page => page.getByText('Access request', { exact: true }).filter({ visible: true }).first().locator('xpath=ancestor::div[contains(@class,"group")][1]') },
    optionalParts: ['notifications-panel', 'tab-selected', 'tab', 'notification-row'] },
  // More opens a navigation popover (a nav, not a menu) of the pages hidden from the sidebar.
  { name: 'more-menu', window: A, reveal: openMenu(`${sidebar} button[aria-label="More"]`),
    parts: { 'nav-popover': 'nav[data-open][data-side]', 'nav-popover-row': page => page.locator('nav[data-open] a[aria-label]').first().locator('xpath=..') } },
  { name: 'account-menu', window: A, reveal: openMenu(S.identity), parts: menuParts },
  { name: 'sessions-new-menu', window: A, reveal: openMenu(`${sidebar} button[aria-label="New"]`), parts: menuParts },
  { name: 'sessions-properties-menu', window: A, reveal: openMenu(`${sidebar} button[aria-label="Properties"]`),
    parts: { ...menuParts, ...menuTitle, 'switch-sm-on': '[role=menu] [role=switch][aria-checked=true]', 'switch-sm-off': '[role=menu] [role=switch][aria-checked=false]' },
    optionalParts: ['switch-sm-on', 'switch-sm-off', 'menu-section-title'] },
  { name: 'help-menu', window: A, reveal: openMenu('[data-slot=sidebar-footer] button[aria-label="Help"]'), parts: menuParts },
  { name: 'session-context-menu', window: A, reveal: rightClickSession,
    parts: { 'context-menu': page => page.locator(S.menu).filter({ visible: true }).last(), 'menu-row': nth('[role=menu] [role=menuitem]', 1), 'menu-separator': S.menuSep } },
  { name: 'tooltip', window: A, state: 'hover',
    reveal: async ({ page }) => { await vis(page, S.iconButton).hover(); await wait(page, 1700); },
    parts: { tooltip: S.tooltip, 'icon-button': S.iconButton } },
  { name: 'sidebar-collapsed', window: A,
    reveal: async ({ page }) => { await vis(page, S.trigger).click(); await wait(page, 1000); },
    after: async ({ page }) => { await btn(page, 'Expand sidebar').click().catch(() => {}); await wait(page, 700); }, parts: { 'expand-button': 'button[aria-label="Expand sidebar"]' } },
  { name: 'automations', window: A, reveal: goNav('Automations'),
    parts: { 'page-title': page => page.locator('h1, h2').filter({ visible: true }).filter({ hasText: /^Automations$/ }).first(),
      'button-primary-inverse': textButton(/^Create automation/), 'banner-info': page => page.getByText('Suggest automations for me').locator('xpath=ancestor::div[contains(@class,"rounded")][1]'),
      'button-secondary': textButton(/^Suggest automations for me$/), 'filter-chip': S.chip, 'filter-chip-selected': S.chipSelected,
      card: page => page.getByText('Triage Bug Reports', { exact: true }).locator('xpath=ancestor::*[self::button or self::a or contains(@class,"rounded")][1]'),
      'integration-badge': page => page.getByText('Slack', { exact: true }).filter({ visible: true }).first().locator('xpath=..') },
    optionalParts: ['banner-info', 'card', 'integration-badge'] },
  { name: 'automations-scrolled', window: A, reveal: async h => { await goNav('Automations')(h); await scrollMain(h.page, 700); }, parts: {} },
  { name: 'wiki', window: A, reveal: goNav('Wiki'),
    parts: { 'search-field': page => page.locator('input[placeholder^="Search wikis"]').locator('xpath=..'), 'button-primary-inverse-sm': textButton(/^Add wiki$/),
      'button-inverse-sm': textButton(/^Generate$/), card: page => page.locator('button, a, div.rounded-\\[10px\\], div.rounded-lg').filter({ has: page.locator('svg') }).filter({ hasText: /ago/ }).filter({ visible: true }).nth(1) },
    optionalParts: ['search-field', 'card', 'button-inverse-sm'] },
  { name: 'review', window: A, reveal: goMore('Review'), parts: {} },
  { name: 'customize', window: A, reveal: goMore('Customize'), parts: {} },
  { name: 'settings-preferences', window: A, reveal: async h => settings(h, 'Preferences'),
    parts: { 'settings-nav': settingsNavRow('Keyboard shortcuts'), 'settings-nav-selected': settingsNavRow('Preferences'), 'settings-search': S.settingsSearch,
      'page-title': nth('h2', 0), 'section-title': nth('h3', 0), 'settings-card': nth(S.settingsCard, 0), 'settings-row': S.settingsRow,
      select: S.select, 'number-field': page => page.locator('button[aria-label="Increase font size"]').first().locator('xpath=..') },
    optionalParts: ['number-field'] },
  { name: 'settings-preferences-scrolled', window: A, reveal: async h => { await settings(h, 'Preferences'); await scrollMain(h.page, 900); },
    parts: { 'switch-on': S.switchOn, 'switch-off': S.switchOff, select: S.select } },
  { name: 'settings-theme-select', window: A,
    reveal: async h => { await settings(h, 'Preferences'); await h.page.locator(S.select).filter({ hasText: /^(Light|Dark|System)$/ }).first().click(); await wait(h.page, 700); },
    parts: { listbox: page => page.locator('[role=listbox]').filter({ visible: true }).last(), option: nth('[role=listbox]:visible [role=option]', 0),
      'option-selected': '[role=listbox]:visible [role=option][aria-selected=true]' } },
  { name: 'settings-shortcuts', window: A, reveal: async h => settings(h, 'Keyboard shortcuts'),
    parts: { 'search-field': page => page.locator('input[placeholder^="Search shortcuts"]').locator('xpath=..'), 'tab-selected': '[role=tab][aria-selected=true]:visible, [role=radio][aria-checked=true]:visible',
      kbd: page => page.locator('main kbd, kbd').filter({ visible: true }).nth(2), 'button-quiet': textButton(/^Reset all$/) },
    optionalParts: ['tab-selected', 'button-quiet', 'search-field'] },
  { name: 'settings-notifications', window: A, reveal: async h => settings(h, 'Notifications'),
    parts: { checkbox: S.checkbox, 'switch-on': S.switchOn, 'callout-info': page => page.getByText(/^Mobile push needs/).locator('xpath=..') },
    optionalParts: ['callout-info'] },
  { name: 'settings-connections', window: A, reveal: async h => settings(h, 'Connections'),
    parts: { 'callout-info': page => page.getByText('MCPs are now in Customize').locator('xpath=ancestor::div[contains(@class,"border")][1]'),
      'button-inverse-sm': textButton(/^Go to Customize$/), 'button-danger-outline': textButton(/^Unlink user$/) },
    optionalParts: ['callout-info'] },
  { name: 'settings-app', window: A, reveal: async h => settings(h, 'App settings'),
    parts: { 'button-outline': textButton(/^Customize$/), 'text-field': page => page.locator('main input:not([type=hidden]), input').filter({ visible: true }).nth(1),
      'text-link': page => page.locator('a').filter({ hasText: /^Available/ }).filter({ visible: true }).first() },
    optionalParts: ['text-link'] },
  { name: 'settings-app-agents', window: A, reveal: async h => { await settings(h, 'App settings'); await scrollMain(h.page, 600); },
    parts: { 'agent-row': page => page.getByText('Devin AI coding agent via Devin CLI').locator('xpath=ancestor::div[contains(@class,"flex")][2]'),
      'status-text': page => page.getByText('Enabled', { exact: true }).filter({ visible: true }).first() },
    optionalParts: ['agent-row'] },
  { name: 'settings-search', window: A, state: 'filled',
    reveal: async h => { await settings(h, 'Preferences'); await h.page.locator(S.settingsSearchInput).click(); await h.page.keyboard.type('theme'); await wait(h.page, 1200); },
    parts: { 'settings-search': S.settingsSearch },
    after: async ({ page }) => { await page.locator(S.settingsSearchInput).click().catch(() => {}); await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); } },

  // ---- states, one part per shot: hover with the real pointer, focus-visible with real keyboard
  // focus, pressed with :active forced through CDP plus Base UI's data-pressed (prepareState).
  ...states([
    ['home', A, async () => {}, { 'icon-button': S.iconButton, 'sidebar-row': S.navRow, 'session-row': nth(S.sessionRow, 1),
      'composer-tool': S.attach, 'mode-button': S.mode, 'capability-button': S.capability, 'voice-button': S.voice, identity: S.identity }, ['hover', 'focus-visible', 'pressed']],
    // A segment's data-pressed is its selected state (Base UI toggle), so it gets no pressed shot.
    ['home', A, async () => {}, { segment: S.segment }, ['hover', 'focus-visible']],
    ['settings', A, async h => settings(h, 'Notifications'), { 'switch-on': S.switchOn, checkbox: S.checkbox, 'settings-nav': settingsNavRow('Preferences') }, ['hover', 'focus-visible', 'pressed']],
    ['settings', A, async h => settings(h, 'Preferences'), { select: S.select }, ['hover', 'focus-visible', 'pressed']],
    // The search group is not focusable; its input takes the pointer and the focus, so it is its own part.
    ['settings', A, async h => settings(h, 'Preferences'), { 'settings-search-input': S.settingsSearchInput }, ['hover', 'focus-visible']],
    ['settings', A, async h => settings(h, 'App settings'), { 'button-outline': textButton(/^Customize$/) }, ['hover', 'focus-visible', 'pressed']],
    ['automations', A, goNav('Automations'), { 'button-primary-inverse': textButton(/^Create automation/), 'filter-chip': S.chip }, ['hover', 'focus-visible', 'pressed']],
    ['palette', A, openPalette, { 'palette-row': nth(`${S.palette} [cmdk-item][aria-selected=false]`, 1) }, ['hover']],
    ['menu', A, rightClickSession, { 'menu-row': nth('[role=menu] [role=menuitem]', 2) }, ['hover']],
  ]),

  // ---- IDE view (the VS Code workbench, Windsurf's) on the empty scratch folder
  { name: 'ide-shell', window: I,
    reveal: async ({ page }) => { if (!(await page.locator('.part.auxiliarybar').isVisible().catch(() => false))) { await page.keyboard.press('Meta+L'); await wait(page, 1500); } },
    parts: { 'left-header': '.part.leftheader', titlebar: '.part.titlebar', 'side-bar': '.part.sidebar', 'status-bar': '.part.statusbar',
      'agent-pane': '.part.auxiliarybar', 'editor-empty': '.part.editor', banner: '.part.banner', 'command-center': '.command-center-center',
      'explorer-row': '.explorer-folders-view .monaco-list-row' },
    optionalParts: ['banner', 'explorer-row'] },
  { name: 'ide-quick-open', window: I, reveal: async ({ page }) => { await page.keyboard.press('Meta+P'); await wait(page, 1000); },
    parts: { 'quick-input': '.quick-input-widget', 'quick-input-box': '.quick-input-widget .monaco-inputbox' } },
  { name: 'ide-command-palette', window: I, reveal: async ({ page }) => { await page.keyboard.press('Meta+Shift+P'); await wait(page, 1000); },
    parts: { 'quick-input': '.quick-input-widget', 'quick-input-row-focused': '.quick-input-list .monaco-list-row.focused', 'quick-input-row': nth('.quick-input-list .monaco-list-row', 1),
      keybinding: nth('.quick-input-list .monaco-keybinding-key', 0) } },
  { name: 'ide-terminal', window: I, reveal: async ({ page }) => { await page.keyboard.press('Control+Backquote'); await wait(page, 2500); },
    parts: { panel: '.part.panel', terminal: '.terminal-wrapper', 'panel-tab': '.part.panel .composite-bar .action-item.checked' },
    optionalParts: ['panel-tab'],
    after: async ({ page }) => { await page.keyboard.press('Control+Backquote'); await wait(page, 800); } },
  // Before the folder is trusted, opening a terminal asks to trust it (the workbench's dialog);
  // cancelling raises an error toast. Both are dismissed; the folder stays untrusted.
  { name: 'ide-terminal-trust-dialog', window: I, optional: true,
    reveal: async ({ page }) => { await page.keyboard.press('Control+Backquote'); await wait(page, 1500); },
    parts: { dialog: '.monaco-dialog-box', 'button-primary': dialogButton(/^Trust Workspace & Continue$/), 'button-secondary': dialogButton(/^Cancel$/) },
    after: async ({ page }) => { await dialogButton(/^Cancel$/)(page).click().catch(() => {}); await wait(page, 800); await closeToasts(page); } },
  { name: 'toast', window: I, optional: true,
    reveal: async ({ page }) => { await page.keyboard.press('Control+Backquote'); await wait(page, 1500);
      await dialogButton(/^Cancel$/)(page).click(); await wait(page, 1500); },
    keepToasts: true,
    parts: { toast: '.notifications-toasts .notification-toast', 'toast-button': '.notifications-toasts .monaco-button', 'toast-close': '.notifications-toasts .codicon-notifications-clear' },
    optionalParts: ['toast-close'],
    after: async ({ page }) => closeToasts(page) },
];

// ---- after the test run: the finished local session (one of the two test sessions run.mjs created
// on the scratch folder) and hello.txt in the editor.
//
// The first capture (2026-10-25) also took `conversation` and `conversation-code-hover` in a past
// cloud session from the owner's history, to show a reply, a PR and its diff review. Opening that
// session woke the agent (it was asleep) and made it post a message, so those two shots are no longer
// in this list: the capture never opens a session it did not create. Their screenshots and readings
// are kept from the first capture (the dark pair still shows the stray toast, see the README);
// quantize.py's KEPT carries them through a capture that does not have them.
const CONVERSATION = {
  'agent-name': '[data-find-exclude=true] span.font-medium', 'inline-code': 'p[data-md-source-start] code', link: 'a[data-streamdown=link]',
  'status-line': page => page.getByText(/^Devin (is awaiting instructions|went to sleep)/).filter({ visible: true }).last(),
  'work-row': page => page.getByText(/^Worked for /).filter({ visible: true }).first().locator('xpath=ancestor::*[self::button or @role="button"][1]'),
  composer: S.composer,
};
// Shots that need the scratch folder trusted and the test run done (run.mjs), taken after it.
export const AFTER_RUN = ['ide-editor', 'ide-terminal', 'conversation-local', 'conversation-local-top', 'conversation-local-hover', 'home-local-trusted'];
// The test session: a local Devin session (devin-cli) that run.mjs created, matched by its link and
// the title Devin gave it, so no other session can be opened. Throws if none is listed.
export const TEST_SESSION_TITLE = 'List Files in the Current Folder';
const testSession = page => page.locator(`${sidebar} [data-slot=sidebar-menu-button] > a[href*="acp%2Fdevin-cli%2F"][aria-label="${TEST_SESSION_TITLE}"]`).first();
const openLocalSession = async ({ page }) => {
  if (!(await testSession(page).count())) throw new Error(`no test session titled ${TEST_SESSION_TITLE} in the sidebar`);
  await testSession(page).click(); await wait(page, 2500);
};
const LOCAL = {
  'user-message': '[role=group][aria-label="User message"] div.rounded-\\[16px\\]',
  'worked-row': page => page.getByText(/^Worked for/).filter({ visible: true }).first(),
  'thoughts-row': page => page.getByText('Thoughts', { exact: true }).filter({ visible: true }).first(),
  'hook-error': page => page.getByText(/^Hook failed/).filter({ visible: true }).first(),
  'status-line': page => page.getByText(/^Devin (is awaiting instructions|went to sleep)/).filter({ visible: true }).last(),
  'session-title': page => page.locator('li [data-pane-drag-handle]').filter({ visible: true }).first(),
  'diff-file-header': '[data-file-path] > div.sticky', 'diff-line-added': '[data-diff-row] [data-diff-cell][class*="tint-green"]',
  composer: S.composer,
};
SHOTS.push(
  { name: 'ide-editor', window: I, reveal: async ({ page }) => { await page.keyboard.press('Meta+P'); await wait(page, 800); await page.keyboard.type('hello.txt'); await wait(page, 800); await page.keyboard.press('Enter'); await wait(page, 1500); },
    parts: { 'editor-tab': '.tabs-container .tab.active', 'explorer-row': '.explorer-folders-view .monaco-list-row', editor: '.monaco-editor .view-lines', 'line-numbers': '.monaco-editor .margin' },
    optional: true, after: async ({ page }) => { await page.keyboard.press('Meta+W'); await wait(page, 600); } },
  { name: 'conversation-local', window: A, optional: true, reveal: openLocalSession, parts: LOCAL,
    optionalParts: ['worked-row', 'thoughts-row', 'hook-error', 'diff-file-header', 'diff-line-added', 'session-title'] },
  { name: 'conversation-local-top', window: A, optional: true,
    reveal: async h => { await openLocalSession(h); await h.page.mouse.move(500, 400); await h.page.mouse.wheel(0, -4000); await wait(h.page, 900); },
    parts: { 'user-message': LOCAL['user-message'] } },
  { name: 'conversation-local-hover', window: A, state: 'hover', optional: true, reveal: openLocalSession, hover: 'user-message',
    parts: { 'user-message': ['[role=group][aria-label="User message"] div.rounded-\\[16px\\]', 0] } },
  { name: 'home-local-trusted', window: A, optional: true,
    reveal: async ({ page }) => { await page.locator(S.segment).filter({ hasText: /^Local$/ }).click(); await wait(page, 1500); },
    parts: { composer: S.composer, 'segment-selected': S.segmentSelected },
    after: async ({ page }) => { await page.locator('button[aria-pressed]').filter({ hasText: /^Cloud$/ }).first().click().catch(() => {}); await wait(page, 500); } },
);

// ---- an agent run, taken by run.mjs. The owner approved (2026-10-25) harmless test prompts in a
// fresh session on the empty folder ~/.design-systems/harness-scratch/devin, approving only actions inside it.
export const SCRATCH = 'harness-scratch/devin';
async function sendPrompt({ page }, text) {
  await page.locator(editor).filter({ visible: true }).last().click();
  await page.keyboard.type(text, { delay: 10 }); await wait(page, 300);
  await page.keyboard.press('Enter'); await wait(page, 1200);
}
// Approval buttons inside the session pane only (never the sidebar's or a menu's).
const approveButton = page => page.locator('main button:visible, [data-slot=chat] button:visible').filter({ hasText: /^(Allow|Approve|Accept|Run|Yes)\b/ }).last();
const rejectButton = page => page.locator('button:visible').filter({ hasText: /^(Deny|Reject|Skip|No|Cancel)\b/ }).last();
export const RUN = {
  window: 'agents',
  async start(h) {
    await home(h);
    await h.page.locator(S.segment).filter({ hasText: /^Local$/ }).click(); await wait(h.page, 1500);
    if (await h.page.getByText('Trust workspace', { exact: true }).isVisible().catch(() => false)) throw new Error('scratch folder not trusted yet');
  },
  async finish(h) { await home(h); },
  async state({ page }) {
    if (await approveButton(page).count()) return 'approval';
    const stop = page.locator('button[aria-label*="Stop" i]:visible, button[aria-label*="Interrupt" i]:visible, button[aria-label*="Cancel" i]:visible');
    const working = page.getByText(/^(Devin is (working|thinking)|Thinking|Working|Running)/).filter({ visible: true });
    return (await stop.count()) || (await working.count()) ? 'running' : 'done';
  },
  async reject({ page }) { await rejectButton(page).click().catch(() => {}); await wait(page, 800); },
  steps: [
    { name: 'list-files', send: h => sendPrompt(h, 'List the files in this folder.') },
    { name: 'create-file', send: h => sendPrompt(h, 'Create hello.txt here with one line: hello from the design capture') },
  ],
  // Parts measured on every frame; the last visible match is measured.
  parts: { composer: S.composer, ...CONVERSATION },
};
