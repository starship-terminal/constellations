// PRODUCT (adapt): everything in this file is Notion 7.40.0's (the Notion desktop app for macOS, Notion Labs;
// Electron 44.9.1, Chrome 152). Another Electron app replaces it whole and keeps cdp.mjs, vars.mjs,
// utilities.mjs, shots.mjs and run.mjs.
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
// Notion's window is two pages: the tab strip (its own WebContents, renderer/tabs/index.html) above the
// active tab's page (app.notion.com, one WebContents per tab; inactive and prewarmed tabs stay as pages).
// The active tab is the one the strip highlights. The page is React with StyleX atomic classes (x1abc...)
// and inline styles over Notion's theme custom properties (--c-*, --ca-*, --cl-*, --cd-*), plus notion-*
// class names on blocks and chrome. The capture works only in its own page, "Design capture (scratch)",
// in its own tab; it never edits, moves or opens for editing any of the owner's pages.

export const NAME = 'Notion';
export const SCRATCH = 'Design capture (scratch)';
export const DB = 'Sample tasks (scratch)';

// The tab the strip highlights (its close button's label names it; its fill is the strip's own).
async function activeTitle(context) {
  const tb = context.pages().find(x => x.url().includes('/tabs/index.html'));
  if (!tb) return null;
  return tb.evaluate(() => {
    const want = getComputedStyle(document.querySelector('#root > div')).backgroundColor;
    for (const b of document.querySelectorAll('[aria-label^="Close Tab, "]')) if (getComputedStyle(b.parentElement).backgroundColor === want) return b.getAttribute('aria-label').slice(11);
    return null;
  }).catch(() => null);
}
// A database page's document title adds the view (`Sample tasks (scratch) | Default view`); the strip shows the page's.
const isActive = async p => { if (!p.url().startsWith('https://app.notion.com/')) return false; const t = await activeTitle(p.context()); const own = await p.title(); return !!t && (own === t || own.startsWith(`${t} | `)); };
export const WINDOWS = { main: isActive, tabs: { url: /\/renderer\/tabs\/index\.html$/ } };
// The tab strip is stacked above every main-window screenshot, so each image is the whole window.
export const ABOVE = { main: 'tabs' };

// ---- helpers (selectors are Notion's own class names, roles, aria-labels and UI words, never account text)
const wait = (page, ms = 600) => page.waitForTimeout(ms);
const vis = (page, sel) => page.locator(sel).filter({ visible: true }).first();
const OPEN = '[role=dialog]:visible, [role=menu]:visible, [role=listbox]:visible, .notion-peek-renderer:visible';
export async function closeAll(page) {
  for (let i = 0; i < 5 && await page.locator(OPEN).first().isVisible().catch(() => false); i++) {
    await page.keyboard.press('Escape'); await wait(page, 350);
  }
}
const SIDEBAR = '.notion-sidebar';
const row = text => page => page.locator(`${SIDEBAR} [role=treeitem]`).filter({ hasText: new RegExp(`^${text.replace(/[()]/g, '\\$&')}$`) }).first();
const scratchRow = row(SCRATCH);
const PAGE = '.notion-frame';
const content = `${PAGE} .notion-page-content`;
async function blur(page) {
  // Leave the editor without selecting a block (Escape in the editor selects the block, and a click in the
  // margin puts the caret in the nearest one): drop focus and the selection through the DOM, then move the
  // pointer, which brings back the topbar Notion fades out while typing.
  await page.evaluate(() => { document.activeElement?.blur(); getSelection().removeAllRanges(); });
  for (const [x, y] of [[1300, 400], [1350, 450], [1440, 600]]) { await page.mouse.move(x, y); await wait(page, 120); }
  await wait(page, 500);
}
async function openScratch(page) {
  if (await page.title() !== SCRATCH) { await scratchRow(page).click(); await wait(page, 2500); }
  if (await page.title() !== SCRATCH) throw new Error('not on the scratch page');
}
async function openDb(page, view) {
  if (!(await page.title()).startsWith(DB)) await openScratch(page);
  // The database is a child page of the scratch page; open it from its block in the page (the sidebar's
  // row would need the scratch row expanded, which Notion remembers).
  if (!(await page.title()).startsWith(DB)) {
    await page.locator(`${content} .notion-collection_view_page-block a`).first().click(); await wait(page, 2500);
  }
  if (!(await page.title()).startsWith(DB)) throw new Error('not on the sample database');
  if (view) {
    const tab = page.locator(`${PAGE} [role=tab]`).filter({ hasText: new RegExp(`^${view}$`) }).first();
    if ((await tab.getAttribute('aria-selected')) !== 'true') { await tab.click(); await wait(page, 1500); }
  }
}
async function dockSidebar(page) {
  const sb = await page.locator(SIDEBAR).boundingBox().catch(() => null);
  if (!sb || sb.x < 0) throw new Error('sidebar is not docked');
}
// The tab strip's shots reset and guard the active tab's page, which sits under the strip.
async function mainPage(h, win) {
  if (win !== 'tabs') return h.page;
  for (const p of h.page.context().pages()) if (await isActive(p)) return p;
  throw new Error('no active tab');
}
export async function reset(h, win) {
  const page = await mainPage(h, win);
  await closeAll(page);
  await closeAi(page);
  await dockSidebar(page);
  await openScratch(page);
  await blur(page);
  await page.evaluate(() => {
    document.querySelector('.notion-frame .notion-scroller')?.scrollTo(0, 0);
    // A drag that starts in the text can scroll the frame's overflow-hidden parent sideways; put it back.
    for (let e = document.querySelector('.notion-frame'); e; e = e.parentElement) if (e.scrollLeft) e.scrollLeft = 0;
  });
  await wait(page, 300);
}
async function settings({ page }, pane) {
  await closeAll(page);
  if (!(await page.locator('[role=dialog] input[placeholder="Search settings"]').isVisible().catch(() => false))) {
    await page.locator('.notion-sidebar-switcher').click(); await wait(page, 900);
    await page.locator('[role=dialog]').getByText('Settings', { exact: true }).first().click(); await wait(page, 2000);
  }
  if (pane) {
    const nav = page.locator('[role=dialog] [role=tab], [role=dialog] [role=button]').filter({ hasText: new RegExp(`^${pane}(New|Beta)?$`) }).first();
    await nav.scrollIntoViewIfNeeded(); await nav.click(); await wait(page, 1800);
  }
  await page.mouse.move(1440, 900);
  // Some panes load their content after opening (Sidebar shows "Loading sidebar presets..."); wait it out.
  for (let i = 0; i < 10 && await page.getByText(/^Loading/).filter({ visible: true }).count(); i++) await wait(page, 700);
}
const SETTINGS_DIALOG = page => page.locator('[role=dialog]').filter({ has: page.locator('input[placeholder="Search settings"]') }).first();

// Notion styles :hover with JS (pointer events) and CSS; a real pointer is used for hover, and
// keyboard focus draws Notion's own ring. Nothing needs switching on.
export async function prepareState() {}

// A fingerprint of what a capture must never change: the theme, the tab strip's tabs, the sidebar's
// favourites, private pages and teamspace rows, and the scratch page's blocks.
export async function guard(h, win) {
  const page = await mainPage(h, win);
  await reset(h, win);
  const strip = await activeTitle(page.context());
  const tabs = await page.context().pages().find(x => x.url().includes('/tabs/index.html'))
    .evaluate(() => [...document.querySelectorAll('[aria-label^="Close Tab, "]')].map(e => e.getAttribute('aria-label').slice(11)).join('/'));
  return JSON.stringify({ strip, tabs, ...(await page.evaluate(() => ({
    theme: document.body.className,
    sidebar: [...document.querySelectorAll('.notion-sidebar [role=treeitem]')].map(e => e.textContent.trim()).join('/'),
    blocks: [...document.querySelectorAll('.notion-frame .notion-page-content [data-block-id]')].map(e => (e.className.match(/notion-([a-z_]+)-block/) || [])[1] + ':' + (e.matches('.notion-collection_view-block') ? '' : e.textContent.trim().slice(0, 40))).join('/'),
    checked: [...document.querySelectorAll('.notion-frame .notion-to_do-block input[type=checkbox]')].map(e => e.checked).join('/'),
  }))) });
}

// The theme is Notion's own setting (Settings > Preferences > Theme: Use system setting, Light or Dark).
// An emulated prefers-color-scheme repaints one tab, but Notion's renderer reports it to the app, which
// stores it and repaints every tab, so the setting is used instead. Returns the label it replaced.
export async function setTheme(h, label) {
  const { page } = h;
  await settings(h, 'Preferences');
  const sel = await page.evaluate(() => {
    const lab = [...document.querySelectorAll('[role=dialog] div')].find(e => e.textContent.trim() === 'Theme' && !e.children.length);
    for (let r = lab, i = 0; r && i < 6; i++) { r = r.parentElement; const b = r.querySelector('[role=button]'); if (b) { b.setAttribute('data-cap', 'theme-select'); return b.textContent.trim(); } }
    return null;
  });
  if (!sel) throw new Error('no Theme select');
  if (sel !== label) {
    await page.locator('[data-cap=theme-select]').click(); await wait(page, 800);
    await page.locator('[role=menuitem], [role=option]').filter({ hasText: new RegExp(`^${label}$`) }).first().click(); await wait(page, 2500);
  }
  await page.evaluate(() => document.querySelector('[data-cap=theme-select]')?.removeAttribute('data-cap'));
  await closeAll(page);
  return sel;
}

// ---- the shot list
const M = 'main', T = 'tabs';
const nth = (sel, i) => [sel, i];
const lastPopup = page => page.locator('[role=dialog]').filter({ visible: true }).last();
const OPTION = '[role=option], [role=menuitem]';
const menuParts = { menu: lastPopup, 'menu-row': page => lastPopup(page).locator(OPTION).filter({ visible: true }).nth(1) };
const block = kind => `${content} .notion-${kind}-block`;
const S = {
  sidebar: SIDEBAR,
  search: `${SIDEBAR} [role=button][aria-label="Search or ask"]`,
  navTabSelected: `${SIDEBAR} [role=tab][aria-selected=true]`,
  navTab: `${SIDEBAR} [role=tab][aria-selected=false]`,
  sectionTitle: page => page.locator(`${SIDEBAR} [role=button]`).filter({ hasText: /^Private$/ }).first(),
  pageRow: row('local-models-inventory'),
  pageRowSelected: scratchRow,
  addNew: page => page.locator(`${SIDEBAR} [role=button]`).filter({ hasText: /^Add new$/ }).first(),
  switcher: '.notion-sidebar-switcher',
  sidebarIcon: `${SIDEBAR} [role=button][aria-label="Library, Trash, more…"]`,
  topbar: '.notion-topbar',
  breadcrumb: '.notion-topbar-breadcrumb-region',
  share: '.notion-topbar-share-menu',
  copyLink: '.notion-topbar [role=button][aria-label="Copy link"]',
  favorite: '.notion-topbar-favorite-button',
  more: '.notion-topbar-more-button',
  title: `${PAGE} h1[contenteditable]`,
  h1: block('header'), h2: block('sub_header'), h3: block('sub_sub_header'),
  text: block('text'), bullet: block('bulleted_list'), numbered: block('numbered_list'),
  todo: block('to_do'), toggle: block('toggle'), quote: block('quote'), callout: block('callout'),
  code: block('code'), divider: block('divider'),
  inlineCode: `${content} .notion-inline-code-container, ${content} code`,
  link: `${content} a.notion-link-token, ${content} .notion-link-token`,
  checkbox: `${content} .notion-to_do-block input[type=checkbox]`,
  aiButton: '.notion-ai-button',
};
// A block's text leaf (the block wrapper keeps the inherited 16px; the leaf carries the block's own type).
const leaf = sel => `${sel} [contenteditable=true]`;
// The selected sidebar row paints its fill on an inner element.
const filled = loc => loc.locator('xpath=.//*[not(self::svg) and not(ancestor::svg)]').filter({ visible: true }).first();
// The page's last top-level text block (blocks sit in a wrapper, so `>` cannot reach them; nested ones such as
// a callout's text are skipped). Notion's editor reverts DOM changes inside the page, so nothing is tagged:
// the block is found by its index among the page's text blocks.
const TEXT = '.notion-page-content .notion-text-block';
const lastTop = async page => {
  const i = await page.evaluate(sel => {
    const all = [...document.querySelectorAll(sel)];
    let k = -1; all.forEach((e, j) => { if (!e.parentElement.closest('.notion-page-content [data-block-id]')) k = j; });
    return k;
  }, TEXT);
  if (i < 0) throw new Error('no top-level text block');
  return page.locator(TEXT).nth(i);
};
// The block being typed in: the text block holding the caret (focus sits on Notion's editor root, not the block),
// remembered by its block id, which Notion keeps stable, so cleanup can only ever touch the block the shot made.
let typedId = null;
const TYPED = () => `.notion-page-content [data-block-id="${typedId}"]`;
const caretBlockId = page => page.evaluate(sel => { const n = getSelection().anchorNode; const b = n && (n.nodeType === 1 ? n : n.parentElement).closest(sel); return b ? b.getAttribute('data-block-id') : null; }, TEXT);
const topCount = page => page.evaluate(sel => [...document.querySelectorAll(sel)].filter(e => !e.parentElement.closest('.notion-page-content [data-block-id]')).length, TEXT);
const typedBlock = async ({ page }, text) => {
  // A new empty block at the end of the scratch page: click the last paragraph's end, Enter.
  const last = (await lastTop(page)).locator('[contenteditable=true]').first();
  const lastId = await (await lastTop(page)).getAttribute('data-block-id');
  await last.click(); await wait(page, 200);
  // The caret goes to the end through the DOM (Notion ignores a synthetic End key).
  await last.evaluate(e => { const r = document.createRange(); r.selectNodeContents(e); r.collapse(false); const s = getSelection(); s.removeAllRanges(); s.addRange(r); });
  await wait(page, 200);
  await page.keyboard.press('Enter'); await wait(page, 500);
  typedId = await caretBlockId(page);
  if (!typedId || typedId === lastId) { typedId = null; throw new Error('the caret is not in a new text block'); }
  if (text) { await page.keyboard.type(text, { delay: 25 }); await wait(page, 1100); }
};
// Undo the typed block: Escape any menu, then remove the one block this shot created (by its id), and only
// while it holds nothing or what the capture typed into it.
async function removeTyped({ page }) {
  await closeAll(page);
  if (!typedId) return blur(page);
  const blockLoc = page.locator(TYPED());
  if (await blockLoc.count()) {
    const text = (await blockLoc.textContent()).trim();
    if (!/^(|\/.*|Text typed by the capture.*)$/.test(text)) throw new Error(`the capture's block holds text it did not type: ${text.slice(0, 40)}`);
    const ed = blockLoc.locator('[contenteditable=true]').first();
    // Caret at the text's end by clicking its right edge, then Backspace once per character and once more
    // to remove the block. Never Cmd+A: in an empty block Notion selects every block on the page.
    const b = await ed.boundingBox();
    await page.mouse.click(b.x + b.width - 2, b.y + b.height / 2); await wait(page, 300);
    for (let j = 0; j <= text.length; j++) { await page.keyboard.press('Backspace'); await wait(page, 40); }
    await wait(page, 600); await closeAll(page);
    if (await page.locator(TYPED()).count()) throw new Error('the capture\'s block could not be removed');
  }
  typedId = null;
  await blur(page);
}
const hoverBlock = sel => async ({ page }) => { await page.locator(sel).first().hover(); await wait(page, 700); };
const dragHandle = page => page.locator('.notion-selectable-hover-menu-item, [role=button][aria-label="Drag"], div[aria-label*="Drag"]').filter({ visible: true }).first();

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

const SETTINGS_PANES = ['Preferences', 'Notifications', 'Mail & Calendar', 'General', 'Sidebar', 'Import', 'Notion AI', 'Meeting notes',
  'Connections', 'Notion MCP', 'Public pages', 'Emoji', 'Offline', 'Developer', 'Teamspaces', 'Security', 'Identity'];
const slug = s => s.toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/-$/, '');

export const SHOTS = [
  // ---- the app shell on the scratch page
  { name: 'page-default', window: M, reveal: async () => {},
    parts: { sidebar: S.sidebar, 'sidebar-surface': '.notion-sidebar-container', 'sidebar-search': S.search, 'nav-tab-selected': S.navTabSelected, 'nav-tab': S.navTab,
      'section-title': S.sectionTitle, 'section-label': page => page.locator(SIDEBAR).getByText('Private', { exact: true }).first(),
      'page-row': S.pageRow, 'page-row-selected': S.pageRowSelected, 'page-row-selected-fill': page => filled(S.pageRowSelected(page)), 'add-row': S.addNew,
      switcher: S.switcher, 'sidebar-icon-button': S.sidebarIcon, topbar: S.topbar, breadcrumb: S.breadcrumb, 'button-share': S.share,
      'topbar-icon-button': S.copyLink, 'page-title': S.title, 'heading-1': leaf(S.h1), 'heading-2': leaf(S.h2), paragraph: leaf(S.text),
      'bulleted-list': leaf(S.bullet), 'numbered-list': leaf(S.numbered), 'to-do': leaf(S.todo), checkbox: S.checkbox,
      'checkbox-box': `${S.todo} > * > * > * > * > div`, toggle: leaf(S.toggle),
      quote: leaf(S.quote), 'quote-bar': `${S.quote} > * > div`, callout: S.callout, 'callout-fill': `${S.callout} > div > div`,
      'inline-code': page => page.locator(`${content} span.notion-enable-hover`).filter({ hasText: /^code$/ }).first(),
      link: S.link, 'ai-button': S.aiButton },
    optionalParts: ['link', 'inline-code', 'page-row-selected-fill', 'checkbox-box'] },
  { name: 'page-scrolled', window: M,
    reveal: async ({ page }) => { await page.mouse.move(900, 600); await page.mouse.wheel(0, 700); await wait(page, 1200); },
    parts: { 'heading-3': leaf(S.h3), code: `${S.code} [contenteditable=true]`, 'code-fill': `${S.code} > div > div > div`, divider: S.divider,
      'database-inline': `${content} .notion-collection_view-block`,
      'table-header-cell': `${content} .notion-table-view-header-cell`, 'table-cell': [`${content} .notion-table-view-cell`, 0], 'table-row': `${content} .notion-table-view-row` },
    optionalParts: ['heading-3'] },
  { name: 'tabbar-default', window: T, reveal: async () => {},
    parts: { tabbar: '#root > div', 'tab-selected': page => page.locator(`[aria-label="Close Tab, ${SCRATCH}"]`).locator('xpath=../../..'),
      tab: page => page.locator('[aria-label^="Close Tab, "]').first().locator('xpath=../../..'), 'tab-pinned': nth('[draggable=true] > div', 0),
      'tab-close': page => page.locator('[aria-label^="Close Tab, Design capture"]').first(), 'tabbar-icon-button': '[aria-label="Inbox"]', 'new-tab': '[aria-label="New Tab"]' },
    optionalParts: ['tab-pinned'] },
  { name: 'sidebar-collapsed', window: M,
    reveal: async ({ page }) => { await page.keyboard.press('Meta+Backslash'); await wait(page, 1200); await page.mouse.move(900, 500); await wait(page, 600); },
    parts: { 'page-title': S.title },
    after: async ({ page }) => { if ((await page.locator(SIDEBAR).boundingBox()).x < 0) { await page.keyboard.press('Meta+Backslash'); await wait(page, 1200); } } },
  { name: 'page-row-menu', window: M,
    reveal: async ({ page }) => { await S.pageRowSelected(page).hover(); await wait(page, 400); await S.pageRowSelected(page).locator('[role=button][aria-label^="Delete, duplicate"]').click({ force: true }); await wait(page, 1000); },
    parts: { ...menuParts, 'menu-search': page => lastPopup(page).locator('input').first() }, optionalParts: ['menu-search'] },
  { name: 'switcher-menu', window: M, reveal: async ({ page }) => { await page.locator(S.switcher).click(); await wait(page, 1000); },
    parts: { menu: lastPopup, 'menu-row-checked': page => lastPopup(page).locator(OPTION).first() } },
  { name: 'page-actions-menu', window: M, reveal: async ({ page }) => { await page.locator(S.more).click(); await wait(page, 1000); },
    parts: { ...menuParts, 'menu-search': page => lastPopup(page).locator('input').first(), 'menu-row-danger': page => lastPopup(page).locator(OPTION).filter({ hasText: /^Move to Trash/ }).first(),
      'menu-switch': page => lastPopup(page).locator('[role=switch], input[type=checkbox]').first() },
    optionalParts: ['menu-search', 'menu-switch'] },
  { name: 'share-menu', window: M, reveal: async ({ page }) => { await page.locator(S.share).click(); await wait(page, 1500); },
    parts: { popover: lastPopup, 'button-primary': page => lastPopup(page).locator('[role=button]').filter({ hasText: /^(Invite|Copy link|Publish)$/ }).first(),
      'text-field': page => lastPopup(page).locator('input').first() },
    optionalParts: ['button-primary', 'text-field'] },
  { name: 'search-palette', window: M, reveal: async ({ page }) => { await page.locator(S.search).click(); await wait(page, 1500); },
    parts: { palette: lastPopup, 'palette-input': page => lastPopup(page).locator('input').first(),
      'palette-row-selected': page => lastPopup(page).locator('[role=option]').first(), 'palette-row': page => lastPopup(page).locator('[role=option]').nth(2),
      'palette-filter': page => lastPopup(page).locator('[role=button]').filter({ hasText: /^Title only$/ }).first() },
    optionalParts: ['palette-filter'] },
  { name: 'search-palette-empty', window: M, state: 'empty',
    reveal: async ({ page }) => { await page.locator(S.search).click(); await wait(page, 1200); await page.keyboard.type('zzqxvj', { delay: 30 }); await wait(page, 2000); },
    parts: { palette: lastPopup } },
  { name: 'tooltip', window: M, state: 'hover', reveal: async ({ page }) => { await page.locator(S.copyLink).hover(); await wait(page, 1500); },
    // Notion's tooltip is a small [role=dialog] in the overlay layer.
    parts: { tooltip: lastPopup, 'topbar-icon-button': S.copyLink } },
  // Copy link writes the scratch page's link to the clipboard and raises Notion's toast.
  { name: 'toast', window: M, reveal: async ({ page }) => { await page.locator(S.copyLink).click(); await wait(page, 700); await page.mouse.move(1440, 600); },
    parts: { toast: page => page.locator('[role=status], [role=alert]').filter({ hasText: /./ }).filter({ visible: true }).first() } },
  // ---- editing states in the scratch page: a new block at its end, removed afterwards
  { name: 'block-empty', window: M, state: 'focused', reveal: async h => typedBlock(h, ''),
    parts: { 'paragraph-empty': page => page.locator(TYPED()) }, after: removeTyped },
  { name: 'slash-menu', window: M, reveal: async h => typedBlock(h, '/'),
    parts: { menu: lastPopup, 'menu-row-selected': page => lastPopup(page).locator('[role=option]').first(), 'menu-row': page => lastPopup(page).locator('[role=option]').nth(2),
      'menu-heading': page => lastPopup(page).getByText(/^(Basic blocks|Suggested)$/).first() },
    optionalParts: ['menu-heading'], after: removeTyped },
  { name: 'slash-menu-filtered', window: M, state: 'filled', reveal: async h => typedBlock(h, '/tab'),
    parts: { menu: lastPopup }, after: removeTyped },
  { name: 'block-typed', window: M, state: 'filled', reveal: async h => typedBlock(h, 'Text typed by the capture, then removed'),
    parts: { paragraph: page => page.locator(TYPED()) }, after: removeTyped },
  { name: 'block-hover', window: M, state: 'hover', reveal: hoverBlock(S.text),
    parts: { 'drag-handle': dragHandle, paragraph: S.text }, optionalParts: ['drag-handle'] },
  { name: 'block-menu', window: M,
    reveal: async ({ page }) => { await hoverBlock(S.text)({ page }); await dragHandle(page).click(); await wait(page, 1200); },
    parts: { ...menuParts, 'block-selected': `${content} .notion-text-block` } },
  { name: 'block-colour-menu', window: M, optional: true,
    reveal: async ({ page }) => { await hoverBlock(S.text)({ page }); await dragHandle(page).click(); await wait(page, 1000);
      await lastPopup(page).locator(OPTION).filter({ hasText: /^Color/ }).first().hover(); await wait(page, 1200); },
    parts: { menu: lastPopup } },
  // A double-click on one word (found through a text Range, so no drag can reach the sidebar's resize edge).
  { name: 'text-selection-toolbar', window: M, state: 'selected',
    reveal: async ({ page }) => {
      const r = await page.evaluate(() => { const blk = document.querySelector('.notion-frame .notion-page-content .notion-text-block'); const w = document.createTreeWalker(blk, NodeFilter.SHOW_TEXT);
        for (let n; (n = w.nextNode());) { const i = n.data.indexOf('sample'); if (i >= 0) { const g = document.createRange(); g.setStart(n, i); g.setEnd(n, i + 6); const b = g.getBoundingClientRect(); return [b.x, b.y, b.width, b.height]; } } return null; });
      if (!r) throw new Error('no word to select');
      await page.mouse.dblclick(r[0] + r[2] / 2, r[1] + r[3] / 2); await wait(page, 1500); },
    parts: { toolbar: '.notion-text-action-menu > div > div', 'toolbar-button': page => page.locator('.notion-text-action-menu [role=button]').nth(2) },
    after: async ({ page }) => blur(page) },
  { name: 'block-selected', window: M, state: 'selected',
    reveal: async ({ page }) => { await page.locator(S.numbered).first().locator('[contenteditable=true]').first().click(); await wait(page, 300); await page.keyboard.press('Escape'); await wait(page, 700); await page.mouse.move(1440, 600); },
    parts: { 'block-selected': S.numbered, 'selection-fill': page => page.locator(`${S.numbered} .notion-selectable-halo, ${S.numbered} > div`).filter({ visible: true }).first() },
    optionalParts: ['selection-fill'] },
  { name: 'toggle-open', window: M, state: 'expanded',
    reveal: async ({ page }) => { await page.locator(`${S.toggle} [role=button]`).first().click(); await wait(page, 800); await page.mouse.move(1440, 600); },
    parts: { toggle: S.toggle, 'toggle-button': `${S.toggle} [role=button]` },
    after: async ({ page }) => { await page.locator(`${S.toggle} [role=button][aria-expanded=true]`).first().click().catch(() => {}); await wait(page, 600); } },
  { name: 'page-controls', window: M, state: 'hover',
    reveal: async ({ page }) => { await page.locator(S.title).hover(); await wait(page, 800); },
    parts: { 'page-control': page => page.locator('.notion-page-controls [role=button]').filter({ visible: true }).first() } },
  // ---- the sample database (a child page of the scratch page): table and board views
  { name: 'database-table', window: M, reveal: async ({ page }) => openDb(page, 'Default view'),
    parts: { 'view-tab-selected': `${PAGE} [role=tab][aria-selected=true]`, 'view-tab': `${PAGE} [role=tab][aria-selected=false]`,
      'table-header-cell': `${PAGE} .notion-table-view-header-cell`, 'table-cell': [`${PAGE} .notion-table-view-cell`, 0], 'table-row': `${PAGE} .notion-table-view-row`,
      'select-pill': page => page.locator(`${PAGE} .notion-table-view-cell`).getByText(/^High$/).first().locator('xpath=../..'), 'select-pill-green': page => page.locator(`${PAGE} .notion-table-view-cell`).getByText(/^Done$/).first().locator('xpath=../..'),
      'checkbox-checked': page => page.locator(`${PAGE} .notion-table-view-cell input[type=checkbox]:checked`).first().locator('xpath=..'), 'button-new': page => page.locator(`${PAGE} [role=button]`).filter({ hasText: /^New$/ }).first(),
      'toolbar-icon-button': `${PAGE} [role=button][aria-label=Filter]`, 'add-row': `${PAGE} .notion-table-view-add-row` },
    optionalParts: ['checkbox-checked'] },
  { name: 'database-board', window: M, reveal: async ({ page }) => openDb(page, 'Board'),
    parts: { 'board-card': `${PAGE} .notion-collection-item`, 'board-column-header': page => page.locator(`${PAGE} [data-board-group-id], ${PAGE} .notion-board-group`).first() },
    optionalParts: ['board-column-header'] },
  { name: 'database-row-hover', window: M, state: 'hover',
    reveal: async ({ page }) => { await openDb(page, 'Default view'); await page.locator(`${PAGE} .notion-table-view-row`).nth(1).hover(); await wait(page, 800); },
    parts: { 'table-row': [`${PAGE} .notion-table-view-row`, 1] } },
  { name: 'database-select-menu', window: M,
    reveal: async ({ page }) => { await openDb(page, 'Default view'); await page.locator(`${PAGE} .notion-table-view-cell`).getByText(/^High$/).first().click(); await wait(page, 1200); },
    parts: { popover: lastPopup, 'select-option': page => lastPopup(page).locator(OPTION).first() } },
  { name: 'database-date-picker', window: M,
    reveal: async ({ page }) => { await openDb(page, 'Default view'); await page.locator(`${PAGE} .notion-table-view-cell`).getByText(/^October 25, 2026$/).first().click(); await wait(page, 1200); },
    parts: { popover: lastPopup } },
  { name: 'database-property-menu', window: M,
    reveal: async ({ page }) => { await openDb(page, 'Default view'); await page.locator(`${PAGE} .notion-table-view-header-cell`).filter({ hasText: /^Priority$/ }).first().click(); await wait(page, 1200); },
    parts: { ...menuParts, 'menu-row-danger': page => lastPopup(page).locator(OPTION).filter({ hasText: /^Delete property/ }).first() }, optionalParts: ['menu-row-danger'] },
  // Delete property on the sample database's Priority column: the confirmation is opened and cancelled.
  { name: 'delete-property-dialog', window: M,
    reveal: async ({ page }) => { await openDb(page, 'Default view'); await page.locator(`${PAGE} .notion-table-view-header-cell`).filter({ hasText: /^Priority$/ }).first().click(); await wait(page, 1000);
      await lastPopup(page).locator(OPTION).filter({ hasText: /^Delete property/ }).first().click(); await wait(page, 1200); },
    parts: { dialog: lastPopup, 'button-danger': page => lastPopup(page).locator('[role=button]').filter({ hasText: /^Delete/ }).last(),
      'button-secondary': page => lastPopup(page).locator('[role=button]').filter({ hasText: /^Cancel$/ }).last() },
    after: async ({ page }) => { await lastPopup(page).locator('[role=button]').filter({ hasText: /^Cancel$/ }).last().click().catch(() => {}); await wait(page, 600); await closeAll(page); } },
  { name: 'database-peek', window: M,
    reveal: async ({ page }) => { await openDb(page, 'Default view'); const c = page.locator(`${PAGE} .notion-table-view-cell`).getByText(/^Measure the table view$/).first(); await c.hover(); await wait(page, 500);
      await page.locator(`${PAGE} [role=button]`).filter({ hasText: /^Open$/ }).filter({ visible: true }).first().click(); await wait(page, 2000); },
    parts: { peek: '.notion-peek-renderer', 'property-row': page => page.locator('.notion-peek-renderer [role=row], .notion-peek-renderer .notion-page-block').first() }, optionalParts: ['property-row'] },
  // ---- Home, Inbox
  // The sidebar's Chat tab lists Notion AI chats; the Home tab is selected again afterwards (a click on the
  // selected Home tab opens its tab menu instead, so it is only clicked when Chat is selected).
  { name: 'sidebar-chat', window: M, reveal: async ({ page }) => { await page.locator(`${SIDEBAR} [role=tab][aria-label=Chat]`).click(); await wait(page, 2000); await page.mouse.move(1440, 900); },
    parts: { 'nav-tab-selected': S.navTabSelected, 'chat-row': page => page.locator(`${SIDEBAR} [role=treeitem], ${SIDEBAR} a`).filter({ visible: true }).first() }, optionalParts: ['chat-row'],
    after: async ({ page }) => { if ((await page.locator(`${SIDEBAR} [role=tab][aria-label=Home]`).getAttribute('aria-selected')) !== 'true') { await page.locator(`${SIDEBAR} [role=tab][aria-label=Home]`).click(); await wait(page, 1200); } } },
  // ---- Settings
  ...SETTINGS_PANES.map(p => ({ name: `settings-${slug(p)}`, window: M, reveal: async h => settings(h, p), parts: {}, optional: true })),
  { name: 'settings-preferences-parts', window: M, reveal: async h => settings(h, 'Preferences'),
    parts: { 'settings-dialog': SETTINGS_DIALOG, 'settings-search': page => SETTINGS_DIALOG(page).locator('input[placeholder="Search settings"]'),
      'settings-nav-selected': page => SETTINGS_DIALOG(page).locator('[role=tab][aria-selected=true], [role=button][aria-selected=true]').first(),
      'settings-nav': page => SETTINGS_DIALOG(page).locator('[role=tab], [role=button]').filter({ hasText: /^Notifications$/ }).first(),
      'settings-page-title': page => SETTINGS_DIALOG(page).getByText(/^Preferences$/).last(), 'section-title': page => SETTINGS_DIALOG(page).getByText(/^Appearance$/).first(),
      select: page => SETTINGS_DIALOG(page).locator('[role=button][aria-haspopup]').filter({ hasText: /^(Dark|Light|Use system setting)$/ }).first(),
      'switch-on': page => SETTINGS_DIALOG(page).locator('[role=switch][aria-checked=true], input[role=switch]:checked').first(),
      'switch-off': page => SETTINGS_DIALOG(page).locator('[role=switch][aria-checked=false], input[role=switch]:not(:checked)').first(),
      'dialog-close': page => SETTINGS_DIALOG(page).locator('[role=button][aria-label=Close]').first() },
    optionalParts: ['settings-nav-selected', 'switch-on', 'switch-off', 'dialog-close'] },
  { name: 'settings-select-menu', window: M, reveal: async h => { await settings(h, 'Preferences'); await SETTINGS_DIALOG(h.page).locator('[role=button][aria-haspopup]').filter({ hasText: /^(English \(US\))$/ }).first().click(); await wait(h.page, 1000); },
    parts: { menu: lastPopup, 'menu-row-checked': page => lastPopup(page).locator('[role=option][aria-selected=true], [role=menuitemradio][aria-checked=true], [role=option]').first() }, optionalParts: ['menu-row-checked'] },
  { name: 'settings-search', window: M, state: 'filled',
    reveal: async h => { await settings(h, 'Preferences'); await SETTINGS_DIALOG(h.page).locator('input[placeholder="Search settings"]').click(); await h.page.keyboard.type('theme', { delay: 30 }); await wait(h.page, 1500); },
    parts: { 'settings-search': page => SETTINGS_DIALOG(page).locator('input[placeholder="Search settings"]') } },

  // ---- states, one part per shot: hover with the real pointer, focus-visible with real keyboard focus,
  // pressed with :hover and :active forced through CDP over the part.
  ...states([
    ['page', M, async () => {}, { 'page-row': S.pageRow, 'add-row': S.addNew, 'sidebar-search': S.search, 'nav-tab': S.navTab, 'button-share': S.share,
      'topbar-icon-button': S.copyLink, switcher: S.switcher }, ['hover', 'focus-visible', 'pressed']],
    ['page', M, async () => {}, { 'page-row-selected': S.pageRowSelected, 'section-title': S.sectionTitle, 'ai-button': S.aiButton }, ['hover']],
    ['page', M, async () => {}, { checkbox: S.checkbox }, ['focus-visible']],
    ['menu', M, async ({ page }) => { await page.locator(S.more).click(); await wait(page, 1000); },
      { 'menu-row': page => lastPopup(page).locator(OPTION).filter({ visible: true }).nth(3) }, ['hover']],
    ['settings', M, async h => settings(h, 'Preferences'), { 'settings-nav': page => SETTINGS_DIALOG(page).locator('[role=tab], [role=button]').filter({ hasText: /^Notifications$/ }).first(),
      select: page => SETTINGS_DIALOG(page).locator('[role=button][aria-haspopup]').filter({ hasText: /^(Dark|Light|Use system setting)$/ }).first() }, ['hover', 'focus-visible']],
    ['database', M, async ({ page }) => openDb(page, 'Default view'), { 'button-new': page => page.locator(`${PAGE} [role=button]`).filter({ hasText: /^New$/ }).first(),
      'table-row': [`${PAGE} .notion-table-view-row`, 1] }, ['hover', 'pressed']],
    ['tabbar', T, async () => {}, { tab: page => page.locator('[aria-label^="Close Tab, "]').first().locator('xpath=../../..'), 'tabbar-icon-button': '[aria-label="Inbox"]' }, ['hover']],
  ]),
];

// ---- Notion AI, taken by run.mjs. The owner approved (2026-10-25) harmless test prompts inside the
// capture's own scratch page or a fresh AI chat only, never acting on other pages.
const AI = '.chat_sidebar';
const aiPanel = page => page.locator(AI).filter({ visible: true }).first();
const aiInput = page => page.locator(`${AI} [role=textbox]`).filter({ visible: true }).first();
async function openAi(page) {
  if (!(await aiPanel(page).isVisible().catch(() => false))) { await page.locator(S.aiButton).click(); await wait(page, 2500); }
  if (!(await aiInput(page).isVisible().catch(() => false))) throw new Error('the AI panel did not open with an input');
}
// Empty the AI input: caret to its end through the DOM, then one Backspace per character.
// Only text the capture typed is cleared: a draft of the owner's stops the capture instead.
const AI_TYPED = [/^Typed by the capture, never sent$/, /^Summarise this page in two sentences\.$/];
async function clearAi(page) {
  const inp = aiInput(page);
  if (!(await inp.isVisible().catch(() => false))) return;
  const text = (await inp.innerText()).trim();
  const n = text.length;
  if (!n) return;
  if (!AI_TYPED.some(re => re.test(text))) throw new Error(`the AI input holds a draft the capture did not type: ${text.slice(0, 40)}`);
  await inp.click();
  await inp.evaluate(e => { const r = document.createRange(); r.selectNodeContents(e); r.collapse(false); const s = getSelection(); s.removeAllRanges(); s.addRange(r); });
  for (let i = 0; i <= n; i++) await page.keyboard.press('Backspace');
  await wait(page, 400);
  if ((await inp.innerText()).length) throw new Error('the AI input could not be emptied');
}
async function closeAi(page) {
  await clearAi(page);
  const hide = page.locator(`${AI} [role=button][aria-label="Hide chat"]`);
  if (await hide.isVisible().catch(() => false)) { await hide.click(); await wait(page, 1200); }
}
export const RUN = {
  window: 'main',
  async start(h) {
    await reset(h);
    await openAi(h.page);
  },
  async finish(h) {
    const { page } = h;
    const stop = page.locator('[role=button][aria-label*="Stop" i]:visible');
    for (let i = 0; i < 40 && await stop.count(); i++) await wait(page, 1000);
    if (await stop.count()) { await stop.first().click().catch(() => {}); await wait(page, 1500); }
    await closeAll(page);
    await closeAi(page);
  },
  async state({ page }) {
    if (await page.locator(AI).getByText(/run out of free AI responses/).count()) return 'done';
    const stop = page.locator('[role=button][aria-label*="Stop" i]:visible');
    return (await stop.count()) ? 'running' : 'done';
  },
  // state() never reads an approval today, so this is not reached; if one ever appears it is refused, inside the
  // AI panel only.
  async reject({ page }) { await page.locator(`${AI} button, ${AI} [role=button]`).filter({ visible: true }).filter({ hasText: /^(Deny|Reject|Skip)\b/ }).last().click().catch(() => {}); await wait(page, 800); },
  // On 2026-10-25 the account had run out of free AI responses: the panel says so and Submit stays disabled,
  // so the prompt below was typed but not sent (finish() empties the input), and no response was captured.
  steps: [
    { name: 'summarise', send: async ({ page }) => { await aiInput(page).click(); await page.keyboard.type('Summarise this page in two sentences.', { delay: 20 }); await wait(page, 500);
      // The owner's Use Enter to add a new line is on, so Cmd+Enter sends.
      await page.keyboard.press('Meta+Enter'); await wait(page, 1500); } },
  ],
  parts: { 'ai-panel': aiPanel, 'ai-input': aiInput, 'ai-submit': `${AI} [role=button][aria-label="Submit AI message"]`,
    'user-message': page => page.locator(`${AI} [data-message-role=user], ${AI} [class*=user-message]`).first() },
};

// The Notion AI side panel on the scratch page, opened and closed (nothing sent here; run.mjs sends).
SHOTS.push(
  { name: 'ai-panel', window: M, reveal: async ({ page }) => { await openAi(page); await page.mouse.move(700, 500); await wait(page, 600); },
    parts: { 'ai-panel': aiPanel, 'ai-input': page => aiInput(page).locator('xpath=../..'), 'ai-submit': `${AI} [role=button][aria-label="Submit AI message"]`,
      'ai-chip': `${AI} [role=button][aria-label="Choose AI model"]`, 'ai-header-button': `${AI} [role=button][aria-label="Start new chat"]`,
      'ai-banner': page => page.locator(AI).getByText(/run out of free AI/).first().locator('xpath=../..') },
    optionalParts: ['ai-banner'], after: async ({ page }) => closeAi(page) },
  { name: 'ai-panel-typed', window: M, state: 'filled',
    reveal: async ({ page }) => { await openAi(page); await aiInput(page).click(); await page.keyboard.type('Typed by the capture, never sent', { delay: 20 }); await wait(page, 800); },
    parts: { 'ai-input': page => aiInput(page).locator('xpath=../..'), 'ai-submit': `${AI} [role=button][aria-label="Submit AI message"]` },
    after: async ({ page }) => closeAi(page) },
  { name: 'ai-model-menu', window: M, reveal: async ({ page }) => { await openAi(page); await page.locator(`${AI} [role=button][aria-label="Choose AI model"]`).click(); await wait(page, 1200); },
    parts: menuParts, after: async ({ page }) => { await closeAll(page); await closeAi(page); } },
);
