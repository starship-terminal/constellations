// PRODUCT (adapt): everything in this file is Capy 0.4.7's. Another Electron app replaces it
// whole and keeps cdp.mjs, vars.mjs, shots.mjs and run.mjs as they are.
//
// A shot is { name, window, state?, reveal(h), parts, force?, hover?, focus?, optional?, optionalParts?, after?(h) }:
//   name    screenshot file name, `{page}-{state}` (the theme folder is added by shots.mjs)
//   window  a key of WINDOWS
//   reveal  async ({ page, cdp, ...helpers }) => {} : clicks, keys and hovers that show the state.
//           Look, don't act: open and close, type and clear, never submit or send.
//   parts   { component: selector | [selector, nth] | (page) => Locator }: each is measured
//           (computed style) and its box recorded for crops, as `{component}-{state}`
//   force   { component: ['hover' | 'focus' | 'focus-visible' | 'active'] }: pseudo-classes forced
//           through CDP on that part before the screenshot
//   after   async (h) => {} : undo what reveal did (clear typed text, close a menu)
//
// Capy's window is one CDP page (capy://app/...), the capy.ai web app served from the bundle's own
// renderer folder over the capy:// scheme. Its Theme setting is System, which follows prefers-color-scheme,
// so the capture runs with SCHEME=light or SCHEME=dark (cdp.mjs emulates it) and the setting is never touched.
//
// Two places are visited. The app itself (home, threads, pull requests, automations, settings, menus and
// dialogs) on the owner's account, where nothing is sent, created or changed; and /design, the gallery of
// Capy's own components that ships in the bundle ("Every component in the system, on the surface it ships
// on"), whose sample data is the product's fixtures. The owner's own threads are never opened.
import { resolve as resolvePath } from 'node:path';
import { allowance, ancestors, approvableCard } from './approve.mjs';
import { stopRun } from './stop.mjs';
import { restoreDraft } from './draft.mjs';

export const NAME = 'Capy';
export const WINDOWS = { app: /\bCapy$/ };
export const SCOPES = { app: ['body'] };

const wait = (page, ms = 700) => page.waitForTimeout(ms);
const vis = (page, sel) => page.locator(sel).filter({ visible: true }).first();
const btn = (page, label) => vis(page, `button[aria-label="${label}"]`);
const slot = (s, extra = '') => `[data-slot="${s}"]${extra}`;

const OPEN = '[role=menu], [role=dialog], [role=alertdialog], [role=listbox], [data-slot=popover-content], [data-slot=tooltip-content], [data-slot=command-menu-content]';
export async function closeAll(page) {
  for (let i = 0; i < 4 && await page.locator(OPEN).filter({ visible: true }).first().isVisible().catch(() => false); i++) {
    await page.keyboard.press('Escape'); await wait(page, 300);
  }
}
const path = page => page.evaluate(() => location.pathname);

// The app shell, on the New thread page. A full load of capy://app/... lands on the desktop tab's last
// route, so the shell is reached by loading it and then following Capy's own links.
async function shell(page) {
  if ((await path(page)) === '/design') { await page.goto('capy://app/new'); await wait(page, 2500); }
  await closeAll(page);
}
export async function home({ page }) {
  await shell(page);
  if ((await path(page)) !== '/new') {
    await vis(page, 'a[href="/new"]').click(); await wait(page, 1200);
  }
  if ((await path(page)) !== '/new') throw new Error(`not on /new: ${await path(page)}`);
  // No focus ring carried over from an earlier focus-visible shot.
  await page.evaluate(() => document.activeElement && document.activeElement.blur());
  await page.mouse.move(700, 790); await wait(page, 300);
}
export async function reset(h) { await home(h); }

async function go({ page }, href) {
  await home({ page });
  await vis(page, `a[href="${href}"]`).click(); await wait(page, 1500);
}
async function more({ page }, label) {
  await home({ page });
  await vis(page, 'nav[aria-label=Main] button:has-text("More")').click(); await wait(page, 600);
  await page.locator('[role=menuitem]').filter({ hasText: new RegExp(`^${label}`) }).first().click(); await wait(page, 1500);
}
async function settings({ page }, pane) {
  await home({ page });
  await page.keyboard.press('Meta+Comma'); await wait(page, 1200);
  if (pane) { await vis(page, `a[href="/settings/${pane}"]`).click(); await wait(page, 1300); }
  await page.mouse.move(700, 790);
}

// The gallery: /design, outside the app shell. Each gallery shot scrolls one section to the top.
async function design({ page }, section) {
  if ((await path(page)) !== '/design') { await page.goto('capy://app/design'); await wait(page, 2500); }
  await closeAll(page);
  await page.evaluate(() => document.activeElement && document.activeElement.blur());
  if (section) {
    const ok = await page.evaluate(name => {
      const h = [...document.querySelectorAll('section > h2')].find(e => e.textContent.trim() === name);
      if (!h) return false;
      h.parentElement.scrollIntoView({ block: 'start' }); window.scrollBy(0, -24); return true;
    }, section);
    if (!ok) throw new Error(`no gallery section ${section}`);
    await wait(page, 900);
  } else {
    await page.evaluate(() => window.scrollTo(0, 0)); await wait(page, 500);
  }
  await page.mouse.move(40, 790);
}
// A part inside one gallery section: sec('Buttons', 'button:has-text("Accent")').
const sec = (name, sel, n = 0) => page => page.locator('section').filter({ has: page.locator('h2', { hasText: new RegExp(`^${name}$`) }) }).first().locator(sel).filter({ visible: true }).nth(n);

// Capy's hover and focus are plain CSS (:hover, :focus-visible), so no state needs help here.
export async function prepareState() {}

// What a capture must never change: the new-thread draft and its project, the composer's model, the colour
// theme, and the desktop tabs. All of it is in the window's localStorage, so the guard reads it there without
// moving the window (a thread can only be deleted from a confirmation the capture never confirms).
// shots.mjs compares this before and after every shot.
export async function guard(h) {
  return h.page.evaluate(() => {
    const v = k => localStorage.getItem(k) || '';
    let tabs = '?';
    try { tabs = JSON.parse(v('capy-desktop:tabs:1')).tabs.length; } catch {}
    return [`tabs ${tabs}`, ...['capy-web:new-thread-draft', 'capy-web:home-project', 'capy-web:last-model', 'capy-web:color-theme-v2', 'theme', 'capy-web:new-thread-run-on']
      .map(k => `${k.replace('capy-web:', '')}=${v(k).length}:${v(k).slice(0, 48)}`)].join(' | ');
  });
}

// ---- the shot list
const A = 'app';
const nth = (s, i) => [s, i];
const S = {
  sidebar: slot('sidebar-container'),
  tabStrip: slot('desktop-tab-strip'),
  tab: '[role=tab]',
  newTab: 'button[aria-label="New tab"]',
  back: 'button[aria-label=Back]',
  update: 'button[aria-label="Restart to update"]',
  home: 'a[aria-label=Home]',
  iconButton: '[data-slot=sidebar-content] button[aria-label=Search]',
  collapse: 'button[aria-label="Close sidebar"]',
  navRow: 'nav[aria-label=Main] a[href="/threads"]',
  navRowSelected: 'nav[aria-label=Main] a[data-status=active]',
  navMore: 'nav[aria-label=Main] button[data-slot=menu-trigger]',
  kbd: 'nav[aria-label=Main] [data-slot=kbd]',
  sectionHeader: page => page.locator('nav[aria-label=Threads] button[data-panel-open]').filter({ hasText: /^Threads$/ }).first(),
  projectGroup: page => page.locator('nav[aria-label=Threads] button[data-panel-open]').nth(1),
  threadRow: slot('sidebar-thread-row'),
  setupCard: 'section[aria-label="Finish setting up"]',
  setupStep: 'section[aria-label="Finish setting up"] button:not([data-slot])',
  setupButton: 'section[aria-label="Finish setting up"] button[data-slot=button]:not([aria-label])',
  dismiss: 'button[aria-label="Dismiss setup"]',
  user: page => page.locator('[data-slot=sidebar-content] button[data-slot=menu-trigger]').filter({ visible: true }).last(),
  avatar: page => page.locator('[data-slot=sidebar-content] button[data-slot=menu-trigger]').filter({ visible: true }).last().locator('img').first(),
  panel: slot('sidebar-panel'),
  composer: slot('composer'),
  editor: '[data-lexical-editor=true]',
  send: 'button[aria-label=Start]',
  voice: 'button[aria-label="Voice input"]',
  add: 'button[aria-label="Add to message"]',
  config: 'button[aria-label="Thread configuration"]',
  model: 'button[aria-label=Model]',
  project: 'button[aria-label=Project]',
  runOn: 'button[aria-label="Run on"]',
  repos: 'button[aria-label="Repositories and branches"]',
  menu: `${slot('menu-content')}, ${slot('context-menu-content')}`,
  menuItem: nth(`${slot('menu-content')} [role=menuitem], ${slot('context-menu-content')} [role=menuitem]`, 0),
  menuItemDanger: page => page.locator('[role=menuitem]').filter({ hasText: /^(Log out|Delete)/ }).filter({ visible: true }).first(),
  menuLabel: slot('menu-label'),
  menuSep: `${slot('menu-content')} [role=separator], ${slot('context-menu-content')} [role=separator]`,
  menuKbd: `${slot('menu-content')} [data-slot=kbd], ${slot('context-menu-content')} [data-slot=kbd], ${slot('menu-content')} kbd, ${slot('context-menu-content')} kbd`,
  tooltip: slot('tooltip-content'),
  // settings
  settingsNav: 'nav[aria-label=Settings] a[href="/settings/general"]',
  settingsNavSelected: '[data-slot=sidebar-content] nav a[data-status=active]',
  settingsSearch: 'input[aria-label="Search settings"]',
  pageTitle: `${slot('sidebar-panel')} h1`,
  pageDescription: `${slot('sidebar-panel')} h1 + p`,
  sectionTitle: `${slot('sidebar-panel')} h2`,
  sectionDescription: `${slot('sidebar-panel')} h2 + p`,
  card: slot('card'),
  row: slot('settings-row'),
  rowLabel: page => page.locator('[data-slot=settings-row]').filter({ visible: true }).first().locator('div.text-sm.font-medium').first(),
  rowDescription: page => page.locator('[data-slot=settings-row]').filter({ visible: true }).first().locator('div.text-muted-foreground-2, div.text-muted-foreground-1').first(),
  switchOn: slot('switch', '[data-checked]:not([data-disabled])'),
  switchOff: slot('switch', '[data-unchecked]:not([data-disabled])'),
  select: `${slot('settings-row')} button[data-slot=menu-trigger]`,
  input: `${slot('settings-row')} input[data-slot=input]`,
  rowButton: `${slot('settings-row')} button[data-slot=button]`,
  segmented: '[role=group][aria-label="Settings scope"] button:not([data-selected])',
  segmentedOn: '[role=group][aria-label="Settings scope"] button[data-selected]',
  badge: slot('badge'),
  table: '[role=table]',
  tableHeader: '[role=columnheader]',
  tableRow: nth('[role=table] [role=row]', 1),
};
const openMenu = (sel, wait_ = 800) => async h => { await home(h); await vis(h.page, sel).click(); await wait(h.page, wait_); };
const openSearch = async h => { await home(h); await btn(h.page, 'Search').click(); await wait(h.page, 1000); };

// One shot per part and state: `{page}-{part}-{state}`, measured as `{part}-{state}`.
function states(groups) {
  const out = [];
  for (const [pageName, reveal, parts, kinds, extra = {}] of groups)
    for (const [part, spec] of Object.entries(parts))
      for (const kind of kinds)
        out.push({ name: `${pageName}-${part}-${kind}`, window: A, state: kind, reveal, parts: { [part]: spec }, ...extra,
          ...(kind === 'hover' ? { hover: part } : kind === 'focus-visible' ? { focus: part } : { force: { [part]: ['hover', 'active'] }, hover: part }) });
  return out;
}
const HFP = ['hover', 'focus-visible', 'pressed'];
const MENU = { menu: S.menu, 'menu-item': S.menuItem, 'menu-label': S.menuLabel, 'menu-separator': S.menuSep, 'menu-kbd': S.menuKbd };
const MENU_OPT = ['menu-label', 'menu-separator', 'menu-kbd'];

const SETTINGS_PANES = ['general', 'appearance', 'profile', 'referrals', 'experiments', 'notifications', 'shortcuts', 'models', 'projects',
  'mcp', 'integrations', 'api', 'devices', 'import', 'capy', 'review/repositories', 'review/agent-config',
  'org/general', 'org/members', 'org/billing', 'org/usage', 'org/activity', 'org/audit-log'];
const SETTINGS_PARTS = { 'page-title': S.pageTitle, 'page-description': S.pageDescription, 'section-title': S.sectionTitle, 'section-description': S.sectionDescription,
  card: S.card, 'settings-row': S.row, 'row-label': S.rowLabel, 'row-description': S.rowDescription, 'switch-on': S.switchOn, 'switch-off': S.switchOff,
  select: S.select, input: S.input, 'row-button': S.rowButton, badge: S.badge, table: S.table, 'table-header': S.tableHeader, 'table-row': S.tableRow };

export const SHOTS = [
  { name: 'home', window: A, reveal: async () => {},
    parts: { sidebar: S.sidebar, 'tab-strip': S.tabStrip, tab: S.tab, 'new-tab': S.newTab, 'back-button': S.back, 'update-button': S.update, 'home-mark': S.home,
      'icon-button': S.iconButton, 'nav-row': S.navRow, 'nav-row-selected': S.navRowSelected, kbd: S.kbd, 'section-header': S.sectionHeader, 'project-group': S.projectGroup,
      'thread-row': S.threadRow, 'setup-card': S.setupCard, 'setup-step': S.setupStep, 'setup-button': S.setupButton, 'user-button': S.user, avatar: S.avatar, panel: S.panel,
      composer: S.composer, 'composer-editor': S.editor, 'send-button': S.send, 'voice-button': S.voice, 'add-button': S.add, 'config-button': S.config,
      'model-button': S.model, 'project-button': S.project, 'run-on-button': S.runOn, 'repos-button': S.repos },
    optionalParts: ['update-button', 'setup-card', 'setup-step', 'setup-button', 'project-group', 'repos-button', 'avatar'] },
  // `after` undoes only what reveal did: Meta+B toggles, so pressing it when Close sidebar was never clicked would close the sidebar.
  { name: 'sidebar-hidden', window: A, reveal: async h => { h.sidebarClosed = false; await btn(h.page, 'Close sidebar').click(); h.sidebarClosed = true; await wait(h.page, 900); },
    after: async h => { if (!h.sidebarClosed) return; h.sidebarClosed = false; await h.page.keyboard.press('Meta+B'); await wait(h.page, 800); }, parts: { panel: S.panel } },
  { name: 'threads', window: A, reveal: h => go(h, '/threads'),
    parts: { 'segmented-item': page => vis(page, 'button:has-text("All threads")'), 'segmented-active': page => vis(page, 'button:has-text("My threads")'),
      'filter-chip': page => btn(page, 'Remove Participants filter').locator('xpath=..'), 'list-section': slot('collapsible-trigger'),
      'list-row': page => page.locator(`${slot('sidebar-panel')} ${slot('collapsible-panel')} ${slot('context-menu-trigger')}`).first(),
      badge: `${slot('sidebar-panel')} ${slot('badge')}`, 'toolbar-icon-button': 'button[aria-label="Filter threads"]', 'nav-row-selected': S.navRowSelected },
    optionalParts: ['filter-chip', 'list-row', 'badge'] },
  { name: 'pull-requests', window: A, reveal: h => go(h, '/pulls'),
    parts: { 'list-row': page => page.locator(`${slot('sidebar-panel')} ${slot('collapsible-panel')} ${slot('context-menu-trigger')}`).first(), 'list-section': slot('collapsible-trigger'),
      'diff-stat': page => page.locator(`${slot('sidebar-panel')} .text-diff-add, ${slot('sidebar-panel')} [class*=text-diff-add]`).first() },
    optionalParts: ['list-row', 'diff-stat'] },
  { name: 'automations', window: A, reveal: h => go(h, '/automations'),
    parts: { 'template-card': page => page.locator(`${slot('sidebar-panel')} ${slot('card')}, ${slot('sidebar-panel')} button.rounded-\\(--radius-card\\)`).first(),
      'empty-text': page => page.getByText('No automations yet', { exact: true }).first() },
    optionalParts: ['template-card', 'empty-text'] },
  { name: 'memory', window: A, reveal: h => more(h, 'Memory'), parts: {} },
  { name: 'drive', window: A, reveal: h => more(h, 'Drive'), parts: {} },
  { name: 'user-menu', window: A, reveal: openMenu(`${slot('sidebar-content')} button[data-slot=menu-trigger]:has(img)`), parts: { ...MENU, 'menu-item-danger': S.menuItemDanger }, optionalParts: MENU_OPT },
  { name: 'more-menu', window: A, reveal: openMenu(S.navMore), parts: MENU, optionalParts: MENU_OPT },
  { name: 'add-menu', window: A, reveal: openMenu(S.add), parts: MENU, optionalParts: MENU_OPT },
  { name: 'config-menu', window: A, reveal: openMenu(S.config), parts: MENU, optionalParts: MENU_OPT },
  { name: 'model-menu', window: A, reveal: openMenu(S.model, 1000),
    parts: { menu: S.menu, 'menu-search': `${slot('menu-content')} input`, 'empty-title': page => page.getByText('No models available', { exact: true }).first(),
      'button-outline': `${slot('menu-content')} button[data-slot=button]` }, optionalParts: ['menu-search', 'empty-title', 'button-outline'] },
  { name: 'project-menu', window: A, reveal: openMenu(S.project), parts: { ...MENU, 'menu-search': `${slot('menu-content')} input` }, optionalParts: [...MENU_OPT, 'menu-search'] },
  { name: 'run-on-menu', window: A, reveal: openMenu(S.runOn), parts: MENU, optionalParts: MENU_OPT },
  { name: 'repos-menu', window: A, reveal: openMenu(S.repos), parts: MENU, optionalParts: MENU_OPT },
  { name: 'thread-options-menu', window: A, reveal: openMenu('button[aria-label="Thread options"]'), parts: MENU, optionalParts: MENU_OPT },
  { name: 'tab-context-menu', window: A, reveal: async h => { await home(h); await vis(h.page, S.tab).click({ button: 'right' }); await wait(h.page, 800); },
    parts: { 'context-menu': slot('context-menu-content'), 'context-item': nth(`${slot('context-menu-content')} [role=menuitem]`, 0), 'menu-kbd': S.menuKbd }, optionalParts: ['menu-kbd'] },
  { name: 'thread-context-menu', window: A, reveal: async h => { await home(h); await vis(h.page, S.threadRow).click({ button: 'right' }); await wait(h.page, 800); },
    parts: { 'context-menu': slot('context-menu-content'), 'context-item': nth(`${slot('context-menu-content')} [role=menuitem]`, 0), 'menu-item-danger': S.menuItemDanger } },
  { name: 'search-palette', window: A, reveal: openSearch,
    parts: { palette: slot('command-menu-content'), 'palette-input': `${slot('command-menu-content')} [role=combobox]`, 'palette-row': nth(`${slot('command-menu-content')} [role=option]`, 1),
      'palette-row-selected': `${slot('command-menu-content')} [role=option][data-highlighted], ${slot('command-menu-content')} [role=option][aria-selected=true]`,
      'palette-tab': page => page.locator(`${slot('command-menu-content')} button`).filter({ hasText: /^Threads$/ }).first(),
      'palette-tab-selected': page => page.locator(`${slot('command-menu-content')} button`).filter({ hasText: /^All$/ }).first(),
      kbd: `${slot('command-menu-content')} kbd, ${slot('command-menu-content')} [data-slot=kbd]`, scrim: '[data-slot=command-menu-backdrop], [data-slot=dialog-backdrop], [data-slot=dialog-overlay]' },
    optionalParts: ['palette-row-selected', 'palette-tab', 'palette-tab-selected', 'kbd', 'scrim'] },
  { name: 'search-palette-empty', window: A, state: 'empty', reveal: async h => { await openSearch(h); await h.page.keyboard.type('zzqxv'); await wait(h.page, 1000); },
    parts: { palette: slot('command-menu-content') } },
  { name: 'tooltip', window: A, state: 'hover', reveal: async h => { await home(h); await vis(h.page, S.iconButton).hover(); await wait(h.page, 1400); },
    parts: { tooltip: S.tooltip, 'icon-button': S.iconButton } },
  { name: 'customize-sidebar-dialog', window: A, reveal: async h => { await home(h); await vis(h.page, S.navMore).click(); await wait(h.page, 600);
    await h.page.locator('[role=menuitem]').filter({ hasText: /^Customize sidebar/ }).first().click(); await wait(h.page, 1100); },
    parts: { dialog: '[role=dialog]', scrim: '[data-slot=dialog-backdrop], [data-slot=dialog-overlay]', 'dialog-title': '[role=dialog] h2', 'button-accent': '[role=dialog] button[data-slot=button]:last-of-type' },
    optionalParts: ['scrim', 'dialog-title', 'button-accent'] },
  { name: 'tabs-two', window: A, reveal: async h => { await home(h); h.tabsBefore = await h.page.locator('[role=tab]').count(); await btn(h.page, 'New tab').click(); await wait(h.page, 1200); await h.page.mouse.move(700, 790); },
    // The new tab is the active one (raised on the popover fill with a hairline); its close button shows on hover.
    // Close it only if reveal really added a tab, so a failed reveal never closes one of the owner's tabs.
    after: async h => { const { page } = h; const before = h.tabsBefore; h.tabsBefore = undefined;
      if (before === undefined || await page.locator('[role=tab]').count() <= before) return;
      const t = page.locator('[role=tab]').last(); await t.hover(); await wait(page, 400); await t.locator('button[aria-label="Close tab"]').click({ force: true }); await wait(page, 900); },
    parts: { 'tab-active': '[role=tab].shadow-card', tab: '[role=tab].border-transparent', 'tab-close': page => page.locator('[role=tab]').last().locator('button[aria-label="Close tab"]') },
    optionalParts: ['tab-close'] },

  // ---- settings: every pane, then the states in it
  ...SETTINGS_PANES.map(p => ({ name: `settings-${p.replace('/', '-')}`, window: A, reveal: h => settings(h, p),
    parts: { 'settings-nav': S.settingsNav, 'settings-nav-selected': S.settingsNavSelected, 'settings-search': S.settingsSearch, ...SETTINGS_PARTS,
      'segmented-item': S.segmented, 'segmented-active': S.segmentedOn },
    optionalParts: [...Object.keys(SETTINGS_PARTS), 'segmented-item', 'segmented-active', 'settings-nav'] })),
  { name: 'settings-search-filled', window: A, state: 'filled', reveal: async h => { await settings(h, 'general'); await vis(h.page, S.settingsSearch).click(); await h.page.keyboard.type('theme'); await wait(h.page, 1000); },
    parts: { 'settings-search': S.settingsSearch }, after: async ({ page }) => { await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); } },
  { name: 'settings-select-open', window: A, reveal: async h => { await settings(h, 'capy'); await vis(h.page, S.select).click(); await wait(h.page, 800); },
    parts: { ...MENU, 'menu-item-checked': `${slot('menu-content')} [role=menuitemradio][aria-checked=true], ${slot('menu-content')} [role=menuitemcheckbox][aria-checked=true], ${slot('menu-content')} [data-checked]` },
    optionalParts: [...MENU_OPT, 'menu-item-checked'] },

  // ---- the gallery at /design: Capy's own specimens on fixture data
  { name: 'design-buttons', window: A, reveal: h => design(h, 'Buttons'),
    parts: { 'button-ghost': sec('Buttons', 'button:text-is("Ghost")'), 'button-soft': sec('Buttons', 'button:text-is("Soft")'), 'button-outline': sec('Buttons', 'button:text-is("Outline")'),
      'button-solid': sec('Buttons', 'button:text-is("Solid")'), 'button-selected': sec('Buttons', 'button:text-is("Selected")'), 'button-accent': sec('Buttons', 'button:text-is("Accent")'),
      'button-inverse': sec('Buttons', 'button:text-is("Inverse")'), 'button-danger': sec('Buttons', 'button:text-is("Delete")'), 'button-danger-text': sec('Buttons', 'button:text-is("Discard")'),
      'button-xs': sec('Buttons', 'button:text-is("Compact")'), 'button-base': sec('Buttons', 'button:text-is("Large")'), 'design-title': 'h1', 'design-section-title': 'section > h2' } },
  { name: 'design-buttons-loading', window: A, reveal: async h => { await design(h, 'Buttons'); await h.page.mouse.wheel(0, 360); await wait(h.page, 600); },
    parts: { 'button-loading': sec('Buttons', 'button:has-text("Publishing")') }, optionalParts: ['button-loading'] },
  { name: 'design-badges', window: A, reveal: h => design(h, 'Badges'),
    parts: { badge: sec('Badges', '[data-slot=badge]', 0), 'badge-running': sec('Badges', '[data-slot=badge]', 1), 'badge-failed': sec('Badges', '[data-slot=badge]', 2),
      'badge-passing': sec('Badges', '[data-slot=badge]', 4), 'badge-ghost': sec('Badges', '[data-slot=badge]', 10), 'badge-filled': sec('Badges', '[data-slot=badge]', 21),
      'badge-count': sec('Badges', '[aria-label$="unread mention of you"]'), 'badge-interactive': sec('Badges', 'button[data-slot=badge]') } },
  { name: 'design-avatar', window: A, reveal: h => design(h, 'Avatar'), parts: { avatar: sec('Avatar', 'span[aria-label].rounded', 1), 'avatar-xs': sec('Avatar', 'span[aria-label].rounded', 0), 'avatar-initials': sec('Avatar', 'span[aria-label="Ada Lovelace"]', 1) } },
  { name: 'design-alerts', window: A, reveal: h => design(h, 'Alerts'),
    parts: { alert: sec('Alerts', '[data-slot=alert]', 0), 'alert-title': sec('Alerts', '[data-slot=alert-title]', 0), 'alert-description': sec('Alerts', '[data-slot=alert-description]', 0),
      'alert-2': sec('Alerts', '[data-slot=alert]', 1), 'alert-3': sec('Alerts', '[data-slot=alert]', 2) }, optionalParts: ['alert-2', 'alert-3'] },
  { name: 'design-cards', window: A, reveal: h => design(h, 'Cards'), parts: { card: sec('Cards', '[data-slot=card]', 0), 'card-header': sec('Cards', '[data-slot=card-header]', 0) }, optionalParts: ['card-header'] },
  { name: 'design-inputs', window: A, reveal: h => design(h, 'Inputs'),
    parts: { input: sec('Inputs', 'input[placeholder="Thread title"]'), 'input-filled': sec('Inputs', 'input[data-slot=input]', 1), 'input-invalid': sec('Inputs', 'input[aria-invalid=true]'),
      'input-disabled': sec('Inputs', 'input[data-slot=input]', 3), 'input-sm': sec('Inputs', 'input[placeholder="Branch prefix"]'), 'input-xs': sec('Inputs', 'input[placeholder="0 9 * * 1-5"]') } },
  { name: 'design-form-fields', window: A, reveal: h => design(h, 'Form fields'), parts: { 'field-label': sec('Form fields', 'label', 0), textarea: sec('Form fields', 'textarea', 0) }, optionalParts: ['textarea'] },
  { name: 'design-table', window: A, reveal: h => design(h, 'Table'),
    parts: { table: sec('Table', '[role=table]', 0), 'table-header': sec('Table', '[role=columnheader]', 0), 'table-row': sec('Table', '[role=row]', 1), 'table-cell': sec('Table', '[role=cell]', 0) } },
  { name: 'design-switch-and-checkbox', window: A, reveal: h => design(h, 'Switch and checkbox'),
    parts: { 'switch-on': sec('Switch and checkbox', '[role=switch][aria-checked=true]'), 'switch-off': sec('Switch and checkbox', '[role=switch][aria-checked=false]:not([aria-disabled])'),
      'switch-disabled': sec('Switch and checkbox', '[role=switch][aria-disabled=true]'), 'checkbox-on': sec('Switch and checkbox', '[role=checkbox][aria-checked=true]'),
      'checkbox-off': sec('Switch and checkbox', '[role=checkbox][aria-checked=false]:not([aria-disabled])'), 'checkbox-disabled': sec('Switch and checkbox', '[role=checkbox][aria-disabled=true]') } },
  { name: 'design-kbd', window: A, reveal: h => design(h, 'Kbd'), parts: { kbd: sec('Kbd', 'kbd, [data-slot=kbd]', 0) } },
  { name: 'design-tooltip', window: A, state: 'hover', reveal: async h => { await design(h, 'Tooltip'); await sec('Tooltip', 'button, [data-slot=tooltip-trigger]', 0)(h.page).hover(); await wait(h.page, 1200); },
    parts: { tooltip: S.tooltip } },
  { name: 'design-preview-card', window: A, reveal: h => design(h, 'Preview card'), parts: {} },
  { name: 'design-dialog', window: A, reveal: h => design(h, 'Dialog'), parts: { 'dialog-trigger': sec('Dialog', 'button[data-slot=dialog-trigger]', 0) } },
  { name: 'delete-confirmation', window: A, reveal: async h => { await design(h, 'Dialog'); await sec('Dialog', 'button:text-is("Delete thread")')(h.page).click(); await wait(h.page, 900); },
    parts: { 'confirm-dialog': '[role=dialog], [role=alertdialog]', scrim: '[data-slot=dialog-backdrop], [data-slot=dialog-overlay], [data-slot=alert-dialog-backdrop]',
      'dialog-title': '[role=dialog] h2, [role=alertdialog] h2', 'dialog-description': '[role=dialog] p, [role=alertdialog] p',
      'button-danger': page => page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Delete thread$/ }).first(),
      'button-ghost': page => page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Cancel$/ }).first() },
    optionalParts: ['scrim', 'dialog-description'], after: async ({ page }) => { await page.keyboard.press('Escape'); await wait(page, 400); } },
  { name: 'paged-dialog', window: A, reveal: async h => { await design(h, 'Dialog'); await sec('Dialog', 'button:text-is("Paged dialog")')(h.page).click(); await wait(h.page, 900); },
    parts: { dialog: '[role=dialog]' }, after: async ({ page }) => { await page.keyboard.press('Escape'); await wait(page, 400); } },
  { name: 'design-sheet-and-drawer', window: A, reveal: h => design(h, 'Sheet and drawer'), parts: {} },
  { name: 'toast', window: A, reveal: async h => { await design(h, 'Toast'); await sec('Toast', 'button:text-is("Thread created")')(h.page).click(); await wait(h.page, 1100); },
    parts: { toast: '[data-sonner-toast] [class*="z-(--z-toast)"]', 'toast-title': '[data-sonner-toast] p.font-medium', 'toast-description': '[data-sonner-toast] div.text-muted-foreground-2',
      'toast-button': '[data-sonner-toast] button[data-slot=button]' }, optionalParts: ['toast-button'] },
  { name: 'toast-error', window: A, reveal: async h => { await design(h, 'Toast'); await sec('Toast', 'button:text-is("Error")')(h.page).click(); await wait(h.page, 1100); },
    parts: { 'toast-error': '[data-sonner-toast] [class*="z-(--z-toast)"]' } },
  { name: 'design-loading', window: A, reveal: h => design(h, 'Loading'), parts: {} },
  { name: 'design-connect-wait', window: A, reveal: h => design(h, 'Connect wait'), parts: {} },
  { name: 'design-provider-card', window: A, reveal: h => design(h, 'Provider card'), parts: {} },
  { name: 'design-collapsible', window: A, reveal: h => design(h, 'Collapsible'), parts: { collapsible: sec('Collapsible', '[data-slot=collapsible-trigger]', 0) }, optionalParts: ['collapsible'] },
  { name: 'design-menus', window: A, reveal: h => design(h, 'Menus'),
    parts: { menu: sec('Menus', '[role=menu], [data-slot=menu-content]', 0), 'menu-item': sec('Menus', '[role=menuitem]', 0), 'menu-label': sec('Menus', '[data-slot=menu-label]', 0) }, optionalParts: ['menu', 'menu-item', 'menu-label'] },
  { name: 'design-composer', window: A, reveal: h => design(h, 'Composer'), parts: { composer: sec('Composer', '[data-slot=composer]', 0) }, optionalParts: ['composer'] },
  { name: 'conversation', window: A, reveal: h => design(h, 'Jam chat'),
    parts: { 'user-message': sec('Jam chat', '[data-slot=user-message]', 0), 'agent-message': sec('Jam chat', '[data-slot=agent-message]', 0), 'chat-stamp': sec('Jam chat', '[data-slot=chat-stamp]', 0),
      'activity-line': sec('Jam chat', '[data-slot=activity-line] button', 0), 'message-text': sec('Jam chat', '[data-slot=agent-message] p', 0), 'file-chip': sec('Jam chat', 'button[aria-label^=Download]', 0),
      alert: sec('Jam chat', '[data-slot=alert]', 0) }, optionalParts: ['file-chip', 'alert'] },
  { name: 'conversation-hover', window: A, state: 'hover', reveal: h => design(h, 'Jam chat'), hover: 'agent-message', parts: { 'agent-message': sec('Jam chat', '[data-slot=agent-message]', 0) } },
  { name: 'tool-rows', window: A, reveal: h => design(h, 'Tool rows'),
    parts: { 'work-group': sec('Tool rows', '[data-slot=collapsible-trigger]', 1), 'tool-row': sec('Tool rows', '[data-slot=collapsible] [role=button]', 1) } },
  { name: 'tool-rows-more', window: A, reveal: async h => { await design(h, 'Tool rows'); await h.page.mouse.wheel(0, 700); await wait(h.page, 700); }, parts: {} },
  { name: 'update-error-rows', window: A, reveal: h => design(h, 'Update, error, and divider rows'), parts: {} },
  { name: 'desktop-request', window: A, reveal: h => design(h, 'Desktop request'), parts: {} },
  { name: 'device-access', window: A, reveal: h => design(h, 'Device access'), parts: {} },
  { name: 'clarify', window: A, reveal: h => design(h, 'Clarify'), parts: {} },
  { name: 'design-filter-chips', window: A, reveal: h => design(h, 'Filter chips'), parts: {} },
  { name: 'design-thread-status', window: A, reveal: h => design(h, 'Thread status'), parts: {} },
  { name: 'diff', window: A, reveal: h => design(h, 'Diff'), parts: {} },
  { name: 'markdown', window: A, reveal: h => design(h, 'Markdown'),
    parts: { 'markdown-h1': sec('Markdown', '[data-component=markdown] h1', 0), 'markdown-h2': sec('Markdown', '[data-component=markdown] h2', 0), 'markdown-p': sec('Markdown', '[data-component=markdown] p', 0),
      'inline-code': sec('Markdown', '[data-component=markdown] p code', 0), 'code-block': sec('Markdown', '[data-component=markdown] pre', 0), link: sec('Markdown', '[data-component=markdown] a', 0) },
    optionalParts: ['inline-code', 'code-block', 'link', 'markdown-h2'] },
  { name: 'markdown-code', window: A, reveal: async h => { await design(h, 'Markdown'); await h.page.mouse.wheel(0, 700); await wait(h.page, 700); }, parts: {} },
  { name: 'crash-card', window: A, reveal: h => design(h, 'Crash card'), parts: {} },

  // ---- states, one part per shot: hover with the real pointer, focus-visible with real keyboard
  // focus, pressed with :active forced through CDP. Each is a full-window screenshot too.
  ...states([
    ['app', async () => {}, { 'icon-button': S.iconButton, 'nav-row': S.navRow, 'thread-row': S.threadRow, tab: S.tab, 'new-tab': S.newTab,
      'model-button': S.model, 'project-button': S.project, 'add-button': S.add, 'send-button': S.send, 'user-button': S.user, 'setup-step': S.setupStep }, HFP],
    ['settings', async h => settings(h, 'capy'), { 'switch-off': S.switchOff, select: S.select, 'row-button': S.rowButton, 'settings-nav': S.settingsNav, segmented: S.segmented }, HFP],
    ['settings', async h => settings(h, 'capy'), { 'settings-search': S.settingsSearch, input: S.input }, ['hover', 'focus-visible']],
    ['notifications', async h => settings(h, 'notifications'), { 'switch-on': S.switchOn }, HFP],
    ['design', async h => design(h, 'Buttons'), { 'button-accent': sec('Buttons', 'button:text-is("Accent")'), 'button-outline': sec('Buttons', 'button:text-is("Outline")'),
      'button-soft': sec('Buttons', 'button:text-is("Soft")'), 'button-ghost': sec('Buttons', 'button:text-is("Ghost")'), 'button-inverse': sec('Buttons', 'button:text-is("Inverse")'),
      'button-danger': sec('Buttons', 'button:text-is("Delete")') }, HFP],
    ['design', async h => design(h, 'Switch and checkbox'), { 'checkbox-off': sec('Switch and checkbox', '[role=checkbox][aria-checked=false]:not([aria-disabled])') }, HFP],
    ['design', async h => design(h, 'Inputs'), { input: sec('Inputs', 'input[placeholder="Thread title"]') }, ['hover', 'focus-visible']],
    ['menu', openMenu(S.navMore), { 'menu-item': nth(`${slot('menu-content')} [role=menuitem]`, 1) }, ['hover']],
    ['palette', openSearch, { 'palette-row': nth(`${slot('command-menu-content')} [role=option]`, 2) }, ['hover']],
  ]),
];


// ---- the agent run, taken by run.mjs. The owner approved (2026-10-25) harmless test prompts in a fresh
// thread only, in a project of its own on the scratch repository ~/.design-systems/harness-scratch/capy/
// (docs/CAPTURE.md), running on This Mac: never the owner's projects, repositories or threads, and never the
// cloud. The project is made once by hand (New project > Folder on a machine > that folder, named
// RUN_PROJECT); each theme's run starts one new thread in it, so the thread view is a real run, not the gallery.
// Capy 0.5.0 runs the thread in the folder itself (Run on: the paired Mac, Current checkout), with the
// account's connected Claude Code and the model the composer already holds; neither is changed here.
// finish() puts the composer's project and draft back; the run-on choice and the model are only compared.
const RUN_PROJECT = process.env.RUN_PROJECT || 'Capture scratch';
const RUN_DIR = '/.design-systems/harness-scratch/capy';
const TOAST = { toast: '[data-sonner-toast] [class*="z-(--z-toast)"]', 'toast-title': '[data-sonner-toast] p.font-medium', 'toast-description': '[data-sonner-toast] div.text-muted-foreground-2' };
const DRAFT_KEY = 'capy-web:new-thread-draft';
const KEPT = ['capy-web:new-thread-run-on', 'capy-web:last-model'];
let before = null;
const kept = page => page.evaluate(keys => keys.map(k => `${k}=${localStorage.getItem(k)}`).join('\n'), KEPT);
async function pickProject(page, name) {
  if ((await btn(page, 'Project').innerText()).trim() === name) return;
  await btn(page, 'Project').click(); await wait(page, 700);
  // The name is matched literally: a project called `Client (web)` must not be read as a pattern.
  const literal = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  await page.locator('[role=menuitem]').filter({ hasText: new RegExp(`^${literal}$`) }).first().click(); await wait(page, 1200);
  const now = (await btn(page, 'Project').innerText()).trim();
  if (now !== name) throw new Error(`project is ${now}, not ${name}`);
}
async function clearEditor(page) {
  await vis(page, S.editor).click(); await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); await wait(page, 400);
}
async function type(page, text, label) {
  const composer = page.locator(S.composer).filter({ visible: true }).last();
  await composer.locator(S.editor).click(); await page.keyboard.type(text, { delay: 10 }); await wait(page, 300);
  await composer.locator(`button[aria-label=${label}]`).click(); await wait(page, 300);
}
// An approval is allowed only when its card shows one of the exact commands or files this run's prompts ask
// for, in the scratch folder, and nothing else that could be a command (approve.mjs). Anything else is denied.
const RUN_ROOT = resolvePath(process.env.HOME || '', RUN_DIR.slice(1));
const ALLOW = allowance({ root: RUN_ROOT, rel: RUN_DIR.slice(1), files: ['hello.txt'] });
async function approveInside({ page }) {
  const allow = page.locator('button').filter({ visible: true }).filter({ hasText: /^(Allow|Approve|Accept)\b/ }).last();
  // The request card, read outwards from the button: the first container naming a target and the next wider one.
  const texts = await allow.evaluate(ancestors).catch(() => []);
  if (!approvableCard(texts, ALLOW)) return false;
  await allow.click(); await wait(page, 800);
  return true;
}
// Any sign that the run is still working: the Stop run button, the tab's Working glyph or a live shimmer.
const STOP = 'button[aria-label="Stop run"]';
const busy = async page => (await page.locator(`${STOP}, svg[aria-label=Working][data-state=working], ${slot('shimmer-text')}[data-state=live]`).filter({ visible: true }).count()) > 0;
export const RUN = {
  window: 'app',
  async start(h) {
    const { page } = h;
    await home(h);
    before = { draft: await page.evaluate(k => localStorage.getItem(k), DRAFT_KEY), project: (await btn(page, 'Project').innerText()).trim(), kept: await kept(page) };
    await pickProject(page, RUN_PROJECT);
    // The project must run on this Mac in the scratch folder, never in the cloud or another checkout.
    await btn(page, 'Run on').click(); await wait(page, 700);
    const mac = page.locator('[role=menuitem], [role=menuitemradio], [role=menuitemcheckbox]').filter({ visible: true }).filter({ hasText: 'This Mac' }).first();
    const target = await mac.innerText().catch(() => '');
    // The current choice, not just the This Mac row: that row names the scratch folder whatever is selected, so
    // another paired machine or checkout would pass a check of its text alone. Fail closed unless the This Mac
    // row is the checked one or the Run on button itself names the whole scratch path (a name fragment such
    // as "capy" would also match another machine called capy-build).
    const checked = await mac.evaluate(el => el.getAttribute('aria-checked') === 'true' || el.getAttribute('data-state') === 'checked').catch(() => false);
    await closeAll(page);
    const runOn = (await btn(page, 'Run on').innerText()).trim();
    if (!target.includes(RUN_DIR.slice(1)) || /^Cloud/.test(runOn) || !(checked || runOn.includes(RUN_DIR.slice(1)))) throw new Error(`Run on is ${runOn} (${target.replace(/\s+/g, ' ')}), not this Mac in ~${RUN_DIR}`);
    await clearEditor(page);
  },
  async finish(h) {
    const { page } = h;
    if (!before) return;
    // A run still going (a step past TIMEOUT, or a frame that failed) is stopped first, from its own thread:
    // Capy's Stop run button (role button, name "Stop run", in the composer; disabled for a moment while the
    // thread starts, so the click waits for it). Stopped, the thread shows "Worked for Ns" with no reply, the
    // composer's Stop run button gives way to Voice input, and the Working glyph and live shimmer go
    // (seen live on 2026-11-07). A run that will not stop fails the capture (stop.mjs).
    if (await stopRun({ running: () => busy(page), stop: () => vis(page, STOP).click({ timeout: 15000 }), wait: ms => wait(page, ms) })) console.log('stopped the agent run');
    await closeAll(page);
    for (const t of await page.locator('[data-sonner-toast] button[aria-label^=Close], [data-sonner-toast] [data-close-button]').all()) await t.click().catch(() => {});
    // The inspector pane was opened in the run's own thread; close it there before leaving. Only when its Close
    // pane button can take a click: a run that stopped before the inspector step leaves the pane slid out of view,
    // its button covered by the header, and a plain click would wait out its timeout and skip the restore below.
    const close = page.locator('button[aria-label="Close pane"]').filter({ visible: true }).first();
    const closable = await close.click({ trial: true, timeout: 2000 }).then(() => true, () => false);
    if ((await path(page)).startsWith('/thread/') && closable) { await close.click(); await wait(page, 600); }
    await home(h);
    await pickProject(page, before.project);
    await clearEditor(page);
    // The draft goes back through localStorage and a reload, never the keyboard: a typed "\n" is Enter, which
    // would submit the composer and start a real thread (draft.mjs).
    await restoreDraft({
      saved: before.draft,
      write: v => page.evaluate(([k, val]) => localStorage.setItem(k, val), [DRAFT_KEY, v]),
      reload: async () => { await page.reload(); await wait(page, 1500); },
      read: () => page.evaluate(k => localStorage.getItem(k), DRAFT_KEY),
    });
    const project = (await btn(page, 'Project').innerText()).trim();
    if (project !== before.project) throw new Error(`project is ${project} after the restore, not ${before.project}`);
    if (await kept(page) !== before.kept) throw new Error(`run-on or model changed:\n${await kept(page)}\nwas\n${before.kept}`);
    await page.mouse.move(700, 790);
  },
  async state({ page }) {
    // A refusal (the plan dialog Cloud shows without a plan, or a failed start) ends the run at once.
    if (await page.getByText('Put Capy to work').filter({ visible: true }).count()) throw new Error('Capy asked for a plan: the thread was going to the cloud');
    const failed = page.locator('[data-sonner-toast]').filter({ visible: true }).filter({ hasText: /^Failed/ });
    if (await failed.count()) throw new Error(`Capy refused: ${(await failed.first().innerText()).replace(/\s+/g, ' ')}`);
    if (!(await path(page)).startsWith('/thread/')) return 'starting';
    if (await page.locator('button').filter({ visible: true }).filter({ hasText: /^(Allow|Approve|Accept)\b/ }).count()) return 'approval';
    const running = await page.locator(`${STOP}, svg[aria-label=Working][data-state=working]`).filter({ visible: true }).count();
    return page.evaluate(running => {
      const live = [...document.querySelectorAll('[data-slot=shimmer-text][data-state=live]')].map(e => e.textContent.trim());
      const msgs = [...document.querySelectorAll('[data-slot=user-message], [data-slot=agent-message]')];
      const replied = msgs.length && msgs.at(-1).getAttribute('data-slot') === 'agent-message';
      // Between two turns the Stop button can drop for a moment; the run is over only once a reply follows the
      // last prompt and nothing is still shimmering.
      if (!running && !live.length && replied) return 'done';
      const work = live.filter(t => !/^Work/.test(t));
      if (work.some(t => !/^Think/.test(t))) return 'tool';
      if (replied) return 'streaming';
      return work.length ? 'thinking' : 'working';
    }, running);
  },
  async reject({ page }) { await page.locator('button').filter({ visible: true }).filter({ hasText: /^(Deny|Reject|Skip)\b/ }).last().click().catch(() => {}); await wait(page, 800); },
  steps: [
    { name: 'list-files', send: async ({ page }) => type(page, 'List the files in this folder.', 'Start'), approve: approveInside },
    { name: 'create-file', send: async ({ page }) => type(page, 'Create hello.txt here with one line.', 'Send'), approve: approveInside },
    // Not a prompt: the thread's right pane (Overview, Diffs), Capy's inspector, opened once the run is over.
    { name: 'inspector', send: async ({ page }) => { await btn(page, 'Open pane').click(); await wait(page, 1200); } },
  ],
  parts: {
    composer: S.composer, 'send-button': `${S.composer} button[aria-label=Send], ${S.send}`, 'stop-button': STOP,
    'user-message': slot('user-message'), 'agent-message': slot('agent-message'), 'message-section': slot('message-section'),
    'message-footer': slot('message-footer'), 'chat-stamp': slot('chat-stamp'), 'activity-line': slot('activity-line'),
    'work-row': `${slot('work-group-panel')} ${slot('collapsible')}`, 'shimmer-live': `${slot('shimmer-text')}[data-state=live]`,
    'working-indicator': 'svg[aria-label=Working]', 'thread-tab': slot('preview-card-trigger'), 'thread-cost': 'button[aria-label^="Thread cost"]',
    'token-budget': 'button[aria-label*="token budget"]', 'machine-button': 'button[aria-label=Machine]', 'inline-code': `${slot('agent-message')} code`,
    'right-panel': slot('right-panel-content'), ...TOAST,
  },
  inventory: '[data-slot], [role], [aria-label]',
};
