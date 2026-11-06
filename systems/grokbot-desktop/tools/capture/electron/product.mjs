// PRODUCT (adapt): everything in this file is Grok Bot 0.75.5's. Another Electron app replaces it
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
// Grok Bot (bundle id com.anysphere.sand) is one window: a sidebar of Bots (a pinned grid, then
// groups), one conversation per Bot, an inspector pane, and Settings as a dialog. Its interface is
// built on the same anysphere-ui kit as Cursor (ui-* classes, --cursor-* tokens) plus its own sand-*
// layer (--sand-* tokens, sand-* classes). It has no data-component attributes: selectors are its
// semantic class names (sand-agent-item, sand-settings-row, ui-menu__row), roles and aria-labels,
// never account text.

import { allowance, approvable } from './approve.mjs';

export const NAME = 'Grok Bot';
// shots.mjs --set-theme connects to the window keyed 'agents' (Cursor's name for its main window), so the
// one window is listed under that key too.
export const WINDOWS = { main: 'Grok Bot', agents: 'Grok Bot' };
export const SCOPES = { main: [':root'] };

// The Bot the capture created for its test prompts (2026-10-25). Every shot starts on its chat, so
// no other Bot's conversation is opened (opening one would mark it read).
export const TEST_BOT = 'Design Capture';
// The conversation open before the capture, reopened at the end: the account's Main Bot, found by the
// marker Grok Bot adds to its aria-label rather than by its name.
export const OPEN_BEFORE = ', Main Bot';

const wait = (page, ms = 600) => page.waitForTimeout(ms);
const btn = (page, label) => page.locator(`button[aria-label="${label}"]`).filter({ visible: true }).first();
const bot = (page, name) => page.locator(name.startsWith(", ") ? `.sand-agent-item[aria-label*="${name}"]` : `.sand-agent-item[aria-label^="${name}"]`).first();
const testBot = page => bot(page, TEST_BOT);

export async function closeAll(page) {
  for (let i = 0; i < 4; i++) {
    const open = await page.locator('[role=menu], [role=dialog], [role=alertdialog]').filter({ visible: true }).count();
    if (!open) break;
    await page.keyboard.press('Escape'); await wait(page, 350);
  }
  // The inspector is a pane, not a dialog, and stays mounted off screen to the right when closed.
  const open = await page.evaluate(() => { const e = document.querySelector('.sand-info-pane__inner'); return !!e && e.getBoundingClientRect().x < innerWidth - 20; });
  if (open) {
    await page.locator('.sand-info-pane button[aria-label="Close"], button[aria-label="Close"]').filter({ visible: true }).first().click({ timeout: 3000 }).catch(() => {}); await wait(page, 700);
  }
}
const scrollSidebarTop = page => page.evaluate(() => {
  const v = document.querySelector('.sand-pinned-grid')?.closest('.ui-scroll-area__viewport'); if (v) v.scrollTop = 0;
});
export async function home({ page }) {
  await closeAll(page);
  const t = testBot(page);
  await t.click(); await wait(page, 900);
  await scrollSidebarTop(page); await wait(page, 300);
  // Park the pointer on the empty sidebar header: over the transcript it reveals a message's actions.
  await page.mouse.move(60, 24);
}
export async function reset(h) { return home(h); }

async function settings({ page }, pane) {
  await page.locator('.sand-agents-sidebar__footer button').filter({ hasText: /\S/ }).first().click(); await wait(page, 700);
  await page.locator('[role=menuitem]').filter({ hasText: /^Settings$/ }).first().click(); await wait(page, 1100);
  if (pane) { await page.locator('.sand-settings-nav__item').filter({ hasText: new RegExp(`^${pane}$`) }).first().click(); await wait(page, 1200); }
}
async function clearPrompt(page) {
  await page.locator('.sand-prompt-field').click();
  await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); await wait(page, 500);
}

// Grok Bot draws focus rings only while the root carries [data-sand-keyboard-nav], which it sets on a
// Tab press (`:root:not([data-sand-keyboard-nav]) :focus-visible { outline: none !important }`). So a
// focus shot presses Tab first, as a keyboard user would, then focuses the part. Hover needs a real
// pointer for the pane rows ([data-pane-row-item]:hover); shots.mjs moves the pointer for hover shots.
export async function prepareState(page, selector, states, on) {
  if (!states.includes('focus-visible') || !on) return;
  await page.keyboard.press('Tab'); await wait(page, 200);
}

// A fingerprint of the account state a capture must never change: every Bot and group name in the
// sidebar with the groups' counts (unread markers stripped, since other Bots' routines post on their
// own). shots.mjs takes it before and after every shot and stops when it differs. Settings are not in
// it: the capture read every General and Computer setting before and after instead (README).
export async function guard(h) {
  const { page } = h;
  const rows = await page.locator('.sand-agent-item, .sand-agents-section__header').evaluateAll(es =>
    es.map(e => (e.getAttribute('aria-label') || e.innerText).replace(/, Unread activity$/, '').replace(/\s+/g, ' ').trim()));
  return rows.join(' / ');
}

// Theme is the app's own setting (Settings > General > Theme: Follow System, Light, Dark). It does not
// follow an emulated prefers-color-scheme (Electron's nativeTheme decides "Follow System"). Returns the
// label it replaced, so the caller can restore it.
export const THEME_LABELS = { light: 'Light', dark: 'Dark', system: 'Follow System' };
export async function setTheme(h, label) {
  const { page } = h;
  await home(h); await settings(h, 'General');
  const trigger = page.locator('button[role=combobox][aria-label="Theme"]');
  const before = (await trigger.innerText()).trim();
  if (before !== label) {
    await trigger.click(); await wait(page, 600);
    await page.locator('[role=option]').filter({ hasText: new RegExp(`^${label}$`) }).first().click(); await wait(page, 1500);
  }
  await closeAll(page); await home(h);
  return before;
}

// ---- the shot list
const M = 'main';
const nth = (sel, i) => [sel, i];
const S = {
  sidebar: '.sand-agents-sidebar',
  sidebarHeader: '.sand-agents-sidebar__header',
  searchButton: 'button[aria-label="Search"]',
  newBotButton: 'button[aria-label="New Bot"]',
  pinnedGrid: '.sand-pinned-grid',
  pinnedTile: page => page.locator('.sand-pinned-grid .sand-agent-item').nth(3),
  pinnedTileSelected: '.sand-pinned-grid .sand-agent-item[aria-current]',
  avatar: nth('.sand-pinned-grid .sand-agent-item__avatar', 3),
  sectionHeader: nth('.sand-agents-section__header', 1),
  listRow: page => testBot(page),
  footer: '.sand-agents-sidebar__footer',
  accountButton: page => page.locator('.sand-agents-sidebar__footer button').filter({ hasText: /\S/ }).first(),
  baseAvatar: '.sand-agents-sidebar__footer .sand-kit-base-avatar',
  connectApps: 'button[aria-label="Connect apps"]',
  updatePill: '.sand-update-pill',
  chatHeader: '.sand-chat-header__identity',
  timeSeparator: '.sand-transcript-time-separator',
  agentBubble: nth('.sand-message[data-role=assistant]', 0),
  userBubble: nth('.sand-message[data-role=user]', 0),
  prose: nth('.sand-message-prose', 0),
  questionCard: '.sand-message-card',
  composer: '.sand-kit-message-input-frame',
  promptField: '.sand-prompt-field',
  attach: 'button[aria-label="Composer actions"]',
  mic: 'button[aria-label="Start voice input"]',
  voice: 'button[aria-label="Start voice chat"]',
  send: 'button[aria-label="Send message"]',
  menu: page => page.locator('[role=menu]').filter({ visible: true }).first(),
  menuRow: nth('[role=menu] .ui-menu__row', 0),
  menuSubmenu: nth('[role=menu] .ui-menu__submenu-trigger', 0),
  dialog: page => page.locator('[role=dialog]').filter({ visible: true }).last(),
  backdrop: '.ui-dialog-backdrop',
  dialogClose: 'button[aria-label="Close dialog"]',
  settingsNav: nth('.sand-settings-nav__item', 1),
  settingsNavSelected: page => page.locator('.sand-settings-nav__item').first(),
  settingsRow: nth('.sand-settings-row', 0),
  settingsCopy: nth('.sand-settings-copy', 0),
  settingsHint: nth('.sand-settings-field__hint', 0),
  select: 'button[role=combobox][aria-label="Theme"]',
  switchOn: '[role=switch][aria-checked=true]',
  switchOff: '[role=switch][aria-checked=false]',
  settingsTitle: '.sand-settings-pane-header',
  settingsClose: '.sand-settings-panel__close',
  accountCard: '.sand-account-card',
  accountAction: nth('.sand-account-card__action', 0),
  copyLink: page => page.locator('.sand-settings-row button.sand-kit-icon-button').first(),
  inviteButton: page => page.locator('.sand-settings-nav').locator('xpath=..').locator('button').filter({ hasText: /^Invite teammates$/ }).first(),
};
const cancelButton = page => page.locator('[role=dialog] button').filter({ hasText: /^Cancel$/ }).first();
const createButton = page => page.locator('[role=dialog] button').filter({ hasText: /^Create$/ }).first();
const newBotDialog = async ({ page }) => { await page.locator(S.newBotButton).click(); await wait(page, 1100); };
const accountMenu = async ({ page }) => { await S.accountButton(page).click(); await wait(page, 800); };
const dialogNameInput = page => page.locator('[role=dialog]').filter({ hasText: 'Create New Bot' }).locator('input[aria-label="Bot name"]');

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

export const SHOTS = [
  { name: 'home-default', window: M, reveal: async () => {},
    optionalParts: ['update-pill', 'time-separator', 'user-message'],
    parts: { sidebar: S.sidebar, 'icon-button': S.searchButton, 'pinned-grid': S.pinnedGrid, 'pinned-tile': S.pinnedTile, 'bot-avatar': S.avatar,
      'section-header': S.sectionHeader, 'sidebar-footer': S.footer, 'account-button': S.accountButton, avatar: S.baseAvatar,
      'connect-apps': S.connectApps, 'update-pill': S.updatePill, 'chat-header': S.chatHeader, 'time-separator': S.timeSeparator,
      'agent-message': S.agentBubble, 'user-message': S.userBubble, 'message-prose': S.prose,
      composer: S.composer, 'prompt-field': S.promptField, 'attach-button': S.attach, 'mic-button': S.mic, 'voice-button': S.voice } },
  { name: 'home-list-row', window: M, state: 'selected',
    reveal: async ({ page }) => { await testBot(page).scrollIntoViewIfNeeded(); await wait(page, 400); },
    parts: { 'list-row-selected': S.listRow, 'section-header': nth('.sand-agents-section__header', 9) } },
  { name: 'home-composer-typed', window: M, state: 'filled',
    reveal: async ({ page }) => { await page.locator(S.promptField).click(); await page.keyboard.type('Draft text, never sent'); await wait(page, 500); },
    parts: { composer: S.composer, 'prompt-field': S.promptField, 'send-button': S.send },
    after: async ({ page }) => clearPrompt(page) },
  { name: 'home-composer-focus', window: M, state: 'focus',
    reveal: async ({ page }) => { await page.locator(S.promptField).click(); await wait(page, 400); },
    parts: { composer: S.composer } },
  { name: 'section-expanded', window: M, optional: true,
    reveal: async ({ page }) => { await page.locator('.sand-agents-section__header').filter({ hasText: /^Developers/ }).click(); await wait(page, 900); },
    parts: { 'section-header-open': page => page.locator('.sand-agents-section__header').filter({ hasText: /^Developers/ }),
      'list-row': page => page.locator('.sand-agents-section').filter({ has: page.locator('.sand-agents-section__header', { hasText: /^Developers/ }) }).locator('.sand-agent-item').first() },
    after: async ({ page }) => { await page.locator('.sand-agents-section__header').filter({ hasText: /^Developers/ }).click(); await wait(page, 700); } },
  { name: 'account-menu', window: M, reveal: accountMenu, optionalParts: ['menu-banner'],
    parts: { menu: S.menu, 'menu-row': nth('[role=menu] .ui-menu__row', 0), 'menu-submenu-trigger': S.menuSubmenu,
      'menu-banner': page => page.locator('[role=menu] button').filter({ hasText: /^Install$/ }).locator('xpath=..') } },
  { name: 'account-submenu', window: M,
    reveal: async h => { await accountMenu(h); await h.page.locator('[role=menu] .ui-menu__submenu-trigger').filter({ hasText: /Weekly usage/ }).hover(); await wait(h.page, 1100); },
    parts: { submenu: page => page.locator('[role=menu]').filter({ visible: true }).last(), 'menu-row-highlighted': '[role=menu] .ui-menu__submenu-trigger[data-highlighted], [role=menu] [aria-expanded=true]' } },
  { name: 'support-submenu', window: M,
    reveal: async h => { await accountMenu(h); await h.page.locator('[role=menu] .ui-menu__submenu-trigger').filter({ hasText: /Support/ }).hover(); await wait(h.page, 1100); },
    parts: { submenu: page => page.locator('[role=menu]').filter({ visible: true }).last() } },
  { name: 'composer-menu', window: M,
    reveal: async ({ page }) => { await page.locator(S.attach).click(); await wait(page, 800); },
    parts: { menu: S.menu, 'menu-row': nth('[role=menu] .ui-menu__row', 0) } },
  { name: 'context-menu', window: M,
    reveal: async ({ page }) => { await testBot(page).click({ button: 'right' }); await wait(page, 800); },
    parts: { 'context-menu': S.menu, 'menu-row': nth('[role=menu] [role=menuitem]', 0), 'menu-row-danger': page => page.locator('[role=menu] [role=menuitem]').filter({ hasText: /^Delete$/ }) } },
  { name: 'delete-confirmation', window: M,
    reveal: async ({ page }) => { await testBot(page).click({ button: 'right' }); await wait(page, 800);
      await page.locator('[role=menu] [role=menuitem]').filter({ hasText: /^Delete$/ }).click(); await wait(page, 1000); },
    parts: { 'confirm-dialog': page => page.locator('[role=dialog], [role=alertdialog]').filter({ visible: true }).last(),
      'button-danger': page => page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Delete/ }).first(),
      'button-secondary': page => page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Cancel$/ }).first() },
    after: async ({ page }) => { await page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Cancel$/ }).first().click().catch(() => {}); await wait(page, 600); } },
  { name: 'tooltip', window: M, state: 'hover',
    reveal: async ({ page }) => { await page.locator(S.searchButton).hover(); await wait(page, 1600); },
    optionalParts: ['tooltip'],
    parts: { tooltip: page => page.locator('[role=tooltip], .ui-tooltip').filter({ visible: true }).first(), 'icon-button': S.searchButton } },
  { name: 'search-palette', window: M,
    reveal: async ({ page }) => { await page.locator(S.searchButton).click(); await wait(page, 1000); },
    parts: { palette: S.dialog, backdrop: S.backdrop, 'palette-input': page => page.locator('[role=dialog] input').first(),
      'palette-row-selected': page => page.locator('[role=dialog] [role=option][aria-selected=true]').first(),
      'palette-row': page => page.locator('[role=dialog] [role=option][aria-selected=false]').first() } },
  { name: 'search-palette-filtered', window: M, state: 'filled',
    reveal: async ({ page }) => { await page.locator(S.searchButton).click(); await wait(page, 1000); await page.keyboard.type('design'); await wait(page, 1000); },
    parts: { palette: S.dialog } },
  { name: 'search-palette-empty', window: M, state: 'empty',
    reveal: async ({ page }) => { await page.locator(S.searchButton).click(); await wait(page, 1000); await page.keyboard.type('zzqxv'); await wait(page, 1000); },
    parts: { palette: S.dialog } },
  { name: 'new-bot-dialog', window: M, reveal: newBotDialog,
    parts: { dialog: S.dialog, backdrop: S.backdrop, 'dialog-close': S.dialogClose, 'text-field': dialogNameInput,
      'shape-option': nth('.sand-agent-character__shape', 0), 'shape-option-selected': page => page.locator('.sand-agent-character__shape[aria-pressed=true], .sand-agent-character__shape[aria-checked=true]').first(),
      'color-swatch': page => page.locator('button[aria-label$="character color"]').first(),
      'button-secondary': cancelButton, 'button-primary-disabled': createButton },
    optionalParts: ['shape-option-selected'],
    after: async ({ page }) => { await cancelButton(page).click().catch(() => {}); await wait(page, 500); } },
  { name: 'new-bot-dialog-filled', window: M, state: 'filled',
    reveal: async h => { await newBotDialog(h); await dialogNameInput(h.page).click(); await h.page.keyboard.type('Typed, never created'); await wait(h.page, 600); },
    parts: { 'text-field': dialogNameInput, 'button-primary': createButton },
    after: async ({ page }) => { await cancelButton(page).click().catch(() => {}); await wait(page, 500); } },
  { name: 'connect-apps', window: M,
    reveal: async ({ page }) => { await page.locator(S.connectApps).click(); await wait(page, 1500); },
    parts: { dialog: S.dialog, 'search-field': page => page.locator('[role=dialog] input').first(),
      'filter-pill-selected': page => page.locator('[role=dialog] button').filter({ hasText: /^All$/ }).first(),
      'filter-pill': page => page.locator('[role=dialog] button').filter({ hasText: /^Productivity$/ }).first(),
      'button-tonal': page => page.locator('[role=dialog] button.sand-button').filter({ hasText: /^Add/ }).first(),
      'app-icon': page => page.locator('[role=dialog] img').first() },
    optionalParts: ['app-icon'] },
  { name: 'connect-apps-scrolled', window: M,
    reveal: async ({ page }) => { await page.locator(S.connectApps).click(); await wait(page, 1500); await page.mouse.move(500, 450); await page.mouse.wheel(0, 700); await wait(page, 900); },
    parts: {} },
  { name: 'inspector-library', window: M,
    reveal: async ({ page }) => { await page.locator('button[aria-label="View conversation details"]').click(); await wait(page, 1300);
      await page.locator('[role=tab]').filter({ hasText: /^Library$/ }).click(); await wait(page, 900); },
    parts: { inspector: '.sand-info-pane__inner', 'tab-selected': '[role=tab][aria-selected=true]', tab: nth('[role=tab][aria-selected=false]', 0),
      'inspector-name': page => page.locator('.sand-info-pane__inner input[aria-label="Bot name"]'), 'icon-button-close': page => page.locator('button[aria-label="Close"]').filter({ visible: true }).first() } },
  { name: 'inspector-details', window: M,
    reveal: async ({ page }) => { await page.locator('button[aria-label="View conversation details"]').click(); await wait(page, 1300);
      await page.locator('[role=tab]').filter({ hasText: /^Details$/ }).click(); await wait(page, 900); },
    parts: { inspector: '.sand-info-pane__inner' } },
  { name: 'inspector-computer', window: M,
    reveal: async ({ page }) => { await page.locator('button[aria-label="View conversation details"]').click(); await wait(page, 1300);
      await page.locator('[role=tab]').filter({ hasText: /^Computer$/ }).click(); await wait(page, 2500); },
    parts: { inspector: '.sand-info-pane__inner' } },
  { name: 'settings-general', window: M, reveal: async h => settings(h, 'General'),
    parts: { 'settings-dialog': '.sand-settings-dialog', 'settings-nav': S.settingsNav, 'settings-nav-selected': S.settingsNavSelected,
      'settings-title': S.settingsTitle, 'account-card': S.accountCard, 'button-secondary': S.accountAction, 'settings-group': nth('.sand-settings-row', 1),
      'settings-row': S.settingsRow, 'settings-label': S.settingsCopy, select: S.select, 'switch-on': S.switchOn, 'icon-button-close': S.settingsClose,
      'button-invite': S.inviteButton } },
  { name: 'settings-general-scrolled', window: M,
    reveal: async h => { await settings(h, 'General'); await h.page.locator('.sand-settings-scroll').evaluate(e => { e.scrollTop = e.scrollHeight; }); await wait(h.page, 700); },
    optionalParts: ['switch-off', 'settings-hint'],
    parts: { 'switch-off': S.switchOff, 'settings-hint': S.settingsHint } },
  { name: 'settings-computer', window: M, reveal: async h => settings(h, 'Computer'),
    parts: { 'settings-hint': S.settingsHint, 'status-dot': nth('.sand-settings-pane .sand-kit-status-dot', 0) }, optionalParts: ['status-dot'] },
  { name: 'settings-vault', window: M, reveal: async h => settings(h, 'Vault'),
    parts: { 'tab-selected': page => page.locator('.sand-settings-pane [role=tab][aria-selected=true]').first(),
      tab: page => page.locator('.sand-settings-pane [role=tab][aria-selected=false]').first(),
      'button-primary': page => page.locator('[role=dialog] button').filter({ hasText: /New item/ }).first() },
    optionalParts: ['tab-selected', 'tab'] },
  { name: 'settings-usage', window: M, reveal: async h => settings(h, 'Usage & Billing'),
    parts: { progress: page => page.locator('.sand-settings-pane [role=progressbar], .sand-settings-pane [role=meter]').first() }, optionalParts: ['progress'] },
  { name: 'settings-updates', window: M, reveal: async h => settings(h, 'Updates'), parts: {} },
  { name: 'settings-theme-select', window: M,
    reveal: async h => { await settings(h, 'General'); await h.page.locator(S.select).click(); await wait(h.page, 700); },
    parts: { listbox: page => page.locator('[role=listbox]').filter({ visible: true }).last(), option: nth('[role=listbox] [role=option]', 1),
      'option-selected': '[role=listbox] [role=option][aria-selected=true]' } },
  { name: 'settings-accent-select', window: M,
    reveal: async h => { await settings(h, 'General'); await h.page.locator('button[role=combobox][aria-label="Accent"]').click(); await wait(h.page, 700); },
    parts: { listbox: page => page.locator('[role=listbox]').filter({ visible: true }).last() } },
  { name: 'settings-search-link', window: M, state: 'hover',
    reveal: async h => { await settings(h, 'General'); await h.page.locator('.sand-settings-row').filter({ hasText: /^Theme/ }).hover(); await wait(h.page, 600); },
    parts: { 'copy-link': S.copyLink }, optionalParts: ['copy-link'] },

  // ---- states, one part per shot: hover with the real pointer, focus-visible with a Tab press then
  // focus, pressed with :active forced through CDP (nothing is clicked).
  ...states([
    ['home', M, async () => {}, { 'icon-button': S.searchButton, 'pinned-tile': S.pinnedTile, 'section-header': S.sectionHeader,
      'account-button': S.accountButton, 'attach-button': S.attach, 'connect-apps': S.connectApps }, ['hover', 'focus-visible', 'pressed']],
    ['home', M, async ({ page }) => { await testBot(page).scrollIntoViewIfNeeded(); await wait(page, 400); }, { 'list-row-selected': S.listRow }, ['hover', 'focus-visible']],
    ['dialog', M, newBotDialog, { 'button-secondary': cancelButton, 'dialog-close': S.dialogClose, 'shape-option': nth('.sand-agent-character__shape', 0),
      'color-swatch': page => page.locator('button[aria-label$="character color"]').first() }, ['hover', 'focus-visible', 'pressed']],
    ['settings', M, async h => settings(h, 'General'), { 'settings-nav': S.settingsNav, select: S.select, 'switch-on': S.switchOn,
      'button-secondary': S.accountAction }, ['hover', 'focus-visible', 'pressed']],
    ['menu', M, accountMenu, { 'menu-row': nth('[role=menu] .ui-menu__row', 0) }, ['hover']],
    ['palette', M, async ({ page }) => { await page.locator(S.searchButton).click(); await wait(page, 1000); }, { 'palette-row': page => page.locator('[role=dialog] [role=option]').nth(2) }, ['hover']],
    ['apps', M, async ({ page }) => { await page.locator(S.connectApps).click(); await wait(page, 1500); },
      { 'filter-pill': page => page.locator('[role=dialog] button').filter({ hasText: /^Productivity$/ }).first(),
        'button-tonal': page => page.locator('[role=dialog] button.sand-button').filter({ hasText: /^Add/ }).first() }, ['hover', 'pressed']],
  ]).map(s => ({ ...s, after: s.after || (async ({ page }) => closeAll(page)) })),
];

// The test conversation after run.mjs, and the conversation that was open before the capture (the
// owner's own, already read: opening it changes nothing).
const CONVERSATION = {
  'user-message': page => page.locator('.sand-message[data-role=user]').filter({ visible: true }).last(),
  'agent-message': page => page.locator('.sand-message[data-role=assistant]').filter({ visible: true }).last(),
  'message-prose': page => page.locator('.sand-message-prose').last(),
  'time-separator': '.sand-transcript-time-separator',
  'row-timestamp': page => page.locator('.sand-row-timestamp').last(),
  'system-event': page => page.locator('.sand-kit-system-event').last(),
  'inline-code': page => page.locator('.sand-message-prose code').last(),
  link: page => page.locator('.sand-message-prose a').filter({ visible: true }).last(),
};
SHOTS.push(
  { name: 'conversation', window: M, reveal: async () => {}, optionalParts: Object.keys(CONVERSATION), parts: { ...CONVERSATION, composer: S.composer } },
  { name: 'conversation-top', window: M, reveal: async ({ page }) => { await page.mouse.move(700, 300); await page.mouse.wheel(0, -4000); await wait(page, 900); },
    optionalParts: ['question-card'], parts: { 'question-card': S.questionCard } },
  { name: 'conversation-history', window: M, optionalParts: Object.keys(CONVERSATION),
    reveal: async ({ page }) => { await bot(page, OPEN_BEFORE).click(); await wait(page, 1500); },
    parts: { ...CONVERSATION, 'pr-pill': page => page.locator('.sand-pill--github-pr').last(), 'chat-header': S.chatHeader },
    after: async ({ page }) => { await testBot(page).click(); await wait(page, 800); } },
  { name: 'conversation-history-inspector', window: M, optional: true,
    reveal: async ({ page }) => { await bot(page, OPEN_BEFORE).click(); await wait(page, 1500);
      await page.locator('button[aria-label="View conversation details"]').click(); await wait(page, 1300);
      await page.locator('[role=tab]').filter({ hasText: /^Details$/ }).click(); await wait(page, 900); },
    optionalParts: ['link-card', 'switch-accent'],
    parts: { 'link-card': page => page.locator('.sand-info-pane__inner button[aria-label^="Open "]').first(), 'switch-accent': page => page.locator('.sand-info-pane__inner [role=switch]').first() },
    after: async ({ page }) => { await closeAll(page); await testBot(page).click(); await wait(page, 800); } },
);

// ---- the agent run, taken by run.mjs. The owner approved (2026-10-25) harmless test prompts in a
// fresh Bot, pointed at the capture's own folder ~/.design-systems/harness-scratch/grokbot, approving
// only actions inside it.
const SCRATCH = '~/.design-systems/harness-scratch/grokbot';
async function sendPrompt({ page }, text) {
  await page.locator(S.promptField).click();
  await page.keyboard.type(text, { delay: 8 }); await wait(page, 300);
  await page.keyboard.press('Enter'); await wait(page, 900);
}
const transcript = page => page.locator('.sand-virtual-transcript');
let idleSamples = 0;
const approveButton = page => transcript(page).locator('button').filter({ visible: true }).filter({ hasText: /^(Allow|Approve|Run|Accept|Yes)\b/ }).last();
const rejectButton = page => transcript(page).locator('button').filter({ visible: true }).filter({ hasText: /^(Deny|Reject|Skip|Cancel|No)\b/ }).last();
export const RUN = {
  window: 'main',
  async start(h) { await home(h); },
  async finish(h) { await closeAll(h.page); },
  // A step is done only when the Bot has answered the prompt just sent and stayed idle for two
  // samples in a row: while it works the transcript ends in an activity row (its mark and a shimmering
  // label), and until it answers the newest row is the owner's. No mark alone is not enough, since the
  // mark appears a moment after the prompt and between a progress message and the next tool call.
  async state({ page }) {
    if (await approveButton(page).count()) return 'approval';
    const stop = page.locator('button[aria-label*="Stop" i], button[aria-label*="Cancel" i]').filter({ visible: true });
    const working = page.locator('.sand-virtual-transcript .sand-activity-mark').filter({ visible: true });
    const newestIsOwner = await page.locator('.sand-transcript-row').evaluateAll(rows => {
      const last = rows.reduce((a, r) => (!a || +r.dataset.index > +a.dataset.index ? r : a), null);
      return !!last && last.getAttribute('data-role') === 'user';
    }).catch(() => true);
    if ((await stop.count()) || (await working.count()) || newestIsOwner) { idleSamples = 0; return 'running'; }
    return ++idleSamples >= 2 ? 'done' : 'running';
  },
  async reject({ page }) { await rejectButton(page).click().catch(() => {}); await wait(page, 800); },
  steps: [],
  parts: {
    composer: S.composer, 'send-button': S.send, 'prompt-field': S.promptField,
    'transcript-row': '.sand-transcript-row', 'message-prose': '.sand-message-prose', 'agent-message': '.sand-message[data-role=assistant]',
    'user-message': '.sand-message[data-role=user]',
    'system-event': '.sand-kit-system-event', 'activity-mark': '.sand-activity-mark', 'activity-label': '.sand-shimmer-text',
  },
};
// Approve only a request whose card shows one of the exact commands or files these prompts ask for, in the
// scratch folder, and nothing else that could be a command (approve.mjs). The card is the nearest ancestor
// of the button holding more than the button's own label, never a wider block: the transcript holds the
// prompt, which names the folder itself. The Bot's working folder is not known, so only absolute and `~/`
// forms are approved.
const ALLOW = allowance({ root: `${process.env.HOME}/${SCRATCH.slice(2)}`, rel: SCRATCH.slice(2), files: ['hello.txt', 'notes.txt'], relative: false });
const approveInScratch = async ({ page }) => {
  const text = await approveButton(page).evaluate(b => {
    let e = b;
    for (let i = 0; i < 8 && e.parentElement; i++) { e = e.parentElement; if (e.innerText.trim().length > b.innerText.trim().length + 20) break; }
    return e.innerText;
  }).catch(() => '');
  if (!approvable(text, ALLOW)) return false;
  await approveButton(page).click(); await wait(page, 800); return true;
};
export const RUN_STEPS = {
  dark: [
    { name: 'list-files', send: h => sendPrompt(h, `List the files in ${SCRATCH} on this Mac.`), approve: approveInScratch },
    { name: 'create-file', send: h => sendPrompt(h, `Create notes.txt in ${SCRATCH} on this Mac with one line: second file from the design capture`), approve: approveInScratch },
    { name: 'answer', send: h => sendPrompt(h, 'In three short bullet points, with one inline code example, what is a design token?') },
  ],
  light: [
    { name: 'read-file', send: h => sendPrompt(h, `Show me what hello.txt in ${SCRATCH} on this Mac says.`), approve: approveInScratch },
    { name: 'answer', send: h => sendPrompt(h, 'Show a three-line CSS example of a colour token in a code block, nothing else.') },
  ],
};
RUN.steps = RUN_STEPS[process.argv[2]] || [];
