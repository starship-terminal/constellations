// Measures kitchenstories.com's public components in every state reachable
// without signing in, checking out or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home recipes recipe stories search plus mobile.
// Writes raw/components-computed.json and crops. The consentmanager overlay
// is hidden, never answered. Search is typed into and cleared, never
// submitted. Cart, checkout, rating submit and profile are never followed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, PAGES, launch, patch, open, closePromo, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: BASE + '/',
  recipes: BASE + '/rezepte',
  recipe: BASE + '/huhnersuppe-mit-zitrone-a-a/192140',
  stories: BASE + '/stories',
  search: BASE + '/?s=pasta',
  plus: PAGES + '/de/plus',
  mobile: BASE + '/',
};
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the client challenge gates this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null } = {}) {
  current = key;
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'de-DE' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'de-DE' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const opened = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (!opened || await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      const r = el.getBoundingClientRect();
      if (r.width < 40 || r.height < 10) continue;
      seen.push({ node: el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0].slice(0, 60), z: cs.zIndex, pos: cs.position, rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, text: (el.innerText || '').slice(0, 40).replace(/\n/g, '|') });
    }
    return seen.sort((a, b) => (parseInt(b.z) || 0) - (parseInt(a.z) || 0)).slice(0, 20);
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
  Object.assign(c, { page: current, run, url: URLS[current] && (URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current]) }, meta);
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
    // A failed re-read must not erase an earlier successful one: keep the
    // saved style and record the failed attempt beside it.
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
    log('  ! missing', key, has && !opts.dropPrior ? '(earlier states kept)' : '');
    // Keep earlier evidence under its own provenance: the states stay but the
    // entry keeps its original page/run/url and records the miss, so a re-run
    // never republishes old readings under a new date. opts.dropPrior is for
    // entries whose saved states were read off the wrong element — that is not
    // evidence to keep, so the miss lands as a plain gap.
    if (opts.dropPrior) {
      out.components[key].states = {};
      out.components[key].missing = true;
      delete out.components[key].recaptureMissed;
    } else if (!has) out.components[key].missing = true;
    else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
    return;
  }
  // The component was found this run: any earlier miss note is stale.
  delete out.components[key].recaptureMissed;
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
        const fld = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again)$/i;
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

// Whether the page paints a different transition under prefers-reduced-motion:
// the same component re-read in a context with reduce on.
async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'de-DE', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(7000);
    await closePromo(p);
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
  shell: 'Navigation and site chrome', home: 'Home page', recipe: 'Recipe page',
  index: 'Recipe index', stories: 'Stories', search: 'Search', plus: 'Plus marketing',
  mobile: 'Mobile (390 wide)', footer: 'Footer', overlay: 'Menus and overlays',
};

const FIELD = ['default', 'focused', 'filled'];

// Opens the desktop "More" dropdown: a local UI toggle inside .megaMenu that
// drops the panel holding the overflow sections. Its links are never followed.
async function openMoreMenu() {
  const populated = (ms) => page.waitForFunction(
    () => [...document.querySelectorAll('.megaMenu *')].some((el) => { const r = el.getBoundingClientRect(); return r.height > 80 && /Member Exclusives|For You|Sports/.test(el.innerText || ''); }),
    undefined, { timeout: ms }).then(() => true).catch(() => false);
  if (await populated(300)) return 'the More panel was already open';
  const more = page.locator('.megaMenu button').filter({ hasText: /^\s*More\s*$/ }).filter({ visible: true }).first();
  if (!(await more.count())) return 'no More toggle';
  for (let i = 0; i < 3; i++) {
    await more.click({ timeout: 4000 }).catch(() => more.evaluate((el) => el.click()));
    if (await populated(4000)) return 'clicked "More" to open the overflow panel';
    await page.waitForTimeout(600);
  }
  return 'clicked "More"; the panel did not report open';
}

// Opens the mobile/desktop side panel: the hamburger (aria-label "Open
// Sidepanel") toggles nav#sidepanel.new-sidepanel-menu — a local UI toggle
// whose links are never followed.
async function openSidepanel() {
  const ok = (ms) => page.waitForFunction(
    () => { const el = document.querySelector('.new-sidepanel-menu.visible, nav#sidepanel:not(.hidden)'); return el && el.getBoundingClientRect().height > 100; },
    undefined, { timeout: ms }).then(() => true).catch(() => false);
  if (await ok(300)) return 'the side panel was already open';
  const ham = page.locator('button[aria-label*="Open" i]').filter({ visible: true }).first();
  const h2 = page.locator('nav button').filter({ visible: true }).first();
  const t = (await ham.count()) ? ham : h2;
  if (!(await t.count())) return 'no sidepanel toggle';
  for (let i = 0; i < 3; i++) {
    await t.click({ timeout: 4000 }).catch(() => t.evaluate((el) => el.click()));
    if (await ok(4000)) return 'clicked the hamburger to open the side panel';
    await page.waitForTimeout(600);
  }
  return 'clicked the hamburger; the panel did not report open';
}

async function mark(sel, attr, pick) {
  await page.evaluate(({ sel, attr, pick }) => {
    document.querySelectorAll(`[${attr}]`).forEach((n) => n.removeAttribute(attr));
    const els = [...document.querySelectorAll(sel)].filter((el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return r.width > 8 && r.height > 8 && cs.visibility !== 'hidden' && +cs.opacity > 0;
    });
    const el = typeof pick === 'number' ? els[pick] : (pick === 'widest' ? els.sort((a, b) => b.getBoundingClientRect().width - a.getBoundingClientRect().width)[0] : els[0]);
    if (el) el.setAttribute(attr, '1');
  }, { sel, attr, pick: pick ?? 0 }).catch(() => {});
}

async function home() {
  if (!(await newPage('home', { wait: 4000 }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await mark('header.site-header, header', 'data-m-header', 0);
  await S('header', q('[data-m-header]'), ['default'], { group: g, title: 'Site header', desc: 'The sticky magazine header: wordmark, primary links (Rezepte, Artikel, App, Plus, Partner) and the search and menu buttons.', sel: 'header' }, { noScroll: true });
  await S('nav-link', q('header a, .site-header a').filter({ hasText: /^Rezepte$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Primary nav link', desc: 'The "Rezepte" link in the header; measured, never followed.', sel: 'header a Rezepte' }, { noScroll: true });
  await S('nav-plus', q('header a').filter({ hasText: /^Plus$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plus link', desc: 'The "Plus" marketing link; measured, never followed. Checkout sits behind it.', sel: 'header a Plus' }, { noScroll: true });
  await mark('header a[href="/"], .site-header a[rel="home"], a.custom-logo-link, header .site-title a', 'data-m-logo', 'widest');
  await S('wordmark', q('[data-m-logo]'), ['default', 'hover'], { group: g, title: 'Wordmark', desc: 'The Kitchen Stories wordmark linking home.', sel: 'header home link' }, { noScroll: true });
  await S('menu-toggle', q('button.desktop-menu-toggle').first(), [...B4, 'opened'], { group: g, title: 'Menu toggle', desc: 'The desktop menu button. Measured before search opens, because opening search slides the header. The opened state is a local toggle; its links are never followed.', sel: 'button.desktop-menu-toggle' }, { noScroll: true });
  await S('search-open', q('button').filter({ hasText: /Suche öffnen/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Open search', desc: 'The "Suche öffnen" button. Measured at rest; the field itself is measured after it opens.', sel: 'button Suche öffnen' }, { noScroll: true });
  await page.getByRole('button', { name: /Suche öffnen/ }).first().click().catch(() => {});
  await page.waitForTimeout(500);
  await S('search-field', q('input[name="s"], input[type="search"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Search field', desc: 'The header search field (placeholder "Suche …"). Focused and typed into, then cleared. Enter is never pressed.', sel: 'input[name=s]' }, { fillText: 'pasta', noScroll: true });
  await S('search-submit', q('button.search-submit, input.search-submit, button[aria-label="Suche"]').filter({ visible: true }).first(), B4, { group: g, title: 'Search submit', desc: 'The search submit control. Measured, never pressed.', sel: 'button.search-submit' }, { noScroll: true });
  await page.keyboard.press('Escape').catch(() => {});
  const h = G.home;
  await S('home-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Home title', desc: 'The home page heading.', sel: 'h1' }, { noScroll: true });
  await mark('article .entry-title a, article h2 a, .entry-title a', 'data-m-card-title', 0);
  await S('recipe-card', q('[data-m-card-title]').locator('xpath=ancestor::article[1]'), ['default'], { group: h, title: 'Recipe card', desc: 'A home recipe card: thumbnail, time, category, title and author.', sel: 'article' });
  await S('card-title', q('[data-m-card-title]'), ['default', 'hover'], { group: h, title: 'Card title', desc: 'A recipe card title link. Measured, never followed.', sel: 'article title a' });
  await S('card-meta', q('article .entry-meta, article .cat-links, .cat-links a').filter({ visible: true }).first(), ['default'], { group: h, title: 'Card meta', desc: 'Category or time meta on a recipe card.', sel: 'article meta' });
  await S('author-link', q('a.url.fn, a[rel="author"], .author a').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Author link', desc: 'An author byline link. Measured, never followed.', sel: 'a[rel=author]' });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: f, title: 'Footer', desc: 'The site footer: follow links, legal links and the published hello@kitchenstories.de contact.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: /Impressum|Datenschutz|Kontakt/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A legal footer link. Measured, never followed.', sel: 'footer a' });
  save();
}

async function recipes() {
  if (!(await newPage('recipes', { wait: 4000 }))) return;
  await sheetsFor('recipes');
  const g = G.index;
  await S('index-title', q('.page-title, .archive-title, h1.page-title, .archive-description, header.page-header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Index title', desc: 'The recipes index title, when the archive paints one. The index is a card grid; it has no h1.', sel: '.page-title' }, { noScroll: true });
  await mark('article', 'data-m-index-card', 0);
  await S('index-card', q('[data-m-index-card]'), ['default'], { group: g, title: 'Index card', desc: 'A recipe card on the /rezepte index.', sel: 'article' });
  await S('pagination', q('.nav-links, nav.navigation, .pagination').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pagination', desc: 'The archive pagination. Measured, never followed.', sel: '.nav-links' });
  await S('page-link', q('.nav-links a, .pagination a').filter({ hasText: /^2$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Page link', desc: 'A pagination page link. Measured, never followed.', sel: 'pagination a' });
  save();
}

async function recipe() {
  if (!(await newPage('recipe', { wait: 5000 }))) return;
  await sheetsFor('recipe');
  const g = G.recipe;
  await S('recipe-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Recipe title', desc: 'The recipe headline.', sel: 'h1' }, { noScroll: true });
  await S('recipe-card-block', q('.wprm-recipe').filter({ visible: true }).first(), ['default'], { group: g, title: 'Recipe card block', desc: 'The WP Recipe Maker card: image, name, rating, ingredients, utensils, nutrition and steps. The cart and rating submit inside it were not pressed.', sel: '.wprm-recipe' });
  await S('recipe-name', q('.wprm-recipe-name').filter({ visible: true }).first(), ['default'], { group: g, title: 'Recipe name', desc: 'The recipe name inside the card.', sel: '.wprm-recipe-name' });
  await S('rating', q('.wprm-recipe-rating').filter({ visible: true }).first(), ['default'], { group: g, title: 'Rating', desc: 'The star rating. Measured at rest. The rating form was not submitted.', sel: '.wprm-recipe-rating' });
  await S('ingredient-heading', q('h3.wprm-recipe-ingredients-header').first(), ['default'], { group: g, title: 'Ingredients heading', desc: 'The "Zutaten" heading inside the recipe card.', sel: 'h3.wprm-recipe-ingredients-header' });
  await S('ingredient', q('.wprm-recipe-ingredient').filter({ visible: true }).first(), ['default'], { group: g, title: 'Ingredient row', desc: 'One ingredient row.', sel: '.wprm-recipe-ingredient' });
  await S('instruction-heading', q('h3.wprm-recipe-instructions-header').first(), ['default'], { group: g, title: 'Steps heading', desc: 'The "Zubereitung" heading inside the recipe card.', sel: 'h3.wprm-recipe-instructions-header' });
  await S('instruction', q('.wprm-recipe-instruction').filter({ visible: true }).first(), ['default'], { group: g, title: 'Step', desc: 'One preparation step.', sel: '.wprm-recipe-instruction' });
  await S('step-nav', q('button, a').filter({ hasText: /Weiter/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Next step', desc: 'The "Weiter" step control if the template renders one. Measured, never used to submit.', sel: 'Weiter' });
  await S('body', q('.entry-content p, article p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Body paragraph', desc: 'A paragraph of the recipe story.', sel: 'article p' });
  await S('app-cta', q('a, button').filter({ hasText: /Jetzt loslegen|App/ }).filter({ visible: true }).first(), B4, { group: g, title: 'App call to action', desc: 'An app download call to action. Measured, never followed.', sel: 'Jetzt loslegen' });
  save();
}

async function stories() {
  if (!(await newPage('stories', { wait: 4000 }))) return;
  const g = G.stories;
  await S('stories-title', q('h2.entry-title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Story title', desc: 'A story title on the /stories index. The index has no page h1.', sel: 'h2.entry-title' }, { noScroll: true });
  await mark('article', 'data-m-story', 0);
  await S('story-card', q('[data-m-story]'), ['default'], { group: g, title: 'Story card', desc: 'A story card on /stories.', sel: 'article' });
  save();
}

async function search() {
  if (!(await newPage('search', { wait: 4000 }))) return;
  await sheetsFor('search');
  const g = G.search;
  await S('results-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Results heading', desc: 'The search results heading ("SUCHERGEBNISSE") for the public query pasta.', sel: 'h1' }, { noScroll: true });
  await S('results-field', q('input[name="s"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Results field', desc: 'The search field on the results page. Typed into and cleared. Never submitted from this pass.', sel: 'input[name=s]' }, { fillText: 'suppe' });
  await mark('article', 'data-m-result', 0);
  await S('result-card', q('[data-m-result]'), ['default'], { group: g, title: 'Result card', desc: 'A search result card.', sel: 'article' });
  save();
}

async function plus() {
  if (!(await newPage('plus', { wait: 4500 }))) return;
  await sheetsFor('plus');
  const g = G.plus;
  await S('plus-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plus heading', desc: 'The Plus marketing headline on pages.kitchenstories.com.', sel: 'h1' }, { noScroll: true });
  await S('plus-cta', q('a').filter({ hasText: /kostenlos starten/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Start free link', desc: 'The "Jetzt kostenlos starten" link to /de/checkout. Measured, never followed. Checkout is a gated surface.', sel: 'a kostenlos starten' });
  await S('plus-nav', q('a').filter({ hasText: /^Über uns$|^Karriere$|^Unsere App$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Marketing nav link', desc: 'A pages.kitchenstories.com nav link. Measured, never followed.', sel: 'marketing nav a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, wait: 4000, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await mark('header', 'data-m-mheader', 0);
  await S('m-header', q('[data-m-mheader]'), ['default'], { group: g, title: 'Mobile header', desc: 'The phone header.', sel: 'header' }, { noScroll: true });
  await S('m-menu', q('button.mobile-menu-toggle').filter({ visible: true }).last(), [...B4, 'opened'], { group: g, title: 'Mobile menu', desc: 'The painted phone hamburger. The first .mobile-menu-toggle sits off-canvas in the header track. Opened as a local toggle; links not followed.', sel: 'button.mobile-menu-toggle:visible' }, { noScroll: true });
  await S('m-menu-panel', q('nav.main-navigation, #menu-main-menue').filter({ visible: true }).first(), ['default'], { group: G.overlay, title: 'Mobile menu panel', desc: 'The phone nav panel opened by the hamburger. Links measured, never followed.', sel: 'nav.main-navigation' }, { noScroll: true });
  await S('m-menu-link', q('#menu-main-menue a, nav.main-navigation a').filter({ hasText: /Artikel|Rezepte/ }).filter({ visible: true }).first(), B4, { group: G.overlay, title: 'Mobile menu link', desc: 'A link in the opened phone menu. Measured, never followed.', sel: '#menu-main-menue a' }, { noScroll: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-card', q('article').filter({ visible: true }).filter({ has: q('h2, h3, .entry-title') }).first(), ['default'], { group: g, title: 'Mobile card', desc: 'A recipe card in the phone feed. The first article is the page wrapper, so the card is the first article that holds a title.', sel: 'article:has(h2)' });
  await S('m-footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Mobile footer', desc: 'The phone footer.', sel: 'footer' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (the Mobile group at 390 x 844); kitchenstories.com paints one light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, recipes, recipe, stories, search, plus, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that animates (the More chevron), so
  // the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page finished this run: a
    // page the run never reached, and an edge-blocked route, keeps its earlier
    // readings under their original provenance instead of being erased and
    // republished.
    if (!touched.has(key) && !pages.length && finishedPages.has(c.page) && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
