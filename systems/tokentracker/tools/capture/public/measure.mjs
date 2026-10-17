// Measures TokenTracker's dashboard components in every state that can be reached without
// signing in, sending or changing a setting.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: dashboard sessions sessionsLoading sessionsError limits settings status skills widgets pet cloud achievements leaderboard. Phone layouts come from the screenshots only. Every page runs in dark (the default)
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
  skills: '/skills',
  widgets: '/widgets',
  pet: '/pet-settings',
  cloud: '/cloud',
  achievements: '/achievements',
  leaderboard: '/leaderboard',
  sessionsLoading: '/sessions',
  sessionsError: '/sessions',
  mobile: '/dashboard',
};
let THEME = 'dark';

let page, cdp, current, context, run;
const touched = new Set();

// ---------- helpers ----------

async function newPage(key, { wait = 3500, routes } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  if (routes) await routes(page);
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

// Popups (tooltips, toasts, menus, dialogs) mount new nodes. markBefore() flags every node that
// exists now; tagNew() then tags the outermost visible node that appeared since and whose text
// matches, so a popup is found by appearing, not by a guessed class name.
async function markBefore() {
  await page.evaluate(() => document.querySelectorAll('body *').forEach((e) => e.setAttribute('data-pre', '')));
}
async function tagNew(name, re) {
  const ok = await page.evaluate(({ name, src }) => {
    const re = src ? new RegExp(src, 'i') : null;
    document.querySelectorAll(`[data-m="${name}"]`).forEach((n) => n.removeAttribute('data-m'));
    const fresh = [...document.querySelectorAll('body *:not([data-pre])')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 4 && r.height > 4 && (!re || re.test(e.innerText || ''));
    });
    const top = fresh.filter((e) => !fresh.some((o) => o !== e && o.contains(e)));
    const el = top.sort((a, b) => (b.innerText || '').length - (a.innerText || '').length)[0];
    document.querySelectorAll('[data-pre]').forEach((e) => e.removeAttribute('data-pre'));
    if (!el) return false;
    el.setAttribute('data-m', name);
    return true;
  }, { name, src: re ? re.source : null });
  return ok;
}
// The full-window layer behind an open dialog: the scrim.
async function tagScrim(name) {
  return page.evaluate((name) => {
    const vw = innerWidth, vh = innerHeight;
    const el = [...document.querySelectorAll('body *')].find((e) => {
      const c = getComputedStyle(e), r = e.getBoundingClientRect();
      return c.position === 'fixed' && c.zIndex !== 'auto' && +c.zIndex > 0 && r.width >= vw - 1 && r.height >= vh - 1 && c.backgroundColor !== 'rgba(0, 0, 0, 0)' && !e.querySelector('[role=dialog]');
    });
    if (el) el.setAttribute('data-m', name);
    return !!el;
  }, name);
}
// Stacking order of every positioned layer on screen right now, by what it holds.
async function layers(label) {
  const l = await page.evaluate(() => [...document.querySelectorAll('body *')].map((e) => {
    const c = getComputedStyle(e);
    if (c.position === 'static' || c.zIndex === 'auto') return null;
    const r = e.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return null;
    const role = e.getAttribute('role') || (e.querySelector('[role=dialog]') ? 'holds dialog' : '');
    return { z: +c.zIndex, position: c.position, role, cls: [...e.classList].filter((x) => !x.includes(':')).slice(0, 4).join('.'), size: `${Math.round(r.width)}x${Math.round(r.height)}` };
  }).filter(Boolean));
  out._meta.layers ??= {};
  out._meta.layers[`${label}.${THEME}`] = l;
}
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
  await T('theme-toggle', { sel: 'button[aria-label*="theme" i], button[title*="theme" i]' }, ['default', 'hover', 'focus-visible'], { group: g, title: 'Theme toggle', desc: 'One of the few controls that keeps a focus outline (.tt-sidebar-theme:focus-visible).', sel: 'button[aria-label*=theme]' }, { noScroll: true });
  await T('sidebar-toggle', { sel: 'button.tt-sidebar-toggle' }, ['default', 'hover', 'focus-visible'], { group: g, title: 'Sidebar collapse button', desc: 'Chevron in the sidebar header; keeps a focus outline.', sel: 'button.tt-sidebar-toggle' }, { noScroll: true });
  await T('account-control', { sel: 'aside button:has(> span.truncate)' }, ['default', 'hover', 'focus-visible'], { group: g, title: 'Account control (signed out)', desc: 'Top of the sidebar: the app mark and "Sign in", where a signed-in account shows its avatar. Measured only; never pressed.', sel: '.tt-sidebar-account-control' }, { noScroll: true });
  await T('star-pill', { sel: 'a[href*="github.com"]' }, ['default', 'hover', 'focus-visible'], { group: g, title: 'GitHub star pill', sel: 'a[href*=github]' }, { noScroll: true });

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
  // Tooltip: hovering the busiest heatmap cell mounts a tooltip with the day and its tokens.
  if (await m('heatmap-cell').count()) {
    await reset(); await centre(m('heatmap-cell'));
    await markBefore();
    await m('heatmap-cell').first().hover(); await page.waitForTimeout(700);
    await mask(page);
    if (await tagNew('tooltip', /token/)) {
      await S('tooltip', m('tooltip'), ['open'], { group: G.feedback, title: 'Tooltip', desc: 'Hovering a heatmap cell: the day, its tokens and the timezone.', sel: 'node that appears on hovering the busiest heatmap cell' }, { noScroll: true, noReset: true });
      await layers('tooltip');
    } else log('  ! tooltip did not appear');
    await reset();
  }
  await T('segmented-2d', { role: 'button', text: '2D', up: 1 }, ['default'], { group: G.control, title: 'Small segmented control', desc: '2D / 3D switch on the heatmap.', sel: 'parent of button "2D"' });
  await T('table-tab-selected', { role: 'button', text: 'Daily Breakdown' }, ['default'], { group: G.table, title: 'Table tab, selected', sel: 'button "Daily Breakdown"' });
  await T('table-tab', { role: 'button', text: 'Project Usage' }, ['default', 'hover'], { group: G.table, title: 'Table tab', sel: 'button "Project Usage"' });
  await T('table-header', { sel: 'main table thead th', nth: 1 }, ['default'], { group: G.table, title: 'Table header cell', sel: 'thead th:nth(1)' });
  await T('table-cell', { sel: 'main table tbody td', nth: 1 }, ['default'], { group: G.table, title: 'Table cell (numeric)', sel: 'tbody td:nth(1)' });
  await T('table-row', { sel: 'main table tbody tr', nth: 1 }, ['default', 'hover'], { group: G.table, title: 'Table row', sel: 'tbody tr:nth(1)' });
  await T('cost-button', { sel: 'main button[aria-label="View cost breakdown"]' }, ['default', 'hover', 'focus-visible', 'pressed'], { group: d, title: 'Hero cost button', desc: 'The cost under the hero number is a button that opens the cost breakdown.', sel: 'button[aria-label="View cost breakdown"]' }, { noScroll: true });
  if (await m('cost-button').count()) {
    await m('cost-button').first().click(); await page.waitForTimeout(900);
    await page.evaluate(() => { const t = [...document.querySelectorAll('[role="tooltip"], .tooltip, [data-radix-popper-content-wrapper] > *')].find((e) => e.getBoundingClientRect().width > 0) || [...document.querySelectorAll('body *')].filter((e) => { const c = getComputedStyle(e); return (c.position === 'absolute' || c.position === 'fixed') && e.getBoundingClientRect().width > 80 && e.getBoundingClientRect().width < 420 && (e.innerText || '').length > 10 && parseFloat(c.zIndex) > 10; })[0]; if (t) t.setAttribute('data-m', 'tooltip'); });
    await page.evaluate(() => { const dlg = document.querySelector('[role="dialog"]'); if (dlg) dlg.setAttribute('data-m', 'dialog'); });
    await S('dialog', m('dialog'), ['open'], { group: G.feedback, title: 'Dialog (cost breakdown)', desc: 'Opened by the hero cost button, closed with Escape.', sel: '[role=dialog]' }, { noScroll: true, noReset: true });
    if (await tagScrim('dialog-scrim')) await S('dialog-scrim', m('dialog-scrim'), ['open'], { group: G.feedback, title: 'Dialog scrim', desc: 'The full-window layer behind the open dialog.', sel: 'fixed full-window layer behind [role=dialog]' }, { noScroll: true, noReset: true, crop: false });
    await layers('dialog');
    await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  }
  // Toast: Share opens the share card; its Copy button draws the card in this headless browser
  // and copies it to that browser's own clipboard (never the machine's), which raises a toast.
  // Nothing is uploaded: the card is drawn locally, and non-GET requests are blocked anyway.
  await reset();
  const share = q('main button').filter({ hasText: /^Share$/ }).first();
  if (await share.count()) {
    await share.click(); await page.waitForTimeout(1500); await mask(page);
    await page.evaluate(() => { const d = [...document.querySelectorAll('[role=dialog]')].find((e) => e.getBoundingClientRect().width > 0); if (d) d.setAttribute('data-m', 'share-dialog'); });
    await S('share-dialog', m('share-dialog'), ['open'], { group: G.feedback, title: 'Dialog (share card)', desc: 'Opened by Share; the image is drawn in the browser.', sel: '[role=dialog] after Share' }, { noScroll: true, noReset: true });
    const copy = m('share-dialog').locator('button').filter({ hasText: /^Copy/i }).first();
    if (await copy.count()) {
      await markBefore();
      await copy.click(); await page.waitForTimeout(1200);
      if (await tagNew('toast', /image|generat|copied|saved|couldn/)) {
        // The new node may be a wrapper; the toast is the first node inside it that paints a fill.
        await page.evaluate(() => { const w = document.querySelector('[data-m="toast"]'); const f = [w, ...w.querySelectorAll('*')].find((e) => getComputedStyle(e).backgroundColor !== 'rgba(0, 0, 0, 0)'); if (f && f !== w) { w.removeAttribute('data-m'); f.setAttribute('data-m', 'toast'); } });
        await S('toast', m('toast'), ['open'], { group: G.feedback, title: 'Toast', desc: 'Feedback after Copy on the share card.', sel: 'node that appears after Copy' }, { noScroll: true, noReset: true });
        await layers('toast');
      } else log('  ! toast did not appear');
    } else log('  ! share card has no Copy button');
    await page.keyboard.press('Escape'); await page.waitForTimeout(600);
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
  await layers('menu');
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  // Empty result: a search nothing matches. Typed, measured, cleared; nothing is sent.
  await reset();
  const search = q('main input[placeholder^="Search"]').first();
  await search.click(); await page.keyboard.type('zzqx-no-match', { delay: 10 }); await page.waitForTimeout(1200);
  await page.evaluate(() => { const t = [...document.querySelectorAll('main *')].find((e) => e.childElementCount === 0 && /^No matching sessions$/.test(e.textContent.trim())); if (!t) return; let n = t.parentElement; while (n && n.getBoundingClientRect().height < 60) n = n.parentElement; (n || t).setAttribute('data-m', 'empty-state'); t.setAttribute('data-m-t', '1'); });
  await S('empty-state', m('empty-state'), ['default'], { group: G.table, title: 'Empty state (no match)', desc: 'Sessions searched for text nothing matches: a title and a hint, no illustration.', sel: 'block around "No matching sessions"' }, { noScroll: true, noReset: true });
  await search.click(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(500);
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
    const badge = [...document.querySelectorAll('main *')].find((e) => e.tagName === 'SPAN' && /^(STALE|RE-AUTH|LIVE|CACHED)\b/i.test((e.innerText || '').trim()) && e.getBoundingClientRect().height < 26 && e.getBoundingClientRect().height > 10);
    if (badge) badge.setAttribute('data-m', 'status-badge');
  });
  await S('usage-row', m('usage-row'), ['default'], { group: g, title: 'Usage row', desc: 'Window label, a thin track with a pace tick, percent and time left.', sel: 'row around the first track' });
  await S('usage-track', m('usage-track'), ['default'], { group: g, title: 'Usage track', sel: 'first track' }, { pad: 4 });
  await S('usage-fill', m('usage-fill'), ['default'], { group: g, title: 'Usage fill', sel: 'its fill' }, { pad: 4 });
  await S('status-badge', m('status-badge'), ['default'], { group: G.feedback, title: 'Status badge', desc: 'CACHED / STALE / RE-AUTH pill beside a limit.', sel: 'pill reading CACHED, STALE or RE-AUTH' });
  // Its hover tooltip explains where the cached limits come from.
  if (await m('status-badge').count()) {
    await reset(); await centre(m('status-badge'));
    await m('status-badge').first().hover(); await page.waitForTimeout(500);
    await page.evaluate(() => { const t = [...document.querySelectorAll('main span')].find((e) => getComputedStyle(e).position === 'absolute' && /^Cached limits|^Real-time|^Sign-in expired/.test(e.textContent.trim()) && e.getBoundingClientRect().width > 0); if (t) t.setAttribute('data-m', 'hint-tooltip'); });
    if (await m('hint-tooltip').count()) await S('hint-tooltip', m('hint-tooltip'), ['open'], { group: G.feedback, title: 'Tooltip (hint)', desc: 'Hovering the CACHED pill on Limits.', sel: 'absolute span that appears on hovering the pill' }, { noScroll: true, noReset: true });
    await reset();
  }
  await T('code-block', { sel: 'main pre' }, ['default'], { group: g, title: 'Code block', sel: 'main pre' });
  // The warning surface Limits renders on its own: the amber notice under a limit.
  await page.evaluate(() => {
    const warn = [...document.querySelectorAll('main div')].find((e) => /border-amber-300\/60/.test(e.className) && e.getBoundingClientRect().width > 0);
    if (warn) warn.setAttribute('data-m', 'warning-notice');
  });
  if (await m('warning-notice').count()) await S('warning-notice', m('warning-notice'), ['default'], { group: G.feedback, title: 'Warning notice', desc: 'The amber notice under a limit (Copilot token usage).', sel: 'div with the amber border on Limits' });
  else log('  ! no warning notice');
  await T('icon-link', { sel: 'main a[href^="/settings"]' }, ['default', 'hover', 'focus-visible'], { group: G.control, title: 'Icon link', desc: 'The gear on Limits ("Display settings" is its accessible label): an icon-only link to Settings.', sel: 'main a[href^=/settings]' });
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
  // Network: an invalid proxy host is typed and checked with Test connection, read, then cleared;
  // the section is never saved (and a save is a POST, which the capture blocks).
  await toggle(q('main button').filter({ hasText: /^Network$/ }));
  await page.waitForTimeout(900);
  // The proxy fields show only for Manual. Choosing it stays in this page: saving it is a POST,
  // which the capture blocks, and System is chosen again before the page closes.
  await toggle(q('main button').filter({ hasText: /^Manual$/ }));
  await page.waitForTimeout(900);
  const field = q('main input[type="text"][placeholder]').filter({ visible: true }).first();
  if (await field.count()) {
    await field.evaluate((el) => el.setAttribute('data-m', 'text-field'));
    await S('text-field', m('text-field'), ['default', 'hover', 'focused'], { group: G.form, title: 'Text field', desc: 'Settings, Network: proxy host. Focus changes the border only.', sel: 'first text input in Network settings' }, { noScroll: true });
    const before = await field.inputValue();
    await field.click(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.type('http://proxy.example/path', { delay: 10 }); await page.keyboard.press('Tab');
    // Errors show on Test connection (or Save). With an invalid host the check fails before any request
    // is made; the test itself would be a POST, which the capture blocks. Save is never pressed.
    await page.locator('main button').filter({ hasText: /^Test connection$/ }).first().click({ timeout: 4000 }); await page.waitForTimeout(700);
    await page.evaluate(() => { const t = [...document.querySelectorAll('main *')].find((e) => e.childElementCount === 0 && /^Enter a host/.test(e.textContent.trim())); if (t) t.setAttribute('data-m', 'field-error'); });
    if (await m('field-error').count()) {
      await S('field-error', m('field-error'), ['default'], { group: G.form, title: 'Field error message', desc: 'Replaces the field hint when Test connection finds an invalid host.', sel: 'leaf "Enter a host ..."' }, { noScroll: true, noReset: true });
      await S('text-field-error', m('text-field'), ['error'], { group: G.form, title: 'Text field, invalid', sel: 'the same input holding an invalid host' }, { noScroll: true, noReset: true });
    } else log('  ! no field error appeared');
    await field.click(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace');
    if (before) await page.keyboard.type(before, { delay: 5 });
    await page.keyboard.press('Tab'); await page.waitForTimeout(400);
  } else log('  ! Network section has no text field');
  await toggle(q('main button').filter({ hasText: /^System$/ })).catch(() => {});
  await page.close();
}

// Sessions while its data is on the way: the sessions request is held for 20s.
async function sessionsLoading() {
  await newPage('sessionsLoading', { wait: 1800, routes: (p) => p.route('**/functions/tokentracker-sessions**', (r) => setTimeout(() => r.continue().catch(() => {}), 20000)) });
  await page.evaluate(() => { const t = [...document.querySelectorAll('main *')].find((e) => e.childElementCount <= 2 && /^Loading sessions/.test(e.textContent.trim())); if (!t) return; let n = t.parentElement; while (n && n.getBoundingClientRect().height < 40) n = n.parentElement; (n || t).setAttribute('data-m', 'loading-state'); });
  await S('loading-state', m('loading-state'), ['loading'], { group: G.table, title: 'Loading state', desc: 'Sessions with its request held back: one quiet line where the list goes.', sel: 'block around "Loading sessions…"' }, { noScroll: true, noReset: true });
  await page.close();
}

// Sessions when its request fails: the sessions request is aborted.
async function sessionsError() {
  await newPage('sessionsError', { wait: 3500, routes: (p) => p.route('**/functions/tokentracker-sessions**', (r) => r.abort()) });
  await page.evaluate(() => { const t = [...document.querySelectorAll('main *')].find((e) => e.childElementCount === 0 && /^Could not load sessions$/.test(e.textContent.trim())); if (!t) return; let n = t.parentElement; while (n && n.getBoundingClientRect().height < 60) n = n.parentElement; (n || t).setAttribute('data-m', 'error-state'); });
  await S('error-state', m('error-state'), ['error'], { group: G.table, title: 'Error state', desc: 'Sessions with its request aborted: a title, the reason and Try again.', sel: 'block around "Could not load sessions"' }, { noScroll: true, noReset: true });
  await T('retry-button', { role: 'button', text: 'Try again' }, ['default', 'hover', 'focus-visible'], { group: G.control, title: 'Retry button', desc: 'Measured, never pressed.', sel: 'button "Try again"' }, { noScroll: true });
  await page.close();
}

// Skills: row checkboxes and the bulk remove confirmation. A row is ticked to show the bulk bar,
// Remove opens the confirmation, Escape cancels it and the tick is cleared. The confirm button is
// hovered and focused only, never pressed, and every non-GET request is blocked regardless.
async function skills() {
  await newPage('skills', { wait: 4500 });
  const g = G.form;
  const box = q('main input[type="checkbox"]').first();
  if (!(await box.count())) { log('  ! no checkbox on Skills'); await page.close(); return; }
  await box.evaluate((el) => { el.setAttribute('data-m', 'checkbox'); const l = el.closest('label') || el.parentElement; l.setAttribute('data-m', 'checkbox-box'); });
  await T('badge', { text: 'Plugin' }, ['default'], { group: G.feedback, title: 'Badge', desc: 'The neutral pill on a skill row ("Plugin").', sel: 'leaf "Plugin"' });
  await box.evaluate((el) => { el.setAttribute('data-m', 'checkbox'); const l = el.closest('label') || el.parentElement; l.setAttribute('data-m', 'checkbox-box'); });
  await S('checkbox', m('checkbox'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Checkbox', desc: 'Selects a skill row for bulk actions.', sel: 'first input[type=checkbox] on Skills' }, { cropLoc: m('checkbox-box'), hoverLoc: m('checkbox-box') });
  await box.check(); await page.waitForTimeout(700); await mask(page);
  await S('checkbox', m('checkbox'), ['checked'], { group: g, title: 'Checkbox', sel: 'first input[type=checkbox] on Skills' }, { cropLoc: m('checkbox-box'), noReset: true });
  const bulk = q('main button').filter({ hasText: /^Remove$/ }).filter({ visible: true }).first();
  if (await bulk.count()) {
    await markBefore();
    await bulk.click(); await page.waitForTimeout(900); await mask(page);
    await page.evaluate(() => { const d = [...document.querySelectorAll('[role=dialog], [role=alertdialog]')].find((e) => e.getBoundingClientRect().width > 0); if (!d) return; d.setAttribute('data-m', 'confirm-dialog'); const b = [...d.querySelectorAll('button')].filter((x) => /^remove/i.test(x.innerText.trim())).pop(); if (b) b.setAttribute('data-m', 'danger-button'); const c = [...d.querySelectorAll('button')].find((x) => /^cancel/i.test(x.innerText.trim())); if (c) c.setAttribute('data-m', 'cancel-button'); });
    if (await m('confirm-dialog').count()) {
      await S('confirm-dialog', m('confirm-dialog'), ['open'], { group: G.feedback, title: 'Confirmation dialog (destructive)', desc: 'Bulk Remove on Skills asks first. Cancelled with Escape.', sel: '[role=dialog] after bulk Remove' }, { noScroll: true, noReset: true });
      // reset() between states moves the pointer off the button and blurs it, so focus-visible is not
      // read with the hover still applied. It only moves the pointer; the dialog stays open.
      await S('danger-button', m('danger-button'), ['default', 'hover', 'focus-visible'], { group: G.control, title: 'Danger button', desc: 'The confirm action in the remove dialog. Hovered and focused only, never pressed.', sel: 'last "Remove" button in the dialog' }, { noScroll: true });
      if (await m('cancel-button').count()) await S('cancel-button', m('cancel-button'), ['default', 'hover'], { group: G.control, title: 'Cancel button', sel: '"Cancel" in the dialog' }, { noScroll: true });
      if (await tagScrim('confirm-scrim')) await S('confirm-scrim', m('confirm-scrim'), ['open'], { group: G.feedback, title: 'Confirmation scrim', sel: 'fixed full-window layer behind the dialog' }, { noScroll: true, noReset: true, crop: false });
      await layers('confirm');
      await page.mouse.move(2, 2);
      await page.keyboard.press('Escape'); await page.waitForTimeout(700);
      if (await q('[role=dialog]').filter({ visible: true }).count()) throw new Error('confirmation did not close on Escape; stopping before anything else');
    } else log('  ! bulk Remove opened no dialog');
  } else log('  ! no bulk Remove button');
  await box.uncheck(); await page.waitForTimeout(400);
  // Danger notice: Refresh with every /functions/ request aborted (reads included) fails, and the
  // page reports it in its red error box. Nothing reaches the server.
  await page.route('**/functions/**', (r) => r.abort());
  const refresh = q('main button').filter({ hasText: /^Refresh$/ }).first();
  if (await refresh.count()) {
    await refresh.click(); await page.waitForTimeout(2500); await mask(page);
    await page.evaluate(() => { const e = [...document.querySelectorAll('main div')].find((x) => /border-red-200/.test(x.className) && x.getBoundingClientRect().width > 0); if (e) e.setAttribute('data-m', 'danger-notice'); });
    if (await m('danger-notice').count()) await S('danger-notice', m('danger-notice'), ['default'], { group: G.feedback, title: 'Error notice', desc: 'Skills reports a failed operation in a red box above the list (Refresh, with its requests aborted in the capture browser).', sel: 'div with the red border on Skills' }, { noScroll: true });
    else log('  ! no danger notice after Refresh');
  } else log('  ! no Refresh on Skills');
  await page.unroute('**/functions/**');
  await page.close();
}

// Leaderboard: only the avatar. Every name, handle and initial in the page is replaced first, photos
// are removed, and no screenshot of the page is kept; the crop is one initials avatar.
async function leaderboard() {
  // Photos never load: image requests to other hosts are aborted, so each avatar falls back to the
  // product's own initials circle (its onError path).
  await newPage('leaderboard', { wait: 8000, routes: (p) => p.route((u) => !u.hostname.startsWith('127.0.0.1'), (r) => (r.request().resourceType() === 'image' ? r.abort() : r.fallback())) });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  await page.evaluate(() => {
    const main = document.body;
    const w = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
    for (let n; (n = w.nextNode());) { const t = n.textContent.trim(); if (t && /[A-Za-z]/.test(t) && !n.parentElement.closest('aside, th, thead, button[role=tab], [role=tablist]')) n.textContent = n.parentElement.closest('[aria-hidden=true].rounded-full') ? 'A' : 'user'; }
    main.querySelectorAll('img').forEach((i) => { if (/rounded-full/.test(i.className)) { i.removeAttribute('src'); i.removeAttribute('srcset'); } });
    main.querySelectorAll('[title], [aria-label], [alt]').forEach((e) => { e.removeAttribute('title'); e.removeAttribute('aria-label'); e.removeAttribute('alt'); });
    const av = [...main.querySelectorAll('div[aria-hidden=true].rounded-full')].find((e) => e.getBoundingClientRect().width >= 16 && e.style.backgroundColor);
    if (av) av.setAttribute('data-m', 'avatar');
  });
  if (await m('avatar').count()) await S('avatar', m('avatar'), ['default'], { group: G.shell, title: 'Avatar', desc: 'The initials fallback: a circle in a colour picked from the person, white semibold initials, a 1px ring. A photo takes the same circle. Names and photos were removed from the page before reading.', sel: 'div[aria-hidden].rounded-full on Leaderboard' }, { pad: 6 });
  else log('  ! no initials avatar on Leaderboard');
  await page.close();
}

// Menu Bar & Widgets: switches (disabled until the Mac app is connected) and a disabled select.
async function widgets() {
  await newPage('widgets', { wait: 3500 });
  const g = G.control;
  await T('switch-on', { sel: 'main [role="switch"][aria-checked="true"]' }, ['disabled', 'hover'], { group: g, title: 'Switch, on', desc: 'Disabled here: the switches only work with the Mac app connected.', sel: '[role=switch][aria-checked=true]' });
  await T('primary-button', { role: 'a', text: 'Download Mac App' }, ['default', 'hover', 'focus-visible', 'pressed'], { group: g, title: 'Primary button', desc: '"Download Mac App": solid near-black in light, near-white in dark. Measured, never pressed.', sel: 'a "Download Mac App"' });
  await T('select-disabled', { sel: 'main button[role="combobox"][disabled]' }, ['disabled'], { group: G.form, title: 'Select, disabled', sel: 'button[role=combobox][disabled]' });
  await page.close();
}

// Pet: a URL field with its Add button disabled until something is typed.
async function pet() {
  await newPage('pet', { wait: 3500 });
  await T('switch-off', { sel: 'main [role="switch"][aria-checked="false"]' }, ['disabled', 'hover'], { group: G.control, title: 'Switch, off', sel: '[role=switch][aria-checked=false]' });
  await T('button-disabled', { sel: 'main button[type="submit"][disabled]' }, ['disabled'], { group: G.control, title: 'Button, disabled', desc: '"Add" before a pet URL is typed.', sel: 'button[type=submit][disabled]' });
  await page.close();
}

// Achievements: the one underlined text link in the app's own copy. Hovered and focused, never followed.
async function achievements() {
  await newPage('achievements', { wait: 3500 });
  await T('link', { role: 'a', text: 'Suggest it on GitHub' }, ['default', 'hover', 'focus-visible'], { group: G.control, title: 'Text link', desc: '"Suggest it on GitHub" under the badges: secondary text with a light underline. Never followed.', sel: 'a "Suggest it on GitHub"' });
  await page.close();
}

// Cloud (signed out): its own focus outline, 2px in the ink colour at a 3px offset.
async function cloud() {
  await newPage('cloud', { wait: 4000 });
  await page.evaluate(() => { const b = [...document.querySelectorAll('.tt-cloud-theme button, .tt-cloud-theme a')].find((e) => { const r = e.getBoundingClientRect(); return r.width > 40 && r.height > 20 && r.top > 0 && r.top < innerHeight; }); if (b) b.setAttribute('data-m', 'cloud-button'); });
  await S('cloud-button', m('cloud-button'), ['default', 'hover', 'focus-visible'], { group: G.control, title: 'Cloud page button', desc: 'First button on the signed-out Cloud page; the Cloud page draws focus outlines. Never pressed.', sel: 'first button in .tt-cloud-theme' }, { noScroll: true });
  await page.close();
}

async function status() {
  await newPage('status', { wait: 8000 });
  await T('status-row', { text: 'Claude', up: 3 }, ['default', 'hover'], { group: G.feedback, title: 'Service status row', sel: 'row around "Claude"' }, { noScroll: true });
  await page.close();
}

const PAGES = { dashboard, sessions, sessionsLoading, sessionsError, limits, settings, status, skills, widgets, pet, cloud, achievements, leaderboard };
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
  out._meta.source = 'TokenTracker v1.4.3 dashboard served by the local CLI at 127.0.0.1:7680, measured headless in Chromium (Playwright) at 1440x900, 2x';
}
save();
if (failures.length) {
  log('FAILED pages:', failures.join(', '), '-> partial readings only, in', OUT.replace(/\.json$/, '.partial.json'));
  process.exit(1);
}
log('done ->', OUT);
