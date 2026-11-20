// Measures excalidraw.com's public signed-out components in every state
// reachable without drawing, opening a file, saving, sharing, exporting,
// generating or signing in.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: welcome editor menus sidebar library dialogs dark mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// excalidraw.com is a single fixed-height canvas app: the welcome screen is
// the first-run state, a picked tool dismisses it. Everything else is chrome
// around the canvas: the floating toolbar Islands, the left properties
// sidebar, the hamburger dropdowns, the library panel and the local dialogs.
// The only presses are local UI toggles — tool buttons, the hamburger, menu
// chevrons, the theme radio, dropdown triggers, dialog close buttons and the
// '?' and Ctrl+/ shortcuts. Nothing is drawn on the canvas and no element is
// created; Open, Save to disk, Live collaboration, Share, every Export
// action, the AI menu items, Reset canvas and all Sign-up links are measured
// never pressed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, domFind, styleOf, crop, centre, RAW, REF, CROPS, UA, UA_MOBILE, pickTool, openMainMenu, setTheme, closeMenus, closeDialog } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { welcome: '/', editor: '/', menus: '/', sidebar: '/', library: '/', dialogs: '/', dark: '/', mobile: '/' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40 || !document.querySelector('.excalidraw');
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 9000, url = null } = {}) {
  current = key;
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const cleared = await open(page, url || BASE + URLS[key], { wait });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

// Fixed/sticky chrome with paint order: the z-index map of the page's bars and
// overlays. Recorded per page into _meta.chrome.
async function chrome(key) {
  const z = await page.evaluate(() => {
    const els = [...document.querySelectorAll('body *')];
    const seen = [];
    for (const el of els) {
      const cs = getComputedStyle(el);
      if (cs.position !== 'fixed' && cs.position !== 'sticky' && cs.position !== 'absolute') continue;
      const r = el.getBoundingClientRect();
      if (r.width < 20 || r.height < 10) continue;
      seen.push({ node: el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0].slice(0, 60), z: cs.zIndex, pos: cs.position, rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, text: (el.innerText || '').slice(0, 40).replace(/\n/g, '|') });
    }
    return seen.sort((a, b) => (parseInt(b.z) || 0) - (parseInt(a.z) || 0)).slice(0, 24);
  }).catch(() => []);
  out._meta.chrome ??= {};
  out._meta.chrome[key] = z;
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

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: BASE + URLS[current] }, meta);
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
    c.states[state] = { ...s, crop: file, via: opts.via, run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    const prev = c.states[state];
    if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
    else c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    if (!has) out.components[key].missing = true;
    else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
    return;
  }
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
      } else if (st === 'selected') {
        // A tool button's pressed-into state: one local click picks the tool.
        // Only ever used on tool buttons — nothing with an action.
        await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click()));
        await page.waitForTimeout(500);
        via = 'clicked the tool once (a local selection)';
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      if (st === 'focus-visible' && via === 'focus failed') {
        // Keyboard focus never reached the element, so a reading now would be the element at rest
        // saved as its focus. Record the miss instead (the builders list it as "focus could not be
        // captured"), and drop the crop an earlier run saved for this state.
        // An earlier run's real focus reading is kept, with the failed retry noted beside it.
        const prevSt = out.components[key].states[st];
        if (prevSt?.style && prevSt.via !== 'focus failed') {
          prevSt.rerunError = 'focus failed: keyboard focus did not reach the element';
          log('  !', key, st, 'focus failed; earlier reading kept');
        } else {
          const old = prevSt?.crop && path.resolve(REF, prevSt.crop);
          if (old && old.startsWith(CROPS + path.sep)) fs.rmSync(old, { force: true });
          out.components[key].states[st] = { skipped: 'focus failed: keyboard focus did not reach the element', via, run };
          log('  -', key, st, 'skipped: focus failed');
        }
      } else await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  // A listed state that failed its re-read kept the earlier evidence under
  // rerunError (and its own earlier `run`); the entry then republishes under
  // the earlier run's page/run/url and records the miss, so retained readings
  // never carry the new run's date.
  if (keep && list.some((st) => out.components[key].states[st]?.rerunError)) {
    Object.assign(out.components[key], keep);
    out.components[key].recaptureMissed = run;
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|try again|open|reset|live collaboration)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function sheetsFor(key) {
  const res = await page.evaluate(() => {
    const transitions = [];
    const walk = (rules) => {
      for (const r of rules) {
        if (r.cssRules && !r.selectorText) { walk(r.cssRules); continue; }
        if (!r.style) continue;
        const t = r.style.getPropertyValue('transition');
        const a = r.style.getPropertyValue('animation');
        if (t || a) transitions.push({ selector: (r.selectorText || '').slice(0, 160), transition: t, animation: a });
      }
    };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin */ } }
    return transitions;
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}

async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(9000);
    const v = await p.evaluate((s) => {
      const el = document.querySelector(s);
      if (!el) return null;
      const cs = getComputedStyle(el);
      return { transition: cs.transition, animation: cs.animation, scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
    }, sel).catch(() => null);
    out._meta.reducedMotion[key] = { selector: sel, reduce: v };
    await ctx.close();
  } catch (e) { out._meta.reducedMotion[key] = { selector: sel, error: String(e).slice(0, 120) }; }
}

const G = {
  welcome: 'Welcome screen (first run)', toolbar: 'Toolbar Islands', menu: 'Main menu and dropdowns',
  footer: 'Footer bar', sidebar: 'Properties sidebar', library: 'Library panel',
  dialogs: 'Dialogs', dark: 'Dark theme', mobile: 'Mobile (390 wide)',
};

// ---- openers: each returns a "via" string after making a local UI state ----

// The main menu: click the hamburger, wait for the radix dropdown panel.
async function openMenu() {
  const populated = () => page.waitForFunction(() => { const el = document.querySelector('.dropdown-menu.main-menu'); return el && el.getBoundingClientRect().height > 50; }, undefined, { timeout: 4000 }).then(() => true).catch(() => false);
  if (await populated()) return 'the main menu was already open';
  await openMainMenu(page);
  if (await populated()) return 'clicked the hamburger to open the main menu';
  return 'clicked the hamburger; the menu did not report open';
}

// The properties sidebar (.App-menu__left) appears once a shape tool is
// picked — a local selection, nothing drawn.
async function openProps() {
  const on = () => page.waitForFunction(() => { const el = document.querySelector('.App-menu__left'); return el && el.getBoundingClientRect().width > 60; }, undefined, { timeout: 4000 }).then(() => true).catch(() => false);
  if (await on()) return 'the properties sidebar was already open';
  await pickTool(page, 'Rectangle');
  if (await on()) return 'picked the Rectangle tool to summon the properties sidebar';
  return 'picked Rectangle; the sidebar did not appear';
}

// The library sidebar slides in on its own trigger (a local toggle).
async function openLibrary() {
  const on = () => page.waitForFunction(() => { const el = document.querySelector('.sidebar'); return el && el.getBoundingClientRect().width > 60; }, undefined, { timeout: 4000 }).then(() => true).catch(() => false);
  if (await on()) return 'the library panel was already open';
  const t = page.locator('button.sidebar-trigger__label-element').filter({ visible: true }).first();
  if (!(await t.count())) return 'no library trigger';
  await t.click({ timeout: 4000 }).catch(() => t.evaluate((el) => el.click()));
  if (await on()) return 'clicked the Library trigger to open the panel';
  return 'clicked the Library trigger; the panel did not report open';
}

async function closeLibrary() {
  const t = page.locator('button.sidebar-trigger__label-element').filter({ visible: true }).first();
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(500);
  if (await page.locator('.sidebar').filter({ visible: true }).count() && await t.count()) await t.click({ timeout: 3000 }).catch(() => {});
  await page.waitForTimeout(500);
}

// The export dialog: menu > "Export image…" opens it; nothing is exported.
async function openExport() {
  const on = () => page.waitForFunction(() => { const el = document.querySelector('.Dialog, [role="dialog"]'); return el && el.getBoundingClientRect().height > 80 && /Export image/.test(el.innerText || ''); }, undefined, { timeout: 5000 }).then(() => true).catch(() => false);
  if (await on()) return 'the export dialog was already open';
  await openMainMenu(page);
  const it = page.locator('.dropdown-menu.main-menu .dropdown-menu-item, .dropdown-menu.main-menu [class*="dropdown-menu-item"]').filter({ hasText: /^Export image/ }).first();
  if (!(await it.count())) { await closeMenus(page); return 'no Export image item'; }
  await it.click({ timeout: 4000 }).catch(() => it.evaluate((el) => el.click()));
  if (await on()) return 'menu > Export image… opened the dialog';
  await closeMenus(page);
  return 'clicked Export image; the dialog did not report open';
}

// The keyboard-shortcuts dialog opens on '?' (Shift+/).
async function openShortcuts() {
  const on = () => page.waitForFunction(() => [...document.querySelectorAll('.Dialog, [role="dialog"]')].some((el) => el.getBoundingClientRect().height > 80 && /Help|shortcut/i.test(el.innerText || '')), undefined, { timeout: 4000 }).then(() => true).catch(() => false);
  if (await on()) return 'the help dialog was already open';
  await page.keyboard.press('Shift+/').catch(() => {});
  await page.waitForTimeout(800);
  if (await on()) return 'pressed ? to open the help/shortcuts dialog';
  const hb = page.locator('button.help-icon, button[aria-label*="help" i]').filter({ visible: true }).first();
  if (await hb.count()) { await hb.click({ timeout: 4000 }).catch(() => hb.evaluate((el) => el.click())); }
  if (await on()) return 'clicked the "?" help button to open the help/shortcuts dialog';
  return 'pressed ? and clicked help; no dialog reported';
}

// The command palette opens on Ctrl+/ .
async function openCmdk() {
  const on = () => page.waitForFunction(() => { const el = document.querySelector('.command-palette-dialog, [class*="command-palette"]'); return el && el.getBoundingClientRect().height > 80; }, undefined, { timeout: 4000 }).then(() => true).catch(() => false);
  if (await on()) return 'the command palette was already open';
  await page.keyboard.press('Control+/');
  if (await on()) return 'pressed Ctrl+/ to open the command palette';
  return 'pressed Ctrl+/; the palette did not report open';
}

const menuItemLoc = (re) => q('.dropdown-menu.main-menu button.dropdown-menu-item').filter({ hasText: re }).first();

// ============================= pages =============================

async function welcome() {
  if (!(await newPage('welcome'))) return;
  await sheetsFor('welcome');
  await chrome('welcome');
  const g = G.welcome;
  await S('welcome-panel', q('.welcome-screen-center').filter({ visible: true }).first(), ['default'], { group: g, title: 'Welcome screen', desc: 'The first-run overlay centred on the blank canvas: the excalifont logo, a storage note and a vertical menu.', sel: '.welcome-screen-center' }, { noScroll: true });
  await S('welcome-logo', q('.welcome-screen-center__logo').filter({ visible: true }).first(), ['default'], { group: g, title: 'Welcome logo', desc: 'The hand-drawn "Excalidraw" wordmark in Excalifont.', sel: '.welcome-screen-center__logo' }, { noScroll: true });
  await S('welcome-heading', q('.welcome-screen-center h1, .welcome-screen-center h2, .welcome-screen-center [class*="heading"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Welcome heading', desc: '"Your drawings are saved in your browser\'s storage." — the privacy note under the logo.', sel: 'welcome heading' }, { noScroll: true });
  await S('welcome-menu', q('.welcome-screen-menu-item, .welcome-screen-center [class*="menu"]').filter({ visible: true }).first().locator('xpath=ancestor::*[contains(@class,"welcome")][1]'), ['default'], { group: g, title: 'Welcome menu', desc: 'The stacked menu inside the welcome card (Open, Help, Live collaboration…, Sign up).', sel: 'welcome menu column' }, { noScroll: true });
  await S('welcome-item', q('.welcome-screen-menu-item, .welcome-screen-center button, .welcome-screen-center a').filter({ hasText: /^Help/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Welcome menu item', desc: 'The "Help" welcome item — a plain row with an icon; measured, its action never used.', sel: 'welcome item Help' }, { noScroll: true });
  await S('welcome-item-signup', q('.welcome-screen-center a, .welcome-screen-center button').filter({ hasText: /Sign up/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Welcome Sign-up item', desc: 'The "Sign up" welcome item — links to Excalidraw+ signup; measured never followed.', sel: 'welcome item Sign up' }, { noScroll: true });
  save();
}

async function editor() {
  if (!(await newPage('editor'))) return;
  await sheetsFor('editor');
  await chrome('editor');
  const t = G.toolbar;
  await pickTool(page, 'Selection');
  await S('tool-island', q('.Island.App-toolbar').filter({ visible: true }).first(), ['default'], { group: t, title: 'Tool island', desc: 'The floating toolbar Island: a rounded shadowed card holding the tool buttons in a row.', sel: '.Island.App-toolbar' }, { noScroll: true });
  await S('menu-trigger', q('button.main-menu-trigger').filter({ visible: true }).first(), B4, { group: t, title: 'Hamburger trigger', desc: 'The main-menu icon button at the toolbar head.', sel: 'button.main-menu-trigger' }, { noScroll: true });
  await S('tool-lock', q('button.ToolIcon[aria-label^="Keep selected tool"]').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: t, title: 'Tool lock', desc: 'The "Keep selected tool active" lock checkbox at the toolbar head.', sel: 'toolbar lock toggle' }, { noScroll: true });
  await S('tool-selection', q('button[aria-label*="Selection"]').filter({ visible: true }).first(), [...B4, 'selected'], { group: t, title: 'Selection tool', desc: 'The Selection tool button — the active tool after entering the editor, so its selected state is the resting one.', sel: 'button[aria-label="Selection"]' }, { noScroll: true });
  await S('tool-rect', q('button[aria-label="Rectangle"]').filter({ visible: true }).first(), [...B4, 'selected'], { group: t, title: 'Rectangle tool', desc: 'A shape tool button; selecting it also summons the properties sidebar (a local selection, nothing drawn).', sel: 'button[aria-label=Rectangle]' }, { noScroll: true });
  await S('tool-draw', q('button[aria-label="Draw"], button[aria-label*="Freedraw"]').filter({ visible: true }).first(), B4, { group: t, title: 'Draw tool', desc: 'The freedraw pen tool button.', sel: 'button[aria-label=Draw]' }, { noScroll: true });
  await S('tool-text', q('button[aria-label="Text"]').filter({ visible: true }).first(), B4, { group: t, title: 'Text tool', desc: 'The text tool button.', sel: 'button[aria-label=Text]' }, { noScroll: true });
  await S('tool-eraser', q('button[aria-label="Eraser"]').filter({ visible: true }).first(), B4, { group: t, title: 'Eraser tool', desc: 'The eraser tool button.', sel: 'button[aria-label=Eraser]' }, { noScroll: true });
  await S('tool-more', q('button.App-toolbar__extra-tools-trigger').filter({ visible: true }).first(), [...B4, 'opened'], { group: t, title: 'Extra tools trigger', desc: 'The "Extra tools" overflow button at the toolbar tail — a local dropdown toggle.', sel: 'button.App-toolbar__extra-tools-trigger' }, { noScroll: true });
  await S('extra-menu', q('.dropdown-menu').filter({ hasText: /Insert image|Frame tool/ }).filter({ visible: true }).last(), ['default'], { group: G.menu, title: 'Extra tools menu', desc: 'The extra-tools dropdown (Insert image, Frame, Web Embed, Draw to shape, Laser, plus the AI entries); its items were measured never pressed.', sel: 'extra tools dropdown' }, { open: async () => {
    const on = () => page.waitForFunction(() => [...document.querySelectorAll('.dropdown-menu')].some((el) => el.getBoundingClientRect().height > 50 && /Insert image|Frame tool/.test(el.innerText || '')), undefined, { timeout: 3000 }).then(() => true).catch(() => false);
    if (await on()) return 'the extra-tools menu was already open';
    const x = q('button.App-toolbar__extra-tools-trigger').filter({ visible: true }).first();
    if (await x.count()) { await x.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(900); }
    return (await on()) ? 'clicked the extra-tools trigger' : 'clicked the extra-tools trigger; menu not reported';
  }, noScroll: true, noReset: true });
  await S('extra-menu-item', q('.dropdown-menu button.dropdown-menu-item').filter({ hasText: /^Lasso/ }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: G.menu, title: 'Extra menu item', desc: 'A row inside the extra-tools dropdown (Lasso selection); measured, never pressed.', sel: 'extra menu item' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(500);
  const f = G.footer;
  await S('undo-btn', q('button[aria-label="Undo"]').filter({ visible: true }).first(), ['default', 'focus-visible'], { group: f, title: 'Undo button', desc: 'The Undo footer button — disabled on a blank canvas, which is its resting reading.', sel: 'button[aria-label=Undo]' }, { noScroll: true });
  await S('redo-btn', q('button[aria-label="Redo"]').filter({ visible: true }).first(), ['default', 'focus-visible'], { group: f, title: 'Redo button', desc: 'The Redo footer button — disabled at rest like Undo.', sel: 'button[aria-label=Redo]' }, { noScroll: true });
  await S('zoom-btn', q('.zoom-button, .zoom-menu-trigger').filter({ visible: true }).first(), [...B4, 'opened'], { group: f, title: 'Zoom control', desc: 'The "− 100% +" zoom pill bottom-left; the opened state is its dropdown (Zen/grid/snap toggles), measured never set.', sel: '.zoom-button' }, { noScroll: true });
  await S('zoom-menu', q('.dropdown-menu').filter({ hasText: /Zoom|Zen|Grid/ }).filter({ visible: true }).last(), ['default'], { group: f, title: 'Zoom menu', desc: 'The zoom footer dropdown (Zoom in/out, Zen mode, Grid, snapping); opened by its own trigger, toggles never set.', sel: 'zoom dropdown' }, { open: async () => {
    const on = () => page.waitForFunction(() => [...document.querySelectorAll('.dropdown-menu')].some((el) => el.getBoundingClientRect().height > 50 && /Zen mode|Zoom in|Grid mode/.test(el.innerText || '')), undefined, { timeout: 3000 }).then(() => true).catch(() => false);
    if (await on()) return 'the zoom menu was already open';
    const z = q('.zoom-button, .zoom-menu-trigger').filter({ visible: true }).first();
    if (await z.count()) { await z.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(900); }
    return (await on()) ? 'clicked the zoom pill' : 'clicked the zoom pill; menu not reported';
  }, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('help-btn', q('button.help-icon, button[aria-label*="help" i]').filter({ visible: true }).first(), B4, { group: f, title: 'Help button', desc: 'The "?" help icon button bottom-right.', sel: 'button.help-icon' }, { noScroll: true });
  await S('collab-btn', q('button.collab-button').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: f, title: 'Share button', desc: 'The purple "Share"/collaboration button — opens a session dialog, never pressed.', sel: 'Share/collab button' }, { noScroll: true });
  await S('plus-btn', q('a, button').filter({ hasText: /Excalidraw\+|Try Excalidraw/i }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: f, title: 'Excalidraw+ promo', desc: 'The Excalidraw+ upsell action; measured never followed.', sel: 'Excalidraw+ promo' }, { noScroll: true });
  await S('lib-trigger', q('button.sidebar-trigger__label-element').filter({ visible: true }).first(), [...B4, 'opened'], { group: t, title: 'Library trigger', desc: 'The "Library" sidebar button top-right — a local panel toggle.', sel: 'button.sidebar-trigger__label-element' }, { noScroll: true });
  await closeLibrary();
  save();
}

async function menus() {
  if (!(await newPage('menus'))) return;
  await pickTool(page, 'Selection');
  const g = G.menu;
  await S('menu-panel', q('.dropdown-menu.main-menu').filter({ visible: true }).first(), ['default'], { group: g, title: 'Main menu', desc: 'The hamburger dropdown: Open / Save to disk / Export image… / Live collaboration / Command palette / Help, then Preferences, Theme, Language and the canvas-background swatches.', sel: '.dropdown-menu.main-menu' }, { open: openMenu, noScroll: true, noReset: true });
  await S('menu-item', menuItemLoc(/^Open/), ['default', 'hover', 'focus-visible'], { group: g, title: 'Menu item', desc: 'The "Open" menu row (icon + label); measured, never pressed.', sel: 'menu item Open' }, { noScroll: true, noReset: true });
  await S('menu-item-collab', menuItemLoc(/Live collaboration/), ['default', 'hover', 'focus-visible'], { group: g, title: 'Collaboration item', desc: '"Live collaboration…" — would start a session; measured never pressed.', sel: 'menu item Live collaboration' }, { noScroll: true, noReset: true });
  await S('menu-sep', q('.dropdown-menu.main-menu .Island > div:not([class])').filter({ visible: true }).first(), ['default'], { group: g, title: 'Menu separator', desc: 'The hairline divider between menu groups.', sel: 'menu separator' }, { noScroll: true, noReset: true });
  await S('theme-radios', q('.dropdown-menu.main-menu .RadioGroup').filter({ visible: true }).first(), ['default'], { group: g, title: 'Theme radio group', desc: 'The Light/Dark/System radio row inside the menu — the real theme control (Dark is set for the dark page, never left on).', sel: 'main menu .RadioGroup' }, { noScroll: true, noReset: true });
  await S('theme-choice', q('.dropdown-menu.main-menu .RadioGroup__choice[title*="Dark"]').first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Theme radio choice', desc: 'A choice in the Theme radio group (Dark); measured at rest.', sel: '.RadioGroup__choice Dark' }, { noScroll: true, noReset: true });
  await S('canvas-swatches', q('.dropdown-menu.main-menu .color-picker, .dropdown-menu.main-menu [class*="color-picker"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Canvas background picker', desc: 'The canvas-background colour row at the menu foot — a strip of preset swatches.', sel: 'menu canvas colour picker' }, { noScroll: true, noReset: true });
  await S('canvas-swatch', q('.dropdown-menu.main-menu .color-picker button, .dropdown-menu.main-menu [class*="color-picker"] button, .dropdown-menu.main-menu [class*="color-picker__button"]').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Canvas swatch', desc: 'One preset swatch in the canvas-background picker; measured, never set.', sel: 'canvas swatch' }, { noScroll: true, noReset: true });
  // Preferences submenu (radix submenu to the right of the panel)
  const pref = q('.dropdown-menu.main-menu .dropdown-menu-item').filter({ hasText: /^Preferences/ }).first();
  if (await pref.count()) { await pref.click({ timeout: 4000 }).catch(() => pref.evaluate((el) => el.click())); await page.waitForTimeout(1100); }
  await S('pref-submenu', q('.dropdown-menu').filter({ hasText: /Zen mode|View mode|Grid mode|Flip|Stats/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Preferences submenu', desc: 'The Preferences submenu (Zen mode, View mode, Grid mode, snapping, stats); toggles measured never set.', sel: 'preferences submenu' }, { noScroll: true, noReset: true });
  await S('pref-item', q('.dropdown-menu .dropdown-menu-item').filter({ hasText: /Zen mode/ }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Preference item', desc: 'A togglable submenu row (Zen mode); measured, never set.', sel: 'preferences item Zen mode' }, { open: async () => {
    // S() resets the pointer after every component, which closes the submenu:
    // re-open the menu and Preferences each time this spec runs.
    const on = () => page.waitForFunction(() => [...document.querySelectorAll('.dropdown-menu')].some((el) => !el.classList.contains('main-menu') && el.getBoundingClientRect().height > 50 && /Zen mode/.test(el.innerText || '')), undefined, { timeout: 3000 }).then(() => true).catch(() => false);
    if (await on()) return 'the preferences submenu was already open';
    await openMenu();
    const it = q('.dropdown-menu.main-menu .dropdown-menu-item').filter({ hasText: /^Preferences/ }).first();
    if (await it.count()) { await it.click({ timeout: 4000 }).catch(() => it.evaluate((el) => el.click())); await page.waitForTimeout(1100); }
    return (await on()) ? 're-opened the preferences submenu' : 'clicked Preferences; submenu not reported';
  }, noScroll: true, noReset: true });
  await closeMenus(page);
  save();
}

async function sidebar() {
  if (!(await newPage('sidebar'))) return;
  const g = G.sidebar;
  await openProps();
  await S('props-panel', q('.App-menu__left').filter({ visible: true }).first(), ['default'], { group: g, title: 'Properties panel', desc: 'The left sidebar summoned by picking a shape tool: Stroke and Background pickers, Stroke width/style, Sloppiness, Edges, Opacity, Layers.', sel: '.App-menu__left' }, { noScroll: true });
  await S('prop-label', q('.App-menu__left legend, .App-menu__left label, .App-menu__left [class*="title"]').filter({ hasText: /^Stroke width/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Property label', desc: 'A section label ("Stroke") inside the properties panel.', sel: 'props label Stroke' }, { noScroll: true });
  await S('stroke-picker', q('.App-menu__left .color-picker, .App-menu__left [class*="color-picker"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Stroke colour picker', desc: 'The Stroke top-picks row: five preset swatches plus the custom picker button.', sel: 'stroke colour picker' }, { noScroll: true });
  await S('stroke-swatch', q('.App-menu__left .color-picker button, .App-menu__left [class*="color-picker"] button, .App-menu__left [class*="color-picker__button"]').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Stroke swatch', desc: 'A preset colour swatch in the Stroke picker — the selected one carries the accent ring.', sel: 'stroke swatch' }, { noScroll: true });
  await S('stroke-width-group', q('.App-menu__left fieldset').filter({ hasText: /^Stroke width/ }).first(), ['default'], { group: g, title: 'Stroke width radio', desc: 'The Stroke-width segmented control (thin/bold/extra-bold icons).', sel: 'stroke width RadioGroup' }, { noScroll: true });
  await S('stroke-choice', q('.App-menu__left fieldset label.active').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Stroke width choice', desc: 'A choice inside a properties RadioGroup — the active choice paints the accent background.', sel: 'stroke RadioGroup choice' }, { noScroll: true });
  await S('opacity-row', q('.App-menu__left label.control-label').filter({ hasText: /Opacity/ }).first(), ['default'], { group: g, title: 'Opacity control', desc: 'The Opacity row: a range slider and a numeric input.', sel: 'opacity control' }, { noScroll: true });
  await S('opacity-slider', q('.App-menu__left input[type="range"], .App-menu__left [role="slider"]').filter({ visible: true }).first(), ['default', 'focus-visible'], { group: g, title: 'Opacity slider', desc: 'The range input inside the Opacity control.', sel: 'opacity input[type=range]' }, { noScroll: true });
  await S('layers-row', q('.App-menu__left fieldset').filter({ hasText: /^Layers/ }).first(), ['default'], { group: g, title: 'Layers row', desc: 'The Layers section: bring-forward/send-backward icon buttons.', sel: 'layers section' }, { noScroll: true });
  await S('layer-btn', q('.App-menu__left button.zIndexButton').filter({ visible: true }).first(), B4, { group: g, title: 'Layer action', desc: 'A z-order icon button in the Layers row.', sel: 'layer action button' }, { noScroll: true });
  save();
}

async function library() {
  if (!(await newPage('library'))) return;
  const g = G.library;
  await pickTool(page, 'Selection');
  await S('lib-panel', q('.sidebar').filter({ visible: true }).first(), ['default'], { group: g, title: 'Library panel', desc: 'The right sidebar holding the shape library: a search field, the empty state and "Browse libraries" — nothing was installed.', sel: '.sidebar' }, { open: openLibrary, noScroll: true, noReset: true });
  await S('lib-search', q('.sidebar input').filter({ visible: true }).first(), ['default', 'focus-visible'], { group: g, title: 'Library search', desc: 'The search field revealed by the first tab button at the library head; focused, never submitted.', sel: 'library search input' }, { open: async () => {
    const on = () => page.waitForSelector('.sidebar input', { state: 'visible', timeout: 2500 }).then(() => true).catch(() => false);
    if (await on()) return 'the library search field was already visible';
    // the magnifier tab at the panel head toggles the search field — a local
    // tab switch, never a query submission
    const tab = q('.sidebar button.sidebar-tab-trigger').filter({ visible: true }).first();
    if (await tab.count()) { await tab.click({ timeout: 4000 }).catch(() => tab.evaluate((el) => el.click())); await page.waitForTimeout(900); }
    return (await on()) ? 'toggled the search tab to reveal the field' : 'clicked the search tab; no field reported';
  }, noScroll: true, noReset: true });
  // The empty-state text only: a bare `.sidebar div` matching /libraries/ caught the
  // "Browse libraries" wrapper on 2026-11-13 (README known gaps).
  await S('lib-empty', q('.sidebar [class*="no-items" i], .sidebar [class*="empty" i]').filter({ hasText: /no items|empty/i }).filter({ hasNotText: /browse libraries/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Library empty state', desc: 'The "no shapes yet" empty-state text inside the panel.', sel: 'library empty state' }, { noScroll: true, noReset: true });
  await S('lib-browse-btn', q('.sidebar button, .sidebar a').filter({ hasText: /Browse|libraries/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Browse libraries button', desc: 'The "Browse libraries" action — opens the community libraries list; measured never followed.', sel: 'library Browse button' }, { noScroll: true, noReset: true });
  await S('lib-overflow', q('.sidebar button[aria-label*="more" i], .sidebar button[aria-label*="menu" i], .sidebar button.dropdown-menu-button').filter({ visible: true }).first(), B4, { group: g, title: 'Library overflow', desc: 'The "…" overflow menu button at the library head (Reset library, import); measured never pressed.', sel: 'library overflow button' }, { noScroll: true, noReset: true });
  await closeLibrary();
  save();
}

async function dialogs() {
  if (!(await newPage('dialogs'))) return;
  const g = G.dialogs;
  await pickTool(page, 'Selection');
  await S('export-dialog', q('.Modal .Island').filter({ hasText: /Export image/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Export dialog', desc: 'The "Export image" modal: checkerboard preview, Background/Dark-mode/Embed switches, the 1×/2×/3× scale radio and PNG/SVG/copy actions — none pressed.', sel: '.Dialog Export image' }, { open: openExport, noScroll: true, noReset: true });
  await S('export-preview', q('.ImageExportModal__preview').filter({ visible: true }).first(), ['default'], { group: g, title: 'Export preview', desc: 'The checkerboard transparency preview pane inside the export dialog.', sel: 'export preview pane' }, { noScroll: true, noReset: true });
  await S('export-switch', q('.Dialog .Switch, .Dialog [class*="Switch" i], .Dialog button[role="switch"], .Dialog input[type="checkbox"]').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Export switch', desc: 'A labelled toggle in the dialog (Background/Dark mode/Embed scene); measured never flipped.', sel: 'export Switch' }, { noScroll: true, noReset: true });
  await S('export-scale', q('.Dialog .RadioGroup').filter({ visible: true }).first(), ['default'], { group: g, title: 'Scale radio', desc: 'The 1×/2×/3× scale segmented control.', sel: 'export scale RadioGroup' }, { noScroll: true, noReset: true });
  await S('export-png', q('.Dialog button, .Dialog a').filter({ hasText: /^\s*PNG\s*$/ }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'PNG button', desc: 'The accent "PNG" export action; measured never pressed (no file was produced).', sel: 'export PNG' }, { noScroll: true, noReset: true });
  await S('export-svg', q('.Dialog button, .Dialog a').filter({ hasText: /^\s*SVG\s*$/ }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'SVG button', desc: 'The "SVG" export action beside PNG; measured never pressed.', sel: 'export SVG' }, { noScroll: true, noReset: true });
  await S('export-copy', q('.Modal button.ExcButton, .Modal button').filter({ hasText: /Copy/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Copy-to-clipboard button', desc: 'The "Copy to clipboard" ExcButton in the export dialog (a filled primary variant); measured never pressed.', sel: '.ExcButton Copy to clipboard' }, { noScroll: true, noReset: true });
  await closeDialog(page);
  await S('shortcuts-dialog', q('.Modal.Dialog.HelpDialog .Modal__content, .Modal.Dialog.HelpDialog .Dialog__content').filter({ visible: true }).first().filter({ visible: true }).first(), ['default'], { group: g, title: 'Shortcuts dialog', desc: 'The keyboard-shortcuts sheet opened by ? — a column of actions and their keycaps.', sel: 'shortcuts dialog' }, { open: openShortcuts, noScroll: true, noReset: true });
  await S('shortcut-row', q('.HelpDialog__island--tools .HelpDialog__island-content, .Dialog [class*="shortcut" i] div').filter({ hasText: /Hand|Select|Undo/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Shortcut row', desc: 'A row in the shortcuts sheet (action name + keycap).', sel: 'shortcut row' }, { noScroll: true, noReset: true });
  await S('keycap', q('.Dialog kbd, .HelpDialog__island-content [class*="key" i], .HelpDialog__island-content .dropdown-menu-item__shortcut').filter({ visible: true }).first(), ['default'], { group: g, title: 'Keycap', desc: 'A rendered key chip (e.g. "Ctrl") inside the shortcuts sheet.', sel: 'kbd keycap' }, { noScroll: true, noReset: true });
  await closeDialog(page);
  await S('cmdk-dialog', q('.command-palette-dialog .Island').filter({ visible: true }).first(), ['default'], { group: g, title: 'Command palette', desc: 'The Ctrl+/ launcher: a search field over grouped commands (App / Editor); nothing was invoked.', sel: '.command-palette-dialog' }, { open: openCmdk, noScroll: true, noReset: true });
  await S('cmdk-input', q('.command-palette-dialog input, [class*="command-palette"] input').filter({ visible: true }).first(), ['default', 'focus-visible'], { group: g, title: 'Palette input', desc: 'The search field at the palette head.', sel: 'palette input' }, { noScroll: true, noReset: true });
  await S('cmdk-item', q('.command-palette-dialog .command-item').filter({ hasText: /Dark mode|Library|Undo/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Palette item', desc: 'A command row inside the palette (with its shortcut hint); measured, never invoked.', sel: 'palette item' }, { noScroll: true, noReset: true });
  await closeDialog(page);
  save();
}

async function dark() {
  if (!(await newPage('dark'))) return;
  const g = G.dark;
  await pickTool(page, 'Selection');
  await setTheme(page, 'dark');
  await closeMenus(page);
  await S('d-island', q('.Island.App-toolbar').filter({ visible: true }).first(), ['default'], { group: g, title: 'Tool island (dark)', desc: 'The same toolbar Island in dark theme — near-black surface, light icons.', sel: '.Island.App-toolbar (theme--dark)' }, { noScroll: true });
  await S('d-tool', q('button[aria-label="Rectangle"]').filter({ visible: true }).first(), B4, { group: g, title: 'Tool button (dark)', desc: 'A tool button in dark theme.', sel: 'tool button (dark)' }, { noScroll: true });
  await S('d-menu-panel', q('.dropdown-menu.main-menu').filter({ visible: true }).first(), ['default'], { group: g, title: 'Main menu (dark)', desc: 'The hamburger dropdown in dark theme.', sel: '.dropdown-menu.main-menu (dark)' }, { open: openMenu, noScroll: true, noReset: true });
  await S('d-menu-item', menuItemLoc(/^Open/), ['default', 'hover'], { group: g, title: 'Menu item (dark)', desc: 'A menu row in dark theme.', sel: 'menu item (dark)' }, { noScroll: true, noReset: true });
  await closeMenus(page);
  await openProps();
  await S('d-props', q('.App-menu__left').filter({ visible: true }).first(), ['default'], { group: g, title: 'Properties panel (dark)', desc: 'The properties sidebar in dark theme.', sel: '.App-menu__left (dark)' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-welcome', q('.welcome-screen-center').filter({ visible: true }).first(), ['default'], { group: g, title: 'Welcome screen (mobile)', desc: 'The first-run overlay at 390 wide: logo, note and menu fill the sheet.', sel: '.welcome-screen-center (mobile)' }, { noScroll: true });
  await S('m-welcome-item', q('.welcome-screen-center button, .welcome-screen-center a').filter({ hasText: /^Help/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Welcome item (mobile)', desc: 'A welcome menu row on the phone layout.', sel: 'welcome item (mobile)' }, { noScroll: true });
  await pickTool(page, 'Selection');
  await S('m-toolbar', q('.mobile-toolbar, .Island.App-toolbar').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile toolbar', desc: 'The bottom tool bar at 390 wide: a single row of tools plus the overflow trigger.', sel: '.mobile-toolbar' }, { noScroll: true });
  await S('m-tool', q('button[aria-label="Selection"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Tool button (mobile)', desc: 'A tool button in the phone toolbar.', sel: 'tool button (mobile)' }, { noScroll: true });
  await S('m-extra-trigger', q('button.App-toolbar__extra-tools-trigger, button.dropdown-menu-button').filter({ visible: true }).first(), ['default'], { group: g, title: 'Extra tools (mobile)', desc: 'The overflow trigger at the phone toolbar tail.', sel: 'extra trigger (mobile)' }, { noScroll: true });
  await S('m-menu-trigger', q('button.main-menu-trigger').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hamburger (mobile)', desc: 'The floating menu button top-left.', sel: 'menu trigger (mobile)' }, { noScroll: true });
  await S('m-lib-trigger', q('button.sidebar-trigger__label-element').filter({ visible: true }).first(), ['default'], { group: g, title: 'Library trigger (mobile)', desc: 'The floating library button top-right.', sel: 'lib trigger (mobile)' }, { noScroll: true });
  await pickTool(page, 'Rectangle');
  await S('m-shape-actions', q('.compact-shape-actions, .Island.compact-shape-actions').filter({ visible: true }).first(), ['default'], { group: g, title: 'Shape actions (mobile)', desc: 'The compact-shape-actions bar that appears above the toolbar when a shape tool is picked on the phone.', sel: '.compact-shape-actions' }, { noScroll: true });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 desktop (mobile group 390 x 844); light and dark themes; the editor is one fixed-height canvas app — nothing scrolls';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { welcome, editor, menus, sidebar, library, dialogs, dark, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  if (!pages.length || pages.includes('editor')) await reducedMotion('editor', 'button[aria-label="Rectangle"]');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length && finishedPages.has(c.page) && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
