// PRODUCT (adapt): everything in this file is Orca 1.4.237's. Another Electron app replaces it
// whole and keeps cdp.mjs, vars.mjs, shots.mjs and run.mjs as they are.
//
// A shot is { name, window, state?, reveal(h), parts, force?, hover?, focus?, optional?, optionalParts?, after?(h), keep? }:
//   name    screenshot file name, `{page}-{state}` (the theme folder is added by shots.mjs)
//   window  a key of WINDOWS
//   reveal  async ({ page, cdp, ...helpers }) => {} : clicks, keys and hovers that show the state.
//           Look, don't act: open and close, type and clear, never submit or send.
//   parts   { component: selector | [selector, nth] | (page) => Locator }: each is measured
//           (computed style) and its box recorded for crops, as `{component}-{state}`
//   force   { component: ['hover' | 'focus' | 'focus-visible' | 'active'] }: pseudo-classes forced
//           through CDP on that part before the screenshot
//   after   async (h) => {} : undo what reveal did (clear typed text, close a menu)
//   keep    overlays this shot shows instead of hiding (see OVERLAYS)
//
// The theme is not switched in the app: Orca's Theme setting is System, which follows
// prefers-color-scheme, so the capture runs with SCHEME=light or SCHEME=dark (cdp.mjs emulates it).
import { execFileSync } from 'node:child_process';

export const NAME = 'Orca';
export const WINDOWS = { app: 'Orca' };
export const SCOPES = { app: ['body'] };

// The owner's own scratch project, added for the capture (`orca repo add`), and the Orca CLI.
export const SCRATCH = `${process.env.HOME}/.design-systems/harness-scratch/orca`;
const ORCA = '/Applications/Orca.app/Contents/Resources/bin/orca';

const wait = (page, ms = 600) => page.waitForTimeout(ms);
const btn = (page, label) => page.locator(`button[aria-label="${label}"]`).filter({ visible: true }).first();
const slot = (s, extra = '') => `[data-slot="${s}"]${extra}`;

// Overlays Orca keeps on screen that would cover other parts: the update card (bottom right) and the
// "Add a setup script" callout (bottom of the sidebar). Hidden with a style the capture injects, never
// dismissed (dismissing writes to the profile). Shots that are about them list them in `keep`.
const OVERLAYS = {
  update: '.app-layout > div.fixed.bottom-10.right-4',
  setup: '[data-setup-script-prompt-layer]',
};
async function overlays(page, keep = []) {
  const css = Object.entries(OVERLAYS).filter(([k]) => !keep.includes(k)).map(([, s]) => `${s}{display:none!important}`).join('\n');
  await page.evaluate(css => {
    let st = document.getElementById('cap-hide');
    if (!st) { st = document.createElement('style'); st.id = 'cap-hide'; document.head.appendChild(st); }
    st.textContent = css;
  }, css);
}

const OPEN = '[role=menu], [role=dialog], [role=alertdialog], [role=listbox], [data-slot=popover-content], [data-slot=tooltip-content], [data-slot=hover-card-content]';
export async function closeAll(page) {
  for (let i = 0; i < 4 && await page.locator(OPEN).filter({ visible: true }).first().isVisible().catch(() => false); i++) {
    await page.keyboard.press('Escape'); await wait(page, 300);
  }
}
const inSettings = page => page.getByText('Back to app', { exact: true }).filter({ visible: true }).first();
const workspaceRow = page => page.locator('[data-worktree-card-surface]').first();
const chatTabs = page => page.locator('[data-tab-strip-slot^="structured-agent-session"]');
const terminalTab = page => page.locator('[data-tab-strip-slot]:not([data-tab-strip-slot^="structured-agent-session"])').first();

// Called before every shot: the scratch workspace, on its first (empty) chat tab, overlays hidden.
export async function home({ page }, tab = 'chat') {
  await closeAll(page);
  if (await inSettings(page).isVisible().catch(() => false)) { await inSettings(page).click(); await wait(page, 800); }
  await workspaceRow(page).click(); await wait(page, 700);
  await (tab === 'chat' ? chatTabs(page).first() : tab === 'run' ? chatTabs(page).last() : terminalTab(page)).click(); await wait(page, 700);
  await overlays(page);
  await page.mouse.move(760, 940);
}
export async function reset(h) { await home(h); }

async function settings({ page }, pane) {
  await btn(page, 'Settings').click(); await wait(page, 900);
  await overlays(page);
  if (pane) {
    await page.locator('button').filter({ hasText: new RegExp(`^${pane.replace(/[&]/g, '\\$&')}(\\s*(OPTIONAL|BETA))?$`, 'i') }).filter({ visible: true }).first().click();
    await wait(page, 900);
  }
}
const nav = (page, label) => page.locator('[data-contextual-tour-target=sidebar-navigation] button, button[data-contextual-tour-target=sidebar-tasks]').filter({ hasText: new RegExp(`^${label}`) }).first();
async function clearComposer(page) {
  await page.locator('.tiptap').first().click();
  await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); await wait(page, 500);
}

// Orca draws focus rings itself (Tailwind focus-visible:ring) and hover is plain CSS :hover, so no
// state needs help here.
export async function prepareState() {}

// A fingerprint of the state a capture must never change: the projects and workspaces in the sidebar,
// the open tabs, and the empty chat's permission mode and model. shots.mjs stops when it changes.
export async function guard(h) {
  const { page } = h;
  await home(h);
  // Projects and workspaces by count and name (agent status lines tick on their own, so they are left out).
  const rows = await page.locator('[data-worktree-card-surface]').count();
  const projects = await page.locator('button[aria-label^="Project actions for "]').evaluateAll(bs => bs.map(b => b.getAttribute('aria-label')).join(', '));
  const tabs = await page.locator('[data-tab-strip-slot]').count();
  const perm = await page.locator('button[aria-label^="Permissions"]').filter({ visible: true }).first().getAttribute('aria-label').catch(() => '?');
  const model = await page.locator('button[aria-label^="Model"]').filter({ visible: true }).first().getAttribute('aria-label').catch(() => '?');
  return `${projects} | ${rows} workspaces | tabs ${tabs} | ${perm} | ${model}`;
}

// ---- the shot list. Selectors are Orca's data-slot names (shadcn/ui), aria-labels and data attributes.
const A = 'app';
const nth = (sel, i) => [sel, i];
const S = {
  sidebar: page => page.locator('.bg-worktree-sidebar').filter({ visible: true }).first(),
  navRow: page => nav(page, 'Automations'),
  navTasks: 'button[data-contextual-tour-target=sidebar-tasks]',
  sidebarSearch: 'button[aria-label="Search worktrees and browser tabs"]',
  projectHeader: page => page.getByText('Projects', { exact: true }).filter({ visible: true }).first(),
  iconButton: 'button[aria-label="Add project"]',
  workspaceRow: '[data-worktree-card-surface]',
  workspaceBadge: '[data-worktree-card-surface] [data-slot=tooltip-trigger][data-variant=outline]',
  newBadge: page => page.locator('[data-contextual-tour-target=sidebar-navigation] *').filter({ hasText: /^New$/ }).last(),
  tab: page => terminalTab(page),
  tabActive: '[data-tab-strip-slot][data-active-tab-dock]',
  newTab: 'button[aria-label="New tab"]',
  commandButton: 'button[aria-label="Add quick command"]',
  rightTab: 'button[aria-label="Agents"]',
  rightTabActive: 'button[aria-label^="Explorer"]',
  toggleItem: nth(slot('toggle-group-item'), 1),
  toggleItemOn: slot('toggle-group-item', '[data-state=on]'),
  findField: 'input[placeholder="Find files"]',
  statusBar: page => btn(page, 'Usage').locator('xpath=ancestor::div[contains(@class,"border-t")][1]'),
  statusChip: 'button[aria-label="Usage"]',
  setupCard: '[data-setup-script-prompt-layer] .pointer-events-auto',
  composer: page => page.locator('.tiptap').filter({ visible: true }).first().locator('xpath=ancestor::div[contains(@class,"rounded-xl")][1]'),
  editor: '.tiptap',
  send: 'button[aria-label="Send"]',
  perm: 'button[aria-label^="Permissions"]',
  model: 'button[aria-label^="Model"]',
  attach: 'button[aria-label="Attach file"]',
  dictation: 'button[aria-label="Start dictation"]',
  menu: slot('dropdown-menu-content'),
  menuItem: nth(slot('dropdown-menu-item'), 0),
  menuItemDestructive: slot('dropdown-menu-item', '[data-variant=destructive]'),
  menuSep: slot('dropdown-menu-separator'),
  menuLabel: slot('dropdown-menu-label'),
  menuShortcut: slot('dropdown-menu-shortcut'),
  contextMenu: slot('context-menu-content'),
  contextItem: nth(slot('context-menu-item'), 0),
  dialog: slot('dialog-content'),
  overlay: slot('dialog-overlay'),
  tooltip: slot('tooltip-content'),
  popover: slot('popover-content'),
  // settings
  settingsNav: page => page.locator('button').filter({ hasText: /^General$/ }).filter({ visible: true }).first(),
  settingsNavSelected: page => page.locator('button').filter({ hasText: /^Agents$/ }).filter({ visible: true }).first(),
  settingsSearch: 'input[placeholder="Search settings"]',
  backToApp: page => page.getByText('Back to app', { exact: true }).filter({ visible: true }).first().locator('xpath=ancestor-or-self::button[1]'),
  // Settings groups are plain bordered divs (not shadcn's Card), titled with an h3; the page title is an h2.
  card: page => page.locator('h3').filter({ visible: true }).first().locator('xpath=ancestor::div[contains(@class,"rounded")][1]'),
  pageTitle: page => page.locator('h2.text-2xl').filter({ visible: true }).first(),
  pageDescription: page => page.locator('h2.text-2xl').filter({ visible: true }).first().locator('xpath=following-sibling::p[1]'),
  sectionTitle: page => page.locator('h3').filter({ visible: true }).first(),
  fieldLabel: nth(slot('label'), 0),
  fieldDescription: nth('p.text-xs.text-muted-foreground', 0),
  radio: nth('[role=radiogroup] [role=radio][aria-checked=false]', 0),
  radioOn: '[role=radiogroup] [role=radio][aria-checked=true]',
  switchOn: slot('switch', '[data-state=checked]'),
  switchOff: slot('switch', '[data-state=unchecked]'),
  select: slot('select-trigger'),
  input: slot('input'),
  buttonOutline: slot('button', '[data-variant=outline]'),
  buttonDefault: slot('button', '[data-variant=default]'),
  buttonGhost: slot('button', '[data-variant=ghost][data-size=sm]'),
  buttonSecondary: slot('button', '[data-variant=secondary]'),
  badge: slot('badge'),
  separator: slot('separator'),
  label: nth(slot('label'), 0),
  checkbox: slot('checkbox'),
  slider: slot('slider'),
  toggleOutline: slot('toggle-group-item', '[data-variant=outline]'),
  kbd: 'kbd',
};
const openSearch = async ({ page }) => { await btn(page, 'Search worktrees and browser tabs').click(); await wait(page, 900); };
const openRemove = async ({ page }) => {
  await page.getByText('orca', { exact: true }).filter({ visible: true }).first().hover(); await wait(page, 300);
  await btn(page, 'Project actions for orca').click(); await wait(page, 700);
  await page.locator('[role=menuitem]').filter({ hasText: /^Remove Project$/ }).first().click(); await wait(page, 900);
};
const cancelDialog = async ({ page }) => { await page.locator('[role=dialog] button').filter({ hasText: /^Cancel$/ }).first().click().catch(() => {}); await wait(page, 400); };
const rightTab = (label, back = 'Explorer') => ({
  reveal: async ({ page }) => { await page.locator(`button[aria-label^="${label}"]`).filter({ visible: true }).first().click(); await wait(page, 1200); },
  after: async ({ page }) => { await page.locator(`button[aria-label^="${back}"]`).filter({ visible: true }).first().click().catch(() => {}); await wait(page, 500); },
});

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

export const SHOTS = [
  { name: 'workspace-terminal', window: A, keep: ['setup'],
    reveal: async h => { await home(h, 'terminal'); await overlays(h.page, ['setup']); },
    parts: { sidebar: S.sidebar, 'sidebar-search': S.sidebarSearch, 'nav-row': S.navRow, 'project-header': S.projectHeader, 'icon-button': S.iconButton,
      'workspace-row': S.workspaceRow, 'workspace-badge': S.workspaceBadge, 'new-badge': S.newBadge, tab: page => chatTabs(page).first(), 'tab-active': S.tabActive,
      'new-tab': S.newTab, 'command-button': S.commandButton, 'right-tab': S.rightTab, 'right-tab-active': S.rightTabActive, 'find-field': S.findField,
      'toggle-item': S.toggleItem, 'toggle-item-on': S.toggleItemOn, 'status-bar': S.statusBar, 'status-chip': S.statusChip, 'setup-card': S.setupCard,
      terminal: '.xterm' },
    optionalParts: ['new-badge', 'status-bar', 'workspace-badge'] },
  { name: 'terminal-output', window: A,
    reveal: async h => { await home(h, 'terminal'); const { page } = h; await page.locator('.xterm').first().click(); await page.keyboard.type('clear; ls -la', { delay: 15 }); await page.keyboard.press('Enter'); await wait(page, 1500); },
    parts: { terminal: '.xterm', 'terminal-pane-title': '.xterm-screen' } },
  { name: 'chat-empty', window: A,
    reveal: async () => {},
    parts: { composer: S.composer, 'composer-editor': S.editor, 'send-button': S.send, 'permission-button': S.perm, 'model-button': S.model,
      'attach-button': S.attach, 'dictation-button': S.dictation, 'empty-title': page => page.getByText(/^Start a chat with/).filter({ visible: true }).first(),
      'empty-description': page => page.getByText(/^Ask .* to inspect code/).filter({ visible: true }).first() } },
  { name: 'chat-composer-typed', window: A, state: 'filled',
    reveal: async ({ page }) => { await page.locator(S.editor).first().click(); await page.keyboard.type('Draft text, never sent'); await wait(page, 500); },
    parts: { composer: S.composer, 'composer-editor': S.editor, 'send-button': S.send },
    after: async ({ page }) => clearComposer(page) },
  { name: 'permission-menu', window: A,
    reveal: async ({ page }) => { await page.locator(S.perm).filter({ visible: true }).first().click(); await wait(page, 700); },
    parts: { menu: S.menu, 'menu-item': S.menuItem, 'menu-item-checked': `${slot('dropdown-menu-content')} [aria-checked=true], ${slot('dropdown-menu-content')} [data-state=checked]`, 'menu-label': S.menuLabel },
    optionalParts: ['menu-item', 'menu-label', 'menu-item-checked'] },
  { name: 'model-menu', window: A,
    reveal: async ({ page }) => { await page.locator(S.model).filter({ visible: true }).first().click(); await wait(page, 900); },
    parts: { menu: page => page.locator('[role=menu], [role=dialog], [role=listbox]').filter({ visible: true }).last(), 'menu-item': S.menuItem, 'menu-label': S.menuLabel, 'menu-separator': S.menuSep },
    optionalParts: ['menu-item', 'menu-label', 'menu-separator'] },
  { name: 'new-tab-menu', window: A,
    reveal: async ({ page }) => { await page.locator(S.newTab).first().click(); await wait(page, 800); },
    parts: { menu: S.menu, 'menu-item': S.menuItem, 'menu-shortcut': S.menuShortcut, 'menu-separator': S.menuSep } },
  { name: 'search-palette', window: A, reveal: openSearch,
    parts: { palette: '[role=dialog]', 'palette-input': '[role=dialog] input', 'palette-row': '[role=dialog] [role=option]', 'palette-filter': page => page.locator('[role=dialog] button').filter({ hasText: /^Filter$/ }).first(),
      kbd: '[role=dialog] kbd', 'palette-section-heading': page => page.locator('[role=dialog]').getByText(/^Recent /i).first() },
    optionalParts: ['kbd', 'palette-section-heading'] },
  { name: 'search-palette-empty', window: A, state: 'empty',
    reveal: async h => { await openSearch(h); await h.page.keyboard.type('zzqxv'); await wait(h.page, 900); },
    parts: { palette: '[role=dialog]' } },
  { name: 'quick-command-dialog', window: A,
    reveal: async ({ page }) => { await page.locator(S.commandButton).first().click(); await wait(page, 900); },
    parts: { dialog: S.dialog, overlay: S.overlay, input: `${slot('dialog-content')} input`, select: `${slot('dialog-content')} ${slot('select-trigger')}`,
      'button-default': `${slot('dialog-content')} ${slot('button')}[data-variant=default]`, 'button-outline': `${slot('dialog-content')} ${slot('button')}[data-variant=outline]`,
      textarea: `${slot('dialog-content')} textarea`, 'dialog-close': `${slot('dialog-content')} button:has(svg):not([data-slot])` },
    optionalParts: ['select', 'button-outline', 'textarea', 'dialog-close'] },
  { name: 'create-worktree-dialog', window: A,
    reveal: async ({ page }) => { await btn(page, 'New workspace').click(); await wait(page, 1100); },
    parts: { dialog: S.dialog, overlay: S.overlay, 'button-default': `${slot('dialog-content')} ${slot('button')}[data-variant=default]`, input: `${slot('dialog-content')} input` },
    optionalParts: ['input'] },
  { name: 'remove-confirmation', window: A, reveal: openRemove, after: cancelDialog,
    parts: { 'confirm-dialog': S.dialog, 'button-destructive': `${slot('dialog-content')} button[data-variant=destructive]`,
      'button-outline': `${slot('dialog-content')} button[data-variant=outline]`, overlay: S.overlay } },
  { name: 'project-menu', window: A,
    reveal: async ({ page }) => { await page.getByText('orca', { exact: true }).filter({ visible: true }).first().hover(); await wait(page, 300); await btn(page, 'Project actions for orca').click(); await wait(page, 700); },
    parts: { menu: S.menu, 'menu-item': S.menuItem, 'menu-item-destructive': S.menuItemDestructive } },
  { name: 'workspace-context-menu', window: A,
    reveal: async ({ page }) => { await page.locator(S.workspaceRow).first().click({ button: 'right' }); await wait(page, 800); },
    parts: { 'context-menu': page => page.locator('[role=menu]').filter({ visible: true }).last(), 'context-item': nth('[role=menu] [role=menuitem]', 1), 'context-separator': '[role=menu] [role=separator]',
      'context-label': page => page.locator('[role=menu]').getByText('Workspace', { exact: true }).first() },
    optionalParts: ['context-separator', 'context-label'] },
  { name: 'tooltip', window: A, state: 'hover',
    reveal: async ({ page }) => { await page.locator(S.iconButton).first().hover(); await wait(page, 1600); },
    parts: { tooltip: S.tooltip, 'icon-button': S.iconButton } },
  { name: 'help-menu', window: A,
    reveal: async ({ page }) => { await btn(page, 'Help').click(); await wait(page, 800); },
    parts: { menu: page => page.locator('[role=menu], [data-slot=popover-content]').filter({ visible: true }).last(), 'menu-item': nth('[role=menuitem]', 0) },
    optionalParts: ['menu-item'] },
  { name: 'activity', window: A,
    reveal: async ({ page }) => { await btn(page, 'View activity').click(); await wait(page, 1000); },
    // View activity swaps the workspace list for an activity list until it is turned off again.
    after: async ({ page }) => { await btn(page, 'Turn off activity view').click().catch(() => {}); await wait(page, 600); },
    parts: { 'filter-field': 'input[placeholder^="Filter"]', 'activity-card': page => page.locator('[aria-label="Turn off activity view"]').locator('xpath=ancestor::div[contains(@class,"flex-col")][2]').locator('div.rounded-lg, div.rounded-md').filter({ visible: true }).first() },
    optionalParts: ['filter-field', 'activity-card'] },
  { name: 'usage-popover', window: A,
    reveal: async ({ page }) => { await btn(page, 'Usage').click(); await wait(page, 900); },
    parts: { popover: page => page.locator('[data-slot=popover-content], [role=dialog], [role=menu]').filter({ visible: true }).last() } },
  { name: 'right-sidebar-agents', window: A, ...rightTab('Agents'), parts: {} },
  { name: 'right-sidebar-source-control', window: A, ...rightTab('Source Control'), parts: {} },
  { name: 'right-sidebar-checks', window: A, ...rightTab('Checks'), parts: {} },
  { name: 'workspace-board', window: A,
    reveal: async ({ page }) => { await btn(page, 'Workspace board').click(); await wait(page, 1300); },
    after: async ({ page }) => { await page.keyboard.press('Escape'); await wait(page, 300); if (await btn(page, 'Workspace board').isVisible().catch(() => false)) {} },
    parts: {} },
  { name: 'sidebar-hidden', window: A,
    reveal: async ({ page }) => { await btn(page, 'Toggle sidebar').click(); await wait(page, 900); },
    after: async ({ page }) => { await btn(page, 'Toggle sidebar').click().catch(() => {}); await wait(page, 700); }, parts: {} },
  { name: 'tasks', window: A, reveal: async ({ page }) => { await page.locator(S.navTasks).click(); await wait(page, 1500); },
    parts: { 'nav-row-selected': S.navTasks, 'segmented-active': page => page.locator('button').filter({ hasText: /^Issues$/ }).filter({ visible: true }).first(),
      'segmented-item': page => page.locator('button').filter({ hasText: /^PRs$/ }).filter({ visible: true }).first(), table: page => page.getByText('TITLE / CONTEXT', { exact: true }).locator('xpath=ancestor::div[contains(@class,"border")][1]') },
    optionalParts: ['table'] },
  { name: 'automations', window: A, reveal: async ({ page }) => { await nav(page, 'Automations').click(); await wait(page, 1500); },
    parts: { 'nav-row-selected': page => nav(page, 'Automations'), 'button-default': page => page.locator('button').filter({ hasText: /^New Automation$/ }).first(),
      'button-outline': page => page.locator('button').filter({ hasText: /^Runs$/ }).first(), 'search-field': page => page.locator('input[placeholder^="Search"]').filter({ visible: true }).first(),
      'template-card': page => page.getByText('Weekday repo audit', { exact: true }).locator('xpath=ancestor::button[1] | ancestor::div[contains(@class,"border")][1]').first(),
      'eyebrow': page => page.getByText('REPO HEALTH', { exact: true }).first() },
    optionalParts: ['template-card', 'eyebrow'] },
  { name: 'orca-mobile', window: A, reveal: async ({ page }) => { await nav(page, 'Orca Mobile').click(); await wait(page, 1500); }, parts: {} },
  { name: 'toast', window: A, keep: ['update'],
    reveal: async ({ page }) => { await overlays(page, ['update']); await wait(page, 400); },
    parts: { toast: '[role=complementary][data-slot=card]', 'button-default': '[role=complementary] button[data-variant=default], [role=complementary] [data-slot=button]', link: '[role=complementary] a, [role=complementary] button.underline' },
    optionalParts: ['link'] },

  // ---- settings
  { name: 'settings-general', window: A, reveal: async h => settings(h, 'General'),
    parts: { 'settings-nav': S.settingsNav, 'settings-search': S.settingsSearch, 'back-to-app': S.backToApp, card: S.card, 'page-title': S.pageTitle, 'page-description': S.pageDescription,
      'card-title': S.sectionTitle, 'field-label': S.fieldLabel, 'field-description': S.fieldDescription,
      'switch-on': S.switchOn, 'switch-off': S.switchOff, select: S.select, input: S.input, 'button-outline': S.buttonOutline, separator: S.separator },
    optionalParts: ['switch-off', 'separator', 'page-description', 'field-description'] },
  { name: 'settings-agents', window: A, reveal: async h => settings(h, 'Agents'),
    parts: { 'settings-nav-selected': S.settingsNavSelected, radio: S.radio, 'radio-on': S.radioOn, 'button-ghost': S.buttonGhost, 'button-xs': slot('button', '[data-size=xs]') },
    optionalParts: ['button-xs', 'button-ghost'] },
  { name: 'settings-ai-provider-accounts', window: A, reveal: async h => settings(h, 'AI Provider Accounts'), parts: { badge: S.badge, 'button-default-xs': slot('button', '[data-variant=default][data-size=xs]') }, optionalParts: ['button-default-xs'] },
  { name: 'settings-appearance', window: A, reveal: async h => settings(h, 'Appearance'),
    parts: { radio: S.radio, 'radio-on': S.radioOn, 'card-header': slot('card-header'), 'button-outline-icon': slot('button', '[data-variant=outline][data-size=icon-sm]') },
    optionalParts: ['card-header', 'button-outline-icon'] },
  { name: 'settings-terminal', window: A, reveal: async h => settings(h, 'Terminal'), parts: { slider: S.slider, 'slider-thumb': slot('slider-thumb') }, optionalParts: ['slider', 'slider-thumb'] },
  { name: 'settings-notifications', window: A, reveal: async h => settings(h, 'Notifications'), parts: { collapsible: slot('collapsible-trigger') }, optionalParts: ['collapsible'] },
  { name: 'settings-shortcuts', window: A, reveal: async h => settings(h, 'Shortcuts'), parts: {} },
  { name: 'settings-integrations', window: A, reveal: async h => settings(h, 'Integrations'), parts: {} },
  { name: 'settings-git', window: A, reveal: async h => settings(h, 'Git & Source Control'), parts: { 'button-secondary': S.buttonSecondary }, optionalParts: ['button-secondary'] },
  { name: 'settings-stats', window: A, reveal: async h => settings(h, 'Stats & Usage'), parts: { badge: S.badge }, optionalParts: ['badge'] },
  { name: 'settings-ssh-hosts', window: A, reveal: async h => settings(h, 'SSH Hosts'), parts: { checkbox: S.checkbox }, optionalParts: ['checkbox'] },
  { name: 'settings-experimental', window: A, reveal: async h => settings(h, 'Experimental'), parts: { 'switch-off': S.switchOff } },
  { name: 'settings-orca-account', window: A, reveal: async h => settings(h, 'Orca Account'), parts: { 'button-default': S.buttonDefault } },
  { name: 'settings-onboarding', window: A, reveal: async h => settings(h, 'Onboarding checklist'),
    parts: { 'step-row': page => page.getByText('Give agents Orca skills', { exact: true }).locator('xpath=ancestor::button[1]'),
      'step-row-selected': page => page.getByText('Choose your default agent', { exact: true }).filter({ visible: true }).locator('xpath=ancestor::button[1]').first() },
    optionalParts: ['step-row', 'step-row-selected'] },
  { name: 'settings-onboarding-skills', window: A,
    reveal: async h => { await settings(h, 'Onboarding checklist'); await h.page.getByText('Give agents Orca skills', { exact: true }).click(); await wait(h.page, 900); },
    parts: { 'button-default': page => page.locator('button').filter({ hasText: /^Install skills$/ }).first() } },
  { name: 'settings-search', window: A, state: 'filled',
    reveal: async h => { await settings(h, 'General'); await h.page.locator(S.settingsSearch).first().click(); await h.page.keyboard.type('font'); await wait(h.page, 1000); },
    parts: { 'settings-search': S.settingsSearch },
    after: async ({ page }) => { await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); } },
  { name: 'settings-select-open', window: A,
    reveal: async h => { await settings(h, 'General'); await h.page.locator(S.select).filter({ visible: true }).first().click(); await wait(h.page, 700); },
    parts: { listbox: slot('select-content'), option: nth(slot('select-item'), 1), 'option-selected': slot('select-item', '[data-state=checked]') },
    optionalParts: ['option-selected'] },

  // ---- states, one part per shot: hover with the real pointer, focus-visible with real keyboard
  // focus, pressed with :active forced through CDP. Each is a full-window screenshot too.
  ...states([
    ['app', async () => {}, { 'icon-button': S.iconButton, 'nav-row': S.navRow, 'workspace-row': S.workspaceRow, tab: S.tab, 'right-tab': S.rightTab,
      'new-tab': S.newTab, 'permission-button': S.perm, 'model-button': S.model, 'status-chip': S.statusChip, 'sidebar-search': S.sidebarSearch }, HFP],
    ['settings', async h => settings(h, 'General'), { 'switch-on': S.switchOn, 'switch-off': S.switchOff, select: S.select, 'button-outline': S.buttonOutline,
      'settings-nav': S.settingsNav, 'back-to-app': S.backToApp }, HFP],
    ['settings', async h => settings(h, 'General'), { 'settings-search': S.settingsSearch, input: S.input }, ['hover', 'focus-visible']],
    ['account', async h => settings(h, 'Orca Account'), { 'button-default': S.buttonDefault }, HFP],
    // The Theme control is only looked at: hover, focus and a forced :active, never a click.
    ['appearance', async h => settings(h, 'Appearance'), { radio: S.radio }, HFP],
    ['dialog', openRemove, { 'button-destructive': `${slot('dialog-content')} button[data-variant=destructive]`, 'button-outline': `${slot('dialog-content')} button[data-variant=outline]` }, HFP, { after: cancelDialog }],
    ['menu', async ({ page }) => { await page.locator(S.newTab).first().click(); await wait(page, 800); }, { 'menu-item': nth(slot('dropdown-menu-item'), 1) }, ['hover']],
    ['palette', openSearch, { 'palette-row': '[role=dialog] [role=option]' }, ['hover']],
  ]),
];

// ---- the agent run, taken by run.mjs. The owner approved (2026-10-25) harmless test prompts in a
// fresh agent on the scratch project only. Each run starts a new Claude chat in the scratch workspace
// with Orca's own CLI (`orca agent launch --surface chat`, which opens Orca's structured chat for this
// one launch without changing the Chat UI setting), so every theme gets its own chat.
const runTab = page => chatTabs(page).last();
const CONVERSATION = {
  'user-message': '[data-native-chat-message-id^="orca:"] .bg-chat-user-surface',
  'assistant-message': '[data-native-chat-message-id^="claude:"]',
  'turn-status': '[data-native-chat-turn-status]',
  'tool-call': '[data-native-chat-tool-run-state]',
  'code-block': '[data-native-chat-code-block]',
  link: '[data-native-chat-message-id^="claude:"] a',
  'context-usage': '[data-native-chat-context-usage]',
};
async function sendPrompt({ page }, text) {
  const ed = page.locator('.tiptap').filter({ visible: true }).last();
  await ed.click(); await page.keyboard.type(text, { delay: 10 }); await wait(page, 300);
  await page.keyboard.press('Enter'); await wait(page, 800);
}
export const RUN = {
  window: 'app',
  async start(h) {
    await home(h);
    const before = await chatTabs(h.page).count();
    execFileSync(ORCA, ['agent', 'launch', '--agent', 'claude', '--surface', 'chat', '--worktree', `path:${SCRATCH}`, '--focus', '--json'], { cwd: SCRATCH });
    for (let i = 0; i < 20 && (await chatTabs(h.page).count()) === before; i++) await wait(h.page, 500);
    if ((await chatTabs(h.page).count()) === before) throw new Error('no new chat tab');
    await runTab(h.page).click(); await wait(h.page, 1200);
    await overlays(h.page);
  },
  async finish(h) { await overlays(h.page); },
  async state({ page }) {
    const stop = page.locator('button[aria-label*="Stop" i], button[aria-label*="Interrupt" i], button[aria-label*="Cancel" i]').filter({ visible: true });
    if (await page.locator('button').filter({ visible: true }).filter({ hasText: /^(Allow|Approve|Accept|Run)\b/ }).count()) return 'approval';
    return (await stop.count()) ? 'running' : 'done';
  },
  async reject({ page }) { await page.locator('button').filter({ visible: true }).filter({ hasText: /^(Deny|Reject|Skip)\b/ }).last().click().catch(() => {}); await wait(page, 800); },
  steps: [
    { name: 'list-files', send: h => sendPrompt(h, 'List the files in this folder.') },
    { name: 'create-file', send: h => sendPrompt(h, 'Create hello.txt here with one line: hello from the design capture') },
    { name: 'run-command', send: h => sendPrompt(h, 'Run ls -la in this folder and show me the output.') },
  ],
  parts: { composer: S.composer, 'send-button': S.send, ...CONVERSATION },
  inventory: '[data-slot], [role], [aria-label]',
};

// The finished test chat, opened again after run.mjs.
const expandLastTurn = async ({ page }) => { await page.locator('[data-native-chat-turn-status]').last().click(); await wait(page, 900); };
SHOTS.push(
  { name: 'conversation', window: A, reveal: async h => { await home(h, 'run'); }, optionalParts: Object.keys(CONVERSATION), parts: { ...CONVERSATION, composer: S.composer, 'tab-active': S.tabActive } },
  { name: 'conversation-expanded', window: A, reveal: async h => { await home(h, 'run'); await expandLastTurn(h); }, after: expandLastTurn,
    optionalParts: ['link', 'context-usage'], parts: { ...CONVERSATION } },
  { name: 'conversation-top', window: A, reveal: async h => { await home(h, 'run'); await h.page.mouse.move(900, 400); await h.page.mouse.wheel(0, -4000); await wait(h.page, 900); },
    optionalParts: Object.keys(CONVERSATION), parts: { ...CONVERSATION } },
  { name: 'conversation-user-message-hover', window: A, state: 'hover', reveal: async h => { await home(h, 'run'); }, hover: 'user-message', parts: { 'user-message': CONVERSATION['user-message'] } },
  { name: 'conversation-code-block-hover', window: A, state: 'hover', reveal: async h => { await home(h, 'run'); }, hover: 'code-block', parts: { 'code-block': CONVERSATION['code-block'] } },
  { name: 'conversation-tool-call-hover', window: A, state: 'hover', reveal: async h => { await home(h, 'run'); await expandLastTurn(h); }, after: expandLastTurn, hover: 'tool-call', parts: { 'tool-call': CONVERSATION['tool-call'] } },
);
