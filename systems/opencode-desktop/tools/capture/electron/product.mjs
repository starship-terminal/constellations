// PRODUCT (adapt): everything in this file is OpenCode 2.1.4's. Another Electron app replaces it
// whole and keeps cdp.mjs, vars.mjs, shots.mjs and run.mjs as they are.
//
// A shot is { name, window, state?, reveal(h), parts, force?, hover?, focus?, after?(h), optional?, optionalParts? }:
//   name    screenshot file name, `{page}-{state}` (the theme folder is added by shots.mjs)
//   window  a key of WINDOWS
//   reveal  async ({ page, cdp, ...helpers }) => {} : clicks, keys and hovers that show the state.
//           Look, don't act: open and close, type and clear, never submit or send.
//   parts   { component: selector | [selector, nth] | (page) => Locator }: each is measured
//           (computed style) and its box recorded for crops, as `{component}-{state}`
//   force   { component: ['hover' | 'focus' | 'focus-visible' | 'active'] }: pseudo-classes forced
//           through CDP on that part before the screenshot (no pointer moves, nothing is clicked)
//   after   async (h) => {} : undo what reveal did (clear typed text, close a menu)
//
// OpenCode (bundle id ai.opencode.desktop) is one window: a row of session tabs across the top, a
// Home page (projects on the left, the project's sessions on the right), the session page (the
// transcript, a composer docked at the bottom, review and terminal panes) and Settings as a page.
// Its interface is SolidJS with Tailwind on two token layers: the theme engine's --background-*,
// --surface-*, --text-*, --border-* ... (written by the `oc-theme` style element from the chosen
// theme, here OpenCode) and the newer --v2-* layer. Every part carries data-component (and
// data-slot), so selectors are those, roles and aria-labels, never account text.
//
// The theme follows prefers-color-scheme (Settings > Appearance > Color scheme is System), so each
// pass runs with COLOR_SCHEME=dark or light (cdp.mjs) and no setting is touched.

import { allowance, approvable } from './approve.mjs';

export const NAME = 'OpenCode';
// shots.mjs --set-theme connects to the window keyed 'agents' (Cursor's name for its main window),
// so the one window is listed under that key too.
export const WINDOWS = { main: 'OpenCode', agents: 'OpenCode' };
export const SCOPES = { main: [':root'] };

// The capture's own project (the folder ~/.design-systems/harness-scratch/opencode, opened through
// Add project on 2026-10-25) and the session run.mjs creates in it. No other project or session is
// opened by a shot.
export const PROJECT = 'opencode';
export const SCRATCH = `${process.env.HOME}/.design-systems/harness-scratch/opencode`;

const wait = (page, ms = 600) => page.waitForTimeout(ms);
const dc = name => `[data-component="${name}"]`;
const visible = (page, sel) => page.locator(sel).filter({ visible: true });
const btn = (page, label) => visible(page, `button[aria-label="${label}"]`).first();
const projectRow = page => page.locator(dc('home-project-row')).filter({ hasText: new RegExp(`^\\s*\\S\\s*${PROJECT}\\s*$`) }).first();

export async function closeAll(page) {
  for (let i = 0; i < 4; i++) {
    const open = await visible(page, '[role=menu], [role=dialog], [role=listbox], [data-component=dialog-v2], [data-component=popover-v2]').count();
    if (!open) break;
    await page.keyboard.press('Escape'); await wait(page, 350);
  }
}
// Home, with the capture's project selected (its sessions on the right, nobody else's).
export async function home({ page }) {
  await closeAll(page);
  // Home (⌘B) toggles: pressed on Home it goes back to the last session, so press it only elsewhere.
  if (!(await visible(page, dc('home-project-row')).count())) { await btn(page, 'Home').click(); await wait(page, 900); }
  const row = projectRow(page);
  if (!(await row.getAttribute('data-selected').then(v => v !== null).catch(() => false))) { await row.click(); await wait(page, 900); }
  await page.mouse.move(640, 790);
}
// The capture's session: the dark run's session, which OpenCode titled from its first prompt. Every
// session shot opens it from its tab, with the review and terminal panes closed.
export const SESSION = 'List folder files';
const sessionTab = page => page.locator(dc('session-tab-popover-trigger')).filter({ hasText: SESSION }).first();
export async function session({ page }) {
  await closeAll(page);
  if (await sessionTab(page).count()) { await sessionTab(page).locator('a').first().click(); await wait(page, 1200); }
  else { await home({ page }); await page.locator(dc('home-session-row')).filter({ hasText: SESSION }).first().click(); await wait(page, 1500); }
  // The review pane and the terminal stay open per session once opened; close them for a clean page.
  if (await visible(page, dc('session-review-v2')).count()) { await btn(page, 'Toggle review').click(); await wait(page, 800); }
  if (await page.evaluate(() => { const t = document.querySelector('[data-component=terminal-panel]'); return !!t && t.getBoundingClientRect().x < innerWidth - 20 && t.getBoundingClientRect().y < innerHeight - 20; })) {
    await page.locator(dc('composer-editor')).click(); await page.keyboard.press('Control+Backquote'); await wait(page, 800);
  }
  await page.mouse.move(640, 790);
}
// The New session page: the draft tab (a tab-link with no session behind it) when one is open,
// else Home's New session.
async function draft({ page }) {
  await closeAll(page);
  const d = page.locator('[data-slot=tab-link]:not([id])').filter({ hasText: /^\s*Session\s*$/ }).first();
  if (await d.count()) await d.click(); else { await home({ page }); await page.locator('[data-action=home-new-session]').click(); }
  await wait(page, 1300); await page.mouse.move(640, 790);
}
// Each shot starts on Home with nothing focused: a focus left by the previous shot's focus-visible
// state would otherwise draw its ring in the next shot.
export async function reset(h) {
  await h.page.evaluate(() => document.activeElement && document.activeElement !== document.body && document.activeElement.blur());
  return home(h);
}

async function settings({ page }, pane) {
  await home({ page });
  await visible(page, 'button').filter({ hasText: /^Settings$/ }).first().click(); await wait(page, 1200);
  if (pane) { await page.locator('[role=tab]').filter({ hasText: new RegExp(`^${pane}$`) }).first().click(); await wait(page, 1000); }
}
async function clearComposer(page) {
  await page.locator(dc('composer-editor')).click();
  await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); await wait(page, 400);
  await page.keyboard.press('Escape'); await wait(page, 300);
}

// A fingerprint of what a capture must never change: the open session tabs. The projects list, the
// sessions, the composer's model and the Settings values are compared before and after the whole
// capture instead (README). shots.mjs takes it before and after every shot and stops when it differs.
export async function guard(h) {
  const { page } = h;
  const tabs = await page.locator(dc('session-tab-popover-trigger')).evaluateAll(es => es.map(e => e.innerText.replace(/\s+/g, ' ').trim()));
  return `tabs: ${tabs.join(' | ')}`;
}

// ---- the shot list
const M = 'main';
const nth = (sel, i) => [sel, i];
const S = {
  home: 'button[aria-label="Home"]',
  tab: page => sessionTab(page),
  tabClose: page => sessionTab(page).locator('button[aria-label="Close tab"]'),
  newTab: page => page.locator('button[aria-label="New session"]').first(),
  projectRow: page => projectRow(page),
  projectRowOther: nth(dc('home-project-row'), 1),
  sessionRow: page => page.locator(dc('home-session-row')).filter({ hasText: SESSION }).first(),
  search: dc('home-session-search'),
  searchInput: `${dc('home-session-search')} input`,
  newSession: `${dc('button-v2')}[data-action=home-new-session]`,
  addProject: 'button[aria-label="Add project"]',
  sideLink: page => visible(page, 'button').filter({ hasText: /^Settings$/ }).first(),
  menu: page => visible(page, '[role=menu]').first(),
  menuRow: nth('[role=menu] [role=menuitem]', 0),
  dialog: page => visible(page, '[role=dialog], [role=alertdialog]').last(),
  composer: dc('composer'),
  editor: dc('composer-editor'),
  attach: 'button[aria-label="Add images and files"]',
  model: page => page.locator(`${dc('composer')} ${dc('button-v2')}`).first(),
  variant: 'button[aria-label="Choose model variant"]',
  send: 'button[aria-label="Send"]',
  more: page => visible(page, 'button[aria-label="More options"]').first(),
  contextButton: 'button[aria-label="Toggle session context"]',
  review: 'button[aria-label="Toggle review"]',
  details: 'button[aria-label="Session details"]',
  projectTrigger: '[data-slot=session-project-trigger]',
  userMessage: page => visible(page, dc('user-message')).last(),
  textPart: page => visible(page, dc('text-part')).last(),
  markdown: page => visible(page, dc('markdown')).last(),
  code: page => visible(page, dc('markdown-code')).last(),
  inlineCode: page => visible(page, `${dc('markdown')} :not(pre) > code`).first(),
  toolGroup: page => visible(page, dc('context-tool-group-trigger')).last(),
  toolTrigger: page => visible(page, dc('tool-trigger')).last(),
  copyResponse: page => visible(page, 'button[aria-label="Copy response"]').last(),
  settingsNav: nth('[role=tablist] [role=tab]', 2),
  settingsNavSelected: '[role=tablist] [role=tab][aria-selected=true]',
  settingsRow: nth(dc('settings-row'), 0),
  settingsList: nth(dc('settings-list'), 0),
  select: nth(dc('select-v2'), 1),
  switchOff: page => visible(page, dc('switch')).first(),
  settingsSearch: `${dc('text-input-v2')}`,
  back: page => visible(page, 'button').filter({ hasText: /^Back to app$/ }).first(),
};
const sessionMenu = async h => { await session(h); await S.more(h.page).click(); await wait(h.page, 800); };
const palette = async h => { await session(h); await h.page.keyboard.press('Meta+K'); await wait(h.page, 1000); };
const typeIn = async (page, text) => { await page.locator(S.editor).click(); await page.keyboard.type(text); await wait(page, 1000); };
const projectMenu = async ({ page }) => {
  await home({ page });
  const row = page.locator('div[role=button]').filter({ has: page.locator(`${dc('home-project-row')}[data-selected]`) });
  await row.hover(); await wait(page, 400); await row.locator('button[aria-label="More options"]').click(); await wait(page, 900);
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

// The empty project, before the first session existed. Taken once on 2026-10-25 (EMPTY=1); after the
// runs the project has sessions, so a default run leaves this shot (and its readings) alone.
const EMPTY = [
  { name: 'home-project-empty', window: M, state: 'empty', reveal: async () => {},
    parts: { 'project-row-selected': page => projectRow(page), 'project-row': nth(dc('home-project-row'), 1), 'project-avatar': nth(dc('project-avatar-v2'), 2),
      'search-field': dc('home-session-search'), 'button-neutral': `${dc('button-v2')}[data-action=home-new-session]`,
      'icon-button': 'button[aria-label="Add project"]', 'session-tab': nth(dc('session-tab-popover-trigger'), 0), 'empty-title': page => page.getByText('Nothing here yet', { exact: true }) } },
];

export const SHOTS = process.env.EMPTY ? EMPTY : [
  // ---- Home
  { name: 'home-default', window: M, reveal: async () => {},
    parts: { 'project-row-selected': S.projectRow, 'project-row': S.projectRowOther, 'project-avatar': nth(dc('project-avatar-v2'), 4),
      'section-label': page => visible(page, 'span, div').filter({ hasText: /^Projects$/ }).last(),
      'search-field': S.search, 'button-neutral': S.newSession, 'icon-button': S.addProject, 'side-link': S.sideLink,
      'session-row': S.sessionRow, 'session-tab': S.tab, 'tab-close': S.tabClose, 'icon-button-home': S.home, 'new-tab': S.newTab,
      titlebar: page => page.locator(S.home).locator('xpath=ancestor::*[contains(@class,"flex")][1]') } },
  { name: 'home-all-projects', window: M,
    reveal: async ({ page }) => { await page.locator(`${dc('home-project-row')}[data-selected]`).click(); await wait(page, 1200); },
    parts: { 'group-label': page => visible(page, 'div, span').filter({ hasText: /^Today$/ }).last(), 'session-row': nth(dc('home-session-row'), 2) },
    after: async ({ page }) => { await projectRow(page).click(); await wait(page, 900); } },
  { name: 'home-search-filled', window: M, state: 'filled',
    reveal: async ({ page }) => { await page.locator(S.searchInput).click(); await page.keyboard.type('hello'); await wait(page, 1200); },
    parts: { 'search-field': S.search },
    after: async ({ page }) => { await page.locator(S.searchInput).fill(''); await wait(page, 500); } },
  { name: 'home-search-empty', window: M, state: 'empty',
    reveal: async ({ page }) => { await page.locator(S.searchInput).click(); await page.keyboard.type('zzqxv'); await wait(page, 1200); },
    parts: { 'search-field': S.search },
    after: async ({ page }) => { await page.locator(S.searchInput).fill(''); await wait(page, 500); } },
  { name: 'project-menu', window: M, reveal: projectMenu,
    parts: { menu: S.menu, 'menu-row': S.menuRow, 'menu-row-disabled': page => page.locator('[role=menu] [role=menuitem][data-disabled], [role=menu] [role=menuitem][aria-disabled=true]').first() },
    optionalParts: ['menu-row-disabled'] },
  { name: 'project-settings', window: M,
    reveal: async h => { await projectMenu(h); await h.page.locator('[role=menuitem]').filter({ hasText: /^Edit project$/ }).click(); await wait(h.page, 1200); },
    parts: { 'text-field': page => visible(page, '[role=tabpanel] input').first(), 'color-swatch': page => visible(page, '[role=tabpanel] [role=radio], [role=tabpanel] button[aria-label*="olor" i]').first(),
      textarea: page => visible(page, '[role=tabpanel] textarea').first(), 'settings-row': S.settingsRow },
    optionalParts: ['color-swatch'],
    after: async ({ page }) => { await visible(page, 'button').filter({ hasText: /^Back to projects$/ }).first().click().catch(() => {}); await wait(page, 600); } },
  { name: 'tooltip', window: M, state: 'hover',
    reveal: async ({ page }) => { await page.locator(S.home).hover(); await wait(page, 1300); },
    parts: { tooltip: page => visible(page, dc('tooltip-v2')).first(), kbd: page => visible(page, dc('keybind-v2')).first() } },
  { name: 'new-session', window: M, reveal: draft,
    parts: { wordmark: dc('new-session-wordmark'), composer: S.composer, 'prompt-field': S.editor, 'attach-button': S.attach, 'model-button': S.model, 'send-button': S.send,
      'project-select': page => visible(page, `${dc('new-session')} button`).filter({ has: page.locator(dc('project-avatar-v2')) }).first(),
      'pill': page => visible(page, `${dc('new-session')} button, ${dc('new-session')} [data-component=tag]`).filter({ hasText: /No Git/ }).first(),
      'draft-tab': page => page.locator('[data-slot=tab-link]:not([id])').first() },
    optionalParts: ['pill'] },

  // ---- the session
  { name: 'conversation', window: M, reveal: session,
    parts: { header: page => S.more(page).locator('xpath=..'), 'session-title': page => S.more(page).locator('xpath=preceding-sibling::*[1]'), 'more-button': S.more,
      'context-button': S.contextButton, 'progress-circle': dc('progress-circle'), 'icon-button': S.review, 'project-trigger': S.projectTrigger,
      'user-message': S.userMessage, 'text-part': S.textPart, markdown: S.markdown, 'code-block': S.code, 'inline-code': S.inlineCode,
      'tool-group': S.toolGroup, 'copy-button': S.copyResponse, 'turn-meta': page => visible(page, `${dc('text-part')} > :last-child`).last(),
      composer: S.composer, 'prompt-field': S.editor, 'attach-button': S.attach, 'model-button': S.model, 'variant-button': S.variant, 'send-button': S.send,
      'session-tab-selected': S.tab },
    optionalParts: ['variant-button', 'turn-meta', 'inline-code'] },
  { name: 'conversation-top', window: M,
    reveal: async h => { await session(h); await h.page.mouse.move(640, 300); await h.page.mouse.wheel(0, -6000); await wait(h.page, 1000); },
    parts: { 'user-message': page => visible(page, dc('user-message')).first(), 'tool-group': page => visible(page, dc('context-tool-group-trigger')).first(),
      'file-link': page => visible(page, `${dc('markdown')} a`).first() }, optionalParts: ['file-link'] },
  { name: 'tool-expanded', window: M,
    reveal: async h => { await session(h); await h.page.mouse.move(640, 300); await h.page.mouse.wheel(0, -6000); await wait(h.page, 900);
      await visible(h.page, dc('context-tool-group-trigger')).first().click(); await wait(h.page, 1200); },
    parts: { 'tool-output': page => visible(page, `${dc('tool-output')}, ${dc('bash-output')}, ${dc('context-tool-group-list')}`).first(), 'tool-trigger-open': page => visible(page, '[data-slot=collapsible-trigger][aria-expanded=true]').first() },
    optionalParts: ['tool-output'],
    after: async ({ page }) => { await visible(page, '[data-slot=collapsible-trigger][aria-expanded=true]').first().click().catch(() => {}); await wait(page, 500); } },
  { name: 'message-actions', window: M, state: 'hover',
    reveal: async h => { await session(h); await S.userMessage(h.page).hover(); await wait(h.page, 800); },
    parts: { 'user-message': S.userMessage, 'icon-button-small': page => visible(page, 'button[aria-label="Copy message"]').last() } },
  { name: 'tab-popover', window: M, state: 'hover',
    reveal: async h => { await session(h); await S.tab(h.page).hover(); await wait(h.page, 1500); },
    parts: { popover: page => visible(page, dc('session-tab-popover')).first() } },
  { name: 'tab-context-menu', window: M,
    reveal: async h => { await session(h); await S.tab(h.page).click({ button: 'right' }); await wait(h.page, 900); },
    parts: { 'context-menu': S.menu, 'menu-row': S.menuRow } },
  { name: 'session-menu', window: M, reveal: sessionMenu,
    parts: { menu: S.menu, 'menu-row': S.menuRow, separator: page => visible(page, '[role=menu] [role=separator]').first() }, optionalParts: ['separator'] },
  { name: 'delete-confirmation', window: M,
    reveal: async h => { await sessionMenu(h); await h.page.locator('[role=menuitem]').filter({ hasText: /^Delete/ }).click(); await wait(h.page, 1000); },
    parts: { 'confirm-dialog': S.dialog, 'dialog-overlay': page => visible(page, dc('dialog-overlay')).first(),
      'button-danger': page => S.dialog(page).locator('button').filter({ hasText: /^Delete session$/ }),
      'button-secondary': page => S.dialog(page).locator('button').filter({ hasText: /^Cancel$/ }) },
    optionalParts: ['dialog-overlay'],
    after: async ({ page }) => { await S.dialog(page).locator('button').filter({ hasText: /^Cancel$/ }).click().catch(() => {}); await wait(page, 600); } },
  { name: 'model-menu', window: M,
    reveal: async h => { await session(h); await S.model(h.page).click(); await wait(h.page, 1200); },
    parts: { 'model-menu': S.menu, 'menu-search': page => visible(page, '[role=menu] input').first(), 'menu-row': nth(`[role=menu] ${dc('menu-v2-item')}`, 1),
      'menu-row-checked': page => visible(page, `[role=menu] ${dc('menu-v2-item')}[aria-checked=true]`).first(),
      'menu-group-label': page => visible(page, '[role=menu] [data-slot=menu-v2-group-label]').first(),
      'tag-free': page => visible(page, `[role=menu] ${dc('tag')}`).first(), 'menu-footer': page => visible(page, '[role=menu] [role=menuitem]').filter({ hasText: /^Manage models$/ }).first() },
    optionalParts: ['menu-group-label', 'tag-free', 'menu-footer', 'menu-row-checked'] },
  { name: 'variant-menu', window: M, optional: true,
    reveal: async h => { await session(h); await h.page.locator(S.editor).click(); await wait(h.page, 500); await h.page.locator(S.variant).click({ timeout: 5000 }); await wait(h.page, 900); },
    parts: { menu: S.menu, 'menu-row-checked': page => visible(page, `[role=menu] ${dc('menu-v2-item')}[aria-checked=true]`).first() },
    optionalParts: ['menu-row-checked'] },
  { name: 'composer-typed', window: M, state: 'filled',
    reveal: async h => { await session(h); await typeIn(h.page, 'Draft text, never sent'); },
    parts: { composer: S.composer, 'prompt-field': S.editor, 'send-button': S.send }, after: async ({ page }) => clearComposer(page) },
  { name: 'composer-focus', window: M, state: 'focus',
    reveal: async h => { await session(h); await h.page.locator(S.editor).click(); await wait(h.page, 500); },
    parts: { composer: S.composer } },
  { name: 'slash-commands', window: M,
    reveal: async h => { await session(h); await typeIn(h.page, '/'); },
    parts: { suggestions: page => visible(page, dc('composer-suggestions')).first(), 'suggestion-row-active': page => visible(page, `${dc('composer-suggestions')} [data-active], ${dc('composer-suggestions')} [aria-selected=true]`).first(),
      'suggestion-row': page => visible(page, `${dc('composer-suggestions')} button, ${dc('composer-suggestions')} [role=option]`).nth(1) },
    optionalParts: ['suggestion-row-active', 'suggestion-row'], after: async ({ page }) => clearComposer(page) },
  { name: 'mention-empty', window: M, state: 'empty',
    reveal: async h => { await session(h); await typeIn(h.page, '@'); },
    parts: { suggestions: page => visible(page, dc('composer-suggestions')).first() }, after: async ({ page }) => clearComposer(page) },
  { name: 'command-palette', window: M, reveal: palette,
    parts: { palette: S.dialog, 'palette-input': page => S.dialog(page).locator('input').first(), 'palette-row-active': page => S.dialog(page).locator('[role=option][aria-selected=true], [role=option][data-active]').first(),
      'palette-row': page => S.dialog(page).locator('[role=option]').nth(2), kbd: page => S.dialog(page).locator(dc('keybind-v2')).first(), 'dialog-overlay': page => visible(page, dc('dialog-overlay')).first() },
    optionalParts: ['palette-row-active', 'dialog-overlay'] },
  { name: 'command-palette-filtered', window: M, state: 'filled',
    reveal: async h => { await palette(h); await h.page.keyboard.type('review'); await wait(h.page, 1000); },
    parts: { palette: S.dialog } },
  { name: 'command-palette-empty', window: M, state: 'empty',
    reveal: async h => { await palette(h); await h.page.keyboard.type('zzqxv'); await wait(h.page, 1000); },
    parts: { palette: S.dialog } },
  { name: 'review-pane', window: M,
    reveal: async h => { await session(h); await h.page.locator(S.review).click(); await wait(h.page, 1200);
      await visible(h.page, '[role=tab]').filter({ hasText: /^Review$/ }).first().click(); await wait(h.page, 1000); },
    parts: { pane: dc('session-review-v2'), 'pane-tab-selected': page => visible(page, '[role=tablist] [role=tab][aria-selected=true]').first(),
      'filter-field': page => visible(page, `${dc('session-review-v2')} input`).first(), 'button-neutral': page => visible(page, `${dc('session-review-v2')} ${dc('button-v2')}`).first() },
    optionalParts: ['filter-field'],
    after: async ({ page }) => { await page.locator(S.review).click().catch(() => {}); await wait(page, 600); } },
  { name: 'context-pane', window: M,
    reveal: async h => { await session(h); await h.page.locator(S.contextButton).click(); await wait(h.page, 1500); },
    parts: { pane: page => visible(page, '[role=tabpanel]').last(), 'pane-tab-selected': page => visible(page, '[role=tablist] [role=tab][aria-selected=true]').last(),
      'list-row': page => visible(page, '[role=tabpanel] button').filter({ hasText: /msg_/ }).first() },
    optionalParts: ['list-row'],
    after: async ({ page }) => { await page.locator(S.review).click().catch(() => {}); await wait(page, 600); } },
  { name: 'session-details', window: M,
    reveal: async h => { await session(h); await h.page.locator(S.details).click(); await wait(h.page, 1200); },
    parts: { popover: S.dialog, 'menu-row': page => S.dialog(page).locator('button, [role=menuitem]').nth(1) },
    optionalParts: ['menu-row'] },
  { name: 'terminal', window: M,
    reveal: async h => { await session(h); await h.page.locator(S.editor).click(); await h.page.keyboard.press('Control+Backquote'); await wait(h.page, 1800); await h.page.mouse.move(640, 300); },
    parts: { terminal: dc('terminal-panel'), 'terminal-tab': page => visible(page, `${dc('terminal-panel')} [role=tab]`).first() },
    optionalParts: ['terminal-tab'],
    // Close the terminal (its shell exits) rather than hide it, so no shell the capture started stays open.
    after: async ({ page }) => { await page.locator(`${dc('terminal-panel')} button[aria-label="Close terminal"]`).click().catch(() => {}); await wait(page, 1000); } },

  // ---- Settings
  ...['Preferences', 'Appearance', 'Notifications', 'Shortcuts', 'Pairing', 'Projects', 'Worktrees', 'Providers', 'Models', 'Extensions', 'Server', 'About'].map(pane => ({
    name: `settings-${pane.toLowerCase()}`, window: M, reveal: h => settings(h, pane),
    parts: pane === 'Preferences' ? { 'settings-nav': S.settingsNav, 'settings-nav-selected': S.settingsNavSelected, 'settings-search': S.settingsSearch, 'back-link': S.back,
      'settings-list': S.settingsList, 'settings-row': S.settingsRow, select: S.select, switch: S.switchOff,
      'section-title': page => visible(page, '[role=tabpanel] h2, [role=tabpanel] h3, [role=tabpanel] [data-slot*=title]').first() }
      : pane === 'Appearance' ? { 'text-field': page => visible(page, '[role=tabpanel] input').first(), link: page => visible(page, '[role=tabpanel] a').first() }
      : pane === 'Notifications' ? { 'switch-on': page => visible(page, `${dc('switch')}:has(input:checked), ${dc('switch')}[data-checked]`).first() }
      : pane === 'Shortcuts' ? { kbd: page => visible(page, `[role=tabpanel] ${dc('keybind-v2')}`).first(), 'button-quiet': page => visible(page, '[role=tabpanel] button').filter({ hasText: /^Reset to defaults$/ }).first() }
      : pane === 'Pairing' ? { 'button-neutral': page => visible(page, '[role=tabpanel] button').filter({ hasText: /^Pair device$/ }).first() }
      : pane === 'Providers' ? { 'tag': page => visible(page, `[role=tabpanel] ${dc('tag')}`).first(), 'provider-icon': page => visible(page, `[role=tabpanel] ${dc('provider-icon')}`).first() }
      : pane === 'Extensions' ? { 'segmented-selected': page => visible(page, '[role=tabpanel] [role=tab][aria-selected=true]').last() }
      : pane === 'Server' ? { 'status-dot': page => visible(page, '[role=tabpanel] [class*="rounded-full"]').first() }
      : {},
    optionalParts: ['kbd', 'switch-on', 'tag', 'provider-icon', 'section-title', 'link', 'status-dot', 'segmented-selected', 'button-quiet'] })),
  { name: 'settings-select-open', window: M,
    reveal: async h => { await settings(h, 'Preferences'); await h.page.locator(`${dc('select-v2')}[aria-label=Tabs]`).click(); await wait(h.page, 800); },
    parts: { listbox: page => visible(page, '[role=listbox]').last(), option: page => visible(page, '[role=listbox] [role=option]').nth(1),
      'option-selected': page => visible(page, '[role=listbox] [role=option][aria-selected=true], [role=listbox] [role=option][data-selected]').first() },
    optionalParts: ['option-selected'] },
  { name: 'settings-search-filled', window: M, state: 'filled',
    reveal: async h => { await settings(h, 'Preferences'); await h.page.locator(`${S.settingsSearch} input`).click(); await h.page.keyboard.type('font'); await wait(h.page, 1000); },
    parts: { 'settings-search': S.settingsSearch },
    after: async ({ page }) => { await page.locator(`${S.settingsSearch} input`).fill('').catch(() => {}); await wait(page, 400); } },

  // ---- states, one part per shot: hover with the real pointer, focus-visible with a key press then
  // focus, pressed with :active forced through CDP (nothing is clicked).
  ...states([
    ['home', M, async () => {}, { 'icon-button-home': S.home, 'project-row': S.projectRowOther, 'session-row': S.sessionRow, 'button-neutral': S.newSession,
      'icon-button': S.addProject, 'side-link': S.sideLink }, ['hover', 'focus-visible', 'pressed']],
    ['home', M, async () => {}, { 'search-field': S.searchInput }, ['hover', 'focus-visible']],
    ['tabs', M, session, { 'session-tab': page => page.locator(dc('session-tab-popover-trigger')).filter({ hasText: 'Contents of hello.txt' }).first() }, ['hover']],
    ['session', M, session, { 'model-button': S.model, 'send-button': S.send, 'attach-button': S.attach, 'more-button': S.more, 'context-button': S.contextButton }, ['hover', 'focus-visible', 'pressed']],
    ['session', M, session, { 'tool-group': S.toolGroup }, ['hover']],
    ['settings', M, async h => settings(h, 'Preferences'), { 'settings-nav': S.settingsNav, select: S.select, switch: S.switchOff }, ['hover', 'focus-visible', 'pressed']],
    ['dialog', M, async h => { await sessionMenu(h); await h.page.locator('[role=menuitem]').filter({ hasText: /^Delete/ }).click(); await wait(h.page, 1000); },
      { 'button-secondary': page => S.dialog(page).locator('button').filter({ hasText: /^Cancel$/ }), 'button-danger': page => S.dialog(page).locator('button').filter({ hasText: /^Delete session$/ }) }, ['hover', 'focus-visible', 'pressed']],
    ['menu', M, sessionMenu, { 'menu-row': S.menuRow }, ['hover']],
    ['palette', M, palette, { 'palette-row': page => S.dialog(page).locator('[role=option]').nth(2) }, ['hover']],
  ]).map(s => ({ ...s, after: s.after || (async ({ page }) => closeAll(page)) })),
];

// ---- the agent run, taken by run.mjs. The owner approved (2026-10-25) harmless test prompts in a
// fresh session on the capture's own folder (the `opencode` project), approving only actions inside it.
// One fresh session per theme, opened from Home's New session; the model is whatever the new session
// offers (the project's default), never changed.
async function sendPrompt({ page }, text) {
  await page.locator(dc('composer-editor')).click();
  await page.keyboard.type(text, { delay: 8 }); await wait(page, 300);
  await page.keyboard.press('Enter'); await wait(page, 900);
}
const permission = page => visible(page, '[data-component=dock-prompt][data-kind=permission]');
const approveButton = page => permission(page).locator('button').filter({ hasText: /^Allow once$/ }).first();
const rejectButton = page => permission(page).locator('button').filter({ hasText: /^Deny$/ }).first();
let idleSamples = 0;
export const RUN = {
  window: 'main',
  // `<theme>-more` continues the theme's session instead of opening a new one (run with RAW set to
  // another folder, since run.mjs empties its run folder first; the frames are merged afterwards).
  async start(h) {
    if (/-more$/.test(process.argv[2] || '')) return session(h);
    await home(h);
    await h.page.locator('[data-action=home-new-session]').click(); await wait(h.page, 1800);
  },
  async finish(h) { await closeAll(h.page); },
  // Done when nothing marks the session as working (the session-working status row, a Stop button,
  // the progress indicator, an open permission dock) and the newest turn holds the agent's answer,
  // for two samples in a row.
  async state({ page }) {
    if (await permission(page).count()) { idleSamples = 0; return 'approval'; }
    const working = await visible(page, '[data-component=session-working], button[aria-label^="Stop" i], [data-component=session-progress-indicator-v2]').count();
    const lastIsUser = await page.locator(dc('session-turn')).evaluateAll(ts => {
      const t = ts[ts.length - 1];
      return !t || (!!t.querySelector('[data-component=user-message]') && !t.querySelector('[data-component=text-part], [data-component=tool-trigger]'));
    }).catch(() => true);
    if (working || lastIsUser) { idleSamples = 0; return 'running'; }
    return ++idleSamples >= 2 ? 'done' : 'running';
  },
  async reject({ page }) { await rejectButton(page).click().catch(() => {}); await wait(page, 800); },
  steps: [],
  parts: {
    composer: dc('composer'), 'send-button': 'button[aria-label="Send"]', 'stop-button': 'button[aria-label^="Stop" i]',
    'user-message': dc('user-message'), 'text-part': dc('text-part'), markdown: dc('markdown'),
    'tool-trigger': dc('tool-trigger'), 'tool-group': dc('context-tool-group-trigger'), 'session-working': dc('session-working'),
    'permission-dock': '[data-component=dock-prompt][data-kind=permission]', 'text-shimmer': dc('text-shimmer'),
    'bash-output': dc('bash-output'), 'write-tool': dc('write-tool'), 'progress-indicator': dc('session-progress-indicator-v2'),
  },
};
// Approve once, and only a request whose dock shows one of the exact commands or files these prompts ask for,
// in the scratch folder, and nothing else that could be a command (approve.mjs). Anything else is denied.
const ALLOW = allowance({ root: SCRATCH, rel: '.design-systems/harness-scratch/opencode', files: ['hello.txt', 'notes.txt'], commands: ['sleep 5; ls'] });
const approveInScratch = async ({ page }) => {
  const text = await permission(page).innerText().catch(() => '');
  if (!approvable(text, ALLOW)) return false;
  await approveButton(page).click(); await wait(page, 800); return true;
};
export const RUN_STEPS = {
  dark: [
    { name: 'list-files', send: h => sendPrompt(h, 'List the files in this folder.'), approve: approveInScratch },
    { name: 'create-file', send: h => sendPrompt(h, 'Create hello.txt here with one line: hello from the design capture'), approve: approveInScratch },
    { name: 'run-command', send: h => sendPrompt(h, 'Run ls -la in this folder and show me the output.'), approve: approveInScratch },
  ],
  'dark-more': [
    { name: 'slow-command', send: h => sendPrompt(h, 'Run `sleep 5; ls` in this folder and tell me what it printed.'), approve: approveInScratch },
    { name: 'answer', send: h => sendPrompt(h, 'In three short bullet points, with one inline code example and a three-line CSS code block, what is a design token?') },
  ],
  light: [
    { name: 'read-file', send: h => sendPrompt(h, 'Show me what hello.txt in this folder says.'), approve: approveInScratch },
    { name: 'create-file', send: h => sendPrompt(h, 'Create notes.txt here with one line: second file from the design capture'), approve: approveInScratch },
    { name: 'slow-command', send: h => sendPrompt(h, 'Run `sleep 5; ls` in this folder and tell me what it printed.'), approve: approveInScratch },
    { name: 'answer', send: h => sendPrompt(h, 'In three short bullet points, with one inline code example and a three-line CSS code block, what is a design token?') },
  ],
};
RUN.steps = RUN_STEPS[process.argv[2]] || [];
