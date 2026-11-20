// PRODUCT (adapt): everything in this file is Superset 1.39.0's. Another Electron app replaces it
// whole and keeps cdp.mjs, vars.mjs, shots.mjs and run.mjs as they are.
//
// A shot is { name, window, state?, reveal(h), parts, force?, hover?, focus?, optional?, optionalParts?, after?(h) }:
//   name    screenshot file name, `{page}-{state}` (the theme folder is added by shots.mjs)
//   window  a key of WINDOWS
//   reveal  async ({ page, cdp }) => {} : clicks, keys and hovers that show the state.
//           Look, don't act: open and close, type and clear, never submit or send.
//   parts   { component: selector | [selector, nth] | (page) => Locator }: each is measured
//           (computed style) and its box recorded for crops, as `{component}-{state}`
//   after   async (h) => {} : undo what reveal did (clear typed text, close a menu)
//
// Superset's renderer is React with shadcn/ui and Tailwind 4: parts are found by their data-slot
// (shadcn's component names), roles, aria-labels and the product's own fixed labels, never by
// account text. The one exception is the scratch project and workspace the capture created
// itself (SCRATCH, WORKSPACE).

import { existsSync } from 'node:fs';

export const NAME = 'Superset';
// One window; its document title is the organisation's name, so match any title. shots.mjs's
// --set-theme opens the window keyed `agents` (Cursor's name for its main window): same window here.
export const WINDOWS = { main: /./, agents: /./ };
export const SCOPES = { main: ['body'] };

// The capture's own project and workspace (created 2026-10-25 in ~/.design-systems/harness-scratch/superset).
export const SCRATCH = 'superset';
export const WORKSPACE = 'List files in this folder';
export const SCRATCH_DIR = `${process.env.HOME}/.design-systems/harness-scratch`;

const wait = (page, ms = 600) => page.waitForTimeout(ms);
// A shot that clicks a Delete control only to show its confirmation must see that confirmation before it goes
// on. If none opens, the click may have deleted something: the whole capture stops (shots.mjs reads `abort`).
async function confirmOpened(page, what) {
  const dialog = page.locator('[role=alertdialog], [role=dialog]').filter({ visible: true }).filter({ has: page.locator('button', { hasText: /^Cancel$/ }) });
  if (await dialog.last().waitFor({ state: 'visible', timeout: 3000 }).then(() => true, () => false)) return;
  throw Object.assign(new Error(`no confirmation dialog after ${what}: check that nothing was deleted`), { abort: true });
}
const re = s => new RegExp(`^${s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}`);
const btn = (page, label) => page.locator(`button[aria-label="${label}"]`).filter({ visible: true }).first();
const textBtn = (page, label) => page.locator('button').filter({ visible: true }).filter({ hasText: re(label) }).first();
const sidebar = page => page.locator('div.border-r.bg-sidebar').first();
const nav = (page, label) => sidebar(page).locator('button').filter({ hasText: re(label) }).first();
const projectRow = page => sidebar(page).locator('[data-slot=context-menu-trigger][role=button]').filter({ hasText: new RegExp(`${SCRATCH}$`) }).first();
const workspaceRow = page => sidebar(page).locator('div.rounded-md.text-left').filter({ hasText: WORKSPACE }).first();

const OPEN = '[role=menu], [role=dialog], [role=alertdialog], [role=listbox], [data-slot=popover-content], [data-slot=tooltip-content]';
export async function closeAll(page) {
  for (let i = 0; i < 4 && await page.locator(OPEN).filter({ visible: true }).first().isVisible().catch(() => false); i++) {
    await page.keyboard.press('Escape'); await wait(page, 300);
  }
}
async function back(page) {
  const b = page.getByText('Back', { exact: true }).first();
  if (await b.isVisible().catch(() => false)) { await b.click(); await wait(page, 700); }
}
// The New Workspace page: the empty composer every shot starts from.
export async function home({ page }) {
  await closeAll(page);
  await back(page);
  await nav(page, 'New Workspace').click(); await wait(page, 900);
  await page.mouse.move(1500, 940);
}
export async function reset(h) { return home(h); }
async function settings({ page }, pane) {
  await btn(page, 'Settings').click(); await wait(page, 900);
  if (pane) { await page.locator('button, a').filter({ visible: true }).filter({ hasText: new RegExp(`^${pane}$`) }).first().click(); await wait(page, 2000); }
}
const sidebarToggle = page => page.locator('button.no-drag.size-8').first();
async function expandProject(page) {
  if (!(await workspaceRow(page).isVisible().catch(() => false))) { await projectRow(page).click(); await wait(page, 700); }
}
// Open the scratch workspace with its right panel on Changes, the pointer off the sidebar (a
// workspace row shows a hover card under the pointer).
async function openWorkspace({ page }) {
  await expandProject(page); await workspaceRow(page).click(); await wait(page, 1500);
  await page.mouse.move(1500, 940);
  const changes = page.locator('button[aria-label^="Changes"]').filter({ visible: true }).first();
  if (await changes.isVisible().catch(() => false)) { await changes.click(); await wait(page, 600); }
  await page.mouse.move(1500, 940); await wait(page, 500);
}
// The diff opens as a second pane beside the terminal; close it again from its header.
async function closeDiffPane({ page }) {
  const pane = page.locator('[data-slot=resizable-panel]').filter({ has: page.locator('div.cursor-grab').filter({ hasText: /^Changes$/ }) }).last();
  if (!(await pane.isVisible().catch(() => false))) return;
  const hdr = pane.locator('div.cursor-grab').first();
  await hdr.hover(); await wait(page, 300); await hdr.locator('button').last().click(); await wait(page, 700);
}
async function goto({ page }, label) { await nav(page, label).click(); await wait(page, 1600); }

// A fingerprint of what a capture must never change: the composer's choices (agent, model, effort,
// device, project, checkout, branch) and the sidebar's rows. shots.mjs takes it before and after
// every shot and stops when it differs.
export async function guard(h) {
  const { page } = h;
  await home(h);
  // The renderer refills the composer and the sidebar a moment after navigation (it reads "No agent"
  // and an empty project list for a few hundred ms), so read until two readings 700 ms apart agree.
  const read = async () => {
    const composer = await page.locator('[data-slot=select-trigger], [data-slot=dropdown-menu-trigger], [data-slot=popover-trigger]')
      .filter({ visible: true }).allInnerTexts().catch(() => []);
    const rows = await sidebar(page).locator('[role=button]').allInnerTexts().catch(() => []);
    return `${composer.map(t => t.trim()).filter(Boolean).join(' / ')} | ${rows.map(t => t.replace(/\s+/g, ' ').trim()).join(' / ')}`;
  };
  let last = await read();
  for (let i = 0; i < 10; i++) {
    await wait(page, 700);
    const now = await read();
    if (now === last && !now.includes('No agent')) return now;
    last = now;
  }
  return last;
}

// Superset's theme is its own setting (Settings > Appearance > Theme), saved in ~/.superset/app-state.json.
// The owner's is Dark, not System, so an emulated prefers-color-scheme changes nothing (checked).
// Returns the label it replaced, so the caller can restore it.
export const THEME_LABELS = { light: 'Light', dark: 'Dark' };
export async function setTheme(h, label) {
  const { page } = h;
  await home(h); await settings(h, 'Appearance');
  const trigger = page.locator('[data-slot=select-trigger]').filter({ visible: true }).first();
  const before = (await trigger.innerText()).replace(/^Aa\s*/, '').trim();
  if (before !== label) {
    await trigger.click(); await wait(page, 600);
    // Each option reads "Aa" (a swatch), a newline, then the theme's name.
    await page.locator('[role=option]').filter({ hasText: new RegExp(`^(Aa\\s*)+${label}$`) }).first().click(); await wait(page, 1500);
  }
  await home(h);
  return before;
}

// ---- parts
const nth = (sel, i) => [sel, i];
const vis = (page, sel) => page.locator(sel).filter({ visible: true });
const composerBox = page => page.locator('div.rounded-2xl.bg-card').filter({ has: page.locator('[role=textbox]') }).first();
const S = {
  sidebar,
  newWorkspace: page => nav(page, 'New Workspace'),
  kbd: page => nav(page, 'New Workspace').locator('kbd').first(),
  navRow: page => nav(page, 'Automations'),
  // The selected row on the Workspaces page is the Workspaces button itself (a class match also hits New Workspace).
  navRowSelected: page => nav(page, 'Workspaces'),
  sectionLabel: 'div[aria-label=Projects]',
  iconButton: page => btn(page, 'Add project'),
  projectRow,
  workspaceRow,
  orgButton: page => btn(page, 'Organization menu'),
  updatePill: page => sidebar(page).locator('button').filter({ hasText: /update$/ }).first(),
  settingsButton: page => btn(page, 'Settings'),
  avatar: '[data-slot=avatar]',
  composer: composerBox,
  editor: '[role=textbox]',
  agentSelect: page => composerBox(page).locator('[data-slot=select-trigger]'),
  modelButton: page => composerBox(page).locator('[data-slot=dropdown-menu-trigger]').first(),
  plusButton: page => btn(page, 'Add files, apps, and more'),
  sendButton: page => composerBox(page).locator('[data-slot=button]').last(),
  dictate: page => btn(page, 'Dictate'),
  footerChip: page => page.locator('button[aria-label^="Device:"]').first(),
  suggestion: page => vis(page, 'button.cursor-pointer.rounded-md.px-2').first(),
  heading: page => page.getByText('What should we build next?').first(),
  history: page => btn(page, 'Previous prompts'),
  menu: page => vis(page, '[role=menu]').last(),
  menuRow: nth('[role=menu] [role=menuitem]', 0),
  menuSep: '[role=menu] [role=separator], [data-slot$=menu-separator]',
  dialog: '[role=dialog]',
  alert: '[role=alertdialog]',
  toast: '[data-sonner-toast]',
  tooltip: '[data-slot=tooltip-content]',
  popover: page => vis(page, '[data-slot=popover-content]').last(),
  listbox: page => vis(page, '[role=listbox]').last(),
  option: nth('[role=listbox] [role=option]', 0),
  optionSelected: '[role=listbox] [role=option][data-state=checked], [role=listbox] [role=option][aria-selected=true]',
  switchOn: '[data-slot=switch][data-state=checked]',
  switchOff: '[data-slot=switch][data-state=unchecked]',
  selectTrigger: page => vis(page, 'main [data-slot=select-trigger], [data-slot=select-trigger]').first(),
  input: page => vis(page, '[data-slot=input]').first(),
  textarea: '[data-slot=textarea]',
  settingsSearch: page => page.getByPlaceholder('Search settings...').first(),
  settingsNav: page => page.locator('button, a').filter({ visible: true }).filter({ hasText: /^Notifications$/ }).first(),
  settingsNavSelected: page => page.locator('button, a').filter({ visible: true }).filter({ hasText: /^General$/ }).first(),
  pageTitle: page => vis(page, 'h1, h2').first(),
  card: page => vis(page, '[data-slot=card]').first(),
  table: '[data-slot=table]',
  tableRow: nth('[data-slot=table-body] [data-slot=table-row]', 0),
  tableHead: '[data-slot=table-header]',
  badge: page => vis(page, '[data-slot=badge]').first(),
  tabsList: page => vis(page, '[data-slot=tabs-list]').first(),
  tab: page => vis(page, '[data-slot=tabs-trigger][data-state=inactive]').first(),
  tabSelected: page => vis(page, '[data-slot=tabs-trigger][data-state=active]').first(),
};
// Workspace view parts
const W = {
  tab: page => vis(page, '[data-pane-area=center] [data-slot=context-menu-trigger].rounded-t-md').first(),
  tabClose: page => btn(page, 'Close tab'),
  tabAdd: page => vis(page, '[data-pane-area=center] [data-slot=dropdown-menu-trigger]').first(),
  presetButton: page => vis(page, '[data-pane-area=center] button[data-slot=tooltip-trigger]').filter({ hasText: /^Codex$/ }).first(),
  paneHeader: page => vis(page, '[data-pane-area=center] div.cursor-grab').first(),
  sessionsButton: page => btn(page, 'Terminal sessions'),
  // The displayed pane's terminal: Superset also keeps an .xterm off screen (at -9999px), so scope to the
  // centre pane's terminal application, the structure the visible pane had in the DOM.
  terminal: page => vis(page, '[data-pane-area=center] [role=application] .xterm').first(),
  activity: page => btn(page, 'Workspace activity'),
  openChanges: page => btn(page, 'Open changes'),
  openIn: page => btn(page, 'Open in Finder'),
  runButton: page => btn(page, 'Configure workspace run command'),
  runMenu: page => btn(page, 'Workspace run options'),
  panelTab: page => btn(page, 'Files'),
  panelTabSelected: page => vis(page, 'button[aria-label^="Changes"]').first(),
  fileRow: page => vis(page, 'div, button').filter({ hasText: /^hello\.txt/ }).last(),
  setupCard: page => sidebar(page).locator('div.rounded-lg.bg-card').first(),
  setupBadge: page => sidebar(page).locator('div.rounded-lg.bg-card [data-slot=badge]').first(),
  setupButton: page => sidebar(page).locator('button').filter({ hasText: /^Configure$/ }).first(),
};
const createProjectItem = async ({ page }) => {
  await btn(page, 'Add project').click(); await wait(page, 700);
  await page.locator('[role=menuitem]').filter({ hasText: /^Create new project/ }).click(); await wait(page, 1000);
};
const dialogButton = (page, label) => page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: new RegExp(`^${label}$`) }).first();
const fillCreateProject = async ({ page }) => {
  const d = page.locator('[role=dialog]');
  await d.locator('input').nth(0).fill(SCRATCH); await d.locator('input').nth(1).fill(SCRATCH_DIR); await wait(page, 400);
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
const M = 'main';
const settingsShot = (name, pane, parts = {}, extra = {}) => ({ name, window: M, reveal: async h => settings(h, pane), parts, ...extra });

export const SHOTS = [
  { name: 'home-default', window: M, reveal: async () => {},
    optionalParts: ['avatar', 'update-pill'],
    parts: { sidebar: S.sidebar, 'button-new-workspace': S.newWorkspace, 'sidebar-row': S.navRow, 'section-label': S.sectionLabel,
      'icon-button': S.iconButton, 'project-row': S.projectRow, 'workspace-row': S.workspaceRow, 'org-button': S.orgButton,
      'update-pill': S.updatePill, 'settings-button': S.settingsButton, avatar: S.avatar, heading: S.heading, 'suggestion-row': S.suggestion,
      composer: S.composer, 'composer-editor': S.editor, 'agent-select': S.agentSelect, 'model-button': S.modelButton, 'plus-button': S.plusButton,
      'send-button': S.sendButton, 'dictate-button': S.dictate, 'footer-chip': S.footerChip, 'history-button': S.history } },
  // The ⌘N hint only shows while the pointer is over New Workspace.
  { name: 'home-kbd', window: M, state: 'hover', hover: 'button-new-workspace', reveal: async ({ page }) => { await S.newWorkspace(page).hover(); await wait(page, 500); },
    parts: { 'button-new-workspace': S.newWorkspace, kbd: S.kbd } },
  { name: 'home-composer-typed', window: M, state: 'filled',
    reveal: async ({ page }) => { await page.locator(S.editor).click(); await page.keyboard.type('Draft text, never sent'); await wait(page, 500); },
    parts: { composer: S.composer, 'composer-editor': S.editor, 'send-button': S.sendButton },
    after: async ({ page }) => { await page.locator(S.editor).click(); await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); await wait(page, 500); } },
  { name: 'agent-select', window: M, reveal: async ({ page }) => { await S.agentSelect(page).click(); await wait(page); },
    parts: { listbox: S.listbox, option: S.option, 'option-selected': S.optionSelected }, optionalParts: ['option-selected'] },
  { name: 'model-menu', window: M, reveal: async ({ page }) => { await S.modelButton(page).click(); await wait(page); },
    parts: { menu: S.menu, 'menu-row': S.menuRow } },
  { name: 'effort-menu', window: M, reveal: async ({ page }) => { await textBtn(page, 'Default effort').click(); await wait(page); },
    parts: { menu: S.menu, 'menu-row': S.menuRow } },
  { name: 'plus-menu', window: M, reveal: async ({ page }) => { await S.plusButton(page).click(); await wait(page); },
    parts: { 'command-menu': page => S.listbox(page).locator('xpath=..'), 'command-option': nth('[role=listbox] [role=option]', 0) } },
  { name: 'device-menu', window: M, reveal: async ({ page }) => { await S.footerChip(page).click(); await wait(page); },
    parts: { menu: S.menu, 'menu-row': S.menuRow } },
  { name: 'project-popover', window: M, reveal: async ({ page }) => { await page.locator('button[data-slot=popover-trigger]').filter({ hasText: new RegExp(`${SCRATCH}$`) }).first().click(); await wait(page); },
    parts: { popover: S.popover, 'command-input': '[data-slot=command-input]', 'command-item': nth('[data-slot=command-item]', 0) }, optionalParts: ['command-input', 'command-item'] },
  { name: 'checkout-menu', window: M, reveal: async ({ page }) => { await page.locator('button[aria-label^="Checkout:"]').first().click(); await wait(page); },
    parts: { menu: S.menu, 'menu-row': S.menuRow } },
  { name: 'history-popover', window: M, optional: true, reveal: async ({ page }) => { await S.history(page).click(); await wait(page); },
    parts: { popover: S.popover } },
  { name: 'search-palette', window: M, reveal: async ({ page }) => { await nav(page, 'Search').click(); await wait(page, 900); },
    parts: { palette: S.dialog, 'palette-input': '[data-slot=command-input-wrapper], [data-slot=command-input]', 'palette-group': nth('[data-slot=command-group]', 0),
      'palette-row': nth('[data-slot=command-item]', 1), 'palette-row-selected': '[data-slot=command-item][data-selected=true]', 'palette-shortcut': nth('[data-slot=command-shortcut], [role=dialog] kbd', 0) },
    optionalParts: ['palette-group', 'palette-row', 'palette-row-selected', 'palette-shortcut'] },
  { name: 'search-palette-empty', window: M, state: 'empty',
    reveal: async ({ page }) => { await nav(page, 'Search').click(); await wait(page, 900); await page.keyboard.type('zzqxv'); await wait(page, 1000); },
    parts: { palette: S.dialog, 'palette-empty': '[data-slot=command-empty]' }, optionalParts: ['palette-empty'] },
  { name: 'tooltip', window: M, state: 'hover', reveal: async ({ page }) => { await S.iconButton(page).hover(); await wait(page, 1500); },
    parts: { tooltip: S.tooltip, 'icon-button': S.iconButton } },
  { name: 'org-menu', window: M, reveal: async ({ page }) => { await S.orgButton(page).click(); await wait(page); },
    parts: { menu: S.menu, 'menu-row': S.menuRow, 'menu-separator': S.menuSep, 'menu-label': '[data-slot=dropdown-menu-label]' }, optionalParts: ['menu-separator', 'menu-label'] },
  { name: 'add-project-menu', window: M, reveal: async ({ page }) => { await S.iconButton(page).click(); await wait(page); },
    parts: { menu: S.menu, 'menu-row': S.menuRow } },
  { name: 'project-context-menu', window: M, reveal: async ({ page }) => { await projectRow(page).click({ button: 'right' }); await wait(page, 800); },
    parts: { 'context-menu': '[data-slot=context-menu-content]', 'menu-row': nth('[data-slot=context-menu-item]', 0), 'menu-separator': '[data-slot=context-menu-separator]' }, optionalParts: ['menu-separator'] },
  { name: 'workspace-context-menu', window: M, reveal: async ({ page }) => { await workspaceRow(page).click({ button: 'right' }); await wait(page, 800); },
    parts: { 'context-menu': '[data-slot=context-menu-content]', 'menu-row': nth('[data-slot=context-menu-item]', 0), 'menu-row-destructive': '[data-slot=context-menu-item][data-variant=destructive]',
      'menu-shortcut': '[data-slot=context-menu-shortcut]', 'menu-sub-trigger': '[data-slot=context-menu-sub-trigger]' },
    optionalParts: ['menu-row-destructive', 'menu-shortcut', 'menu-sub-trigger'] },
  { name: 'delete-confirmation', window: M,
    reveal: async ({ page }) => { await workspaceRow(page).click({ button: 'right' }); await wait(page, 800);
      await page.locator('[role=menuitem]').filter({ hasText: /^Delete/ }).first().click(); await confirmOpened(page, `Delete on the ${WORKSPACE} workspace`); await wait(page, 1000); },
    parts: { 'confirm-dialog': S.alert, scrim: '[data-slot=alert-dialog-overlay]', 'button-destructive': page => dialogButton(page, 'Delete'), 'button-ghost-sm': page => dialogButton(page, 'Cancel') },
    after: async ({ page }) => { await dialogButton(page, 'Cancel').click().catch(() => {}); await wait(page, 500); } },
  { name: 'create-project-dialog', window: M, reveal: createProjectItem,
    parts: { dialog: S.dialog, scrim: '[data-slot=dialog-overlay]', 'text-field': nth('[role=dialog] input', 0), 'text-field-mono': nth('[role=dialog] input', 1), 'button-primary-disabled': page => dialogButton(page, 'Create project'),
      'button-ghost': page => dialogButton(page, 'Cancel'), 'dialog-close': page => page.locator('[role=dialog] [data-slot=dialog-close], [role=dialog] button').filter({ hasText: /^Close$/ }).first(),
      'field-label': nth('[role=dialog] [data-slot=label], [role=dialog] label', 0) } },
  { name: 'create-project-filled', window: M, state: 'filled', reveal: async h => { await createProjectItem(h); await fillCreateProject(h); },
    parts: { 'text-field': nth('[role=dialog] input', 0), 'button-primary': page => dialogButton(page, 'Create project') } },
  // Submitting the scratch folder's name again fails: the folder exists. That gives the error toast,
  // and nothing is created.
  { name: 'create-project-error', window: M, state: 'error',
    reveal: async h => {
      // Without the folder the submit would create a project instead of failing: stop before clicking.
      if (!existsSync(`${SCRATCH_DIR}/${SCRATCH}`)) throw Object.assign(new Error(`${SCRATCH_DIR}/${SCRATCH} is missing, so Create project would succeed`), { abort: true });
      await createProjectItem(h); await fillCreateProject(h); await dialogButton(h.page, 'Create project').click(); await wait(h.page, 1500); },
    parts: { toast: S.toast, dialog: S.dialog },
    after: async ({ page }) => { await dialogButton(page, 'Cancel').click().catch(() => {}); await wait(page, 4000); } },
  { name: 'workspaces', window: M, reveal: async h => goto(h, 'Workspaces'),
    parts: { 'sidebar-row-selected': S.navRowSelected, 'button-primary-sm': page => textBtn(page, 'Create workspace'), 'search-field': page => page.getByPlaceholder(/Search workspaces/).first(),
      'board-column': page => vis(page, 'div').filter({ hasText: /^Idle\s*\d*/ }).last().locator('xpath=..'),
      'segmented': page => textBtn(page, 'List').locator('xpath=..'), 'segment': page => textBtn(page, 'List'), 'segment-selected': page => textBtn(page, 'Board'),
      'toolbar-button': page => textBtn(page, 'Filter'), 'title-select': page => textBtn(page, 'This device') },
    optionalParts: ['board-column', 'segmented'] },
  { name: 'automations-pro', window: M, reveal: async h => goto(h, 'Automations'),
    parts: { dialog: S.dialog, 'dialog-nav-row': page => page.locator('[role=dialog] button').filter({ hasText: /^Remote Access$/ }).first(),
      'dialog-nav-row-selected': page => page.locator('[role=dialog] button').filter({ hasText: /^Automations$/ }).first(), 'badge-pro': page => page.locator('[role=dialog] span, [role=dialog] div').filter({ hasText: /^PRO$/ }).last(),
      'button-primary': page => dialogButton(page, 'Get Superset Pro'), 'button-secondary-lg': page => dialogButton(page, 'Cancel') } },
  { name: 'tasks-pro', window: M, reveal: async h => goto(h, 'Tasks'), parts: { dialog: S.dialog, scrim: '[data-slot=dialog-overlay]' }, optionalParts: ['scrim'] },
  { name: 'pull-requests', window: M, reveal: async h => goto(h, 'Pull requests'),
    parts: { 'search-field': page => page.getByPlaceholder(/Search pull requests/).first(), segment: page => textBtn(page, 'All'), 'segment-selected': page => textBtn(page, 'Open'),
      'empty-state': page => page.getByText('Add a project to see pull requests.').first() }, optionalParts: ['empty-state'] },
  { name: 'pages', window: M, reveal: async h => goto(h, 'Pages'),
    parts: { 'button-primary-sm': page => textBtn(page, 'Create with AI'), segment: page => textBtn(page, 'Team'), 'segment-selected': page => textBtn(page, 'All'),
      'empty-state': page => page.getByText('No pages yet').first().locator('xpath=..'), 'search-field': page => page.getByPlaceholder(/Search pages/).first(), 'page-title': S.pageTitle } },
  { name: 'plugins', window: M, reveal: async h => goto(h, 'Plugins'),
    parts: { 'search-field': page => page.getByPlaceholder(/Search plugins/).first(), 'plugin-row': page => vis(page, 'div').filter({ has: page.locator('button').filter({ hasText: /^Install$/ }) }).filter({ hasText: /^Linear/ }).last(),
      'button-secondary': page => textBtn(page, 'Install'), badge: page => vis(page, 'span').filter({ hasText: /^MCP$/ }).first(), segment: page => textBtn(page, 'Skills'), 'segment-selected': page => textBtn(page, 'Plugins'),
      'page-title': S.pageTitle, 'section-heading': page => page.getByText('Productivity', { exact: true }).first() } },
  { name: 'skills', window: M, reveal: async h => { await goto(h, 'Plugins'); await textBtn(h.page, 'Skills').click(); await wait(h.page, 1200); }, parts: {} },

  // ---- Settings: every pane
  settingsShot('settings-account', 'Account', { 'settings-search': S.settingsSearch, 'settings-nav': S.settingsNav, 'settings-nav-selected': page => page.locator('button, a').filter({ visible: true }).filter({ hasText: /^Account$/ }).first(),
    'page-title': S.pageTitle, 'text-field': S.input, textarea: S.textarea, 'switch-on': S.switchOn, 'button-destructive': page => textBtn(page, 'Delete account'), 'button-primary-sm': page => textBtn(page, 'Save profile'),
    'button-secondary-lg': page => textBtn(page, 'Sign out') }, { optionalParts: ['switch-on', 'textarea', 'button-primary-sm', 'button-secondary-lg'] }),
  settingsShot('settings-appearance', 'Appearance', { 'select-trigger-sm': S.selectTrigger, 'button-outline': page => textBtn(page, 'Download starter'), 'field-group': S.card,
    'text-field': S.input, 'switch-on': S.switchOn, 'link': page => vis(page, 'main a, a').filter({ hasText: /^marketplace/ }).first() }, { optionalParts: ['field-group', 'link'] }),
  { name: 'settings-theme-select', window: M, reveal: async h => { await settings(h, 'Appearance'); await S.selectTrigger(h.page).click(); await wait(h.page); },
    parts: { listbox: S.listbox, option: S.option, 'option-selected': S.optionSelected, 'select-label': '[data-slot=select-label]', 'select-separator': '[data-slot=select-separator]' },
    optionalParts: ['option-selected', 'select-label', 'select-separator'] },
  settingsShot('settings-appearance-typography', 'Appearance', {}, { reveal: async h => { await settings(h, 'Appearance'); await h.page.mouse.move(900, 600); await h.page.mouse.wheel(0, 700); await wait(h.page, 800); } }),
  settingsShot('settings-notifications', 'Notifications', { 'switch-on': S.switchOn, 'list-row': page => vis(page, 'div').filter({ hasText: /^Shamisen/ }).last() }, { optionalParts: ['list-row'] }),
  settingsShot('settings-usage', 'Usage', { 'tabs-list': S.tabsList, progress: nth('[data-slot=progress], [role=progressbar]', 0), 'switch-off': S.switchOff, badge: S.badge },
    { optionalParts: ['tabs-list', 'progress', 'badge'] }),
  settingsShot('settings-mobile', 'Mobile'),
  settingsShot('settings-general', 'General', { 'switch-on': S.switchOn, 'select-trigger': S.selectTrigger, 'settings-nav-selected': S.settingsNavSelected, 'settings-nav': S.settingsNav }),
  settingsShot('settings-keyboard', 'Keyboard', { kbd: nth('main kbd, kbd', 0), 'text-field': S.input, 'button-secondary': page => textBtn(page, 'Reset') }, { optionalParts: ['button-secondary'] }),
  settingsShot('settings-git-worktrees', 'Git & Worktrees', { 'select-trigger': S.selectTrigger, 'text-field-mono': S.input }, { optionalParts: ['text-field-mono'] }),
  settingsShot('settings-agent-commands', 'Agent commands', { 'text-field': S.input, 'switch-on': S.switchOn, 'list-row': page => vis(page, 'button.h-7').filter({ hasText: /^Codex$/ }).first(),
    'list-row-selected': page => vis(page, 'button.h-7').filter({ hasText: /^Claude$/ }).first() }, { optionalParts: ['list-row', 'list-row-selected'] }),
  settingsShot('settings-terminal', 'Terminal', { 'button-primary-sm': page => textBtn(page, 'Add script'), 'list-row': page => vis(page, 'div').filter({ hasText: /^Claude/ }).filter({ hasText: /All projects/ }).last() },
    { optionalParts: ['button-primary-sm', 'list-row'] }),
  settingsShot('settings-files-editor', 'Files & Editor', { 'select-trigger': S.selectTrigger }),
  settingsShot('settings-browser', 'Browser', { 'text-field': S.input }),
  settingsShot('settings-organization', 'Organization', { table: S.table, 'table-row': S.tableRow, 'table-head': S.tableHead, 'button-destructive': page => textBtn(page, 'Delete organization'), avatar: S.avatar, badge: S.badge },
    { optionalParts: ['table', 'table-row', 'table-head', 'avatar', 'badge'] }),
  settingsShot('settings-teams', 'Teams', { table: S.table, 'button-primary': page => textBtn(page, 'Create team') }, { optionalParts: ['table'] }),
  settingsShot('settings-projects', 'Projects', { 'text-field': S.input, textarea: S.textarea }, { optionalParts: ['textarea'] }),
  settingsShot('settings-hosts', 'Hosts'),
  settingsShot('settings-integrations', 'Integrations', { 'button-secondary': page => textBtn(page, 'Connect') }, { optionalParts: ['button-secondary'] }),
  settingsShot('settings-billing', 'Billing', { 'button-primary-sm': page => textBtn(page, 'Upgrade') }, { optionalParts: ['button-primary-sm'] }),
  settingsShot('settings-api-keys', 'API Keys', { 'empty-state': page => page.getByText('No API keys yet').first().locator('xpath=..') }, { optionalParts: ['empty-state'] }),
  settingsShot('settings-remote-access', 'Remote Access', { 'switch-off': S.switchOff }, { optionalParts: ['switch-off'] }),
  settingsShot('settings-permissions', 'Permissions', { badge: S.badge }, { optionalParts: ['badge'] }),
  settingsShot('settings-experimental', 'Experimental', { 'switch-off': S.switchOff }, { optionalParts: ['switch-off'] }),
  { name: 'settings-search', window: M, state: 'filled',
    reveal: async h => { await settings(h, 'General'); await S.settingsSearch(h.page).click(); await h.page.keyboard.type('font'); await wait(h.page, 1000); },
    parts: { 'settings-search': S.settingsSearch },
    after: async ({ page }) => { await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); } },

  // ---- the scratch workspace
  { name: 'workspace-default', window: M, reveal: openWorkspace,
    optionalParts: ['open-changes', 'setup-card', 'setup-badge', 'setup-button', 'file-row'],
    parts: { 'workspace-row-selected': S.workspaceRow, tab: W.tab, 'tab-close': W.tabClose, 'tab-add': W.tabAdd, 'preset-button': W.presetButton,
      'pane-header': W.paneHeader, 'sessions-button': W.sessionsButton, terminal: W.terminal, 'activity-button': W.activity, 'open-changes': W.openChanges,
      'open-in': W.openIn, 'run-button': W.runButton, 'run-menu': W.runMenu, 'panel-tab': W.panelTab, 'panel-tab-selected': W.panelTabSelected,
      'file-row': W.fileRow, 'setup-card': W.setupCard, 'setup-badge': W.setupBadge, 'setup-button': W.setupButton } },
  { name: 'workspace-files', window: M, reveal: async h => { await openWorkspace(h); await W.panelTab(h.page).click(); await wait(h.page, 1200); },
    parts: { 'tree-row': page => vis(page, 'div, button').filter({ hasText: /^hello\.txt$/ }).last() }, optionalParts: ['tree-row'] },
  { name: 'workspace-diff', window: M,
    reveal: async h => { await openWorkspace(h); await W.fileRow(h.page).click(); await wait(h.page, 2000); await h.page.mouse.move(1500, 940); await wait(h.page, 400); },
    parts: { 'file-row-selected': W.fileRow, 'diff-pane-header': page => vis(page, '[data-pane-area=center] div.cursor-grab').filter({ hasText: /^Changes$/ }).first(),
      'diff-card': page => vis(page, 'diffs-container').first() },
    after: closeDiffPane },
  { name: 'workspace-review', window: M, reveal: async h => { await openWorkspace(h); await btn(h.page, 'Review').click(); await wait(h.page, 1200); }, parts: {} },
  { name: 'workspace-tab-menu', window: M, reveal: async h => { await openWorkspace(h); await W.tabAdd(h.page).click(); await wait(h.page); },
    parts: { menu: S.menu, 'menu-row': S.menuRow, 'menu-shortcut': '[data-slot=dropdown-menu-shortcut]' }, optionalParts: ['menu-shortcut'] },
  { name: 'workspace-run-menu', window: M, reveal: async h => { await openWorkspace(h); await W.runMenu(h.page).click(); await wait(h.page); },
    parts: { menu: S.menu, 'menu-row': S.menuRow } },
  { name: 'workspace-open-in-menu', window: M, reveal: async h => { await openWorkspace(h); await W.openIn(h.page).locator('xpath=following-sibling::button[1]').click(); await wait(h.page); },
    parts: { menu: S.menu, 'menu-row': S.menuRow } },
  { name: 'workspace-activity', window: M, optional: true, reveal: async h => { await openWorkspace(h); await W.activity(h.page).click(); await wait(h.page, 900); },
    parts: { popover: S.popover } },
  { name: 'workspace-sessions-menu', window: M, reveal: async h => { await openWorkspace(h); await W.sessionsButton(h.page).click(); await wait(h.page); },
    parts: { menu: S.menu, 'menu-row': S.menuRow } },
  { name: 'workspace-rich-input', window: M, optional: true,
    reveal: async h => { await openWorkspace(h); await btn(h.page, 'Rich input (⌘I)').click(); await wait(h.page, 900); },
    parts: { 'input-group': page => vis(page, '[data-pane-area=center] [data-slot=input-group]').last(), 'input-submit': page => vis(page, '[data-pane-area=center] button[aria-label=Submit]').last() },
    after: async ({ page }) => { await btn(page, 'Rich input (⌘I)').click().catch(() => {}); await wait(page, 500); } },
  { name: 'workspace-tab-tooltip', window: M, state: 'hover', reveal: async h => { await openWorkspace(h); await W.presetButton(h.page).hover(); await wait(h.page, 1500); },
    parts: { tooltip: S.tooltip } },
  // The top-left toggle folds the sidebar to an icon rail. Unfolding it collapses the project's
  // group, so `after` opens the group again (the guard checks the sidebar's rows).
  { name: 'sidebar-collapsed', window: M,
    reveal: async ({ page }) => { await sidebarToggle(page).click(); await wait(page, 900); },
    after: async ({ page }) => { await sidebarToggle(page).click().catch(() => {}); await wait(page, 900); await expandProject(page); }, parts: {} },

  // ---- states, one part per shot: hover with the real pointer, focus-visible with real keyboard
  // focus, pressed with :active forced through CDP and the pointer over the part.
  ...states([
    ['home', M, async () => {}, { 'button-new-workspace': S.newWorkspace, 'sidebar-row': S.navRow, 'icon-button': S.iconButton, 'project-row': S.projectRow,
      'workspace-row': S.workspaceRow, 'agent-select': S.agentSelect, 'model-button': S.modelButton, 'suggestion-row': S.suggestion, 'footer-chip': S.footerChip,
      'org-button': S.orgButton, 'plus-button': S.plusButton }, ['hover', 'focus-visible', 'pressed']],
    ['dialog', M, async h => { await createProjectItem(h); await fillCreateProject(h); }, { 'button-primary': page => dialogButton(page, 'Create project'),
      'button-ghost': page => dialogButton(page, 'Cancel') }, ['hover', 'focus-visible', 'pressed']],
    ['dialog', M, createProjectItem, { 'text-field': nth('[role=dialog] input', 0) }, ['hover', 'focus-visible']],
    ['settings', M, async h => settings(h, 'General'), { 'switch-on': S.switchOn, 'select-trigger': S.selectTrigger, 'settings-nav': S.settingsNav }, ['hover', 'focus-visible', 'pressed']],
    ['settings', M, async h => settings(h, 'General'), { 'settings-search': S.settingsSearch }, ['hover', 'focus-visible']],
    ['account', M, async h => settings(h, 'Account'), { 'button-destructive': page => textBtn(page, 'Delete account') }, ['hover', 'focus-visible', 'pressed']],
    ['appearance', M, async h => settings(h, 'Appearance'), { 'button-outline': page => textBtn(page, 'Download starter') }, ['hover', 'focus-visible', 'pressed']],
    ['pages', M, async h => goto(h, 'Pages'), { 'button-primary-sm': page => textBtn(page, 'Create with AI'), segment: page => textBtn(page, 'Team') }, ['hover', 'focus-visible', 'pressed']],
    ['workspaces', M, async h => goto(h, 'Workspaces'), { 'button-primary-sm': page => textBtn(page, 'Create workspace'), 'toolbar-button': page => textBtn(page, 'Filter') }, ['hover', 'focus-visible', 'pressed']],
    ['plugins', M, async h => goto(h, 'Plugins'), { 'button-secondary': page => textBtn(page, 'Install') }, ['hover', 'focus-visible', 'pressed']],
    ['workspace', M, openWorkspace, { tab: W.tab, 'preset-button': W.presetButton, 'panel-tab': W.panelTab, 'run-button': W.runButton }, ['hover', 'focus-visible', 'pressed']],
  ]),
];

// ---- an agent run, taken by run.mjs. The owner approved (2026-10-25) harmless test prompts in a
// fresh agent in the scratch workspace only, approving only actions inside it. Superset starts its
// Claude preset as `claude --dangerously-skip-permissions` in a terminal tab (Settings > Agent
// commands), so Claude Code asks for no tool approvals; the one prompt it can show is its own
// folder-trust question, answered for the scratch folder on the first run (see README).
const THEME = process.argv[2] || 'dark';
const centre = page => page.locator('[data-pane-area=center]');
const tabs = page => vis(page, '[data-pane-area=center] [data-slot=context-menu-trigger].rounded-t-md');
// The run's own tab: start() records how many tabs there were before the preset opened a new one, so
// another agent working in the same workspace cannot hold the run open.
let runTab = null;
const runningDot = page => (runTab === null ? centre(page) : tabs(page).nth(runTab)).locator('span.rounded-full.bg-amber-500').filter({ visible: true });
// Types only into the run tab's visible terminal. Superset keeps another .xterm off screen, so an
// unscoped `.last()` focus could send the prompt and Enter to another tab's shell or session: select
// the run's own tab, focus the input inside the displayed terminal, and check focus landed there.
// The displayed terminal: of the centre pane's .xterm elements, the first whose bounding box is on
// screen. Playwright counts the off-screen copy (x=-9999 in the saved run) as visible, so
// W.terminal's first() can pick it; a box with a negative x or y, no size, or outside the viewport
// is never chosen.
export async function displayedTerminal(page) {
  const all = page.locator('[data-pane-area=center] [role=application] .xterm');
  const view = page.viewportSize() || { width: Infinity, height: Infinity };
  for (let i = 0, n = await all.count(); i < n; i++) {
    const term = all.nth(i);
    const box = await term.boundingBox();
    if (box && box.width > 0 && box.height > 0 && box.x >= 0 && box.y >= 0 && box.x < view.width && box.y < view.height) return term;
  }
  throw new Error('no terminal on screen in the run tab; nothing was typed');
}
export async function sendToTerminal({ page }, text) {
  if (runTab !== null) { await tabs(page).nth(runTab).click(); await wait(page, 300); }
  const term = await displayedTerminal(page);
  await term.click();
  const input = term.locator('.xterm-helper-textarea');
  await input.focus();
  const inRunTerminal = await input.evaluate((el) => {
    const box = el.closest('.xterm')?.getBoundingClientRect();
    return el === document.activeElement && !!box && box.width > 0 && box.left >= 0 && box.top >= 0;
  });
  if (!inRunTerminal) throw new Error('keyboard focus is not in the run tab\'s visible terminal; nothing was typed');
  await page.keyboard.type(text, { delay: 12 }); await wait(page, 300);
  await page.keyboard.press('Enter'); await wait(page, 800);
}
export const RUN = {
  window: 'main',
  // A fresh Claude agent: the Claude preset opens a new terminal tab running Claude Code.
  async start(h) {
    const { page } = h;
    await home(h); await openWorkspace(h);
    runTab = await tabs(page).count();
    await vis(page, '[data-pane-area=center] button[data-slot=tooltip-trigger]').filter({ hasText: /^Claude$/ }).first().click();
    await wait(page, 7000);
    if ((await tabs(page).count()) !== runTab + 1) throw new Error('the Claude preset did not open one new tab');
  },
  // A run still going when run.mjs gives up (a step past TIMEOUT, or a failed frame) is `claude
  // --dangerously-skip-permissions` working on the Mac, so finish refuses to leave it: it fails the capture and
  // leaves the run's tab in front for the person to stop. Superset 2.0.5 (2026-11-07) no longer opens the
  // remote-debugging port, so its own Stop control could not be read live; until it is, the run is stopped by hand.
  async finish(h) {
    const { page } = h;
    if (runTab !== null && await runningDot(page).count()) throw new Error('the Claude run is still working in the scratch workspace (its tab shows the amber dot): stop it by hand (Esc, then /exit) before anything else');
    await home(h);
  },
  async state({ page }) { return (await runningDot(page).count()) ? 'running' : 'done'; },
  async reject() {},
  steps: [
    { name: 'list-files', send: h => sendToTerminal(h, 'List the files in this folder.') },
    { name: 'create-file', send: h => sendToTerminal(h, `Create hello-${THEME}.txt here with one line: hello from the design capture`) },
  ],
  // Parts measured on every frame; the last visible match is measured.
  parts: {
    tab: page => vis(page, '[data-pane-area=center] [data-slot=context-menu-trigger].rounded-t-md'),
    'tab-running-dot': page => runningDot(page),
    'pane-header': page => vis(page, '[data-pane-area=center] div.cursor-grab'),
    terminal: page => W.terminal(page),
    'workspace-row-selected': page => workspaceRow(page),
    'open-changes': page => btn(page, 'Open changes'),
  },
};
