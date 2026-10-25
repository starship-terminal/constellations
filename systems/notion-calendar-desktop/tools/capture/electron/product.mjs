// PRODUCT (adapt): everything in this file is Notion Calendar 1.142.0's (the Notion Calendar desktop app for macOS,
// formerly Cron; bundle id com.cron.electron, Electron 44.9.1). Its one window loads the web app from
// https://calendar.notion.so/, so the page is the same React app as the web version, inside a desktop frame.
// Another Electron app replaces this file whole and keeps cdp.mjs, vars.mjs, utilities.mjs, shots.mjs and run.mjs.
//
// A shot is { name, window, state?, reveal(h), parts, force?, hover?, focus?, after?(h), optional?, optionalParts? }:
//   name    screenshot file name, `{page}-{state}` (the theme folder is added by shots.mjs)
//   window  a key of WINDOWS
//   reveal  async ({ page, cdp, ...helpers }) => {} : clicks, keys and hovers that show the state.
//           Look, don't act: open and close, never save, send, RSVP, move or delete.
//   parts   { component: selector | [selector, nth] | (page) => Locator }: each is measured
//           (computed style) and its box recorded for crops, as `{component}-{state}`
//   force   { component: ['hover' | 'focus' | 'focus-visible' | 'active'] }: pseudo-classes forced through CDP
//   after   async (h) => {} : undo what reveal did (close a menu, discard a draft)
//
// The owner's calendars are real and shared with other people. The capture never creates, edits, moves, RSVPs to,
// deletes or shares an event, never creates a scheduling link and never changes availability. Two traps found on
// 2026-10-25: (1) Escape on the new-event editor SAVES the draft once anything was typed into it, even after the
// text is cleared again (no discard prompt); an untouched editor closed with Escape is discarded. So the editor is
// only ever opened and closed, never typed into. (2) Playwright's hover() scrolls the week grid (a canvas almost
// a million pixels wide) to bring an element into view, which moves the visible week; every shot starts from
// home(), which goes back to today and pins both scroll positions.
//
// The app is styled-components (class names sc-<component>-<n> are stable for this build; the second class is
// the variant) on Notion's design system custom properties (--nds-*). Few elements carry roles or labels, so
// selectors are those component classes, data attributes (data-event-chip-key, data-calendar-id, data-grid-date,
// data-floating-context-panel, aria-modal) and UI words, never account text, except EVENT below.

export const NAME = 'Notion Calendar';
export const WINDOWS = { main: { url: /^https:\/\/calendar\.notion\.so\// } };
export const SCOPES = { main: ['html'] };

// The one owner event the popover shots open, on the fixed week of 2026-10-19 (a meeting with participants,
// organised by a coworker). Viewed only: its fields are never typed into and its RSVP is never touched.
export const EVENT = /^Tech Sync/;
const GRID_SCROLL_TOP = 360;          // 07:30 SG at the top of the grid (48px per hour)

// The grid is a horizontally virtualised canvas that also holds the weeks either side of the visible one, so parts
// are looked up inside one visible day column: data-grid-date is that day's local midnight in ms.
function dayMs(offset) {               // offset 0 = Monday of this week
  const d = new Date(); d.setHours(0, 0, 0, 0); d.setDate(d.getDate() - (d.getDay() + 6) % 7 + offset); return d.getTime();
}
const COL = offset => `[data-grid-date="${dayMs(offset)}"]`;
const markAllDay = async ({ page }) => page.evaluate(() => {
  const c = [...document.querySelectorAll('.sc-5i99wb-12 [data-event-chip-key]')].find(e => { const r = e.getBoundingClientRect(); return r.x > 340 && r.right < innerWidth; });
  c?.setAttribute('data-cap-allday', '');
});
const wait = (page, ms = 600) => page.waitForTimeout(ms);
const vis = (page, sel) => page.locator(sel).filter({ visible: true }).first();

// ---- what counts as "something is open"
const OPEN = '[role=listbox]:visible, [aria-modal=true]:visible, [data-floating-context-panel=true]:visible, [role=tooltip]:visible';
const busy = async page => (await page.locator(OPEN).count().catch(() => 0)) > 0 || /\/(event|scheduling|settings|shortcuts)\b/.test(new URL(page.url()).pathname);
export async function closeAll(page) {
  for (let i = 0; i < 6 && await busy(page); i++) {
    await page.keyboard.press('Escape'); await wait(page, 400);
    // A menu whose submenu was opened ignores Escape; a click on its backdrop (over the empty title bar) closes it.
    if (i >= 2 && await page.locator('[role=listbox]:visible').count()) { await page.mouse.click(600, 25); await wait(page, 400); }
  }
  // The scheduling pane closes with its own Close button, not Escape.
  if (/\/scheduling\b/.test(page.url())) { await paneClose(page).click().catch(() => {}); await wait(page, 800); }
}
const paneClose = page => page.locator('button.sc-19af6fi-0').filter({ visible: true }).first();

const S = {
  sidebar: '.sc-18kxtj6-3',
  sidebarScroll: '.sc-j54sno-8',
  gridScroll: '.sc-5i99wb-17',
  sidebarToggle: page => sidebarTop(page).nth(0),
  searchButton: page => sidebarTop(page).nth(1),
  createButton: page => sidebarTop(page).nth(2),
  miniCalendar: '.rdp-root',
  miniMonth: '.rdp-month_grid',
  miniDay: '.rdp-root td.rdp-day:not([data-today]):not([data-outside]) button',
  miniToday: '.rdp-root td.rdp-day[data-today] button',
  miniWeekday: '.rdp-root th.rdp-head_cell',
  miniNav: page => page.locator('.rdp-root').locator('xpath=..').locator('button').filter({ visible: true }).first(),
  schedulingRow: page => page.locator(`${S.sidebar} [role=button]`).filter({ hasText: /^Scheduling$/ }).first(),
  meetWith: 'input[placeholder^="Meet with"]',
  meetWithField: page => page.locator('input[placeholder^="Meet with"]').locator('xpath=..'),
  accountHeader: page => inSidebar(page, '.sc-1t04wmy-5').first(),
  calendarRow: page => inSidebar(page, '[data-calendar-id].sc-19bicfc-13').first(),
  calendarSwatch: page => inSidebar(page, '[data-calendar-id].sc-19bicfc-13').first().locator('.sc-19bicfc-10'),
  addCalendar: page => page.locator(`${S.sidebar} button`).filter({ hasText: /^Add calendar account$/ }).first(),
  helpButton: '.sc-jm22j0-0 button',
  avatar: 'button.sc-165quv-0',
  viewButton: page => page.locator('button.sc-gfyskm-3').filter({ hasText: /^(Week|Day|Month|\d+ days)$/ }).first(),
  todayButton: page => page.locator('button.sc-gfyskm-3').filter({ hasText: /^Today$/ }).first(),
  navArrow: 'button.sc-16r9m8z-4',
  contextToggle: 'button.sc-egm50s-0',
  monthTitle: '.sc-16r9m8z-1 strong',
  weekLabel: '.sc-16r9m8z-0',
  dayHeader: page => page.locator(`${COL(1)} .sc-ia3tqw-0`).first(),
  dayHeaderToday: page => todayHeader(page),
  timezoneLabel: '.sc-1xzq800-1 label',
  timeColumn: '.sc-7b0feo-2',
  nowBadge: '.sc-7b0feo-1',
  addTimezone: 'button.sc-1j8qt94-4',
  // All-day chips sit outside the day columns; markAllDay tags the first one inside the visible grid.
  allDayChip: '[data-cap-allday]',
  eventChip: page => page.locator(`${COL(1)} [data-event-chip-key]`).filter({ hasText: EVENT }).first(),
  eventChipOther: page => page.locator(`${COL(3)} [data-event-chip-key]`).filter({ visible: true }).first(),
  daysButton: 'button.sc-9dkkmz-5',
  menu: '[role=listbox]',
  modal: '[aria-modal=true] [data-elevated=true]',
  panel: '[data-floating-context-panel=true]',
  tooltip: '[role=tooltip]',
};
const sidebarTop = page => page.locator('.sc-98hv0u-3 button').filter({ visible: true });
// Sidebar rows inside the scrolled list's visible box (rows scrolled under the fixed top are skipped).
const inSidebar = (page, sel) => page.locator(`${S.sidebarScroll} ${sel}`).filter({ visible: true });
const visibleChips = page => page.locator('[data-event-chip-key]').filter({ visible: true });
// The day header's variant class for today (a red date badge).
const todayHeader = page => page.locator('.sc-ia3tqw-0.eEuPNj').filter({ visible: true }).first();
const lastMenu = page => page.locator(S.menu).filter({ visible: true }).last();
// Menu rows carry data-key (the action); the event menu's colour swatches carry a hex colour as theirs.
const menuRow = (page, n = 0) => lastMenu(page).locator('[data-key]:not([data-key^="#"])').filter({ visible: true }).nth(n);
const CMD_ROW = '[aria-modal=true] li.sc-1slm0q2-5';   // command menu rows; the highlighted one has an inline background
const menuParts = { menu: lastMenu, 'menu-row': page => menuRow(page, 1) };

// The empty week of today, as the owner left it: Week view, today's week, grid at 07:30, sidebar at its top.
export async function home({ page }) {
  await closeAll(page);
  await page.evaluate(() => document.activeElement?.blur?.());   // single-letter shortcuts below must reach the page, not a field
  await page.mouse.move(700, 30);
  const view = ((await S.viewButton(page).innerText().catch(() => '')) || '').trim();
  if (view !== 'Week') { await page.keyboard.press('w'); await wait(page, 900); }
  await S.todayButton(page).click(); await wait(page, 900);
  await page.evaluate(({ g, s, top }) => {
    const grid = document.querySelector(g); if (grid) grid.scrollTop = top;
    const side = document.querySelector(s); if (side) side.scrollTop = 0;
  }, { g: S.gridScroll, s: S.sidebarScroll, top: GRID_SCROLL_TOP });
  await page.mouse.move(700, 30); await wait(page, 500);
}
export async function reset(h) { return home(h); }

// Notion Calendar styles :hover, :active and :focus-visible directly, so no state needs help.
export async function prepareState() {}

// A fingerprint of what a capture must never change: the account's synced settings (theme, time zones, time
// format), the view and visible range, every event chip on today's week (key and text), which calendars are
// shown, and the scheduling pane's lock. ui.sidebarState's last-opened pane is not in it: opening the
// scheduling pane rewrites it, and it is put back at the end of the capture.
export async function guard(h) {
  const { page } = h;
  await home(h);
  return JSON.stringify(await page.evaluate(() => {
    const ls = Object.keys(localStorage).find(k => k.startsWith('user.settings.v1.'));
    const settings = JSON.parse(localStorage.getItem(ls) || '{}').snapshot || {};
    const chips = [...document.querySelectorAll('[data-event-chip-key]')].map(e => e.getAttribute('data-event-chip-key') + '=' + e.innerText.replace(/\s+/g, ' ').trim()).sort();
    let hash = 0; for (const c of chips.join('|')) hash = (hash * 31 + c.charCodeAt(0)) | 0;
    return {
      theme: document.documentElement.className,
      settings: JSON.stringify(settings),
      title: document.title,
      chips: `${chips.length}:${hash}`,
      calendars: [...document.querySelectorAll('[data-calendar-id].sc-19bicfc-13')].map(e => e.className.split(' ')[1]).join(','),
      paneLocked: JSON.parse(localStorage.getItem('ui.sidebarState') || '{}').sidebarPaneLocked,
    };
  }));
}

// The theme is Settings > General > Theme (Auto, Light mode, Dark mode). The owner's is Dark mode, so an emulated
// prefers-color-scheme changes nothing. Returns the label it replaced.
export const THEME_LABELS = { light: 'Light mode', dark: 'Dark mode', system: 'Auto' };
export async function setTheme(h, label) {
  const { page } = h;
  await settings(h, 'General');
  const scroller = page.locator('[aria-modal=true] .sc-6f59x4-0');
  await scroller.evaluate(e => { e.scrollTop = e.scrollHeight; }); await wait(page, 500);
  const labels = page.locator('[aria-modal=true] label:has(input[type=radio])');
  const before = await labels.evaluateAll(ls => ls.find(l => l.querySelector('input').checked)?.innerText.trim());
  if (before !== label) { await labels.filter({ hasText: label }).first().click(); await wait(page, 2000); }
  const now = await labels.evaluateAll(ls => ls.find(l => l.querySelector('input').checked)?.innerText.trim());
  await home(h);
  if (now !== label) throw new Error(`theme is ${now}, wanted ${label}`);
  return before;
}

// Settings is a modal (Cmd+,) with a navigation list; panes are picked by their label.
const NAV = '[aria-modal=true] .sc-1z4ze5-3';
async function settings({ page }, pane) {
  await closeAll(page);
  await page.keyboard.press('Meta+Comma'); await wait(page, 1500);
  if (pane) { await page.locator(NAV).filter({ hasText: pane }).first().click(); await wait(page, 1200); }
  await page.mouse.move(1040, 940); await wait(page, 300);
}
const settingsScroll = async (page, y) => { await page.locator('[aria-modal=true] .sc-6f59x4-0').evaluate((e, y) => { e.scrollTop = y; }, y); await wait(page, 500); };
const ACCOUNT_PANES = { 'settings-calendar-account': 5, 'settings-notion-workspace': 8 };   // nth nav item: the first calendar account, the first workspace

const openMenu = spec => async ({ page }) => { const l = typeof spec === 'function' ? spec(page) : vis(page, spec); await l.click(); await wait(page, 900); };
// Clears a field by setting its value, never with Cmd+A and Backspace: outside a field those select every
// visible event and delete them.
const clearInput = sel => async ({ page }) => { await page.locator(sel).filter({ visible: true }).first().fill('').catch(() => {}); await wait(page, 300); };
// Types only when a text field has focus: on the page itself every letter is a shortcut (x selects an event,
// c creates one, z travels time zones).
async function safeType(page, text) {
  const ok = await page.evaluate(() => { const a = document.activeElement; return !!a && (a.tagName === 'INPUT' || a.tagName === 'TEXTAREA'); });
  if (!ok) throw new Error('no text field has focus; not typing');
  await page.keyboard.type(text, { delay: 30 }); await wait(page, 900);
}
const key = k => async ({ page }) => { await page.keyboard.press(k); await wait(page, 1200); await page.mouse.move(700, 30); };
const openEvent = async ({ page }) => {
  const c = S.eventChip(page); const b = await c.boundingBox();
  if (!b) throw new Error('event chip not on screen');
  await page.mouse.click(b.x + b.width / 2, b.y + Math.min(12, b.height / 2)); await wait(page, 1500);
  await page.mouse.move(700, 30); await wait(page, 300);
  if (!(await page.locator(S.panel).count())) throw new Error('event panel did not open');
};
// The new-event editor, opened with the Create event button and never typed into. after() closes it with
// Escape (first blurs the title, second discards the untouched draft) and checks no draft chip is left.
const newEvent = async ({ page }) => { await S.createButton(page).click(); await wait(page, 1500); await page.mouse.move(700, 30); };
const discardNew = async ({ page }) => {
  for (let i = 0; i < 4 && /\/event\/create/.test(page.url()); i++) { await page.keyboard.press('Escape'); await wait(page, 900); }
  if (/\/event\/create/.test(page.url())) throw new Error('new-event editor still open');
};
const panelParts = {
  panel: S.panel,
  'panel-header': page => page.locator(`${S.panel} .sc-15zpq92-7`).first(),
  'panel-title': page => page.locator(`${S.panel} [contenteditable=true], ${S.panel} textarea, ${S.panel} input`).filter({ visible: true }).first(),
  'panel-icon-button': page => page.locator(`${S.panel} button`).filter({ visible: true }).first(),
  'panel-button': page => page.locator(`${S.panel} button`).filter({ hasText: /\S/ }).filter({ visible: true }).first(),
  'panel-section': page => page.locator(`${S.panel} [data-context-panel-root] > *`).filter({ visible: true }).nth(1),
};

const M = 'main';
const nth = (sel, i) => [sel, i];

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

const WEEK_PARTS = {
  sidebar: S.sidebar, 'sidebar-toggle': S.sidebarToggle, 'search-button': S.searchButton, 'create-button': S.createButton,
  'mini-calendar': S.miniCalendar, 'mini-day': S.miniDay, 'mini-day-today': S.miniToday, 'mini-weekday': S.miniWeekday,
  'scheduling-row': S.schedulingRow, 'meet-with': S.meetWithField, 'account-header': S.accountHeader, 'calendar-row': S.calendarRow,
  'calendar-swatch': S.calendarSwatch, 'help-button': S.helpButton, avatar: S.avatar, 'view-button': S.viewButton, 'today-button': S.todayButton,
  'nav-arrow': S.navArrow, 'context-toggle': S.contextToggle, 'month-title': S.monthTitle, 'week-label': S.weekLabel,
  'day-header': S.dayHeader, 'day-header-today': S.dayHeaderToday, 'timezone-label': S.timezoneLabel, 'time-column': S.timeColumn,
  'now-badge': S.nowBadge, 'add-timezone': S.addTimezone, 'all-day-chip': S.allDayChip, 'event-chip': S.eventChip, 'event-chip-other': S.eventChipOther,
  'days-button': S.daysButton,
};

export const SHOTS = [
  { name: 'week-default', window: M, reveal: markAllDay, parts: WEEK_PARTS,
    after: async ({ page }) => page.evaluate(() => document.querySelectorAll('[data-cap-allday]').forEach(e => e.removeAttribute('data-cap-allday'))), optionalParts: ['now-badge', 'all-day-chip', 'add-timezone', 'days-button', 'calendar-swatch'] },
  { name: 'day-view', window: M, reveal: key('d'), parts: { 'day-header': page => page.locator(`${COL(6)} .sc-ia3tqw-0`).first(), 'event-chip': page => page.locator(`${COL(6)} [data-event-chip-key]`).first() }, optionalParts: ['event-chip'], after: key('w') },
  { name: 'month-view', window: M, reveal: key('m'),
    // In month view each week row is one grid container, keyed by its Monday.
    parts: { 'month-week-row': page => page.locator(COL(0)).first(), 'month-chip': page => page.locator(`${COL(0)} [data-event-chip-key]`).nth(1) },
    optionalParts: ['month-chip'], after: key('w') },
  { name: 'sidebar-hidden', window: M, reveal: async ({ page }) => { await S.sidebarToggle(page).click(); await wait(page, 1000); await page.mouse.move(700, 30); },
    parts: {}, after: async ({ page }) => { await page.keyboard.press('Meta+Backslash'); await wait(page, 1000); } },
  // Menus: open, look, Escape. None of their rows is chosen.
  { name: 'view-menu', window: M, reveal: openMenu(S.viewButton), parts: { ...menuParts, 'menu-row-checked': page => menuRow(page, 1), 'menu-separator': page => lastMenu(page).locator('[role=separator], hr').first() },
    optionalParts: ['menu-separator', 'menu-row-checked'] },
  { name: 'view-submenu', window: M, reveal: async h => { await openMenu(S.viewButton)(h); await lastMenu(h.page).getByText('View settings', { exact: true }).hover(); await wait(h.page, 1000); },
    parts: { submenu: lastMenu } },
  { name: 'days-submenu', window: M, optional: true, reveal: async h => { await openMenu(S.viewButton)(h); await lastMenu(h.page).getByText('Number of days', { exact: true }).hover(); await wait(h.page, 1000); },
    parts: { submenu: lastMenu } },
  { name: 'profile-menu', window: M, reveal: openMenu(S.avatar), parts: { ...menuParts, 'menu-header': page => lastMenu(page).locator('> *').first() }, optionalParts: ['menu-header'] },
  { name: 'help-menu', window: M, reveal: openMenu(S.helpButton), parts: menuParts },
  { name: 'event-context-menu', window: M,
    reveal: async ({ page }) => { const b = await S.eventChip(page).boundingBox(); await page.mouse.click(b.x + b.width / 2, b.y + 12, { button: 'right' }); await wait(page, 1000); await page.mouse.move(700, 30); },
    parts: { ...menuParts, 'menu-row-danger': page => lastMenu(page).locator('[data-key=deleteEvent]'), 'colour-swatch': page => lastMenu(page).locator('[data-key^="#"]').filter({ visible: true }).nth(1) } },
  { name: 'grid-context-menu', window: M,
    reveal: async ({ page }) => { await page.mouse.click(1000, 300, { button: 'right' }); await wait(page, 1000); await page.mouse.move(700, 30); }, parts: menuParts },
  { name: 'command-menu', window: M, reveal: key('Meta+k'),
    parts: { 'command-menu': S.modal, 'command-input': '[aria-modal=true] input', 'command-row-selected': page => page.locator(`${CMD_ROW}[style*=background]`).first(),
      'command-row': page => page.locator(CMD_ROW).filter({ visible: true }).nth(2), 'command-heading': page => page.locator('[aria-modal=true]').getByText('Navigation', { exact: true }).first(),
      'command-footer': page => page.locator('[aria-modal=true]').getByText('Navigate', { exact: true }).first().locator('xpath=../..') },
    optionalParts: ['command-row-selected', 'command-row', 'command-footer'] },
  // Text typed into the command menu's search, never run, then cleared.
  { name: 'command-menu-typed', window: M, state: 'filled',
    reveal: async h => { await key('Meta+k')(h); await safeType(h.page, 'week'); },
    parts: { 'command-menu': S.modal, 'command-input': '[aria-modal=true] input' },
    after: clearInput('[aria-modal=true] input') },
  { name: 'command-menu-empty', window: M, state: 'empty',
    reveal: async h => { await key('Meta+k')(h); await safeType(h.page, 'zzqxv'); },
    parts: { 'command-menu': S.modal },
    after: clearInput('[aria-modal=true] input') },
  { name: 'shortcuts', window: M, reveal: key('Shift+Slash'),
    parts: { 'shortcuts-panel': S.panel, 'search-field': page => page.locator('input[placeholder^="Find keyboard"]').locator('xpath=..'),
      kbd: page => page.locator(S.panel).getByText('K', { exact: true }).first() }, optionalParts: ['kbd'] },
  // Typed into the shortcuts search (it only filters the list), then cleared.
  { name: 'shortcuts-search', window: M, state: 'filled',
    reveal: async h => { await key('Shift+Slash')(h); await h.page.locator('input[placeholder^="Find keyboard"]').click(); await safeType(h.page, 'today'); },
    parts: { 'search-field': page => page.locator('input[placeholder^="Find keyboard"]').locator('xpath=..') }, after: clearInput('input[placeholder^="Find keyboard"]') },
  { name: 'tooltip', window: M, state: 'hover', reveal: async ({ page }) => { await S.todayButton(page).hover(); await wait(page, 1500); }, parts: { tooltip: S.tooltip, 'today-button': S.todayButton } },
  // An existing event: its popover (the floating context panel), viewed and closed with Escape.
  { name: 'event-popover', window: M, reveal: openEvent,
    parts: { ...panelParts, 'event-chip-selected': S.eventChip,
      'rsvp-control': page => page.locator(S.panel).getByText(/^Yes$/).first().locator('xpath=ancestor::*[.//text()[.="Maybe"]][1]'),
      'participant-row': page => page.locator(S.panel).getByText('Organizer', { exact: true }).first().locator('xpath=ancestor::*[2]') },
    optionalParts: ['panel-header', 'panel-section', 'rsvp-control', 'participant-row', 'panel-title'] },
  // The new-event editor: opened, never typed into, discarded untouched.
  { name: 'new-event', window: M, reveal: newEvent,
    parts: { ...panelParts, 'draft-chip': page => page.locator('[data-event-chip-key]').filter({ visible: true }).filter({ hasText: /^\d\d:\d\d$/ }).first(),
      'editor-row': page => page.locator(S.panel).getByText('Participants', { exact: true }).first().locator('xpath=..') },
    optionalParts: ['panel-header', 'panel-section', 'draft-chip', 'editor-row', 'panel-button'], after: discardNew },
  { name: 'scheduling', window: M, reveal: async ({ page }) => { await S.schedulingRow(page).click(); await wait(page, 1500); await page.mouse.move(700, 30); },
    parts: { pane: page => page.getByText('Create scheduling links to quickly find times', { exact: false }).first().locator('xpath=ancestor::*[3]'),
      'button-primary': page => page.locator('button').filter({ hasText: /^Create recurring link$/ }).first(),
      'button-secondary': page => page.locator('button').filter({ hasText: /^Create one-off link/ }).first(),
      'scheduling-row-selected': S.schedulingRow },
    optionalParts: ['pane'] },
  // Settings, every pane but Add calendar account and Add Notion workspace (both start a sign-in).
  ...['General', 'Profile', 'Notifications', 'Menu bar', 'Conferencing'].map(p => ({ name: `settings-${p.toLowerCase().replace(/ /g, '-')}`, window: M, reveal: async h => settings(h, p), parts: {} })),
  ...Object.entries(ACCOUNT_PANES).map(([name, i]) => ({ name, window: M, optional: true,
    reveal: async h => { await settings(h); await h.page.locator(NAV).nth(i).click(); await wait(h.page, 1300); await h.page.mouse.move(1040, 940); }, parts: {} })),
  { name: 'settings-general-scrolled', window: M, reveal: async h => { await settings(h, 'General'); await settingsScroll(h.page, 99999); },
    parts: { radio: '[aria-modal=true] label:has(input[type=radio]:not(:checked))', 'radio-selected': '[aria-modal=true] label:has(input[type=radio]:checked)',
      checkbox: page => page.locator('[aria-modal=true] label:has(input[type=checkbox])').filter({ visible: true }).first() },
    optionalParts: ['checkbox'] },
  { name: 'settings-general-detail', window: M, reveal: async h => settings(h, 'General'),
    parts: { dialog: S.modal, 'settings-nav': page => page.locator(NAV).nth(1), 'settings-nav-selected': page => page.locator(NAV).first(),
      'settings-heading': page => page.locator('[aria-modal=true]').getByText('Calendar view', { exact: true }).first(),
      'settings-section-label': page => page.locator('[aria-modal=true]').getByText('Account', { exact: true }).first(),
      'switch-on': '[aria-modal=true] button[role=switch][aria-checked=true]', 'switch-label': '[aria-modal=true] label:has(button[role=switch])',
      select: '[aria-modal=true] [role=button][data-input=true]', link: page => page.locator('[aria-modal=true] button').filter({ hasText: /^keyboard shortcuts$/ }).first(),
      kbd: page => page.locator('[aria-modal=true]').getByText('T', { exact: true }).first(), 'dialog-close': '[aria-modal=true] .sc-ud7x4f-0 > button',
      'settings-text': page => page.locator('[aria-modal=true]').getByText(/^Configure the view/).first() },
    optionalParts: ['kbd', 'switch-off', 'settings-section-label'] },
  { name: 'settings-select-open', window: M, reveal: async h => { await settings(h, 'General'); await vis(h.page, '[aria-modal=true] [role=button][data-input=true]').click(); await wait(h.page, 900); },
    parts: { ...menuParts, 'menu-row-checked': page => lastMenu(page).locator('[data-key]').filter({ has: page.locator('svg') }).first() }, optionalParts: ['menu-row-checked'] },
  { name: 'settings-profile-detail', window: M, reveal: async h => settings(h, 'Profile'),
    parts: { 'text-field': page => page.locator('[aria-modal=true] input').filter({ visible: true }).first(),
      'button-danger': page => page.locator('[aria-modal=true] button').filter({ hasText: /^Delete Notion Calendar account$/ }).first(),
      'text-link-button': page => page.locator('[aria-modal=true] button').filter({ hasText: /^Edit in Notion$/ }).first() },
    optionalParts: ['text-field', 'text-link-button'] },
  { name: 'settings-conferencing-detail', window: M, reveal: async h => settings(h, 'Conferencing'),
    parts: { 'text-link-button-sm': page => page.locator('[aria-modal=true] button').filter({ hasText: /^Configure$/ }).first(),
      'button-danger-sm': page => page.locator('[aria-modal=true] button').filter({ hasText: /^Disconnect$/ }).first(),
      'settings-card': page => page.locator('[aria-modal=true]').getByText('Google Meet', { exact: true }).first().locator('xpath=ancestor::*[3]') },
    optionalParts: ['settings-card', 'button-danger-sm'] },

  // ---- states, one part per shot: hover with the real pointer, focus-visible with real keyboard focus,
  // pressed with :hover and :active forced through CDP over the part. Event chips are never pressed for real.
  ...states([
    ['week', M, async () => {}, { 'today-button': S.todayButton, 'view-button': S.viewButton, 'nav-arrow': S.navArrow, 'search-button': S.searchButton,
      'calendar-row': S.calendarRow, 'mini-day': S.miniDay, 'scheduling-row': S.schedulingRow }, ['hover', 'focus-visible', 'pressed']],
    ['week', M, async () => {}, { 'event-chip': S.eventChip, 'day-header': S.dayHeader, 'account-header': S.accountHeader }, ['hover', 'pressed']],
    ['settings', M, async h => settings(h, 'General'), { 'settings-nav': page => page.locator(NAV).nth(1), 'switch-on': '[aria-modal=true] button[role=switch][aria-checked=true]',
      select: '[aria-modal=true] [role=button][data-input=true]', link: page => page.locator('[aria-modal=true] button').filter({ hasText: /^keyboard shortcuts$/ }).first() },
      ['hover', 'focus-visible', 'pressed']],
    ['menu', M, openMenu(S.viewButton), { 'menu-row': page => menuRow(page, 2) }, ['hover']],
    ['command', M, key('Meta+k'), { 'command-row': page => page.locator(CMD_ROW).filter({ visible: true }).nth(2) }, ['hover']],
  ]),
];

// No agent run: Notion Calendar has no agent and the capture sends nothing.
export const RUN = null;
