// PRODUCT (adapt): everything in this file is Cursor 3.27.6's. Another Electron app replaces it
// whole and keeps cdp.mjs, vars.mjs, shots.mjs and measure.mjs as they are.
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

export const NAME = 'Cursor';
export const WINDOWS = { agents: 'Cursor Agents', ide: /harness-scratch$/ };
// Scopes vars.mjs resolves custom properties on, besides html and body.
export const SCOPES = { agents: ['[data-component="root"]'], ide: ['.monaco-workbench'] };

// ---- navigation helpers (selectors are Cursor's own class names and aria-labels, never account text)
const btn = (page, label) => page.locator(`button[aria-label="${label}"]:visible`).first();
const navRow = (page, label) => page.locator('.ui-sidebar-menu-button-trigger').filter({ hasText: new RegExp(`^${label.replace(/[&]/g, '\\$&')}$`) }).first();
const wait = (page, ms = 600) => page.waitForTimeout(ms);
async function esc(page, n = 2) { for (let i = 0; i < n; i++) { await page.keyboard.press('Escape'); await wait(page, 200); } }

const OPEN = '[data-component$="-backdrop"], [role=menu], [role=dialog], [role=listbox], [role=tooltip], [role=alertdialog]';
export async function closeAll(page) {
  for (let i = 0; i < 4 && await page.locator(OPEN).first().isVisible().catch(() => false); i++) {
    await page.keyboard.press('Escape'); await wait(page, 300);
    const bd = page.locator('[data-component$="-backdrop"]').first();
    if (i >= 1 && await bd.isVisible().catch(() => false)) await bd.click({ position: { x: 5, y: 5 }, force: true }).catch(() => {});
  }
}
export async function home({ page }) {
  await closeAll(page);
  if (await page.getByText('Back', { exact: true }).first().isVisible().catch(() => false)) {
    await page.getByText('Back', { exact: true }).first().click(); await wait(page);
  }
  if (!(await btn(page, 'Hide Sidebar').isVisible().catch(() => false)) && (await btn(page, 'Show Sidebar').isVisible().catch(() => false))) {
    await btn(page, 'Show Sidebar').click(); await wait(page);
  }
  await navRow(page, 'New Chat').click(); await wait(page, 800);
  await page.mouse.move(5, 940);
}
// Called before every shot: bring the window back to a known screen.
export async function reset(h, win) { if (win === 'agents') return home(h); await esc(h.page); }
async function settings({ page }, pane) {
  await btn(page, 'Settings').click(); await wait(page, 900);
  if (pane) { await navRow(page, pane).click(); await wait(page, 900); }
}
// Typing in the composer saves an unsent draft agent in the sidebar; emptying the composer removes it.
async function clearPrompt(page) {
  await page.locator('.ui-prompt-input-editor__input').click();
  await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); await wait(page, 800);
}

// What a state needs besides the pointer or keyboard, in this product. Called with on=true before
// the screenshot and on=false after. Cursor's focus ring is 0px wide unless the Agents window's root
// carries [data-focus-ring] (its CSS: `[data-component="root"][data-focus-ring] { --cursor-focus-ring-width:
// var(--glass-focus-ring-width) }`); a Tab press does not set it. Focus shots set it and the README says so.
// Hover needs no help when it is a real pointer: anysphere-ui gates hover fills on
// [data-pointer-hover-intent], which its JS sets on pointer movement, so a CDP-forced :hover shows nothing.
export async function prepareState(page, selector, states, on) {
  if (!states.includes('focus-visible')) return;
  await page.evaluate(on => {
    const root = document.querySelector('[data-component="root"]');
    if (root) on ? root.setAttribute('data-focus-ring', '') : root.removeAttribute('data-focus-ring');
  }, on);
}

// A fingerprint of the account state a capture must never change: the composer's model and the
// sidebar's rows. shots.mjs takes it before and after every shot and stops when it differs.
export async function guard(h, win) {
  if (win !== 'agents') return '';
  const { page } = h;
  await home(h);
  const model = await page.locator('.ui-prompt-input-toolbar__right button.ui-button').first().innerText().catch(() => '?');
  const rows = await page.locator('.ui-sidebar-menu-button-trigger').allInnerTexts().catch(() => []);
  return `${model} | ${rows.join(' / ')}`;
}

// The theme is Cursor's own setting (Settings > Appearance > Theme); it does not follow an emulated
// prefers-color-scheme. Returns the label it replaced, so the caller can restore it.
export const THEME_LABELS = { light: 'Cursor Light', dark: 'Cursor Dark' };
const ALL_THEMES = ['System', 'Cursor Light', 'Cursor Light Colorblind', 'Cursor Dark', 'Cursor Dark High Contrast'];
export async function setTheme(h, label) {
  const { page } = h;
  await home(h); await settings(h, 'Appearance');
  const trigger = page.locator('button.ui-select-trigger').filter({ hasText: new RegExp(`^(${ALL_THEMES.join('|')})$`) }).first();
  const before = (await trigger.innerText()).trim();
  if (before !== label) {
    await trigger.click(); await wait(page, 500);
    await page.locator('[role=option]').filter({ hasText: new RegExp(`^${label}$`) }).first().click(); await wait(page, 1500);
  }
  await home(h);
  return before;
}

// ---- the shot list. Selectors are Cursor's data-component names, roles and class names.
const A = 'agents', I = 'ide';
const dc = n => `[data-component="${n}"]`;
const nth = (sel, i) => [sel, i];
const S = {
  sidebar: dc('workspace-sidebar'),
  navRow: nth('.ui-sidebar-menu-button', 1),           // Automations: an unselected row
  navRowSelected: '.ui-sidebar-menu-button:has([aria-current=page])',
  agentRow: page => page.locator('.ui-sidebar-menu-button:has(.ui-sidebar-menu-button-status-icon)').first(),
  groupLabel: '.ui-sidebar-group-label',
  iconButton: 'button[aria-label="Search"]',
  statusBadge: '.ui-status-badge',
  footer: dc('glass-sidebar-footer'),
  avatar: dc('avatar'),
  updateButton: dc('glass-sidebar-update-button'),
  selectText: 'button[role=combobox][data-variant=text]',
  composer: '.ui-prompt-input__container',
  editor: '.ui-prompt-input-editor__input',
  voice: dc('realtime-voice-start'),
  modelButton: '.ui-prompt-input-toolbar__right button.ui-button',
  pill: 'button.ui-pill',
  ideCta: dc('open-editor-window-cta'),
  importCta: dc('claude-code-import-cta'),
  menu: dc('menu-popup'),
  menuRow: nth(dc('menu-row'), 0),
  menuSep: dc('menu-separator'),
  dialog: '[role=dialog]',
  tooltip: dc('tooltip-popup'),
  tab: '[role=tab][aria-selected=false]',
  tabSelected: '[role=tab][aria-selected=true]',
  switchOn: '[role=switch][aria-checked=true]:not([aria-disabled=true])',
  switchOff: '[role=switch][aria-checked=false]',
  switchDisabled: '[role=switch][aria-disabled=true]',
  selectOutline: 'button[role=combobox][data-variant=outline]',
  settingsSearch: '.ui-input-group',
  settingsSearchInput: '.ui-input-group__input',
  settingsNav: nth('.ui-sidebar-menu-button', 2),
  settingsNavSelected: '.ui-sidebar-menu-button:has([aria-current=page])',
  fieldGroup: '.ui-field-group',
  fieldRow: nth('.ui-field-group__entry', 0),
  banner: dc('settings-inline-banner'),
};
const createButton = page => page.locator('[role=dialog] button').filter({ hasText: /^Create Project$/ }).first();
const openButton = page => page.locator('button').filter({ hasText: /^Open$/ }).first();
const newAutomation = page => page.locator('button').filter({ hasText: /^New Automation$/ }).first();
const dialogClose = page => page.locator('[role=dialog] button[aria-label]').first();
const openProjectDialog = async ({ page }) => { await btn(page, 'New Project').click(); await wait(page, 1000); };

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
  { name: 'home-default', window: A, reveal: async () => {},
    parts: { sidebar: S.sidebar, 'sidebar-row': S.navRow, 'sidebar-row-selected': S.navRowSelected, 'agent-row': S.agentRow,
      'sidebar-group-label': S.groupLabel, 'icon-button': S.iconButton, 'status-badge': S.statusBadge, 'sidebar-footer': S.footer,
      avatar: S.avatar, 'button-update': S.updateButton, 'select-text': S.selectText, composer: S.composer, 'composer-editor': S.editor,
      'voice-button': S.voice, 'model-button': S.modelButton, pill: S.pill, 'ide-button': S.ideCta, 'import-cta': S.importCta } },
  { name: 'home-composer-typed', window: A, state: 'filled',
    reveal: async ({ page }) => { await page.locator(S.editor).click(); await page.keyboard.type('Draft text, never sent'); await wait(page, 500); },
    parts: { composer: S.composer, 'composer-editor': S.editor, 'send-button': '.ui-prompt-input-submit-button' },
    after: async ({ page }) => clearPrompt(page) },
  { name: 'search-palette', window: A,
    reveal: async ({ page }) => { await btn(page, 'Search').click(); await wait(page, 900); },
    parts: { palette: dc('base-dialog-popup'), backdrop: dc('base-dialog-backdrop'), 'palette-input': dc('palette-input-row'), tab: S.tab, 'tab-selected': S.tabSelected,
      'palette-section-heading': dc('palette-section-heading'), 'palette-row': `${dc('palette-item')}[aria-selected=false]`,
      'palette-row-selected': `${dc('palette-item')}[aria-selected=true]`, kbd: dc('palette-shortcut') } },
  { name: 'search-palette-empty', window: A, state: 'empty',
    reveal: async ({ page }) => { await btn(page, 'Search').click(); await wait(page, 900); await page.keyboard.type('zzqxv'); await wait(page, 1000); },
    parts: { palette: dc('base-dialog-popup') } },
  { name: 'model-menu', window: A,
    reveal: async ({ page }) => { await page.locator(S.modelButton).first().click(); await wait(page); },
    parts: { menu: S.menu, 'menu-toggle-row': dc('menu-toggle-row'), 'switch-sm': `${dc('menu-toggle-row')} ${dc('switch')}`,
      'menu-submenu-trigger': nth(dc('menu-submenu-trigger'), 0), 'menu-footer': dc('menu-footer') } },
  { name: 'model-submenu', window: A,
    reveal: async ({ page }) => { await page.locator(S.modelButton).first().click(); await wait(page);
      await page.locator(dc('menu-footer')).locator(dc('menu-submenu-trigger')).hover(); await wait(page, 1000); },
    parts: { submenu: page => page.locator(S.menu).last(), 'menu-section-title': dc('menu-section-title'), 'menu-search': dc('menu-search-row') } },
  { name: 'plus-menu', window: A,
    reveal: async ({ page }) => { await btn(page, 'Add agents, context, tools').click(); await wait(page); },
    parts: { 'command-menu': page => page.locator('[role=listbox]').last().locator('xpath=..'), 'command-option': nth('[role=listbox] [role=option]', 0) } },
  { name: 'environment-select', window: A,
    reveal: async ({ page }) => { await page.locator(S.selectText).first().click(); await wait(page, 800);
      await page.locator(dc('search-menu-row')).filter({ hasText: /^This Mac$/ }).first().hover(); await wait(page, 1000); },
    parts: { 'select-popover': nth(dc('search-menu-popup'), 0), 'select-search': nth(dc('search-menu-input'), 0), 'select-section-title': dc('search-menu-section-title'),
      'select-option': nth(dc('search-menu-row'), 0), 'select-option-highlighted': `${dc('search-menu-row')}[data-highlighted]`, 'submenu-popover': nth(dc('search-menu-popup'), 1),
      'switch-sm-off': `${dc('search-menu-row')} ${dc('switch')}` } },
  { name: 'chat-actions-menu', window: A,
    reveal: async ({ page }) => { await btn(page, 'Chat actions').click(); await wait(page); },
    parts: { menu: S.menu, 'menu-row': S.menuRow } },
  { name: 'tooltip', window: A, state: 'hover',
    reveal: async ({ page }) => { await btn(page, 'Search').hover(); await wait(page, 1700); },
    parts: { tooltip: S.tooltip, 'icon-button': S.iconButton } },
  { name: 'sidebar-hover-card', window: A, state: 'hover',
    reveal: async ({ page }) => { await page.locator('.ui-sidebar-group').nth(0).locator('.ui-sidebar-menu-button').first().hover(); await wait(page, 1500); },
    parts: { 'sidebar-row': page => page.locator('.ui-sidebar-group').nth(0).locator('.ui-sidebar-menu-button').first(), 'hover-card': dc('preview-card-layer-popup') } },
  { name: 'sidebar-context-menu', window: A,
    reveal: async ({ page }) => { await S.agentRow(page).click({ button: 'right' }); await wait(page, 800); },
    parts: { 'context-menu': S.menu, 'menu-row': S.menuRow, 'menu-separator': S.menuSep, 'menu-submenu-trigger': dc('menu-submenu-trigger') } },
  { name: 'create-project-dialog', window: A, reveal: openProjectDialog,
    parts: { dialog: S.dialog, 'button-primary': createButton, 'dialog-close': dialogClose, 'icon-picker': dc('popover-trigger'), 'select-text': `[role=dialog] ${S.selectText}` } },
  { name: 'customize', window: A,
    reveal: async ({ page }) => { await navRow(page, 'Customize').click(); await wait(page, 1600); },
    parts: { banner: S.banner, 'search-field': '.ui-customize-view .ui-input-group', 'filter-pill': nth('.ui-customize-view button.ui-pill', 1),
      'select-outline': '.ui-customize-view .ui-select-trigger', 'list-row': nth('[data-mcp-manage-server]', 0), badge: '[data-mcp-manage-server] .ui-pill',
      'text-button-accent': 'button[data-tone=accent][data-variant=text]', 'button-secondary': page => page.locator('.ui-customize-view button').filter({ hasText: /^Browse Marketplace$/ }).first() } },
  { name: 'automations', window: A,
    reveal: async ({ page }) => { await navRow(page, 'Automations').click(); await wait(page, 1600); },
    parts: { 'page-header': '.ui-page-header', 'button-primary-inverse': newAutomation, 'feature-banner': dc('managed-agents-get-started-banner'),
      'tabs-list': nth(dc('tabs-list'), 0), tab: S.tab, 'tab-selected': S.tabSelected, table: '.ui-automations-list-table',
      'table-header': '.ui-automations-list-table__header-row', 'table-row': nth('.ui-automations-list-table__row', 0),
      'search-field-outlined': '.ui-automations-compact-search-outlined', 'template-card': nth('.ui-automations-template-card', 0) } },
  { name: 'automations-scrolled', window: A,
    reveal: async ({ page }) => { await navRow(page, 'Automations').click(); await wait(page, 1600); await page.mouse.move(900, 600); await page.mouse.wheel(0, 600); await wait(page, 800); },
    parts: { 'template-card': nth('.ui-automations-template-card', 0) } },
  { name: 'delete-confirmation', window: A, optional: true,
    reveal: async ({ page }) => { await navRow(page, 'Automations').click(); await wait(page, 1600);
      const row = page.locator('.ui-automations-list-table__row').filter({ hasText: /^Untitled/ }).first(); await row.hover();
      const bs = row.locator('button'); await bs.nth((await bs.count()) - 1).click(); await wait(page, 600);
      await page.locator('[role=menuitem]').filter({ hasText: /^Delete/ }).first().click(); await wait(page, 1000); },
    parts: { 'confirm-dialog': page => page.locator('[role=dialog], [role=alertdialog]').last(), 'button-danger': page => page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Delete/ }).first(),
      'button-secondary': page => page.locator('[role=dialog] button, [role=alertdialog] button').filter({ hasText: /^Cancel$/ }).first() },
    after: async ({ page }) => { await page.locator('[role=dialog] button').filter({ hasText: /^Cancel$/ }).first().click().catch(() => {}); } },
  { name: 'settings-general', window: A, reveal: async h => settings(h, 'General'),
    parts: { 'settings-nav': S.settingsNav, 'settings-nav-selected': S.settingsNavSelected, 'settings-search': S.settingsSearch, 'info-banner': S.banner,
      'field-group': nth(S.fieldGroup, 0), 'field-row': S.fieldRow, 'field-label': nth('.ui-field-group__entry-label', 0), 'field-description': nth('.ui-field-group__entry-description', 0),
      'switch-on': S.switchOn, 'switch-off': S.switchOff, 'button-secondary': openButton, 'button-accent': page => page.locator('button').filter({ hasText: /Invite/ }).first(),
      'select-outline': S.selectOutline, 'page-title': nth('[data-component=glass-settings-tab] h1, [data-component=glass-settings-tab] h2', 0) } },
  { name: 'settings-appearance', window: A, reveal: async h => settings(h, 'Appearance'),
    parts: { 'select-outline': S.selectOutline, slider: nth(dc('slider'), 0), 'number-field': nth(dc('number-field'), 0), 'switch-on': S.switchOn, 'switch-off': S.switchOff,
      'switch-disabled': S.switchDisabled } },
  { name: 'settings-theme-select', window: A,
    reveal: async h => { await settings(h, 'Appearance'); await h.page.locator(S.selectOutline).first().click(); await wait(h.page); },
    parts: { listbox: page => page.locator('[role=listbox]').last(), option: nth('[role=listbox] [role=option]', 1), 'option-selected': '[role=listbox] [role=option][aria-selected=true]' } },
  { name: 'settings-plan', window: A, reveal: async h => settings(h, 'Plan & Usage'),
    parts: { progress: nth('[role=progressbar]', 0), 'field-group': nth(S.fieldGroup, 0) } },
  { name: 'settings-agents', window: A, reveal: async h => settings(h, 'Agents'), parts: { 'select-outline': S.selectOutline } },
  { name: 'settings-models', window: A, reveal: async h => settings(h, 'Models'),
    parts: { 'text-field': page => page.locator('.ui-field-group input, [data-component=glass-settings-tab] input').first(), 'switch-on': S.switchOn, 'switch-off': S.switchOff,
      'text-link': page => page.locator('a, button, span').filter({ hasText: /^View All Models$/ }).last() } },
  { name: 'settings-source-control', window: A, reveal: async h => settings(h, 'Source Control'),
    parts: { 'text-field': page => page.locator('.ui-field-group__entry input:not([inputmode=numeric])').first(), 'number-field': nth(dc('number-field'), 0) } },
  { name: 'settings-code-intelligence', window: A, reveal: async h => settings(h, 'Code Intelligence'), parts: {} },
  { name: 'settings-voice', window: A, reveal: async h => settings(h, 'Voice'), parts: {} },
  { name: 'settings-search', window: A, state: 'filled',
    reveal: async h => { await settings(h, 'General'); await h.page.locator(S.settingsSearchInput).first().click(); await h.page.keyboard.type('font'); await wait(h.page, 1000); },
    parts: { 'settings-search': S.settingsSearch },
    after: async ({ page }) => { await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); } },
  { name: 'sidebar-hidden', window: A,
    reveal: async ({ page }) => { await btn(page, 'Hide Sidebar').click(); await wait(page, 1000); },
    after: async ({ page }) => { await btn(page, 'Show Sidebar').click().catch(() => {}); await wait(page, 700); }, parts: {} },

  // ---- states, one part per shot: hover with the real pointer, focus-visible with real keyboard
  // focus, pressed with :active forced through CDP. Each is a full-window screenshot too.
  ...states([
    ['home', A, async () => {}, { 'icon-button': S.iconButton, pill: S.pill, 'select-text': S.selectText, 'model-button': S.modelButton,
      'sidebar-row': S.navRow, 'agent-row': S.agentRow, 'button-update': S.updateButton, 'voice-button': S.voice }, ['hover', 'focus-visible', 'pressed']],
    ['dialog', A, openProjectDialog, { 'button-primary': createButton, 'dialog-close': dialogClose, 'icon-picker': dc('popover-trigger') }, ['hover', 'focus-visible', 'pressed']],
    ['settings', A, async h => settings(h, 'General'), { 'switch-on': S.switchOn, 'switch-off': S.switchOff, 'button-secondary': openButton,
      'select-outline': S.selectOutline, 'settings-nav': S.settingsNav, 'button-accent': page => page.locator('button').filter({ hasText: /Invite/ }).first() }, ['hover', 'focus-visible', 'pressed']],
    ['settings', A, async h => settings(h, 'General'), { 'settings-search': S.settingsSearchInput }, ['hover', 'focus-visible']],
    ['automations', A, async ({ page }) => { await navRow(page, 'Automations').click(); await wait(page, 1600); },
      { 'table-row': nth('.ui-automations-list-table__row', 0), 'button-primary-inverse': newAutomation, tab: S.tab, 'template-card': nth('.ui-automations-template-card', 0) }, ['hover', 'focus-visible', 'pressed']],
    ['customize', A, async ({ page }) => { await navRow(page, 'Customize').click(); await wait(page, 1600); },
      { 'filter-pill': nth('.ui-customize-view button.ui-pill', 1), 'list-row': nth('[data-mcp-manage-server]', 0), 'text-button-accent': 'button[data-tone=accent][data-variant=text]' }, ['hover']],
    ['palette', A, async ({ page }) => { await btn(page, 'Search').click(); await wait(page, 900); }, { 'palette-row': nth(`${dc('palette-item')}[aria-selected=false]`, 0), tab: S.tab }, ['hover']],
    ['menu', A, async ({ page }) => { await S.agentRow(page).click({ button: 'right' }); await wait(page, 800); }, { 'menu-row': nth(dc('menu-row'), 1) }, ['hover']],
  ]),

  // ---- IDE window (the VS Code workbench) on the empty scratch folder
  { name: 'ide-shell', window: I, reveal: async () => {},
    parts: { titlebar: '.part.titlebar', 'side-bar': '.part.sidebar', 'status-bar': '.part.statusbar',
      'agent-pane': '.part.auxiliarybar', 'editor-empty': '.part.editor' } },
  { name: 'ide-quick-open', window: I, reveal: async ({ page }) => { await page.keyboard.press('Meta+P'); await wait(page, 1000); },
    parts: { 'quick-input': '.quick-input-widget', 'quick-input-box': '.quick-input-widget .monaco-inputbox' } },
  { name: 'ide-command-palette', window: I, reveal: async ({ page }) => { await page.keyboard.press('Meta+Shift+P'); await wait(page, 1000); },
    parts: { 'quick-input': '.quick-input-widget', 'quick-input-row-focused': '.quick-input-list .monaco-list-row.focused', 'quick-input-row': nth('.quick-input-list .monaco-list-row', 1),
      keybinding: nth('.quick-input-list .monaco-keybinding-key', 0) } },
];

// The finished test chat, opened again after run.mjs: the first chat under the scratch folder.
const CONVERSATION = {
  'user-message': '.ui-agent-transcript-human-bubble', 'assistant-message': '.agent-transcript-row-markdown',
  'step-group-header': '.ui-step-group-header', 'turn-actions': '.agent-transcript-turn-actions', 'code-block': '.ui-code-block',
  'file-card': dc('transcript-card-root'), 'file-card-row': dc('transcript-card-row'), 'conversation-tab': '.ui-tab-system-tab',
  'tool-call': '.ui-tool-call-line', 'inline-code': '.agent-transcript-row-markdown code', link: '.ui-markdown__link',
};
const openTestChat = async ({ page }) => {
  await page.locator('.ui-sidebar-section').filter({ hasText: SCRATCH }).locator('.ui-sidebar-section-content .ui-sidebar-menu-button-trigger').first().click(); await wait(page, 1500);
};
SHOTS.push(
  { name: 'ide-editor', window: I, reveal: async ({ page }) => { await page.keyboard.press('Meta+P'); await wait(page, 800); await page.keyboard.type('hello.txt'); await wait(page, 800); await page.keyboard.press('Enter'); await wait(page, 1200); },
    parts: { 'editor-tab': '.tabs-container .tab.active', 'explorer-row': '.explorer-folders-view .monaco-list-row', editor: '.monaco-editor .view-lines', 'line-numbers': '.monaco-editor .margin' } },
  { name: 'conversation', window: A, reveal: openTestChat, parts: { ...CONVERSATION, composer: '.ui-prompt-input__container', 'apps-rail': dc('collapsed-apps-rail-top-label-text') } },
  { name: 'conversation-top', window: A, reveal: async h => { await openTestChat(h); await h.page.mouse.move(760, 400); await h.page.mouse.wheel(0, -3000); await wait(h.page, 900); },
    parts: { 'user-message': '.ui-agent-transcript-human-bubble', 'step-group-header': '.ui-step-group-header' } },
  { name: 'conversation-turn-actions-hover', window: A, state: 'hover', reveal: openTestChat, hover: 'turn-actions', parts: { 'turn-actions': nth('.agent-transcript-turn-actions', 0) } },
  { name: 'conversation-code-block-hover', window: A, state: 'hover', reveal: openTestChat, hover: 'code-block', parts: { 'code-block': '.ui-code-block' } },
  { name: 'conversation-user-message-hover', window: A, state: 'hover', reveal: openTestChat, hover: 'user-message', parts: { 'user-message': nth('.ui-agent-transcript-human-bubble', 0) } },
);

// ---- an agent run, taken by run.mjs. The owner approved (2026-10-25) harmless test prompts in a
// fresh chat on the empty folder ~/.design-systems/harness-scratch, approving only actions inside it.
const SCRATCH = 'harness-scratch';
const ENV_BEFORE = 'Toolbox Fullstack Environment';   // the composer's environment before the run, restored after
async function pickEnvironment({ page }, label) {
  await page.locator(S.selectText).first().click(); await wait(page, 800);
  await page.locator(dc('search-menu-row')).filter({ hasText: new RegExp(`^${label}`) }).first().click(); await wait(page, 1000);
  await closeAll(page);
  const now = await page.locator(S.selectText).filter({ visible: true }).first().innerText();
  if (!now.startsWith(label)) throw new Error(`environment is ${now}, wanted ${label}`);
}
async function sendPrompt({ page }, text) {
  await page.locator(S.editor).filter({ visible: true }).last().click();
  await page.keyboard.type(text, { delay: 10 }); await wait(page, 300);
  await page.keyboard.press('Enter'); await wait(page, 800);
}
const panel = page => page.locator(dc('agent-panel'));
const approveButton = page => panel(page).locator('button').filter({ visible: true }).filter({ hasText: /^(Run|Allow|Accept|Approve)\b/ }).last();
const rejectButton = page => panel(page).locator('button').filter({ visible: true }).filter({ hasText: /^(Skip|Reject|Deny|Cancel)\b/ }).last();
export const RUN = {
  window: 'agents',
  async start(h) { await home(h); await pickEnvironment(h, SCRATCH); },
  async finish(h) { await home(h); await pickEnvironment(h, ENV_BEFORE); },
  async state({ page }) {
    if (await approveButton(page).count()) return 'approval';
    const stop = panel(page).locator('button[aria-label*="Stop" i], button[aria-label*="Cancel" i], [data-component*=stop]').filter({ visible: true });
    return (await stop.count()) ? 'running' : 'done';
  },
  async reject({ page }) { await rejectButton(page).click().catch(() => {}); await wait(page, 800); },
  steps: [
    { name: 'list-files', send: h => sendPrompt(h, 'List the files in this folder.') },
    { name: 'create-file', send: h => sendPrompt(h, 'Create hello.txt here containing one line: hello from the design capture') },
    { name: 'run-command', send: h => sendPrompt(h, 'Run ls -la in this folder in the terminal and show me the output.'),
      // Approve only a plain listing of the scratch folder.
      approve: async ({ page }) => {
        const block = await panel(page).innerText();
        const tail = block.slice(-600);
        if (!/\bls -la\b/.test(tail) || /\b(rm|mv|curl|sudo|git|npm|cd \/|>)\b/.test(tail.replace(/ls -la/g, ''))) return false;
        await approveButton(page).click(); await wait(page, 800); return true;
      } },
  ],
  // Parts measured on every frame, by data-component name; the last visible match is measured.
  parts: {
    composer: S.composer, 'send-button': '.ui-prompt-input-submit-button',
    ...CONVERSATION,
    'run-status': '[data-component="collapsible-header"][role=status], [role=status]',
  },
};
