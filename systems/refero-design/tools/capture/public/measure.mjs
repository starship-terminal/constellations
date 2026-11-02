// Measures Refero's components on its public pages, in every state that can be
// reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home search apps pricing mcp overlay styles entity mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be re-run)
// and one crop per component and state into components/crops/. raw/measurements.md
// is then built from the JSON by build-measurements.mjs.
//
// Two surfaces, one package (see lib.mjs): refero.design is the product shell
// (fixed left sidebar, atomic hash classes), styles.refero.design the Tailwind
// gallery the repo's refero/ snapshot mirrors.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or submit button can fire
//   focused        the field clicked into (a text field only)
//   filled         sample text typed into a field, measured, then deleted; Enter is never pressed
//   anything else  a resting state reached by the page itself or by a UI toggle (a chip,
//                  a tab); nothing that submits research, starts a trial or signs in is
//                  ever pressed
import fs from 'node:fs';
import path from 'node:path';
import { BASE, STYLES, launch, open, closePromo, firstStyleHref, styleOf, crop, centre, markFixed, RAW } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

// URLS values are absolute paths on refero.design; 'STYLES-ENTITY' resolves to
// the first /style/<id> card on the styles index at run time.
const URLS = {
  home: '/', search: '/search', apps: '/apps/search', pricing: '/pricing', mcp: '/mcp',
  styles: 'STYLES:/', entity: 'STYLES-ENTITY', 'entity-deep': 'STYLES-ENTITY',
};
let entityHref = null;
const urlFor = (key) => {
  const u = URLS[key];
  if (u === 'STYLES-ENTITY') return entityHref ? STYLES + entityHref : STYLES + '/';
  if (u.startsWith('STYLES:')) return STYLES + u.slice(7);
  return BASE + u;
};

let page, cdp, current, context, run;
const touched = new Set();

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 6000 } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '', urlFor(key));
  await open(page, urlFor(key), { wait, promo });
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

// Clicks a UI toggle (a chip, a doc tab). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log in|create|generate|upload|search by image|explore mcp|connect mcp|get started|start free trial|upgrade|subscribe|open|share)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: URLS[current] && urlFor(current) }, meta);
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

const FILL = 'a calm banking app dashboard';

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
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
      } else if (st === 'video') {
        await (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000, force: true }).catch(() => {});
        await page.waitForTimeout(3000); // the preview video buffers over the CDN
        via = 'mouse hover, 3s, so the scroll-preview video loads';
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

// Depth of the nearest ancestor matching a JS predicate, so a locator can be
// built that re-resolves on every call. Refero hydrates/rotates parts of the
// tree, which detaches nodes tagged with data-m between tagging and measuring.
async function depthOf(sel, predSrc) {
  return page.evaluate(([s, src]) => {
    const f = new Function('el', 'return (' + src + ')(el)');
    const els = [...document.querySelectorAll(s)];
    for (const el of els) {
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) continue; // hidden inputs sit in this tree too
      let n = el;
      for (let d = 1; d <= 12 && n.parentElement; d++) { n = n.parentElement; if (f(n)) return d; }
    }
    return -1;
  }, [sel, predSrc]).catch(() => -1);
}
// First *visible* match for sel, climbed depth ancestors. Mirrors depthOf.
const up = (sel, depth) => page.locator(sel).filter({ visible: true }).first().locator('xpath=ancestor::*[' + depth + ']');
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Tags the first element matching an in-page probe so a locator can find it:
// await tag('sidebar', () => {...return element or null...}) then q('[data-m="sidebar"]').
async function tag(name, probe) {
  return page.evaluate(([n, src]) => {
    const el = (new Function('return (' + src + ')')())();
    if (!el) return false;
    el.setAttribute('data-m', n);
    return true;
  }, [name, probe.toString()]).catch(() => false);
}

// Tags the smallest element whose trimmed text matches reSrc inside scopeSel,
// preferring an interactive tag or a cursor:pointer box. Refero renders its
// buttons, chips and close controls as styled divs, so role selectors alone
// miss them.
async function tagEl(name, reSrc, scopeSel) {
  return page.evaluate(([n, src, scope]) => {
    const re = new RegExp(src, 'i');
    const sc = (scope && document.querySelector(scope)) || document;
    const cands = [...sc.querySelectorAll('a,button,[role=button],[role=tab],li,div,span')].filter((e) => {
      const t = (e.innerText || e.getAttribute('aria-label') || '').trim(); const r = e.getBoundingClientRect();
      return re.test(t) && t.length < 80 && r.width > 10 && r.height > 8;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    const el = cands.find((e) => e.matches('a,button,[role=button],[role=tab],li,[tabindex]') || getComputedStyle(e).cursor === 'pointer') || cands[0];
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

// ---------- groups ----------
const G = {
  shell: 'Shell and sidebar', home: 'Home and research', search: 'Search and galleries',
  pricing: 'Pricing', mcp: 'MCP page', overlay: 'Promos and overlays',
  styles: 'Styles gallery', entity: 'Style entity page', mobile: 'Mobile (390 wide)',
};

// ---------- refero.design ----------

async function home() {
  await newPage('home', { promo: 'keep' });
  await sheetsFor('home');
  const g = G.shell;

  // The left rail: a fixed column holding the logo, "New research" and the
  // destination links; a second fixed block at its foot holds the quiet links.
  const side = await tag('sidebar', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => {
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      return cs.position === 'fixed' && r.left <= 16 && r.top <= 16 && r.height > 500 && r.width > 100 && r.width < 340 && /New research/.test(e.innerText || '');
    });
    return cands.sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height)[0] || null;
  });
  const selside = 'the fixed left column holding the logo, New research and nav';
  if (side) {
    await S('sidebar', q('[data-m="sidebar"]'), ['default'], { group: g, title: 'Left sidebar', desc: 'Refero\u2019s shell: a fixed white left rail with the logo, the New research button and the destination links (Web apps, iOS apps, Styles, Pricing); a second fixed block at the foot holds the quiet links (Connect MCP, Figma Plugin, Log In/Sign Up).', sel: selside }, { noScroll: true });
    if (await tagEl('newr', 'New research', '[data-m="sidebar"]'))
      await S('side-new-research', q('[data-m="newr"]'), B4, { group: g, title: 'New research button', desc: 'The primary action in the sidebar. Measured and focused, never pressed: it would clear the current research session.', sel: selside + ' "New research"' }, { noScroll: true });
    if (await tagEl('navlink', '^web apps', '[data-m="sidebar"]'))
      await S('side-nav-link', q('[data-m="navlink"]'), B4, { group: g, title: 'Sidebar destination link', desc: 'A nav row in the left rail. Measured, never followed.', sel: selside + ' "Web apps"' }, { noScroll: true });
  }
  const foot = await tag('sidefoot', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => {
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      return cs.position === 'fixed' && r.bottom >= innerHeight - 4 && r.left <= 40 && /Sign Up/.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width)[0] || null;
  });
  if (foot && await tagEl('footlink', '^pricing', '[data-m="sidefoot"]'))
    await S('side-foot-link', q('[data-m="footlink"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Sidebar footer link', desc: 'A quiet link in the rail\u2019s bottom block (Pricing, Connect MCP, Figma Plugin, Log In/Sign Up).', sel: 'fixed bottom-left link column' }, { noScroll: true });

  const h = G.home;
  // The research box is the centred search card every page opens with: a
  // "Search by Image" upload affordance, a prompt field and the mode chips.
  const box = await tag('rbox', () => {
    const ta = document.querySelector('textarea, [contenteditable=true]');
    if (!ta) return null;
    let n = ta;
    for (let i = 0; i < 8 && n.parentElement; i++) { n = n.parentElement; if (/Research mode|Web apps/i.test(n.innerText || '') && n.getBoundingClientRect().width < innerWidth - 200) return n; }
    return ta.parentElement;
  });
  const selbox = 'the centred card holding the prompt field, upload and mode chips';
  if (box) {
    await S('research-box', q('[data-m="rbox"]'), ['default'], { group: h, title: 'Research box', desc: 'The centred search card refero.design opens every page with: a prompt field with a Search by Image upload affordance, mode chips (Research mode, Web apps, iOS apps) and a submit.', sel: selbox });
    await S('research-input', q('[data-m="rbox"]').locator('textarea, [contenteditable=true]').first(), ['default', 'focus-visible'], { group: h, title: 'Research prompt field', sel: selbox + ' textarea' }, { crop: false });
    await S('research-box-state', q('[data-m="rbox"]'), ['focused', 'filled'], { group: h, title: 'Research box, field active', desc: 'The same card with the prompt clicked into and sample text typed, then deleted; nothing was submitted.', sel: selbox }, { fieldLoc: q('[data-m="rbox"]').locator('textarea, [contenteditable=true]').first() });
    if (await tagEl('rchip', '^(web apps|ios apps)$', '[data-m="rbox"]'))
      await S('research-chip', q('[data-m="rchip"]'), B4, { group: h, title: 'Mode chip', desc: 'One of the research-box scope chips (Research mode / Web apps / iOS apps). Pressed states are forced, not clicked: a real press switches the corpus.', sel: 'a mode chip in the research box' });
    const up = await tag('rupload', () => {
      const scope = document.querySelector('[data-m="rbox"]') || document;
      return [...scope.querySelectorAll('button, [role=button], div')].filter((b) => /search by image|drag|upload/i.test(b.innerText || b.getAttribute('aria-label') || '')).sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width)[0] || null;
    });
    if (up) await S('research-upload', q('[data-m="rupload"]'), ['default', 'hover', 'focus-visible'], { group: h, title: 'Search by Image affordance', desc: 'The image-search affordance in the research box. Hovered and focused only; no file was chosen.', sel: 'the upload affordance in the research box' });
  }
  await S('hero-title', q('h1').first(), ['default'], { group: h, title: 'Hero title', desc: '"Design Research for the AI Era" \u2014 the display line the home page opens with.', sel: 'main h1' }, { noScroll: true });
  await S('hero-sub', q('h1').first().locator('xpath=following::*[self::p or self::div][string-length(normalize-space())>30][1]').first().or(q('h1').locator('..').locator('p').first()), ['default'], { group: h, title: 'Hero subline', sel: 'the paragraph under main h1' }, { crop: false, noScroll: true });
  await S('section-title', q('h2').filter({ hasText: 'Page Types' }).first().or(q('h2').first()), ['default'], { group: h, title: 'Section title', desc: 'A home section head (Page Types, Flows, UX Patterns, UI Elements, Sites).', sel: 'h2 "Page Types"' });
  // The first card of the "Page Types" section: the section is the h2's
  // grandparent (a UL chip row and the card grid are its siblings); cards are
  // grid items holding a screenshot tile and a name. Tag it, scroll it into
  // view inside the probe so the measurement finds it painted.
  // The whole section re-renders on the hero rotation timer, so nothing in it
  // can hold a data-m tag. Resolve from the h2 down: nearest ancestor holding
  // an <img> is the section; its first child with an <img> inside is the card
  // grid; the grid's first child is the first card.
  const ptH2 = page.getByRole('heading', { name: 'Page Types' }).first().or(page.locator('h2').first());
  const ptSec = ptH2.locator('xpath=ancestor::*[.//img][1]');
  const cardLoc = ptSec.locator('xpath=./*[.//img]').first().locator('xpath=./*[1]');
  await S('result-card', cardLoc, B4, { group: h, title: 'Result card', desc: 'A gallery card on the home page: a screenshot tile in a rounded padded card with a title under it. Measured, never followed.', sel: 'first card under the Page Types section' });
  await S('result-card-title', cardLoc.locator('xpath=.//*[not(*) and normalize-space(.)]').last(), ['default'], { group: h, title: 'Result card label', sel: 'text under the card tile' }, { crop: false });
  await page.close();
}

async function search() {
  await newPage('search');
  const g = G.search;
  const box = await tag('rbox', () => {
    const ta = document.querySelector('textarea, [contenteditable=true], input[type=text], input:not([type])');
    if (!ta) return null;
    let n = ta;
    for (let i = 0; i < 8 && n.parentElement; i++) { n = n.parentElement; if (/Web apps/i.test(n.innerText || '') && n.getBoundingClientRect().width < innerWidth - 200) return n; }
    return ta.parentElement;
  });
  if (box) {
    await S('search-box', q('[data-m="rbox"]'), ['default', 'focused'], { group: g, title: 'Search box (results page)', desc: 'The same research card pinned above the results on /search.', sel: 'research card on /search' }, { fieldLoc: q('[data-m="rbox"]').locator('textarea, [contenteditable=true], input').first() });
  }
  // A result card in the /search grid: the screenshot tile plus the
  // favicon-and-name label under it; the label alone is ~19px, the card ~200px.
  const t = await tag('stile', () => {
    const cands = [...document.querySelectorAll('a, div, li')].filter((x) => {
      const r = x.getBoundingClientRect();
      return x.querySelector('img') && r.width > 200 && r.height > 140 && r.height < 400 && r.top > 120;
    });
    const el = cands.sort((a, b) => a.getBoundingClientRect().y - b.getBoundingClientRect().y || a.getBoundingClientRect().x - b.getBoundingClientRect().x)[0];
    if (el) el.scrollIntoView({ block: 'center' });
    return el || null;
  });
  if (t) await S('search-tile', q('[data-m="stile"]'), ['default', 'hover'], { group: g, title: 'Search result tile', desc: 'A result card in the /search grid: a padded tile with a screen image and a favicon-and-name label. Hovered only.', sel: 'first result tile in the grid' });
  await page.close();
}

async function apps() {
  await newPage('apps');
  const g = G.search;
  const t = await tag('atile', () => {
    const cands = [...document.querySelectorAll('a, div, li')].filter((x) => {
      const r = x.getBoundingClientRect();
      return x.querySelector('img') && r.width > 100 && r.width < 320 && r.height > 140 && r.top > 120;
    });
    const el = cands.sort((a, b) => a.getBoundingClientRect().y - b.getBoundingClientRect().y || a.getBoundingClientRect().x - b.getBoundingClientRect().x)[0];
    if (el) el.scrollIntoView({ block: 'center' });
    return el || null;
  });
  if (t) await S('ios-tile', q('[data-m="atile"]'), ['default', 'hover'], { group: g, title: 'iOS app tile', desc: 'A phone-shaped app card in the iOS gallery: a tall rounded screenshot tile. Hovered only.', sel: 'first app card in the iOS grid' });
  await page.close();
}

async function pricing() {
  await newPage('pricing');
  const g = G.pricing;
  await S('pricing-title', q('h1').first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1 "Pricing"' }, { noScroll: true });
  const pc = await tag('pcard', () => {
    const cands = [...document.querySelectorAll('main *, body *')].filter((e) => {
      const r = e.getBoundingClientRect(), t = (e.innerText || '');
      return r.width > 240 && r.width < 560 && r.height > 200 && /\$\d|month|year|free/i.test(t) && e.querySelector('button, a');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width || a.innerText.length - b.innerText.length).filter((e) => !cands.some((o) => o !== e && e.contains(o)))[0] || null;
  });
  if (pc) {
    await S('plan-card', q('[data-m="pcard"]'), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card: name, price, feature list and a call-to-action button.', sel: 'first pricing plan card' });
    const cta = await tag('pcta', () => {
      const card = document.querySelector('[data-m="pcard"]');
      return card && [...card.querySelectorAll('button, a')].filter((b) => (b.innerText || '').trim().length > 1 && (b.innerText || '').trim().length < 40).pop() || null;
    });
    if (cta) await S('plan-cta', q('[data-m="pcta"]'), ['default', 'hover', 'focus-visible', 'pressed'], { group: g, title: 'Plan CTA button', desc: 'The call-to-action inside a plan card. Pressed state is forced; a real press would start checkout.', sel: 'button in the plan card' });
  }
  const dc = await tag('dcard', () => {
    const h = [...document.querySelectorAll('h2, h3')].find((x) => /Student discount/i.test(x.innerText));
    if (!h) return null;
    let n = h;
    while (n.parentElement && n.getBoundingClientRect().width < 320) n = n.parentElement;
    return n;
  });
  if (dc) await S('discount-card', q('[data-m="dcard"]'), ['default'], { group: g, title: 'Student discount card', desc: 'The info card beside the plans (Student discount / Enterprise / Integrate Refero).', sel: 'the Student discount card' });
  await page.close();
}

async function mcp() {
  await newPage('mcp');
  const g = G.mcp;
  await S('mcp-title', q('h1').first(), ['default'], { group: g, title: 'MCP title', desc: '"Give your AI agent design taste" \u2014 the /mcp hero.', sel: 'main h1' }, { noScroll: true });
  const step = await tag('mstep', () => {
    const h = [...document.querySelectorAll('h2')].find((x) => /install/i.test(x.innerText));
    if (!h) return null;
    let n = h.parentElement;
    return [...n.querySelectorAll('pre, code, [class*=code]')].find((e) => e.getBoundingClientRect().width > 200) || null;
  });
  if (step) await S('mcp-code', q('[data-m="mstep"]'), ['default'], { group: g, title: 'Install code block', desc: 'A copyable install command block in the "How to install MCP" section.', sel: 'code block under the install section' });
  const cb = await tag('mcta', () => {
    const h = [...document.querySelectorAll('h2')].find((x) => /install/i.test(x.innerText));
    const scope = h ? h.parentElement : document;
    return [...scope.querySelectorAll('button, [role=button]')].find((b) => /copy/i.test(b.innerText || b.getAttribute('aria-label') || '')) || null;
  });
  if (cb) await S('mcp-copy', q('[data-m="mcta"]'), B4, { group: g, title: 'Copy install command button', sel: 'copy button beside an install command' });
  await page.close();
}

// The promo surfaces get their own run so the measured page still shows them:
// the bottom-left "Refero MCP" card and, on a fresh profile, the coach box
// over the research input.
async function overlay() {
  await newPage('home', { promo: 'keep' });
  const g = G.overlay;
  const card = await tag('mcpcard', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => {
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      return cs.position === 'fixed' && r.top > 200 && r.top < innerHeight - 100 && r.width > 200 && r.width < 520 && /MCP/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
  });
  if (card) {
    await S('mcp-card', q('[data-m="mcpcard"]'), ['default'], { group: g, title: 'Refero MCP promo card', desc: 'The floating card pinned over the content: "Refero MCP connects your agent to a curated library\u2026" with an Explore MCP button and a Close.', sel: 'the fixed MCP promo card' }, { noScroll: true });
    if (await tagEl('mcpcta', 'Explore MCP', '[data-m="mcpcard"]'))
      await S('mcp-card-cta', q('[data-m="mcpcta"]'), B4, { group: g, title: 'Explore MCP button', desc: 'The dark button in the promo card. Measured and focused, never pressed.', sel: '"Explore MCP" in the promo card' }, { noScroll: true });
    if (await tagEl('mcpclose', '^close$', '[data-m="mcpcard"]'))
      await S('mcp-card-close', q('[data-m="mcpclose"]'), B4, { group: g, title: 'Promo card Close button', desc: 'Dismisses the card (a styled div, not a button). Measured, never pressed: closing happens after the measurements.', sel: '"Close" in the promo card' }, { noScroll: true });
  }
  const coach = await tag('coach', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => /Meet new research mode/i.test(e.innerText || '') && (e.innerText || '').length < 500 && [...e.querySelectorAll('svg')].some((s) => getComputedStyle(s).cursor === 'pointer'));
    return cands.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0] || null;
  });
  if (coach) {
    await S('coach-box', q('[data-m="coach"]'), ['default'], { group: g, title: 'Research-mode coach box', desc: 'The "Meet new research mode" coach a fresh profile shows once over the research input.', sel: 'the research-mode coach box' }, { noScroll: true });
    const x = await tag('coachx', () => { const c = document.querySelector('[data-m="coach"]'); return c && [...c.querySelectorAll('svg')].find((s) => getComputedStyle(s).cursor === 'pointer') || null; });
    if (x) await S('coach-close', q('[data-m="coachx"]'), ['default', 'hover'], { group: g, title: 'Coach close X', desc: 'The dismissal: a bare 24px svg with cursor:pointer, not a button. Measured and hovered, never clicked.', sel: 'the X svg in the coach box' }, { noScroll: true });
  }
  await closePromo(page);
  await page.close();
}

// ---------- styles.refero.design ----------

async function styles() {
  await newPage('styles');
  await sheetsFor('styles-index');
  const g = G.styles;
  await S('styles-header', q('header').first(), ['default'], { group: g, title: 'Styles header', desc: 'The sticky translucent bar: logo, section links and the sign-in on styles.refero.design.', sel: 'header' }, { noScroll: true });
  await S('styles-hero', q('h1').first().locator('..').first().or(q('main').locator('> *').first()), ['default'], { group: g, title: 'Gallery hero', desc: 'The serif violet display headline and search the index opens with.', sel: 'index hero block' }, { noScroll: true });
  await S('styles-hero-title', q('h1').first(), ['default'], { group: g, title: 'Gallery headline', desc: 'The kalice serif display line, set in violet.', sel: 'index h1' }, { noScroll: true });
  const si = await tag('sinput', () => document.querySelector('input[type=search], input[placeholder], input') || null);
  if (si) {
    await tag('sinputbox', () => { let n = document.querySelector('[data-m="sinput"]'); for (let k = 0; k < 5 && n.parentElement && n.getBoundingClientRect().width < innerWidth - 500; k++) n = n.parentElement; return n; });
    await S('styles-search', q('[data-m="sinput"]'), ['default', 'focused', 'filled'], { group: g, title: 'Search field', desc: 'The rounded search pill under the headline. Sample text was typed and deleted.', sel: 'the search input and its pill' }, { fieldLoc: q('[data-m="sinput"]'), cropLoc: q('[data-m="sinputbox"]'), fillText: 'linear' });
  }
  const chip = await tag('schip', () => {
    const cands = [...document.querySelectorAll('a, button, [role=button], div, span')].filter((b) => {
      const t = (b.innerText || '').trim(); const r = b.getBoundingClientRect();
      return t.length >= 2 && t.length <= 26 && r.top > 90 && r.top < 560 && r.width >= 40 && r.width <= 280 && e0(b);
      function e0(x) { return getComputedStyle(x).borderRadius !== '0px' || getComputedStyle(x).cursor === 'pointer' || x.matches('a,button,[role=button]'); }
    });
    const el = cands.sort((a, b) => a.innerText.length - b.innerText.length)[0];
    return el || null;
  });
  if (chip) await S('styles-chip', q('[data-m="schip"]'), B4, { group: g, title: 'Filter chip', desc: 'A prompt/filter chip under the search. Pressed state is forced, not clicked: a real press applies the filter.', sel: 'a chip under the search' });
  const card = await tag('scard', () => [...document.querySelectorAll('a[href^="/style/"]')].find((x) => x.getBoundingClientRect().width > 100) || null);
  if (card) {
    await S('styles-card', q('[data-m="scard"]'), ['default', 'focus-visible'], { group: g, title: 'Style card', desc: 'A gallery card: a padded rounded tile holding the site screenshot, a footer with the site\u2019s favicon, name and tagline.', sel: 'a[href^="/style/"]' });
    await S('styles-card-video', q('[data-m="scard"]'), ['video'], { group: g, title: 'Style card, video playing', desc: 'On hover the tile\u2019s screenshot gives way to a scroll-through video of the site, streamed from images.refero.design.', sel: 'a[href^="/style/"] on hover', via: 'mouse hover, 3s' });
    const fav = await tag('sfav', () => {
      const c = document.querySelector('[data-m="scard"]');
      return c && c.querySelector('img[width], img') || null;
    });
    if (fav) await S('styles-card-favicon', q('[data-m="scard"]').locator('img').last(), ['default'], { group: g, title: 'Card footer favicon', desc: 'The site\u2019s favicon in the card footer, ~32px in a small rounded tile.', sel: 'favicon img in the card footer' });
  }
  await page.close();
}

async function entity() {
  await newPage('entity', { wait: 8000 }); // the page video buffers, then fades in
  await sheetsFor('entity');
  const g = G.entity;
  const frame = await tag('eframe', () => {
    const v = document.querySelector('video');
    if (v) { let n = v; while (n.parentElement && n.getBoundingClientRect().width < 300) n = n.parentElement; return n; }
    return [...document.querySelectorAll('main img, img')].filter((i) => i.getBoundingClientRect().width > 300)[0] || null;
  });
  if (frame) await S('entity-frame', q('[data-m="eframe"]'), ['default'], { group: g, title: 'Media frame', desc: 'The large rounded frame over the page: the site\u2019s scroll video fades in over the poster still, border and shadow around it.', sel: 'the video and its rounded frame' }, { noScroll: true });
  await S('entity-title', q('h1').first(), ['default'], { group: g, title: 'Style name', desc: 'The site\u2019s name in the kalice display serif, next to its round favicon.', sel: 'entity h1' }, { noScroll: true });
  const fav = await tag('efav', () => {
    const h = document.querySelector('h1');
    if (!h) return null;
    let n = h.parentElement;
    for (let i = 0; i < 4 && n; i++, n = n.parentElement) { const im = n.querySelector('img'); if (im && im.getBoundingClientRect().width < 100) return im; }
    return null;
  });
  if (fav) await S('entity-favicon', q('[data-m="efav"]'), ['default'], { group: g, title: 'Style favicon', desc: 'The site\u2019s favicon in a bordered circle beside the name.', sel: 'favicon beside h1' }, { noScroll: true });
  const tabs = await tagEl('etab', 'Tailwind|CSS Variables|Design Tokens');
  if (tabs) {
    await S('entity-tab', q('[data-m="etab"]'), B4, { group: g, title: 'Doc tab', desc: 'A tab in the documentation pane (DESIGN.md, Tailwind v4, CSS Variables, Design Tokens). Pressed is forced; a real press switches the document.', sel: 'a tab in the doc pane' });
    // The tab list re-renders (it exists twice, per breakpoint); select the
    // aria-selected button live instead of tagging a node that may detach.
    // No .first(): S filters to the visible one (the tab row renders twice,
    // once per breakpoint).
    const activeLoc = q('button[aria-selected="true"]');
    if (await activeLoc.count()) await S('entity-tab-active', activeLoc, ['default', 'focus-visible'], { group: g, title: 'Doc tab, current', desc: 'The selected tab (DESIGN.md) is measured at rest: it is the tab the page opens on.', sel: 'the selected doc tab' });
  }
  if (await tagEl('ecopy', '^copy$')) await S('entity-copy', q('[data-m="ecopy"]'), B4, { group: g, title: 'Copy button', desc: 'Copies the open document. Measured, never pressed.', sel: '"Copy" in the doc pane' });
  const sw = await tag('esw', () => {
    return [...document.querySelectorAll('main *, body *')].filter((e) => { const cs = getComputedStyle(e), r = e.getBoundingClientRect(); return r.width >= 24 && r.width <= 80 && Math.abs(r.width - r.height) < 4 && cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && !e.children.length; }).filter((e) => e.getBoundingClientRect().top > 300)[0] || null;
  });
  if (sw) await S('entity-swatch', q('[data-m="esw"]'), ['default', 'hover'], { group: g, title: 'Colour swatch', desc: 'A palette swatch in the Colors section; hover raises a Copy pill.', sel: 'a colour swatch tile' });
  const sim = await tag('esim', () => {
    const h = [...document.querySelectorAll('h2, h3')].find((x) => /similar/i.test(x.innerText));
    const scope = h ? h.parentElement : document;
    return [...scope.querySelectorAll('a')].find((x) => x.querySelector('img') && x.getBoundingClientRect().width > 100) || null;
  });
  if (sim) await S('entity-similar', q('[data-m="esim"]'), ['default', 'hover'], { group: g, title: 'Similar style card', desc: 'A card in the Similar styles row at the foot of the page.', sel: 'a similar-styles card' });
  await page.close();
}

// ---------- mobile ----------
async function mobile() {
  const g = G.mobile;
  await newPage('home', { mobile: true, promo: 'keep' });
  await closePromo(page);
  const menu = await page.evaluate(() => { const b = [...document.querySelectorAll('button, [role=button]')].find((e) => { const r = e.getBoundingClientRect(); return r.top < 60 && r.width >= 20 && r.width <= 60 && e.querySelector('svg'); }); if (b) b.setAttribute('data-m', 'm-menu'); return !!b; });
  if (menu) await S('m-menu-button', q('[data-m="m-menu"]'), ['default'], { group: g, title: 'Mobile menu button', sel: 'top bar menu button' }, { noScroll: true });
  // Hydration swaps the input node; resolve it live and climb to the card
  // ancestor each time rather than tagging a node. The mobile card is flat
  // (no border/shadow), so anchor on the <form> first, then a wide rounded box.
  const mSel = 'main textarea, main input, main [contenteditable], body textarea, body input, body [contenteditable]';
  let rd = await depthOf(mSel, 'function (el) { return el.tagName === "FORM"; }');
  if (rd < 0) rd = await depthOf(mSel, 'function (el) { const s = getComputedStyle(el); const r = el.getBoundingClientRect(); return r.width > 240 && r.height > 40 && parseFloat(s.borderRadius) >= 4; }');
  if (rd > 0) {
    const loc = up(mSel, rd);
    await loc.scrollIntoViewIfNeeded().catch(() => {});
    await S('m-research-box', loc, ['default'], { group: g, title: 'Research box (mobile)', sel: 'the research card at 390 wide' });
  } else log('  ! missing m-research-box (no input ancestor)');
  await page.close();
  await newPage('styles', { mobile: true });
  const card = await tag('scard', () => [...document.querySelectorAll('a[href^="/style/"]')].find((x) => x.getBoundingClientRect().width > 100) || null);
  if (card) await S('m-styles-card', q('[data-m="scard"]'), ['default'], { group: g, title: 'Style card (mobile)', sel: 'a[href^="/style/"] at 390 wide' });
  await S('m-styles-header', q('header').first(), ['default'], { group: g, title: 'Styles header (mobile)', sel: 'header at 390 wide' }, { noScroll: true });
  await page.close();
}

const PAGES = { home, search, apps, pricing, mcp, overlay, styles, entity, mobile };
const want = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(PAGES);
// resolve the entity page once, from the styles index
{
  const l0 = await launch();
  const p0 = await l0.context.newPage();
  entityHref = await firstStyleHref(p0);
  log('entity page:', entityHref || '(index only)');
  await l0.browser.close();
}
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
