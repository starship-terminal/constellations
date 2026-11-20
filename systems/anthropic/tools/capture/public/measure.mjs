// Measures Anthropic's components on its public pages, in every state that can be
// reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home news research engineering product platform-api pricing contact-sales
//        docs-home docs-start docs-api mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be re-run),
// raw/layout.json (the frame of each page) and one crop per component and state
// into components/crops/. raw/measurements.md is then built from the JSON by
// build-measurements.mjs.
//
// Three surfaces: www.anthropic.com (marketing, CSS modules `X-module-...__name`
// plus `hash_name` component classes and shared text-*/theme-* utilities),
// claude.com (the product pages, same build) and platform.claude.com/docs (the
// Claude Platform docs, a cds-* Tailwind design system). claude.ai and
// console.anthropic.com are the signed-in products and are never touched; the
// /contact-sales form is measured, never submitted.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or submit button can fire
//   focused        the field clicked into (a text field only)
//   filled         sample text typed into a field, measured, then deleted; Enter is never pressed
//   open           a resting state reached by a UI toggle (a nav dropdown, a plan
//                  tab, a docs panel); nothing that submits, calls or signs
//                  in is ever pressed
import fs from 'node:fs';
import path from 'node:path';
import { BASE, DOCS, launch, open, closePromo, styleOf, crop, centre, markFixed, RAW } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const LAYOUT_OUT = path.join(RAW, 'layout.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
const layout = fs.existsSync(LAYOUT_OUT) ? JSON.parse(fs.readFileSync(LAYOUT_OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const saveLayout = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(LAYOUT_OUT, JSON.stringify(layout, null, 1) + '\n'); };

const URLS = {
  home: BASE + '/', news: BASE + '/news', research: BASE + '/research', engineering: BASE + '/engineering',
  product: 'https://claude.com/product/overview', 'platform-api': 'https://claude.com/platform/api',
  pricing: 'https://claude.com/pricing', 'contact-sales': 'https://claude.com/contact-sales',
  'docs-home': DOCS + '/en/home', 'docs-start': DOCS + '/en/docs/get-started', 'docs-api': DOCS + '/en/api/messages',
};

let page, cdp, current, context, run;
const touched = new Set();

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 7000 } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '', URLS[key]);
  await open(page, URLS[key], { wait, promo });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await markFixed(page);
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

// Clicks a UI toggle (a nav trigger, a plan tab, a menu button). Refuses a
// submit button and any control whose text names an action this kit must
// never take.
const NEVER = /^(send|submit|sign in|log in|try claude|contact sales|get api key|create|generate|upload|get started|start|start building|start free trial|upgrade|subscribe|apply|accept all|reject all|manage cookies|privacy choices|cookie settings|request demo|get a demo|book|join|open|share|explore here)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: URLS[current] }, meta);
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

const FILL = 'a voice agent for a clinic';

// Records the listed states of one component. meta: title, group, desc, sel.
// The target is checked before comp() touches the entry: a component several
// pages share keeps its earlier states and page details when a later page does
// not carry it, instead of being rewritten page-details-and-all as missing.
async function S(key, target, list, meta = {}, opts = {}) {
  if (opts.open) { await reset(); await opts.open(); }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    if (Object.keys(out.components[key]?.states || {}).length) { touched.add(key); log('  ! not on this page, keeping earlier capture', key); }
    else { comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel }); out.components[key].missing = true; log('  ! missing', key); }
    return;
  }
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  delete out.components[key].missing;
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
        // opts.focusLoc may name an sr-only control (the real focus target of a
        // styled switch, say): it is not visibility-filtered the way loc is.
        via = await kbFocus(opts.focusLoc ? opts.focusLoc.first() : loc.filter({ visible: true }).first());
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
      } else via = via || opts.via || 'at rest';
      if (via === 'focus failed') {
        // The element never took focus: a resting read labelled focus-visible is
        // not a captured focus, so the attempt is recorded as an error instead.
        out.components[key].states[st] = { error: 'keyboard focus could not reach the element', via };
        log('  !', key, st, 'focus failed');
      } else {
        await measure(key, st, loc, { ...opts, via });
      }
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

// Tags the first element matching an in-page probe so a locator can find it:
// await tag('nav', () => {...return element or null...}) then q('[data-m="nav"]').
async function tag(name, probe) {
  return page.evaluate(([n, src]) => {
    const el = (new Function('return (' + src + ')')())();
    for (const old of document.querySelectorAll(`[data-m="${n}"]`)) old.removeAttribute('data-m');
    if (!el) return false;
    el.setAttribute('data-m', n);
    return true;
  }, [name, probe.toString()]).catch(() => false);
}

// Tags the smallest element whose trimmed text matches reSrc inside scopeSel,
// preferring an interactive tag or a cursor:pointer box.
async function tagEl(name, reSrc, scopeSel) {
  return page.evaluate(([n, src, scope]) => {
    const re = new RegExp(src, 'i');
    const sc = scope ? document.querySelector(scope) : document;
    if (!sc) return false; // the scope is gone: never fall back to the whole page
    const cands = [...sc.querySelectorAll('a,button,[role=button],[role=tab],li,div,span')].filter((e) => {
      const t = (e.innerText || e.getAttribute('aria-label') || '').trim(); const r = e.getBoundingClientRect();
      return re.test(t) && t.length < 80 && r.width > 10 && r.height > 8;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    const el = cands.find((e) => e.matches('a,button,[role=button],[role=tab],li,[tabindex]') || getComputedStyle(e).cursor === 'pointer') || cands[0];
    for (const old of document.querySelectorAll(`[data-m="${n}"]`)) old.removeAttribute('data-m');
    if (!el) return false;
    el.setAttribute('data-m', n);
    return true;
  }, [name, reSrc, scopeSel || null]).catch(() => false);
}

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

// The page's frame: nav height and position, the widest content column, the
// card grids' column counts and gaps, and every fixed overlay still painted.
async function layoutFor(key) {
  layout[key] = await page.evaluate(() => {
    const vw = innerWidth, vh = innerHeight;
    const vis = (e) => { const r = e.getBoundingClientRect(); return r.width > 4 && r.height > 4 && getComputedStyle(e).visibility !== 'hidden'; };
    const fixed = [...document.querySelectorAll('body *')].filter((e) => { const cs = getComputedStyle(e); return (cs.position === 'fixed' || cs.position === 'sticky') && vis(e) && e.getBoundingClientRect().top < vh && e.getBoundingClientRect().bottom > 0; })
      .map((e) => ({ el: e.tagName.toLowerCase() + (e.classList[0] ? '.' + String(e.classList[0]).split('__').pop() : ''), pos: getComputedStyle(e).position, top: +e.getBoundingClientRect().top.toFixed(0), w: +e.getBoundingClientRect().width.toFixed(0), h: +e.getBoundingClientRect().height.toFixed(0), text: (e.innerText || '').trim().slice(0, 60), backdrop: getComputedStyle(e).backdropFilter !== 'none' ? getComputedStyle(e).backdropFilter : undefined })).slice(0, 12);
    const maxWidths = [...document.querySelectorAll('main *, body > * > *')].filter(vis).map((e) => ({ w: +e.getBoundingClientRect().width.toFixed(0), max: getComputedStyle(e).maxWidth }))
      .filter((m) => m.max !== 'none' && parseFloat(m.max) > 200).slice(0, 8);
    const grids = [...document.querySelectorAll('body *')].filter((e) => getComputedStyle(e).display === 'grid' && vis(e)).map((e) => {
      const cs = getComputedStyle(e);
      return { el: e.tagName.toLowerCase() + (e.classList[0] ? '.' + String(e.classList[0]).split('__').pop() : ''), cols: cs.gridTemplateColumns.slice(0, 90), colGap: cs.columnGap, rowGap: cs.rowGap, w: +e.getBoundingClientRect().width.toFixed(0) };
    }).filter((g) => g.cols.split(' ').length > 1).slice(0, 8);
    return { vw, vh, docH: document.documentElement.scrollHeight, fixed, maxWidths, grids };
  }).catch((e) => ({ error: String(e).slice(0, 200) }));
  saveLayout();
}

// ---------- groups ----------
const G = {
  shell: 'Shell and navigation', home: 'Home', cards: 'Cards and indexes',
  product: 'Product pages', pricing: 'Pricing', contact: 'Contact sales form',
  docs: 'Docs (platform.claude.com)', overlay: 'Overlays', mobile: 'Mobile (390 wide)',
};
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// The marketing/product chrome on both www.anthropic.com and claude.com:
// a fixed header with the wordmark, section triggers (Product, Developers,
// Enterprise, Resources, Pricing), Search and Try Claude.
async function shell(pageKey) {
  const g = G.shell;
  const nav = await tag('nav', () => {
    const cands = [...document.querySelectorAll('header, [class*="__header"], nav')].filter((e) => {
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      return r.top <= 80 && r.width > 500 && r.height > 24 && r.height < 140 && /product|pricing|search|developers/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().height * a.getBoundingClientRect().width - b.getBoundingClientRect().height * b.getBoundingClientRect().width)[0] || null;
  });
  if (nav) {
    await S('nav-bar', q('[data-m="nav"]'), ['default'], { group: g, title: 'Top navigation bar', desc: 'The fixed header on every marketing and product page: the Anthropic wordmark, section triggers, Search and the Try Claude pill.', sel: 'header.__header' }, { noScroll: true });
    const tr = await tag('navtrig', () => document.querySelector('header [class*="__trigger"], [data-m="nav"] [class*="__trigger"]') || null);
    if (!tr) await tagEl('navtrig', 'product|developers|resources|enterprise', '[data-m="nav"]');
    if (await q('[data-m="navtrig"]').count())
      await S('nav-trigger', q('[data-m="navtrig"]'), B4, { group: g, title: 'Nav dropdown trigger', desc: 'A section trigger in the header; opens the section dropdown on hover. Measured, never followed.', sel: '"Product" trigger' }, { noScroll: true });
    else if (await tagEl('navpill', '^news$|^research$|^policy$|^commitments$|^company$|^pricing$', '[data-m="nav"]'))
      await S('nav-pill', q('[data-m="navpill"]'), B4, { group: g, title: 'Nav pill link', desc: 'A section pill in the header (News, Research, Policy, Commitments, Company). Measured, never followed.', sel: 'a header pill link' }, { noScroll: true });
    if (await tagEl('navsearch', '^search$', '[data-m="nav"]'))
      await S('nav-search', q('[data-m="navsearch"]'), B4, { group: g, title: 'Nav search button', desc: 'The square search icon button in the header.', sel: '"Search" icon button' }, { noScroll: true });
    if (await tagEl('navcta', '^try claude$|^explore here$|^get started$', '[data-m="nav"]'))
      await S('nav-cta', q('[data-m="navcta"]'), B4, { group: g, title: 'Nav CTA button', desc: 'The header\'s primary action pill ("Try Claude" on the marketing site, "Explore here" on claude.com). Measured and focused, never followed.', sel: 'the CTA in the header' }, { noScroll: true });
    const trig = q('[data-m="navtrig"]');
    if (await trig.count()) {
      await trig.hover({ timeout: 4000 }).catch(() => {});
      await page.waitForTimeout(1400);
      const menu = await tag('submenu', () => {
        const cands = [...document.querySelectorAll('[class*="__dropdown"], [class*="__menu"], [role=menu], [class*="__panel"]')].filter((e) => {
          const r = e.getBoundingClientRect();
          return r.top > 40 && r.top < 200 && r.width > 150 && r.height > 80 && e.querySelector('a');
        });
        return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
      });
      if (menu) await S('nav-dropdown', q('[data-m="submenu"]'), ['default'], { group: g, title: 'Nav dropdown', desc: 'The dropdown under a header section (Product: Claude, Claude Code, Claude in Chrome, …). Shown in its hover-open state.', sel: 'the open dropdown panel' }, { noScroll: true, noReset: true, via: 'hover over the trigger' });
      if (await tagEl('sublink', 'claude code|claude in|api|docs', '[data-m="submenu"]'))
        await S('nav-dropdown-link', q('[data-m="sublink"]'), ['default', 'hover'], { group: g, title: 'Dropdown link', desc: 'An item in the open nav dropdown.', sel: 'an item in the dropdown' }, { noScroll: true, open: async () => { await trig.hover({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(1400); } });
      await reset();
    }
  }
  // Footer: link columns, social, Privacy choices.
  const foot = await tag('foot', () => {
    const cands = [...document.querySelectorAll('footer, [class*="__footer"]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 500 && r.height > 80;
    });
    return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
  });
  if (foot) {
    await S('footer', q('[data-m="foot"]'), ['default'], { group: g, title: 'Footer', desc: 'The site footer: link columns, the wordmark, legal row with Privacy choices.', sel: 'footer' });
    if (await tagEl('flink', '^careers$|^news$|^trust center$|^privacy policy$|privacy choices', '[data-m="foot"]'))
      await S('footer-link', q('[data-m="flink"]'), B4, { group: g, title: 'Footer link', desc: 'A link in the footer columns. Privacy choices opens a settings dialog and is never pressed.', sel: 'a footer link' });
  }
}

// ---------- home ----------
async function home() {
  await newPage('home');
  await shell('home');
  const g = G.home;
  const h1 = await tag('h1', () => document.querySelector('h1'));
  if (h1) await S('hero-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'Hero title', desc: 'The home h1, a large serif display line ("AI research and products that put safety at the frontier.").', sel: 'h1' }, { noScroll: true });
  if (await tagEl('herocta', '^try claude$|^learn more$|^explore', 'main'))
    await S('hero-cta', q('[data-m="herocta"]'), B4, { group: g, title: 'Hero CTA', desc: 'The primary pill under the hero title.', sel: 'the first primary button on the page' });
  // Feature/news cards further down the page.
  const card = await tag('ncard', () => {
    const cands = [...document.querySelectorAll('a, [class*="card" i], [class*="slide" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 260 && r.height > 150 && r.top > 300 && e.tagName === 'A' ? /learn more|read more|report|announce/i.test(e.innerText || '') : /card|slide/i.test(e.className || '');
    });
    return cands[0] || null;
  });
  if (card) await S('feature-card', q('[data-m="ncard"]'), ['default', 'hover'], { group: G.cards, title: 'Feature card', desc: 'A large card or slide on the home page (the report/announcement feature).', sel: 'a card-sized element' });
  await sheetsFor('home');
  await layoutFor('home');
  await page.close();
}

// ---------- index pages (news, research, engineering) ----------
async function indexPage(key, g, title, cardKey, cardDesc) {
  await newPage(key);
  const h1 = await tag('h1', () => document.querySelector('h1'));
  if (h1) await S(cardKey + '-title', q('[data-m="h1"]'), ['default'], { group: g, title, sel: 'h1' }, { noScroll: true });
  const card = await tag('icard', () => {
    const cands = [...document.querySelectorAll('a')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 240 && r.height > 60 && r.top > 200 && (e.querySelector('h2, h3, img, [class*="title" i], [class*="headline" i], [class*="info" i]'));
    });
    return cands[0] || null;
  });
  if (card) await S(cardKey, q('[data-m="icard"]'), ['default', 'hover'], { group: g, title: cardDesc.split(':')[0], desc: cardDesc, sel: 'a linked card in the index' });
  const info = await tag('ilink', () => document.querySelector('[class*="info-link" i], [class*="card-title" i]') || null);
  if (info) await S(cardKey + '-link', q('[data-m="ilink"]'), ['default', 'hover'], { group: g, title: cardDesc.split(':')[0] + ' title link', desc: 'The caption/title link of an index entry.', sel: 'the carousel info link' });
  await layoutFor(key);
  await page.close();
}

// ---------- product pages (claude.com) ----------
async function product() {
  await newPage('product');
  await shell('product');
  const g = G.product;
  const h1 = await tag('h1', () => document.querySelector('h1'));
  if (h1) await S('product-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'Product page title', desc: 'The product page h1 (the Claude product overview).', sel: 'h1' }, { noScroll: true });
  if (await tagEl('pcta', '^try claude$|^get started|^learn more', 'main'))
    await S('product-cta', q('[data-m="pcta"]'), B4, { group: g, title: 'Product CTA', desc: 'A primary button on the product page.', sel: 'the first CTA' });
  const card = await tag('pcard', () => {
    const cands = [...document.querySelectorAll('a, [class*="card" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 240 && r.height > 120 && r.top > 300;
    });
    return cands[0] || null;
  });
  if (card) await S('product-card', q('[data-m="pcard"]'), ['default', 'hover'], { group: g, title: 'Product card', desc: 'A card on the product overview page.', sel: 'a card' });
  await layoutFor('product');
  await page.close();
}

async function platformApi() {
  await newPage('platform-api');
  const g = G.product;
  const h1 = await tag('h1', () => [...document.querySelectorAll('h1, h2')].filter((e) => e.getBoundingClientRect().height > 20).sort((a, b) => parseFloat(getComputedStyle(b).fontSize) - parseFloat(getComputedStyle(a).fontSize))[0] || null);
  if (h1) await S('api-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'Platform page title', desc: 'The Claude Platform/API page headline.', sel: 'the largest heading' }, { noScroll: true });
  if (await tagEl('acta', '^start building|^get api key|^read the docs|^docs$|^learn more|^log in to the console', 'main'))
    await S('api-cta', q('[data-m="acta"]'), B4, { group: g, title: 'Platform CTA', desc: 'A primary button or link on the platform page.', sel: 'the first CTA' });
  const code = await tag('acode', () => {
    const cands = [...document.querySelectorAll('pre, [class*="code" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 200 && r.height > 40;
    });
    return cands[0] || null;
  });
  if (code) await S('api-code', q('[data-m="acode"]'), ['default'], { group: g, title: 'Code sample', desc: 'A code sample on the platform page.', sel: 'pre or code panel' });
  await layoutFor('platform-api');
  await page.close();
}

// ---------- pricing ----------
async function pricing() {
  await newPage('pricing');
  await shell('pricing');
  const g = G.pricing;
  const h1 = await tag('h1', () => document.querySelector('h1'));
  if (h1) await S('pricing-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'Pricing title', desc: 'The "Pricing" h1 on claude.com/pricing.', sel: 'h1' }, { noScroll: true });
  const tabs = await tag('tabs', () => {
    const cands = [...document.querySelectorAll('[role=tablist], [class*="tab" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 150 && r.height > 20 && r.height < 80 && /individual|developer|team/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
  });
  // Plan card and its CTA first, on the default tab: switching to API replaces
  // the plan cards with the API usage table. The CTA is searched inside the card.
  const card = await tag('pcard', () => {
    const cands = [...document.querySelectorAll('[class*="card" i], [class*="plan" i], article, li')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 200 && r.width < 700 && r.height > 200 && /\$\d|per month|\/mo|free|pro|max|team|enterprise/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
  });
  if (card) await S('plan-card', q('[data-m="pcard"]'), ['default'], { group: g, title: 'Plan card', desc: 'A plan card on the pricing grid.', sel: 'a plan column' });
  if (card && await tagEl('planc', '^try claude$|^contact sales$|^subscribe|^get started', '[data-m="pcard"]'))
    await S('plan-cta', q('[data-m="planc"]'), B4, { group: g, title: 'Plan CTA', desc: 'A button inside a plan card ("Try Claude", "Contact sales"). Measured and focused, never followed.', sel: 'a plan card button' });
  if (tabs) {
    await S('plan-tabs', q('[data-m="tabs"]'), ['default'], { group: g, title: 'Plan type tabs', desc: 'The Individual / Developer / Team plan tabs.', sel: 'the tab strip' });
    if (await tagEl('tabitem', '^developer$|^individual$|^team$', '[data-m="tabs"]'))
      await S('plan-tab', q('[data-m="tabitem"]'), B4, { group: g, title: 'Plan tab', desc: 'One segment of the plan-type tabs.', sel: '"Developer" tab' });
    if (await tagEl('tabitem2', '^api$', '[data-m="tabs"]')) {
      await S('plan-tab-active', q('[data-m="tabitem2"]'), ['default'], { group: g, title: 'Plan tab, switched', desc: 'The same tab strip after a local click: the API segment is the active one, and the API usage table replaces the plan cards.', sel: 'the "API" tab after clicking it' }, { open: async () => { await toggle(q('[data-m="tabitem2"]')); await page.waitForTimeout(1800); } });
    }
  }
  // The batch banner lives on the API tab's usage table — click it first.
  const apiTab = page.locator('[role=tab]').filter({ hasText: /^api$/i }).first();
  if (await apiTab.count()) { await apiTab.click().catch(() => {}); await page.waitForTimeout(1800); }
  const bt = await tag('batch', () => {
    const cands = [...document.querySelectorAll('[class*="__banner"], [class*="banner" i], [role=switch], label')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 150 && r.height > 15 && /batch processing|save 50/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
  });
  if (bt) {
    await S('batch-banner', q('[data-m="batch"]'), ['default'], { group: g, title: 'Batch processing banner', desc: 'The "Save 50% with batch processing" toggle banner on the API pricing tab.', sel: 'the batch banner' });
    // The switch is label.bannerToggle > input[role=switch].sr-only + a painted
    // track span: measure the painted track, focus the sr-only input behind it.
    const sw = await tag('bswitch', () => document.querySelector('[data-m="batch"] [class*="__switch"], [data-m="batch"] [class*="Switch"], [data-m="batch"] input[role=switch]') || null);
    if (sw)
      await S('batch-toggle', q('[data-m="bswitch"]'), B4, { group: g, title: 'Batch toggle', desc: 'The switch that shows batch-processing prices; a local toggle.', sel: 'the painted track of the batch switch (input[role=switch])' }, { focusLoc: q('[data-m="batch"] input[role=switch]') });
    const trow = await tag('apirow', () => {
      const cands = [...document.querySelectorAll('tr, [class*="row" i], li')].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.width > 400 && r.height > 15 && r.height < 90 && /\$|per MTok|input|output|opus|sonnet|haiku/i.test(e.innerText || '');
      });
      return cands[0] || null;
    });
    if (trow) await S('api-price-row', q('[data-m="apirow"]'), ['default'], { group: g, title: 'API price row', desc: 'A model/usage row in the API pricing table.', sel: 'a pricing table row' });
  }
  const faq = await tag('faqitem', () => {
    const cands = [...document.querySelectorAll('button, [role=button], summary, details')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 300 && r.height > 15 && /\?/i.test(e.innerText || '');
    });
    return cands[0] || null;
  });
  if (faq) await S('faq-item', q('[data-m="faqitem"]'), ['default', 'hover'], { group: g, title: 'FAQ item', desc: 'An accordion question in the pricing FAQ.', sel: 'an accordion button' });
  await layoutFor('pricing');
  await page.close();
}

// ---------- contact-sales form ----------
async function contactSales() {
  await newPage('contact-sales');
  const g = G.contact;
  const h1 = await tag('h1', () => document.querySelector('h1, h2'));
  if (h1) await S('contact-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'Contact page title', desc: 'The heading over the contact-sales form.', sel: 'h1' }, { noScroll: true });
  const form = await tag('form', () => {
    const f = document.querySelector('form') || [...document.querySelectorAll('main *')].find((e) => e.querySelector('input') && e.getBoundingClientRect().width < 800);
    return f || null;
  });
  if (form) {
    await S('contact-form', q('[data-m="form"]'), ['default'], { group: g, title: 'Contact form', desc: 'The HubSpot contact-sales form: a "What can we help you with?" radio topic group first, then dependent fields. Photographed and focused, never submitted.', sel: 'form' });
    // The form opens with a radio topic group; picking a topic reveals the fields.
    const radioRow = await tag('rrow', () => document.querySelector('.hs-form-radio') || [...document.querySelectorAll('li')].find((e) => e.querySelector('input[type=radio]')) || null);
    if (radioRow) {
      await S('topic-radio-row', q('[data-m="rrow"]'), ['default', 'hover'], { group: g, title: 'Topic radio row', desc: 'A radio row in the "What can we help you with?" topic group.', sel: 'a .hs-form-radio row' });
      const radio = q('[data-m="rrow"] input[type=radio]').first();
      if (await radio.count()) await S('topic-radio', radio, ['default'], { group: g, title: 'Radio input', desc: 'The radio input inside a topic row.', sel: 'input[type=radio]' });
      // Choose the first topic — a local selection that reveals dependent fields; not a submission.
      await q('[data-m="rrow"] label').first().click({ timeout: 4000 }).catch(() => q('[data-m="rrow"]').first().click({ timeout: 4000 }).catch(() => {}));
      await page.waitForTimeout(1500);
    }
    if (await tagEl('label', 'name|email|company|team size|use case|how can|first|last', '[data-m="form"]'))
      await S('field-label', q('[data-m="label"]'), ['default'], { group: g, title: 'Field label', desc: 'A label over a field in the form.', sel: 'a label' });
    const input = q('form input:not([type=checkbox]):not([type=radio]):not([type=hidden]):not([type=submit]), main input:not([type=checkbox]):not([type=radio]):not([type=hidden])').filter({ visible: true }).first();
    if (await input.count()) {
      await S('text-field', input, ['default', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'A text input in the form. Focused and filled with sample text that was deleted; nothing was sent.', sel: 'the first text input' });
      await S('text-field-box', input, ['default'], { group: g, title: 'Text field box', desc: 'The same field measured at rest (default only).', sel: 'the first text input' }, { crop: false });
    }
    const ta = q('form textarea').filter({ visible: true }).first();
    if (await ta.count()) await S('text-area', ta, ['default', 'focused'], { group: g, title: 'Text area', desc: 'The message textarea.', sel: 'textarea' });
    const sel = q('form select, form [role=combobox], form [role=listbox]').filter({ visible: true }).first();
    if (await sel.count()) await S('select-field', sel, ['default'], { group: g, title: 'Select field', desc: 'A select/combobox in the form.', sel: 'select' });
    const cb = q('form input[type=checkbox]').filter({ visible: true }).first();
    if (await cb.count()) await S('checkbox', cb, ['default'], { group: g, title: 'Checkbox', desc: 'A checkbox in the form (marketing consent).', sel: 'input[type=checkbox]' });
    if (await tagEl('submit', '^submit$|^contact sales$|^send$|^talk to sales$', '[data-m="form"]'))
      await S('submit-button', q('[data-m="submit"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Submit button', desc: 'The form submit. Measured and focused, never pressed.', sel: 'the submit button' });
  }
  await layoutFor('contact-sales');
  await page.close();
}

// ---------- docs (platform.claude.com/docs) ----------
async function docsChrome(g) {
  const top = await tag('dtop', () => {
    const cands = [...document.querySelectorAll('header, [class*="topbar" i], nav')].filter((e) => {
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      return (cs.position === 'fixed' || cs.position === 'sticky') && r.top <= 8 && r.width > 600 && r.height < 100 && /messages|search|docs|log in|console/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().height * a.getBoundingClientRect().width - b.getBoundingClientRect().height * b.getBoundingClientRect().width)[0] || null;
  });
  if (top) {
    await S('docs-topbar', q('[data-m="dtop"]'), ['default'], { group: g, title: 'Docs top bar', desc: 'The 56px docs header: product tabs, search, language, Console, Log in.', sel: 'the fixed docs header' }, { noScroll: true });
    if (await tagEl('dtab', '^messages$|^managed agents$|^admin$|^api reference$', '[data-m="dtop"]'))
      await S('docs-tab', q('[data-m="dtab"]'), B4, { group: g, title: 'Docs top tab', desc: 'A product tab in the docs header.', sel: '"Messages" tab' }, { noScroll: true });
    const sf = await tag('dsearch', () => document.querySelector('[class*="fill-field"]') || null) || await tagEl('dsearch', 'search');
    if (sf || await q('[data-m="dsearch"]').count())
      await S('docs-search-field', q('[data-m="dsearch"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Search field', desc: 'The "Search ⌘K" field in the docs chrome (288x32, bg-fill-field). Opens the search dialog.', sel: 'the search field button' }, { noScroll: true });
    if (await tagEl('dlang', '^english|^en$', '[data-m="dtop"]'))
      await S('docs-lang', q('[data-m="dlang"]'), ['default', 'hover'], { group: g, title: 'Language picker', desc: 'The "English" locale picker in the docs header.', sel: 'the lang button' }, { noScroll: true });
  }
  const side = await tag('dside', () => {
    const cands = [...document.querySelectorAll('nav, aside, [class*="sidebar" i], [class*="nav" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.left < 320 && r.width > 160 && r.width < 400 && r.height > 300;
    });
    return cands.sort((a, b) => a.getBoundingClientRect().left - b.getBoundingClientRect().left)[0] || null;
  });
  if (side) {
    await S('docs-sidebar', q('[data-m="dside"]'), ['default'], { group: g, title: 'Docs sidebar', desc: 'The left docs navigation: section groups and page links.', sel: 'the left nav' });
    if (await tagEl('dslink', 'get started|quickstart|models|pricing|overview|introduction', '[data-m="dside"]'))
      await S('docs-nav-link', q('[data-m="dslink"]'), B4, { group: g, title: 'Docs nav link', desc: 'A link in the docs sidebar.', sel: 'a sidebar link' });
    const act = await tag('dact', () => {
      const cands = [...document.querySelectorAll('nav a[aria-current], nav a[class*="active" i], nav a[class*="selected" i], [data-m="dside"] a')].filter((e) => {
        const cs = getComputedStyle(e);
        return cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.fontWeight === '600' || cs.fontWeight === '700';
      });
      return cands[0] || null;
    });
    if (act) await S('docs-nav-active', q('[data-m="dact"]'), ['default'], { group: g, title: 'Docs nav link, current', desc: 'The current page in the docs sidebar.', sel: 'the active sidebar link' });
  }
}

async function docsHome() {
  await newPage('docs-home');
  const g = G.docs;
  await docsChrome(g);
  const h1 = await tag('dh1', () => document.querySelector('h1'));
  if (h1) await S('docs-hero-title', q('[data-m="dh1"]'), ['default'], { group: g, title: 'Docs home title', desc: 'The docs home h1 ("Start building with Claude").', sel: 'h1' });
  const card = await tag('dcard', () => {
    const cands = [...document.querySelectorAll('a')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 180 && r.height > 60 && r.top > 200 && /get started|quickstart|api key|sdk|claude code|course/i.test(e.innerText || '');
    });
    return cands[0] || null;
  });
  if (card) await S('docs-card', q('[data-m="dcard"]'), ['default', 'hover'], { group: g, title: 'Docs link card', desc: 'A linked card on the docs home (Get started, Quickstart, Get API key, SDKs).', sel: 'a docs card' });
  const top = q('[data-m="dsearch"]');
  if (await top.count()) {
    await top.click({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(1500);
    const dlg = await tag('ddlg', () => {
      const cands = [...document.querySelectorAll('[role=dialog], [class*="modal" i], [class*="search" i]')].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.width > 300 && r.height > 40 && e.querySelector('input, [class*="field" i]');
      });
      return cands[0] || null;
    });
    if (dlg) {
      await S('docs-search-dialog', q('[data-m="ddlg"]'), ['default'], { group: G.overlay, title: 'Search dialog', desc: 'The docs search dialog opened from the header field. Nothing was typed.', sel: 'the open search dialog' }, { noScroll: true });
      const inp = q('[data-m="ddlg"] input').first();
      if (await inp.count()) await S('docs-search-input', inp, ['default'], { group: G.overlay, title: 'Search input', desc: 'The field inside the search dialog.', sel: 'input in the dialog' }, { noScroll: true });
    }
    await page.keyboard.press('Escape');
    await page.waitForTimeout(600);
  }
  await layoutFor('docs-home');
  await page.close();
}

async function docsPage(key) {
  await newPage(key);
  const g = G.docs;
  await docsChrome(g);
  const h1 = await tag('dh1', () => document.querySelector('h1'));
  if (h1) await S(key + '-title', q('[data-m="dh1"]'), ['default'], { group: g, title: 'Docs page title', desc: 'The h1 at the top of a docs page.', sel: 'h1' });
  const body = await tag('dbody', () => {
    const cands = [...document.querySelectorAll('main p, article p, [class*="prose" i] p, main li')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 300 && r.height > 10 && e.innerText.trim().length > 40;
    });
    return cands[0] || null;
  });
  if (body) await S(key + '-body', q('[data-m="dbody"]'), ['default'], { group: g, title: 'Docs body text', desc: 'A paragraph of docs body copy.', sel: 'a prose paragraph' });
  const code = await tag('dcode', () => {
    const cands = [...document.querySelectorAll('pre')].filter((e) => e.getBoundingClientRect().width > 200 && e.getBoundingClientRect().height > 30);
    return cands[0] || null;
  });
  if (code) await S(key + '-code-block', q('[data-m="dcode"]'), ['default'], { group: g, title: 'Docs code block', desc: 'A fenced code block in the docs.', sel: 'pre' });
  const ic = await tag('dicode', () => {
    const cands = [...document.querySelectorAll('p code, li code')].filter((e) => e.getBoundingClientRect().width > 10);
    return cands[0] || null;
  });
  if (ic) await S(key + '-inline-code', q('[data-m="dicode"]'), ['default'], { group: g, title: 'Docs inline code', desc: 'Inline `code` in the docs body.', sel: 'p code' });
  if (key === 'docs-api') {
    const row = await tag('dparam', () => {
      const cands = [...document.querySelectorAll('[class*="param" i], [class*="field" i], li, tr')].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.width > 300 && r.height > 20 && /required|optional|string|integer|array|boolean|model|max_tokens|messages/i.test(e.innerText || '');
      });
      return cands[0] || null;
    });
    if (row) await S('docs-param-row', q('[data-m="dparam"]'), ['default'], { group: g, title: 'API parameter row', desc: 'A parameter row on the API reference (name, type, required).', sel: 'a param row' });
    const meth = await tag('dmeth', () => {
      const cands = [...document.querySelectorAll('[class*="method" i], [class*="badge" i], [class*="pill" i], code, span')].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.width < 120 && /^(GET|POST|PUT|DELETE|PATCH)$/i.test((e.innerText || '').trim());
      });
      return cands[0] || null;
    });
    if (meth) await S('docs-method-badge', q('[data-m="dmeth"]'), ['default'], { group: g, title: 'HTTP method badge', desc: 'The method badge on an endpoint (POST, GET).', sel: 'the method pill' });
  }
  const copy = await tag('dcopy', () => {
    const cands = [...document.querySelectorAll('button, a')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 4 && r.height > 4 && /copy page|copy/i.test((e.innerText || e.getAttribute('aria-label') || '').trim());
    });
    return cands[0] || null;
  });
  if (copy) await S('docs-copy-page', q('[data-m="dcopy"]'), ['default', 'hover'], { group: g, title: 'Copy page button', desc: 'The "Copy page" utility button above the docs body.', sel: 'the Copy page button' });
  await sheetsFor(key);
  await layoutFor(key);
  await page.close();
}

// ---------- mobile ----------
async function mobile() {
  await newPage('home', { mobile: true });
  const g = G.mobile;
  const nav = await tag('mnav', () => {
    const cands = [...document.querySelectorAll('header, [class*="__header"], nav')].filter((e) => {
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      return r.top <= 60 && r.width > 200 && r.height < 120;
    });
    return cands[0] || null;
  });
  if (nav) await S('m-nav-bar', q('[data-m="mnav"]'), ['default'], { group: g, title: 'Top navigation bar (mobile)', desc: 'The header at 390: wordmark and menu button.', sel: 'the mobile header' }, { noScroll: true });
  const menu = await tag('mmenu', () => [...document.querySelectorAll('button')].find((e) => /menu|nav/i.test((e.innerText || e.getAttribute('aria-label') || '').trim())) || null);
  if (menu) {
    await S('m-nav-menu-btn', q('[data-m="mmenu"]'), ['default'], { group: g, title: 'Nav menu button (mobile)', desc: 'The menu button in the mobile header. Opened for the screenshot; nothing is followed.', sel: 'the menu button' }, { noScroll: true });
    await toggle(q('[data-m="mmenu"]')).catch(() => {});
    await page.waitForTimeout(1500);
    const sheet = await tag('msheet', () => {
      const cands = [...document.querySelectorAll('[role=dialog], [class*="menu" i], nav')].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.height > 200 && r.width > 200;
      });
      return cands[0] || null;
    });
    if (sheet) await S('m-nav-sheet', q('[data-m="msheet"]'), ['default'], { group: g, title: 'Mobile nav sheet', desc: 'The open navigation sheet at 390.', sel: 'the open menu' }, { noScroll: true });
  }
  const h1 = await tag('mh1', () => document.querySelector('h1'));
  if (h1) await S('m-hero-title', q('[data-m="mh1"]'), ['default'], { group: g, title: 'Hero title (mobile)', desc: 'The h1 at 390.', sel: 'h1' });
  await layoutFor('mobile-home');
  await page.close();
}

const PAGES = {
  home,
  news: () => indexPage('news', G.cards, 'News page title', 'news-card', 'News card: a linked post card in the news index.'),
  research: () => indexPage('research', G.cards, 'Research page title', 'research-card', 'Research entry: a linked paper/post in the research index.'),
  engineering: () => indexPage('engineering', G.cards, 'Engineering page title', 'engineering-card', 'Engineering entry: a linked post in the engineering index.'),
  product, 'platform-api': platformApi, pricing, 'contact-sales': contactSales,
  'docs-home': docsHome, 'docs-start': () => docsPage('docs-start'), 'docs-api': () => docsPage('docs-api'), mobile,
};

const want = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(PAGES);
const done = new Set(); // pages whose capture ran to the end
for (const k of want) {
  const isMobile = k === 'mobile';
  const l = await launch({ mobile: isMobile });
  context = l.context;
  run = k;
  try { await PAGES[k](); done.add(k); } catch (e) { log('PAGE FAILED', k, String(e.message).split('\n')[0]); }
  out._meta.read = new Date().toLocaleDateString('en-CA'); // the local date of the capture
  save();
  await l.browser.close();
}
// a component a page no longer produces is dropped, so a re-run cannot leave stale entries; a page that
// failed partway keeps its earlier entries, since what it did not reach is not known to be gone
for (const [key, c] of Object.entries(out.components)) if (done.has(c.run) && !touched.has(key)) { delete out.components[key]; log('dropped stale', key); }
save();
log('done ->', OUT);
