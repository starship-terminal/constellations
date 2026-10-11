// Measures TokenTracker's dashboard components in every state that can be reached without
// signing in, sending or changing a setting.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: dashboard sessions limits settings status. Phone layouts come from the screenshots only. Every page runs in dark (the default)
// and light; light entries are keyed `<name>.light`. Writes raw/components-computed.json (merged,
// so a subset of pages can be re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed
//   focused        the field clicked into (a text field only)
//   filled         sample text typed into a field, measured, then deleted; Enter is never pressed
//   selected/open  a resting state the page reaches itself (the current tab, an open select menu)
// mask() from lib.mjs runs on every page before any crop, so no private text reaches a crop.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, mask, styleOf, crop, centre, RAW } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
// Readings are written once, at the end, and only when every page ran; a failed run goes to
// <OUT>.partial.json and exits 1, so the last complete readings are never mixed with a partial one.
const failures = [];
const save = () => {
  if (failures.length) {
    fs.writeFileSync(OUT.replace(/\.json$/, '.partial.json'), JSON.stringify(out, null, 1) + '\n');
    return;
  }
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
};

const URLS = {
  dashboard: '/dashboard',
  sessions: '/sessions',
  limits: '/limits',
  settings: '/settings',
  status: '/service-status',
  mobile: '/dashboard',
};
let THEME = 'dark';

let page, cdp, current, context, run;
const touched = new Set();

// ---------- helpers ----------

async function newPage(key, { wait = 3500 } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, THEME);
  await open(page, BASE + URLS[key], { wait });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(250);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await page.keyboard.press('Shift');
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el);
    how = 'keydown then focus()';
  }
  await page.waitForTimeout(350);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(400);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

// Clicks a UI toggle (tab, menu, show more). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log in|create|generate|upload|download|install|share|copy|refresh|open in mac app|add|import from codex|choose package|check for updates)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

const FILL = 'claude-opus';

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  if (THEME !== 'dark') key = `${key}.light`;
  await mask(page);
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  delete out.components[key].missing;
  if (opts.open) { await reset(); await opts.open(); }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) { log('  ! missing', key); out.components[key].missing = true; return; }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (opts.before?.[st]) via = await opts.before[st](loc);
      if (st === 'hover') {
        await (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).filter({ visible: true }).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).filter({ visible: true }).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await (opts.fieldLoc || loc).filter({ visible: true }).first().click({ timeout: 4000 });
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || FILL, { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || FILL}", then deleted; nothing sent`;
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Transitions and animations declared in every readable sheet, by selector.
async function sheetsFor(key) {
  const res = await page.evaluate(() => {
    const transitions = [];
    const walk = (rules) => {
      for (const r of rules) {
        if (r.cssRules && !r.selectorText) { walk(r.cssRules); continue; }
        if (!r.style) continue;
        const t = r.style.getPropertyValue('transition');
        const a = r.style.getPropertyValue('animation');
        if (t || a) transitions.push({ selector: (r.selectorText || '').replace(/__[A-Za-z0-9_-]{5,6}/g, '').slice(0, 160), transition: t, animation: a });
      }
    };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin, read by vars.mjs */ } }
    return transitions;
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}

// ---------- finders ----------
// Elements are found by role, visible label text the product itself prints (nav labels, column
// headers, button labels), or structure, never by account text. tag() marks a match with data-m.
async function tag(name, { text, role, up = 0, sel, nth = 0, within } = {}) {
  return page.evaluate(({ name, text, role, up, sel, nth, within }) => {
    document.querySelectorAll(`[data-m="${name}"]`).forEach((n) => n.removeAttribute('data-m'));
    const scope = within ? document.querySelector(within) : document;
    if (!scope) return false;
    let list;
    if (sel) list = [...scope.querySelectorAll(sel)];
    else list = [...scope.querySelectorAll(role ? `[role="${role}"], ${role}` : '*')].filter((e) => {
      // textContent, not innerText: CSS uppercase would change innerText.
      const t = (role ? (e.innerText ?? '') : (e.textContent ?? '')).trim();
      return role ? t === text : e.childElementCount === 0 && t === text;
    });
    list = list.filter((e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    let el = list[nth];
    if (!el) return false;
    for (let i = 0; i < up && el.parentElement; i++) el = el.parentElement;
    el.setAttribute('data-m', name);
    return true;
  }, { name, text, role, up, sel, nth, within });
}
const m = (name) => q(`[data-m="${name}"]`);
async function T(key, find, list, meta, opts) {
  if (!(await tag(key, find))) { log('  ! not found', key); comp(THEME === 'dark' ? key : `${key}.light`, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel }).missing = true; return; }
  await S(key, m(key), list, meta, opts);
}

// ---------- product ----------
const G = {
  shell: 'Shell and navigation', header: 'Page header', dash: 'Tokens page', table: 'Tables and lists',
  form: 'Fields and selects', control: 'Buttons and segmented controls', limits: 'Limits', settings: 'Settings',
  feedback: 'Badges, tooltips and status', mobile: 'Mobile (390 wide)',
};

async function dashboard() {
  await newPage('dashboard');
  await sheetsFor('dashboard');
  out._meta.page ??= {};
  out._meta.page[THEME] = await page.evaluate(() => {
    const cs = (e) => e && getComputedStyle(e);
    const main = document.querySelector('main');
    let panel = main; while (panel && panel.parentElement && !/rounded/.test(panel.className)) panel = panel.parentElement;
    return { html: document.documentElement.className, body: cs(document.body).backgroundColor, bodyFont: cs(document.body).fontFamily,
      root: cs(document.querySelector('#root > div') || document.body).backgroundColor };
  });
  const g = G.shell;
  await T('sidebar', { sel: 'aside, nav', up: 0 }, ['default'], { group: g, title: 'Sidebar', desc: 'The 220px rail on the page wash: no fill of its own, three groups, footer pills.', sel: 'aside' }, { noScroll: true });
  await T('sidebar-group-label', { text: 'Tools' }, ['default'], { group: g, title: 'Sidebar group label', sel: 'leaf "Tools"' }, { noScroll: true });
  await T('nav-item-active', { sel: 'a[href="/dashboard"]' }, ['default', 'focus-visible'], { group: g, title: 'Nav item, current', sel: 'a[href="/dashboard"] (Tokens)' }, { noScroll: true });
  await T('nav-item', { sel: 'a[href="/sessions"]' }, ['default', 'hover', 'focus-visible', 'pressed'], { group: g, title: 'Nav item', sel: 'a[href="/sessions"]' }, { noScroll: true });
  await T('nav-icon', { sel: 'a[href="/sessions"] svg' }, ['default'], { group: g, title: 'Nav icon', desc: 'Lucide History at the nav size.', sel: 'a[href="/sessions"] svg' }, { noScroll: true, pad: 4 });
  await page.evaluate(() => {
    // The panel is the widest rounded, filled box on the page (it need not wrap <main>).
    const panel = [...document.querySelectorAll('body *')].filter((n) => { const c = getComputedStyle(n); const r = n.getBoundingClientRect(); return r.width > 900 && r.height > 600 && parseFloat(c.borderTopLeftRadius) > 0 && (c.backgroundColor !== 'rgba(0, 0, 0, 0)' || c.boxShadow !== 'none' || parseFloat(c.borderTopWidth) > 0); })
      .sort((x, y) => y.getBoundingClientRect().width - x.getBoundingClientRect().width)[0];
    if (panel) panel.setAttribute('data-m', 'content-panel');
  });
  await S('content-panel', m('content-panel'), ['default'], { group: g, title: 'Content panel', desc: 'The rounded panel the pages sit in, inset from the window edge on the page wash.', sel: 'first rounded, filled ancestor of main' }, { noScroll: true, crop: false });
  await T('theme-toggle', { sel: 'button[aria-label*="theme" i], button[title*="theme" i]' }, ['default', 'hover'], { group: g, title: 'Theme toggle', sel: 'button[aria-label*=theme]' }, { noScroll: true });
  await T('star-pill', { sel: 'a[href*="github.com"]' }, ['default', 'hover'], { group: g, title: 'GitHub star pill', sel: 'a[href*=github]' }, { noScroll: true });

  const d = G.dash;
  await T('period-tabs', { role: 'tablist', sel: '[role="tablist"][aria-label="Time period"]' }, ['default'], { group: G.control, title: 'Period tabs', sel: '[role=tablist][aria-label="Time period"]' }, { noScroll: true });
  await T('period-tab-selected', { sel: '[role="tablist"][aria-label="Time period"] [aria-selected="true"]' }, ['default', 'focus-visible'], { group: G.control, title: 'Period tab, selected', sel: '[role=tab][aria-selected=true]' }, { noScroll: true });
  await T('period-tab', { sel: '[role="tablist"][aria-label="Time period"] [aria-selected="false"]' }, ['default', 'hover', 'focus-visible'], { group: G.control, title: 'Period tab', sel: '[role=tab][aria-selected=false]' }, { noScroll: true });
  await T('hero-label', { text: 'Total tokens' }, ['default'], { group: d, title: 'Hero metric label', desc: 'Set in uppercase by CSS (the text is "Total tokens").', sel: 'leaf "Total tokens"' }, { noScroll: true });
  await page.evaluate(() => {
    const big = [...document.querySelectorAll('main *')].filter((e) => e.getBoundingClientRect().height > 40 && parseFloat(getComputedStyle(e).fontSize) >= 48)
      .sort((a, b) => parseFloat(getComputedStyle(b).fontSize) - parseFloat(getComputedStyle(a).fontSize))[0];
    if (big) big.setAttribute('data-m', 'hero-metric');
    const cost = [...document.querySelectorAll('main *')].find((e) => e.childElementCount <= 1 && /^≥?\$[\d,]+\.\d\d$/.test((e.innerText || '').trim()) && parseFloat(getComputedStyle(e).fontSize) >= 18);
    if (cost) cost.setAttribute('data-m', 'hero-cost');
  });
  await S('hero-metric', m('hero-metric'), ['default'], { group: d, title: 'Hero metric', desc: 'The one giant number: total tokens for the period.', sel: 'largest text in main' }, { noScroll: true });
  await S('hero-cost', m('hero-cost'), ['default'], { group: d, title: 'Hero cost', desc: 'Cost under the hero number, in the brand green.', sel: 'text matching $n.nn' }, { noScroll: true });
  await T('share-button', { role: 'button', text: 'Share' }, ['default', 'hover', 'focus-visible', 'pressed'], { group: G.control, title: 'Secondary button', desc: 'Outlined, as on Share. Measured, never pressed.', sel: 'button "Share"' }, { noScroll: true });
  await T('primary-button', { role: 'button', text: 'Open in Mac app' }, ['default', 'hover', 'focus-visible', 'pressed'], { group: G.control, title: 'Primary button', desc: 'Solid near-black in light, near-white in dark. Measured, never pressed.', sel: 'button "Open in Mac app"' }, { noScroll: true });
  await T('provider-tile', { text: 'CLAUDE', up: 2 }, ['default', 'hover'], { group: d, title: 'Provider share tile', sel: 'tile holding "CLAUDE"' }, { noScroll: true });
  await T('provider-tile-all', { text: 'All', up: 2 }, ['default'], { group: d, title: 'Provider share tile, all', sel: 'tile holding "All"' }, { noScroll: true });
  await T('stat-chip', { text: '7d', up: 1 }, ['default'], { group: d, title: 'Stat chip', desc: 'A small filled tile: value over a caption (7d, 30d, avg, convs).', sel: 'parent of "7d"' }, { noScroll: true });
  await T('card', { text: 'Daily Breakdown', role: 'tab' , up: 0 }, ['default'], { group: d, title: '(placeholder)', sel: '' }, { noScroll: true, crop: false });
  delete out.components[THEME === 'dark' ? 'card' : 'card.light'];
  await page.evaluate(() => { const t = [...document.querySelectorAll('main *')].find((e) => e.childElementCount === 0 && /^Activity heatmap$/i.test(e.textContent.trim())); if (!t) return; t.setAttribute('data-m', 'card-title'); let n = t; while (n && !/rounded-(xl|2xl)/.test(n.className)) n = n.parentElement; if (n) n.setAttribute('data-m', 'card'); });
  await S('card', m('card'), ['default'], { group: d, title: 'Card', desc: 'The Activity heatmap card: the shared card surface.', sel: 'card around "Activity heatmap"' });
  await S('card-title', m('card-title'), ['default'], { group: d, title: 'Card title (legacy, uppercase)', desc: 'Older cards title themselves in small tracked uppercase.', sel: 'leaf "Activity heatmap"' });
  await page.evaluate(() => {
    const cells = [...document.querySelectorAll('main span.rounded-\\[2px\\]')].filter((e) => { const r = e.getBoundingClientRect(); return r.width === 12 && r.height === 12; });
    // Busiest = the fill farthest from the empty-day fill; empty = the least saturated fill.
    const rgb = (e) => (getComputedStyle(e).backgroundColor.match(/\d+/g) || [0, 0, 0]).slice(0, 3).map(Number);
    const sat = (e) => { const c = rgb(e); return Math.max(...c) - Math.min(...c); };
    const emptyCell = cells.slice().sort((a, b) => sat(a) - sat(b))[0];
    const e0 = emptyCell ? rgb(emptyCell) : [0, 0, 0];
    const lum = (e) => rgb(e).reduce((t, v, i) => t + (v - e0[i]) ** 2, 0);
    const busy = cells.slice().sort((a, b) => lum(b) - lum(a));
    if (busy[0]) busy[0].setAttribute('data-m', 'heatmap-cell');
    if (emptyCell) emptyCell.setAttribute('data-m', 'heatmap-cell-empty');
    window.__heat = [...new Set(cells.map((e) => getComputedStyle(e).backgroundColor))];
  });
  out._meta.heatmap ??= {};
  out._meta.heatmap[THEME] = await page.evaluate(() => window.__heat);
  await S('heatmap-cell', m('heatmap-cell'), ['default', 'hover'], { group: d, title: 'Heatmap cell, busiest', sel: 'span.rounded-[2px] whose fill is farthest from the empty fill' }, { pad: 6 });
  await S('heatmap-cell-empty', m('heatmap-cell-empty'), ['default'], { group: d, title: 'Heatmap cell, empty', sel: 'span.rounded-[2px] with the least saturated fill' }, { pad: 6 });
  await T('segmented-2d', { role: 'button', text: '2D', up: 1 }, ['default'], { group: G.control, title: 'Small segmented control', desc: '2D / 3D switch on the heatmap.', sel: 'parent of button "2D"' });
  await T('beta-badge', { text: 'BETA' }, ['default'], { group: G.feedback, title: 'Badge', sel: 'leaf "BETA"' }, { noScroll: true });
  await T('table-tab-selected', { role: 'button', text: 'Daily Breakdown' }, ['default'], { group: G.table, title: 'Table tab, selected', sel: 'button "Daily Breakdown"' });
  await T('table-tab', { role: 'button', text: 'Project Usage' }, ['default', 'hover'], { group: G.table, title: 'Table tab', sel: 'button "Project Usage"' });
  await T('table-header', { sel: 'main table thead th', nth: 1 }, ['default'], { group: G.table, title: 'Table header cell', sel: 'thead th:nth(1)' });
  await T('table-cell', { sel: 'main table tbody td', nth: 1 }, ['default'], { group: G.table, title: 'Table cell (numeric)', sel: 'tbody td:nth(1)' });
  await T('table-row', { sel: 'main table tbody tr', nth: 1 }, ['default', 'hover'], { group: G.table, title: 'Table row', sel: 'tbody tr:nth(1)' });
  await T('cost-button', { sel: 'main button[aria-label="View cost breakdown"]' }, ['default', 'hover', 'focus-visible'], { group: d, title: 'Hero cost button', desc: 'The cost under the hero number is a button that opens the cost breakdown.', sel: 'button[aria-label="View cost breakdown"]' }, { noScroll: true });
  if (await m('cost-button').count()) {
    await m('cost-button').first().click(); await page.waitForTimeout(900);
    await page.evaluate(() => { const t = [...document.querySelectorAll('[role="tooltip"], .tooltip, [data-radix-popper-content-wrapper] > *')].find((e) => e.getBoundingClientRect().width > 0) || [...document.querySelectorAll('body *')].filter((e) => { const c = getComputedStyle(e); return (c.position === 'absolute' || c.position === 'fixed') && e.getBoundingClientRect().width > 80 && e.getBoundingClientRect().width < 420 && (e.innerText || '').length > 10 && parseFloat(c.zIndex) > 10; })[0]; if (t) t.setAttribute('data-m', 'tooltip'); });
    await page.evaluate(() => { const dlg = document.querySelector('[role="dialog"]'); if (dlg) dlg.setAttribute('data-m', 'dialog'); });
    await S('dialog', m('dialog'), ['open'], { group: G.feedback, title: 'Dialog (cost breakdown)', desc: 'Opened by the hero cost button, closed with Escape.', sel: '[role=dialog]' }, { noScroll: true, noReset: true });
    await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  }
  await page.close();
}

async function sessions() {
  await newPage('sessions');
  const g = G.header;
  await T('page-title', { sel: 'main h1' }, ['default'], { group: g, title: 'Page title', sel: 'main h1' }, { noScroll: true });
  await T('page-subtitle', { sel: 'main h1 + p, main h1 ~ p' }, ['default'], { group: g, title: 'Page subtitle', sel: 'main h1 + p' }, { noScroll: true });
  await T('icon-button', { sel: 'main button[aria-label]' }, ['default', 'hover', 'focus-visible', 'pressed'], { group: G.control, title: 'Icon button', desc: 'Refresh at the top right. Measured, never pressed.', sel: 'main button[aria-label]' }, { noScroll: true });
  const f = G.form;
  await T('search-field', { sel: 'main input[placeholder^="Search"]', up: 1 }, ['default', 'hover'], { group: f, title: 'Search field', sel: 'input[placeholder^=Search] parent' }, { noScroll: true });
  await T('search-input', { sel: 'main input[placeholder^="Search"]' }, ['default', 'focused', 'filled'], { group: f, title: 'Search input', desc: 'A model name was typed and deleted; nothing was sent.', sel: 'input[placeholder^=Search]' }, { noScroll: true, cropLoc: q('main input[placeholder^="Search"]').locator('xpath=..') });
  await page.evaluate(() => { const s = [...document.querySelectorAll('main span.truncate')].find((e) => e.textContent.trim() === 'All tools'); if (s) s.closest('button,[role="combobox"]').setAttribute('data-m', 'select'); });
  await S('select', m('select'), ['default', 'hover', 'focus-visible'], { group: f, title: 'Select button', sel: 'button holding "All tools"' }, { noScroll: true });
  await m('select').first().click(); await page.waitForTimeout(600);
  await page.evaluate(() => { const l = document.querySelector('[role="listbox"], [role="menu"]'); if (l) { l.setAttribute('data-m', 'select-menu'); const o = l.querySelectorAll('[role="option"], [role="menuitem"], button, li'); if (o[0]) o[0].setAttribute('data-m', 'select-option-selected'); if (o[1]) o[1].setAttribute('data-m', 'select-option'); } });
  await S('select-menu', m('select-menu'), ['open'], { group: f, title: 'Select menu', sel: '[role=listbox]' }, { noScroll: true, noReset: true });
  await S('select-option-selected', m('select-option-selected'), ['open'], { group: f, title: 'Select option, selected', sel: 'first option' }, { noScroll: true, noReset: true });
  await S('select-option', m('select-option'), ['open', 'hover'], { group: f, title: 'Select option', sel: 'second option' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  await T('summary-strip', { text: 'Matching sessions', up: 2 }, ['default'], { group: G.table, title: 'Summary strip', desc: 'Four figures in one bordered box, split by rules.', sel: 'box around "Matching sessions"' }, { noScroll: true });
  await T('summary-label', { text: 'Matching sessions' }, ['default'], { group: G.table, title: 'Summary label', sel: 'leaf "Matching sessions"' }, { noScroll: true });
  await T('list-header', { text: 'Session / project' }, ['default'], { group: G.table, title: 'List column header', sel: 'leaf "Session / project"' }, { noScroll: true });
  await T('list-row', { sel: '.sessions-row', nth: 1 }, ['default', 'hover'], { group: G.table, title: 'Session row', sel: '.sessions-row' });
  await T('list-row-title', { sel: '.sessions-row-title', nth: 1 }, ['default', 'hover', 'focus-visible'], { group: G.table, title: 'Session row title', sel: '.sessions-row-title' });
  await T('list-group-label', { sel: 'main ul', up: 0 }, ['default'], { group: G.table, title: '(unused)', sel: '' }, { crop: false });
  delete out.components[THEME === 'dark' ? 'list-group-label' : 'list-group-label.light'];
  await page.close();
}

async function limits() {
  await newPage('limits', { wait: 3000 });
  // Limits load from the local API at their own pace; wait for the first track to render.
  for (let i = 0; i < 40 && !(await page.evaluate(() => [...document.querySelectorAll('main *')].some((e) => /uppercase/.test(e.className) && /^usage limits/i.test(e.textContent.trim())))); i++) await page.waitForTimeout(500);
  await mask(page);
  const g = G.limits;
  await page.evaluate(() => { const t = [...document.querySelectorAll('main *')].find((e) => /uppercase/.test(e.className) && /^usage limits/i.test(e.textContent.trim()) && e.textContent.trim().length < 30); if (t) { let n = t; while (n && !/rounded/.test(n.className)) n = n.parentElement; if (n) n.setAttribute('data-m', 'limits-card'); t.setAttribute('data-m', 'limits-title'); } });
  await S('limits-card', m('limits-card'), ['default'], { group: g, title: 'Limits card', sel: 'card around the "Usage limits" title' }, { crop: false });
  await S('limits-title', m('limits-title'), ['default'], { group: g, title: 'Limits card title', sel: 'leaf "Usage limits"' }, { noScroll: true });
  await page.evaluate(() => {
    const bars = [...document.querySelectorAll('main div')].filter((e) => { const r = e.getBoundingClientRect(); return r.height >= 3 && r.height <= 8 && r.width > 300 && e.children.length >= 1; });
    if (bars[0]) { bars[0].setAttribute('data-m', 'usage-track'); const fill = [...bars[0].querySelectorAll('div')].find((c) => c.getBoundingClientRect().width > 20); if (fill) fill.setAttribute('data-m', 'usage-fill'); }
    const row = bars[0] && bars[0].parentElement; if (row) row.setAttribute('data-m', 'usage-row');
    const badge = [...document.querySelectorAll('main *')].find((e) => /^(STALE|RE-AUTH|LIVE)\b/i.test((e.innerText || '').trim()) && e.getBoundingClientRect().height < 26 && e.getBoundingClientRect().height > 10);
    if (badge) badge.setAttribute('data-m', 'status-badge');
  });
  await S('usage-row', m('usage-row'), ['default'], { group: g, title: 'Usage row', desc: 'Window label, a thin track with a pace tick, percent and time left.', sel: 'row around the first track' });
  await S('usage-track', m('usage-track'), ['default'], { group: g, title: 'Usage track', sel: 'first track' }, { pad: 4 });
  await S('usage-fill', m('usage-fill'), ['default'], { group: g, title: 'Usage fill', sel: 'its fill' }, { pad: 4 });
  await S('status-badge', m('status-badge'), ['default'], { group: G.feedback, title: 'Status badge', desc: 'STALE / RE-AUTH pill with a coloured dot.', sel: 'pill reading STALE' });
  await T('code-block', { sel: 'main pre' }, ['default'], { group: g, title: 'Code block', sel: 'main pre' });
  await page.close();
}

async function settings() {
  await newPage('settings');
  const g = G.settings;
  await T('subnav-item-active', { role: 'button', text: 'Appearance' }, ['default'], { group: g, title: 'Settings nav item, current', sel: 'button "Appearance"' }, { noScroll: true });
  await T('subnav-item', { role: 'button', text: 'Account' }, ['default', 'hover', 'focus-visible'], { group: g, title: 'Settings nav item', sel: 'button "Account"' }, { noScroll: true });
  await T('subnav-group-label', { text: 'App' }, ['default'], { group: g, title: 'Settings nav group label', sel: 'leaf "App"' }, { noScroll: true });
  await T('section-title', { sel: 'main h2' }, ['default'], { group: g, title: 'Section title', sel: 'main h2' }, { noScroll: true });
  await T('settings-card', { text: 'Theme', up: 3 }, ['default'], { group: g, title: 'Settings card', sel: 'card around "Theme"' }, { noScroll: true, crop: false });
  await T('setting-label', { text: 'Theme' }, ['default'], { group: g, title: 'Setting label', sel: 'leaf "Theme"' }, { noScroll: true });
  await T('setting-description', { text: 'Choose how Token Tracker looks across the dashboard.' }, ['default'], { group: g, title: 'Setting description', sel: 'leaf description' }, { noScroll: true });
  await T('segmented', { role: 'button', text: 'Compact', up: 1 }, ['default'], { group: G.control, title: 'Segmented control', sel: 'parent of button "Compact"' }, { noScroll: true });
  await T('segment-selected', { role: 'button', text: 'Compact' }, ['default', 'focus-visible'], { group: G.control, title: 'Segment, selected', sel: 'button "Compact"' }, { noScroll: true });
  await T('segment', { role: 'button', text: 'Full' }, ['default', 'hover', 'focus-visible'], { group: G.control, title: 'Segment', desc: 'Hovered and focused only; never pressed, so the setting is unchanged.', sel: 'button "Full"' }, { noScroll: true });
  await T('footer-link', { role: 'button', text: 'Check for updates' }, ['default', 'hover'], { group: g, title: 'Footer link', sel: 'button "Check for updates"' });
  await page.close();
}

async function status() {
  await newPage('status', { wait: 8000 });
  await T('status-row', { text: 'Claude', up: 3 }, ['default', 'hover'], { group: G.feedback, title: 'Service status row', sel: 'row around "Claude"' }, { noScroll: true });
  await page.close();
}

const PAGES = { dashboard, sessions, limits, settings, status };
const want = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(PAGES);
const done = new Set();
for (const theme of ['dark', 'light']) {
  THEME = theme;
  for (const k of want) {
    const l = await launch({ mobile: k === 'mobile', theme });
    context = l.context;
    run = `${k}-${theme}`;
    try { await PAGES[k](); done.add(run); } catch (e) { failures.push(`${k} ${theme}`); log('PAGE FAILED', k, theme, String(e.message).split('\n')[0]); }
    await l.browser.close();
  }
}
for (const [key, c] of Object.entries(out.components)) if (done.has(c.run) && !touched.has(key)) { delete out.components[key]; log('dropped stale', key); }
if (!failures.length) {
  out._meta.read = new Date().toLocaleDateString('en-CA');
  out._meta.source = 'TokenTracker v1.3.5 dashboard served by the local CLI at 127.0.0.1:7680, measured headless in Chromium (Playwright) at 1440x900, 2x';
}
save();
if (failures.length) {
  log('FAILED pages:', failures.join(', '), '-> partial readings only, in', OUT.replace(/\.json$/, '.partial.json'));
  process.exit(1);
}
log('done ->', OUT);
