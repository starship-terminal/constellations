// Measures grow.google's signed-out public components in every state
// reachable without signing in, enrolling or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home certificates certux ai mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// grow.google is Google's glue marketing framework (classes glue-header,
// glue-btn, glue-card, glue-expansion-panel, glue-footer), light-only — no
// theme toggle, no dark media query. Like public.mjs it runs the US
// edition: grow.google 302s a request that announces a real user agent or
// an explicit locale to the regional /intl/<locale>/ edition, so every
// context here is bare (no userAgent, no locale). Deep links are never
// redirected; / and /certificates/ are.
//
// Nothing is sent, enrolled in, or signed into: the only activations are
// local UI toggles — the "Career Certificates" header mega-menu (a click
// toggle), a glue-expansion-panel FAQ row, and the phone's navigation
// drawer button. Buttons and links are measured, never followed; the
// footer's lang-selector <select> is measured, never changed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', certificates: '/certificates', 'cert-ux': '/certificates/ux-design/',
  ai: '/ai/', mobile: '/',
};
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes an edge block gates this run: components last measured on them keep
// their earlier readings instead of being pruned below (a blocked pass must
// never erase evidence).
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
  // Bare contexts, same as the screenshot pass: a real user agent or an
  // explicit locale is 302'd to the regional /intl/<locale>/ edition.
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  let loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    // Keep earlier evidence under its own provenance: the states stay but the
    // entry keeps its original page/run/url and records the miss, so a re-run
    // never republishes old readings under a new date.
    if (!has) out.components[key].missing = true;
    else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
    return;
  }
  // A broad selector re-resolves against the live DOM on every use, so an
  // overlay that mounts mid-run can swap the node a state reads. opts.pin
  // marks the resolved element once and every state below measures that same
  // node.
  if (opts.pin) {
    await loc.evaluate((el) => el.setAttribute('data-m-pin', '1')).catch(() => {});
    loc = page.locator('[data-m-pin="1"]').first();
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
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc).filter({ visible: true }).first();
        if (opts.focusInner) {
          // A control whose label click toggles it (a checkbox) focuses its
          // inner input directly — never clicked, never toggled.
          await fld.evaluate((el) => {
            const t = el.matches('input,textarea,select') ? el : (el.querySelector('input,textarea,select') || el);
            t.focus();
          });
          await page.waitForTimeout(400);
          via = 'focused the inner input via .focus() — never clicked (a label click would check the box)';
        } else {
          await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
          await page.waitForTimeout(400);
          via = 'clicked into the field';
        }
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        // A before.opened callback already toggled the control open — a second
        // generic click would close it again before the reading.
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else if (!via) { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
        const exp = await loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null);
        if (exp !== null) via = (via || 'opened') + (exp === 'true' ? ' (aria-expanded=true at save)' : ' (aria-expanded=false at save — the open did not hold)');
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  if (opts.pin) await page.evaluate(() => document.querySelectorAll('[data-m-pin]').forEach((n) => n.removeAttribute('data-m-pin'))).catch(() => {});
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again|start for free|try for free|book a demo|start free trial|start planning|restore|send reset|reset password|send reset link|next|book \d+ service.*|book now)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// The first element matching `sel` whose trimmed text is at least `min` chars
// (hasText cannot express a trimmed length — /\S{20,}/ means twenty
// *consecutive* non-space characters, which no normal paragraph matches).
const p20 = async (sel, min = 20) => {
  const all = q(sel).filter({ visible: true });
  const n = Math.min(await all.count(), 25);
  for (let i = 0; i < n; i++) {
    const el = all.nth(i);
    const box = await el.boundingBox().catch(() => null);
    if (!box || box.width < 40 || box.height < 8) continue; // a11y-only text, hidden duplicates
    const t = ((await el.innerText().catch(() => '')) || '').trim();
    if (t.length >= min) return el;
  }
  return all.first();
};

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
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, reducedMotion: 'reduce' });
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
  shell: 'Site chrome', home: 'Home', certs: 'Certificates', cert: 'Certificate detail',
  ai: 'AI training', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the "Career Certificates" header mega-menu — a click toggle on the
// visible .glue-header__item.dropdown anchor (hidden duplicate li's share
// the text; hover does nothing; the anchor reports aria-expanded once
// opened). A local UI toggle; the opened panel's links are measured, never
// followed.
async function openMega() {
  const opened = async () => page.evaluate(() => !!document.querySelector('.glue-header__item.dropdown a[aria-expanded="true"], .glue-header__item.dropdown[aria-expanded="true"]')).catch(() => false);
  if (await opened()) return 'the "Career Certificates" menu was already open';
  for (let i = 0; i < 3; i++) {
    await page.evaluate(() => {
      const li = [...document.querySelectorAll('.glue-header__item.dropdown')].find((l) => /Career Certificates/.test(l.innerText || '') && l.getBoundingClientRect().width > 50);
      if (li) li.querySelector('a').click();
    }).catch(() => {});
    await page.waitForTimeout(1200);
    if (await opened()) return 'clicked the "Career Certificates" trigger; the mega-menu is open';
  }
  return 'clicked the "Career Certificates" trigger; the menu did not report open';
}

// Opens one glue-expansion-panel FAQ row on a certificate page: a click on
// the panel's header toggles it (aria-expanded flips on the button).
async function openPanel(loc) {
  const head = loc.locator('.glue-expansion-panel-header, [class*="expansion"] button, .glue-expansion-panel button').first();
  const btn = (await head.count()) ? head : loc;
  await btn.click({ timeout: 4000 }).catch(() => btn.evaluate((el) => el.click()));
  await page.waitForTimeout(1000);
  const exp = await loc.evaluate((el) => el.getAttribute('aria-expanded') || (el.querySelector('[aria-expanded]') || {}).getAttribute?.('aria-expanded')).catch(() => null);
  return `clicked the expansion-panel header${exp === 'true' ? ' (aria-expanded=true at save)' : ''}`;
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('.glue-header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The glue top bar: the "Grow with Google" wordmark, the Career Certificates / AI Training / For Partners / Stories & Resources nav and its dropdown mega-menus.', sel: '.glue-header' }, { noScroll: true });
  await S('header-logo', q('.glue-header__bar--desktop .glue-header__logo-link').filter({ visible: true }).first(), B4, { group: g, title: 'Logo', desc: 'The "Grow with Google" lockup in the header (a .glue-header__logo-link anchor in the desktop bar — the Google mark plus the "Grow with Google" img wordmark, 210x48; the mobile bar carries a second display:none copy).', sel: '.glue-header__bar--desktop .glue-header__logo-link' }, { noScroll: true });
  await S('nav-link', await domFind(page, /^AI Training$/i, { sel: '.glue-header a', tag: 'nl', minW: 40, minH: 14 }), B4, { group: g, title: 'Nav link', desc: 'A header nav link (AI Training); measured, never followed.', sel: 'header nav link' }, { noScroll: true });
  await S('nav-drop-trigger', await domFind(page, /^Career Certificates$/i, { sel: '.glue-header__item.dropdown a, .glue-header a', tag: 'nd', minW: 60, minH: 14 }), [...B4, 'opened'], { group: g, title: 'Mega-menu trigger', desc: 'The "Career Certificates" nav item that opens the three-column mega-menu (Foundational / Advanced / Courses). opened was measured after clicking it — a local UI toggle.', sel: 'header dropdown trigger' }, { noScroll: true, before: { opened: openMega } });
  await S('mega-panel', q('.glue-header__item.dropdown [class*="dropdown"], .glue-header__item.dropdown ul').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mega-menu panel', desc: 'The opened mega-menu panel: Foundational, Advanced and Courses columns.', sel: 'header dropdown panel' }, { noScroll: true, open: openMega, noReset: true });
  await S('mega-item', await domFind(page, /^UX Design$|^Data Analytics$/i, { sel: 'a', tag: 'mi', minW: 30, minH: 10 }), B4, { group: g, title: 'Mega-menu item', desc: 'A certificate link inside the opened mega-menu; measured while the menu was held open, never followed.', sel: 'mega-menu link' }, { noScroll: true, open: openMega, noReset: true });
  // Close the menu: left open, its panel would overlay (and be captured in)
  // every later crop.
  await page.keyboard.press('Escape');
  await page.waitForTimeout(600);
  // The promo banner is one anchor: the "New! Enroll in the AI Certificate…"
  // copy sits in a span.anchorText inside an <a> that also carries the
  // "Enroll now →" tail.
  await S('promo-banner', await domFind(page, /Enroll in the AI Certificate|vibe coding/i, { sel: 'a', tag: 'pb', leaf: false, up: 'p, div', minW: 300, minH: 20 }), B4, { group: G.home, title: 'Promo banner', desc: 'The blue "New! Enroll in the AI Certificate and learn vibe coding…" promotion banner under the header — the whole banner is one anchor.', sel: 'promo banner' });
  await S('promo-link', await domFind(page, /Enroll now/i, { sel: 'a, span.anchorText, span, [class*="anchor"]', tag: 'pl', minW: 40, minH: 14 }), B4, { group: G.home, title: 'Promo link', desc: 'The banner\'s "Enroll now →" tail; measured, never followed.', sel: 'promo Enroll now' });
  const gh = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: gh, title: 'Hero headline', desc: 'The home display heading.', sel: 'home h1' }, { noScroll: true });
  await S('hero-cta', await domFind(page, /^Get started$|^Learn more$/i, { sel: 'a.glue-button--high-emphasis, a.glue-button, a[class*="glue-button"], .glue-button', tag: 'hc', minW: 60, minH: 20 }), B4, { group: gh, title: 'Hero CTA', desc: 'The hero\'s blue pill action (glue-button--high-emphasis); measured, never followed.', sel: '.glue-button--high-emphasis' });
  await S('video-teaser', q('.glue-video.glue-modal__trigger, .glue-video__preview-container').filter({ visible: true }).first(), B4, { group: gh, title: 'Video teaser', desc: 'The hero video preview with the 48px play overlay; clicking it opens a glue-modal carrying a YouTube embed. Measured at rest; the modal was screenshotted in the capture pass and closed.', sel: '.glue-video' });
  await S('h2', q('h2').filter({ visible: true }).first(), ['default'], { group: gh, title: 'Section heading', desc: 'A section heading on the marketing home.', sel: 'home h2' });
  await S('body-p', await p20('main p, section p, p', 40), ['default'], { group: gh, title: 'Body paragraph', desc: 'A body paragraph on the marketing home.', sel: 'home p' });
  await S('card', await p20('.glue-card, [class*="card"]', 15), ['default', 'hover'], { group: gh, title: 'Content card', desc: 'A bordered content card on the home (the "New vibe coding course…" announcement cards).', sel: '.glue-card' }, { pin: true });
  await S('card-link', await domFind(page, /learn more/i, { sel: '.glue-card a, [class*="card"] a, a', tag: 'cl', minW: 40, minH: 12 }), B4, { group: gh, title: 'Card link', desc: 'The "Learn more →" link inside a card; measured, never followed.', sel: 'card Learn more' });
  await S('footer', q('.glue-footer, footer').filter({ visible: true }).last(), ['default'], { group: G.footer, title: 'Footer', desc: 'The marketing footer: link columns, social marks, legal links and the locale <select>.', sel: '.glue-footer' });
  await S('footer-link', await domFind(page, /privacy|terms|about google/i, { sel: '.glue-footer a, footer a', tag: 'fl', minW: 20, minH: 10 }), B4, { group: G.footer, title: 'Footer link', desc: 'A footer link; measured, never followed.', sel: 'footer link' });
  await S('footer-lang', q('select[name="lang-selector"], .glue-footer select').filter({ visible: true }).first(), B4, { group: G.footer, title: 'Locale select', desc: 'The footer region/language <select>; measured, never changed — its form posts to services.google.com.', sel: 'footer select' });
  save();
}

async function certificates() {
  if (!(await newPage('certificates'))) return;
  await sheetsFor('certificates');
  const g = G.certs;
  await S('breadcrumb', await domFind(page, /^Grow with Google$/i, { sel: 'a', tag: 'br', minW: 60, minH: 12 }), B4, { group: g, title: 'Breadcrumb link', desc: 'The "Grow with Google" link opening the breadcrumb trail above the catalog heading.', sel: 'breadcrumb link' }, { noScroll: true });
  await S('eyebrow', q('.glue-eyebrow, [class*="eyebrow"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Eyebrow', desc: 'The "GOOGLE CAREER CERTIFICATES" eyebrow over the page heading.', sel: '.glue-eyebrow' });
  await S('certs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Certificates headline', desc: '"Job-ready skills you can put to work" — the catalog display heading with a coloured first phrase.', sel: 'certificates h1' });
  await S('stat-chip', await domFind(page, /mos|%|\$|\dM/i, { sel: '.bsp-statistics__number, [class*="bsp-statistics"]', tag: 'sc', minW: 40, minH: 20 }), ['default'], { group: g, title: 'Stat number', desc: 'A coloured stat figure in the certificates statistics band (3-6 mos / 70%+ / $102,000+ / 1.7M+ — red, blue, yellow and green numbers over captions).', sel: '.bsp-statistics__number' });
  await S('learn-more-btn', q('a.glue-button, .glue-button, a, button').filter({ hasText: /^Learn more/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Learn more button', desc: 'The blue pill "Learn more ↓" anchor that scrolls to the catalog; measured, never followed.', sel: 'Learn more button' });
  await S('tab-bar', q('.glue-jumplinks__list, .glue-jumplinks, [class*="jumplinks"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section tabs', desc: 'The pill tab bar (Overview / Professional Certificates / Path to jobs / AI training / FAQs) — glue-jumplinks in-page anchors.', sel: '.glue-jumplinks__list' });
  await S('tab', q('a.glue-jumplinks__link, .glue-jumplinks a').filter({ visible: true }).first(), B4, { group: g, title: 'Tab item', desc: 'One pill tab in the jumplinks bar; measured, never followed.', sel: '.glue-jumplinks__link' });
  await S('cert-card', await domFind(page, /^Cybersecurity$|^IT Support$|^Digital Marketing/i, { sel: 'h2, h3, h4, [class*="title"], a, div', tag: 'cc2', up: '[class*="glue-grid__col"], [class*="card"], article, li', minW: 200, minH: 150 }), ['default', 'hover'], { group: g, title: 'Certificate card', desc: 'A certificate card in the "Foundational certificates" grid — a glue-grid__col cell painted as a white rounded card on the light-blue band: icon, title, rating, blurb, "If you like:" line and a "Get started on Coursera" pill.', sel: 'certificate card' }, { pin: true });
  save();
}

async function certux() {
  if (!(await newPage('cert-ux'))) return;
  await sheetsFor('cert-ux');
  const g = G.cert;
  await S('cert-hero', q('section, [class*="hero"], .bsp-hero').filter({ has: q('h1') }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Dark hero', desc: 'The certificate page\'s dark hero band — an editorial dark section on a light-only site.', sel: 'cert hero' }, { noScroll: true });
  await S('cert-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Certificate headline', desc: '"Google UX Design Certificate" — white display type on the dark hero.', sel: 'cert h1' }, { noScroll: true });
  await S('cert-cta', q('a.glue-button, .glue-button, a, button').filter({ hasText: /Get started on Coursera/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Coursera CTA', desc: 'The "Get started on Coursera →" button — an outbound enrolment link; its states were measured but it was never followed (no enrolment, no external navigation).', sel: 'cert Coursera CTA' }, { noScroll: true });
  await S('badge-card', await domFind(page, /GRADUATE/i, { sel: 'div, span, p, [class*="badge"], [class*="card"], [class*="label"]', tag: 'bc', up: '[class*="badge"], [class*="card"], [class*="label"], [class*="caption"]', minW: 60, minH: 20 }), ['default'], { group: g, title: 'Graduate badge card', desc: 'The "GABE — GOOGLE UX DESIGN GRADUATE" overlay card on the hero photo.', sel: 'badge card' });
  await S('expansion-panel', q('.glue-expansion-panel').filter({ hasText: /What is a UX designer|difference between UX and UI/i }).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'Expansion panel', desc: 'One glue-expansion-panel FAQ row; opened was measured after clicking its header — a local UI toggle.', sel: '.glue-expansion-panel' }, { pin: true, before: { opened: openPanel } });
  await S('expansion-content', q('.glue-expansion-panel.glue-is-expanded .glue-expansion-panel__content, .glue-expansion-panel--expanded .glue-expansion-panel__content').filter({ visible: true }).first(), ['default'], { group: g, title: 'Expansion content', desc: 'An expanded panel\'s answer block (1296x120, the .glue-expansion-panel__content of the glue-is-expanded row); measured while the row above was held open.', sel: '.glue-is-expanded .glue-expansion-panel__content' }, { pin: true, open: async () => {
    const pl = q('.glue-expansion-panel').filter({ hasText: /What is a UX designer|difference between UX and UI/i }).first();
    const expanded = await pl.evaluate((el) => el.classList.contains('glue-is-expanded')).catch(() => false);
    return expanded ? 'the FAQ row was already expanded' : openPanel(pl);
  } });
  await page.keyboard.press('Escape');
  await page.waitForTimeout(500);
  save();
}

async function ai() {
  if (!(await newPage('ai'))) return;
  await sheetsFor('ai');
  const g = G.ai;
  await S('ai-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'AI page headline', desc: '"Essential AI skills for everyone" — the AI training page heading.', sel: 'ai h1' }, { noScroll: true });
  await S('ai-card', await p20('.glue-card, [class*="card"], [class*="tile"]', 15), ['default', 'hover'], { group: g, title: 'AI card', desc: 'A training/course card on the AI page.', sel: 'ai card' }, { pin: true });
  await S('ai-link', q('a.glue-button, .glue-button, a').filter({ hasText: /learn more|get started/i }).filter({ visible: true }).first(), B4, { group: g, title: 'AI page CTA', desc: 'An action on the AI training page; measured, never followed.', sel: 'ai CTA' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('.glue-header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header at 390 wide: wordmark and the drawer toggle.', sel: 'mobile header' }, { noScroll: true });
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The home display heading at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', await domFind(page, /get started|learn more/i, { sel: 'a.glue-button--high-emphasis, a.glue-button, .glue-button, a[class*="glue-button"]', tag: 'mc', minW: 60, minH: 20 }), B4, { group: g, title: 'Mobile hero CTA', desc: 'The hero action at 390 wide; measured, never followed.', sel: 'mobile hero CTA' });
  await S('m-drawer-btn', q('.glue-header button, button[aria-label*="drawer" i], button[aria-label*="menu" i]').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Drawer toggle', desc: 'The header button that opens the navigation drawer at 390 wide; opened was measured after tapping it — a local UI toggle.', sel: 'mobile drawer button' }, { noScroll: true, before: { opened: async (loc) => { await loc.tap({ timeout: 4000 }).catch(() => loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click()))); await page.waitForTimeout(1200); return 'tapped the drawer button to open the navigation drawer'; } } });
  await S('m-drawer-link', q('.glue-header__drawer--is-open a.glue-header__link:not(.glue-header__skip-content), .glue-is-showing-drawer a.glue-header__link:not(.glue-header__skip-content)').filter({ visible: true }).first(), B4, { group: g, title: 'Drawer link', desc: 'A link inside the opened navigation drawer (Career Certificates, 326x50); measured while the drawer was held open, never followed.', sel: '.glue-header__drawer--is-open a.glue-header__link' }, { noScroll: true, noReset: true, open: async () => {
    // The drawer may already be open from the toggle's `opened` state — only
    // press the button when it is not, a second press would close it.
    const showing = await page.evaluate(() => !!document.querySelector('.glue-is-showing-drawer, .glue-header__drawer--is-open')).catch(() => false);
    if (!showing) { const b = q('.glue-header__drawer-toggle-btn, .glue-header button').filter({ visible: true }).first(); await b.tap({ timeout: 4000 }).catch(() => b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()))); }
    await page.waitForTimeout(1200);
  } });
  await S('m-skip-link', q('.glue-header__skip-content').filter({ visible: true }).first(), ['default', 'focus-visible', 'pressed'], { group: g, title: 'Skip link', desc: 'The "Jump to Content" skip link — parked off-canvas at y -999, revealed at 39,8 (160x48) by keyboard focus; hover does not apply to a hidden element.', sel: '.glue-header__skip-content' }, { noScroll: true });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); grow.google paints light only — no theme toggle or dark media query observed on any signed-out route; bare headless contexts receive the US edition (a real user agent or explicit locale is 302\'d to the regional /intl/<locale>/ edition)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, certificates, certux, ai, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (a header nav
  // link's hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.glue-header a, .glue-btn');
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
