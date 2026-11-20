// Measures esquire.com's public components in every state reachable without
// signing in, subscribing or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home section article essay offers premium search about mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// esquire.com is Hearst's FRE design-token site, light-only on the public
// surface: home, section fronts, articles, the /offers/premium-membership plan
// page, the /esq-premium-exclusive/ hub, search results and the about page.
// The css-* classes are hashed Emotion output, so specs select by
// data-tracking-id, aria-label, structure or text. Nothing is sent, bought or
// signed into: the only presses are local UI toggles — the "More" nav dropdown,
// an FAQ accordion header, the mobile hamburger and the "US" edition switcher;
// the search and newsletter fields are typed into and cleared, never
// submitted; Sign In, Subscribe, Join, Follow and every article link are
// measured, never followed. The OneTrust consent layer is hidden, never
// answered; third-party ad/tracker requests are aborted so ad slots read as
// blank containers while the page's own "Advertisement - Continue Reading
// Below" furniture stays.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', section: '/style/', article: '/entertainment/movies/a71465908/dwayne-johnson-the-rock-interview-2026/',
  essay: '/lifestyle/sex/a74076291/ai-chatbots-flirting-texts/', offers: '/offers/premium-membership/',
  premium: '/esq-premium-exclusive/', search: '/search/?q=suits', about: '/about/a26377/about-us/', mobile: '/',
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
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const cleared = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });  // false: the bot check did not clear (lib.mjs)
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
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
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
  shell: 'Navigation and site chrome', home: 'Home page', article: 'Article page',
  offers: 'Membership offers', search: 'Search', section: 'Section front',
  mobile: 'Mobile (390 wide)', footer: 'Footer', overlay: 'Side panel and overlays',
};

const FIELD = ['default', 'focused', 'filled'];
const NAV = 'nav[data-tracking-id="topNav"]';

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

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('nav', q(NAV).filter({ visible: true }).first(), ['default'], { group: g, title: 'Desktop navigation', desc: 'The full top chrome: the dark utility strip (edition, Newsletter), the main bar (search field, Esquire wordmark, Sign In, Subscribe) and the .megaMenu category strip.', sel: 'nav[data-tracking-id=topNav]' }, { noScroll: true });
  await S('nav-utility', q(NAV + ' button').filter({ hasText: /^\s*US\s*$/ }).filter({ visible: true }).first().locator('xpath=ancestor::div[1]'), ['default'], { group: g, title: 'Utility strip', desc: 'The 32px top utility bar holding the US edition switcher and the Newsletter link.', sel: 'div ancestor of the US button' }, { noScroll: true });
  await S('nav-edition', q(NAV + ' button').filter({ hasText: /^\s*US\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Edition switcher', desc: 'The "US" edition button in the utility strip; measured, never toggled open beyond a hover.', sel: 'nav US button' }, { noScroll: true });
  await S('nav-newsletter', q(NAV + ' a').filter({ hasText: /^\s*Newsletter\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Newsletter link', desc: 'The "Newsletter" utility link; measured, never followed.', sel: 'nav a Newsletter' }, { noScroll: true });
  // The wordmark anchor holds the big inline svg and paints no text; a bare
  // a:has(svg) first-matches the Newsletter link's icon, so mark the nav
  // anchor whose svg paints widest (data-m-mark per FIELD-NOTES).
  await page.evaluate(() => {
    let best = null, w = 0;
    for (const a of document.querySelectorAll('nav[data-tracking-id="topNav"] a')) {
      const r = a.querySelector('svg') && a.querySelector('svg').getBoundingClientRect();
      if (r && r.width > w) { w = r.width; best = a; }
    }
    if (best) best.setAttribute('data-m-mark', 'nav-logo');
  }).catch(() => {});
  await S('nav-logo', q('[data-m-mark="nav-logo"]'), ['default'], { group: g, title: 'Wordmark', desc: 'The Esquire wordmark lockup centred in the main bar (a link home holding the widest inline svg).', sel: 'widest svg inside a nav anchor' }, { noScroll: true });
  await S('nav-signin', q(NAV + ' a').filter({ hasText: /^\s*Sign In\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign In link', desc: 'The "Sign In" link to account.esquire.com; measured, never followed.', sel: 'nav a Sign In' }, { noScroll: true });
  await S('nav-subscribe', q(NAV + ' a, ' + NAV + ' button').filter({ hasText: /^\s*Subscribe\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Subscribe button', desc: 'The red "Subscribe" call-to-action in the main bar; measured, never followed.', sel: 'nav Subscribe' }, { noScroll: true });
  await S('megamenu', q('.megaMenu').filter({ visible: true }).first(), ['default'], { group: g, title: 'Category menu', desc: 'The .megaMenu category strip under the main bar: Entertainment through Food and Drinks plus the "More" overflow toggle.', sel: '.megaMenu' }, { noScroll: true });
  await S('nav-link', q('.megaMenu a').filter({ hasText: /Entertainment/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Category link', desc: 'A .megaMenu category link ("Entertainment"); measured, never followed.', sel: '.megaMenu a Entertainment' }, { noScroll: true });
  await S('nav-subchevron', q('.megaMenu button[aria-label*="submenu" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Submenu chevron', desc: 'The per-category "Open X submenu" chevron button; measured, never toggled.', sel: '.megaMenu button[aria-label*=submenu]' }, { noScroll: true });
  await S('more-btn', q('.megaMenu button').filter({ hasText: /^\s*More\s*$/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'More toggle', desc: 'The "More" overflow toggle — a local UI toggle; the opened state was measured after clicking it, its links never followed.', sel: '.megaMenu button More' }, { noScroll: true });
  await S('more-panel', q('.megaMenu div, .megaMenu ul').filter({ hasText: /Member Exclusives/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'More panel', desc: 'The overflow panel opened by "More" — the hidden sections (Sports, Member Exclusives, For You) plus their submenu links.', sel: '.megaMenu overflow panel' }, { open: openMoreMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  const h = G.home;
  await S('ad-disclaimer', q('.ad-disclaimer').filter({ visible: true }).last(), ['default'], { group: h, title: 'Ad disclaimer', desc: 'The "Advertisement - Continue Reading Below" furniture label that sits above each blank ad slot; the slots themselves stay empty because ad requests are aborted.', sel: '.ad-disclaimer' });
  await S('section-h2', q('h2').filter({ hasText: /^\s*The Latest\s*$/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A home-page section heading ("The Latest") — 32px Lausanne.', sel: 'h2 The Latest' });
  await S('story-card', q('main h3').filter({ visible: true }).first().locator('xpath=ancestor::*[.//img][1]'), ['default'], { group: h, title: 'Story list card', desc: 'A story row in "The Latest": thumbnail, 18px Lausanne headline, byline and read-time.', sel: 'ancestor of first main h3' });
  await S('story-title', q('main h3').filter({ visible: true }).first(), ['default'], { group: h, title: 'Story headline', desc: 'An 18px Lausanne story headline in the Latest list.', sel: 'main h3' });
  await S('story-thumb', q('main h3').filter({ visible: true }).first().locator('xpath=ancestor::*[.//img][1]').locator('img').first(), ['default'], { group: h, title: 'Story thumbnail', desc: 'The thumbnail image inside a story list card.', sel: 'story card img' });
  await S('byline', q('main').locator('xpath=.//*[starts-with(translate(normalize-space(.)," "," "),"By ")][string-length(normalize-space(.))<60][not(.//*[starts-with(translate(normalize-space(.)," "," "),"By ")])]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Byline', desc: 'A "BY <AUTHOR>" byline under a story headline.', sel: 'main BY-line' });
  await S('readtime', q('main').locator('xpath=.//*[contains(.,"min read")][not(.//*[contains(.,"min read")])]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Read time', desc: 'The "min read" duration label with its clock icon on a story card.', sel: 'min read label' });
  await S('eyebrow', q('main').locator('xpath=.//*[contains(" NEWS MAN AT HIS BEST STYLE LIFESTYLE WATCHES ENTERTAINMENT FOOD ",concat(" ",translate(normalize-space(.),"abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ")," "))][string-length(normalize-space(.))<30][not(.//*[string-length(normalize-space(.))<30])]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Eyebrow', desc: 'The small uppercase red eyebrow ("NEWS" / "STYLE") over a headline.', sel: 'uppercase eyebrow' });
  // The hero is the one headline painted at display size: mark the largest h3
  // with data-m-hero in the page, then measure that locator.
  await page.evaluate(() => { let best = null, fs = 0; for (const el of document.querySelectorAll('main h3')) { const f = parseFloat(getComputedStyle(el).fontSize); const r = el.getBoundingClientRect(); if (r.width > 300 && r.height > 20 && f > fs) { fs = f; best = el; } } if (best) best.setAttribute('data-m-hero', '1'); }).catch(() => {});
  await S('hero-story', q('[data-m-hero]').first(), ['default'], { group: h, title: 'Hero story', desc: 'The cover hero headline painted at display size (56px PlayFair).', sel: 'largest h3 by computed font-size' });
  await S('hero-dek', q('main p').filter({ hasText: /shoes|footwear|sold men/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero dek', desc: 'The standfirst paragraph under the hero headline.', sel: 'hero dek p' });
  await S('rail-card', q('h3').filter({ visible: true }).nth(7).locator('xpath=ancestor::*[.//img][1]'), ['default'], { group: h, title: 'Rail card', desc: 'A right-rail "MAN AT HIS BEST" style card: thumbnail over a 20px headline with a dek.', sel: 'rail card ancestor of h3' });
  await S('newsletter-block', q('form').filter({ hasText: /email/i }).filter({ visible: true }).first().locator('xpath=ancestor::*[self::section or self::div][2]'), ['default'], { group: h, title: 'Newsletter block', desc: 'The mid-page "Real journalism and real style" newsletter band: 28px Lausanne pitch, email field, Sign Up button and terms copy.', sel: 'newsletter form ancestor' });
  await S('newsletter-input', q('input[placeholder*="email" i]').filter({ visible: true }).first(), FIELD, { group: h, title: 'Newsletter field', desc: 'The "Enter your email address" field; focused and typed into then cleared — never submitted.', sel: 'input[placeholder*=email]' }, { fillText: 'name@example.com' });
  await S('newsletter-signup', q('form button').filter({ hasText: /^\s*Sign Up\s*$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Sign Up button', desc: 'The red "Sign Up" submit inside the newsletter band; measured, never pressed.', sel: 'newsletter Sign Up' });
  await S('pagination', q('nav[aria-label="Pagination"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Pagination', desc: 'The "1 | 2 | 3" pagination under the story feed; measured, never followed.', sel: 'nav[aria-label=Pagination]' });
  // The header search field is measured last: typing can drive the page's own
  // search JS, so it comes after everything else and the form is never
  // submitted.
  await S('nav-search', q(NAV + ' input[placeholder*="Search" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Search field', desc: 'The header "Search..." input; focused and typed into then cleared — never submitted.', sel: 'nav input[placeholder*=Search]' }, { noScroll: true, fillText: 'suits' });
  await S('nav-search-btn', q(NAV + ' button[aria-label="Search"]').filter({ visible: true }).first(), B4, { group: g, title: 'Search icon button', desc: 'The search-icon submit inside the header search box; measured, never pressed.', sel: 'nav button[aria-label=Search]' }, { noScroll: true });
  const f = G.footer;
  // The first <footer> in the DOM is the (hidden) sidepanel's; the page footer
  // is the one holding nav[data-track-type=footer-menu].
  await S('footer', q('nav[data-track-type="footer-menu"]').filter({ visible: true }).last().locator('xpath=ancestor::*[self::footer or self::div][1]'), ['default'], { group: f, title: 'Footer', desc: 'The site footer: wordmark, social icons, the Newsletter/About Us link columns and the legal line.', sel: 'footer holding nav[footer-menu]' });
  await S('footer-link', q('nav[data-track-type="footer-menu"] a').filter({ hasText: /^\s*About Us\s*$/i }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer nav link ("About Us"); measured, never followed.', sel: 'footer-menu a' });
  await S('footer-social', q('a:has(img[alt*="tiktok" i]), a:has(img[alt*="facebook" i]), a:has(img[alt*="instagram" i])').filter({ visible: true }).last(), B4, { group: f, title: 'Social icon link', desc: 'A square social icon button in the footer (x, tiktok, youtube…); measured, never followed.', sel: 'footer social a' });
  save();
}

async function section() {
  if (!(await newPage('section'))) return;
  await sheetsFor('section');
  await chrome('section');
  const g = G.section;
  await S('sec-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section title', desc: 'The section-front title ("Style") — the display word at the top of the front.', sel: 'section h1' }, { noScroll: true });
  await S('sec-desc', q('main p, main div').filter({ hasText: /style advice|fashion|menswear|latest/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Section description', desc: 'The standfirst describing the section under its title.', sel: 'section description' });
  // The lead story card is the first main link that carries an image — a card
  // big enough to be the feature. First-match on a heading alone caught the
  // "just landed" band title, and climbing from it caught the whole band
  // section. Mark the linked card, then measure the mark.
  await page.evaluate(() => {
    for (const a of document.querySelectorAll('main a')) {
      const r = a.getBoundingClientRect();
      if (r.width < 200 || r.height < 100) continue;
      if (!a.querySelector('img')) continue;
      a.setAttribute('data-m-mark', 'lead');
      return;
    }
  }).catch(() => {});
  await S('sec-hero', q('[data-m-mark="lead"]'), ['default'], { group: g, title: 'Section lead card', desc: 'The lead story card on the section front — the first image-carrying story link on the front.', sel: 'first main a with img' });
  await S('sec-eyebrow', q('main').locator('xpath=.//*[contains(" NEWS MAN AT HIS BEST STYLE LIFESTYLE WATCHES ENTERTAINMENT FOOD ",concat(" ",translate(normalize-space(.),"abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ")," "))][string-length(normalize-space(.))<30][not(.//*[string-length(normalize-space(.))<30])]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section eyebrow', desc: 'The uppercase eyebrow over the lead story.', sel: 'section eyebrow' });
  await S('sec-card', q('main h3, main h2').filter({ visible: true }).last().locator('xpath=ancestor::*[.//img][1]'), ['default'], { group: g, title: 'Section card', desc: 'A standard story card lower on the section front.', sel: 'section card' });
  await S('sec-see-more', q('button, a').filter({ hasText: /^\s*(see more|load more|more stories)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'See More button', desc: 'The "See More" pagination ghost button — dark #121212 outline, red text; measured, never pressed.', sel: 'See More' });
  save();
}

async function article() {
  if (!(await newPage('article', { wait: 12000 }))) return;
  await sheetsFor('article');
  await chrome('article');
  const g = G.article;
  await S('related-strip', q('a').filter({ hasText: /Monday with Brad Pitt/ }).filter({ visible: true }).first().locator('xpath=ancestor::*[self::ul or self::ol][1]'), ['default'], { group: g, title: 'Related strip', desc: 'The "RELATED" pill row pinned under the nav linking sibling stories; measured, never followed.', sel: 'RELATED strip' }, { noScroll: true });
  await S('art-breadcrumb', q('main nav, header nav, article nav, [class*="breadcrumb" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Breadcrumb', desc: 'The section breadcrumb over the headline ("Entertainment › Movies").', sel: 'article breadcrumb' }, { noScroll: true });
  await S('art-h1', q('article h1, main h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article headline', desc: 'The cover-story headline — large PlayFair display.', sel: 'article h1' }, { noScroll: true });
  await S('art-standfirst', q('p').filter({ hasText: /.+/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Standfirst', desc: 'The intro standfirst under the headline — lighter, larger Lausanne copy.', sel: 'article standfirst p' });
  await S('art-byline', q('a[href*="/author/"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Byline', desc: 'The author byline link ("By <name>"); measured, never followed.', sel: 'a[href*=author]' });
  await S('art-hero', q('article img, main img, figure img, header img').filter({ visible: true }).first().locator('xpath=ancestor::*[self::figure or self::picture or self::div][1]'), ['default'], { group: g, title: 'Hero image', desc: 'The hero photograph under the article header.', sel: 'article hero figure' });
  await S('art-caption', q('figcaption').filter({ visible: true }).first(), ['default'], { group: g, title: 'Caption', desc: 'The photo caption / credit line under the hero.', sel: 'figcaption' });
  await S('art-para', q('.article-body p').filter({ visible: true }).nth(1), ['default'], { group: g, title: 'Body paragraph', desc: 'A body paragraph — Lora 18px on the measure.', sel: 'article body p' });
  await S('art-dropcap', q('p.body-dropcap, [class*="dropcap" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Drop-cap paragraph', desc: 'The lede paragraph whose first letter paints a drop cap.', sel: 'p.body-dropcap' });
  // An inline story link sits inside the text flow: inline display, no button
  // chrome, not a standalone CTA. A bare first-match on the body anchors
  // caught a styled "SUBSCRIBE" button, so mark a link that reads as text.
  // When no inline link exists on the story the entry must be a gap, not the
  // CTA re-published — dropPrior keeps the miss honest.
  await page.evaluate(() => {
    for (const a of document.querySelectorAll('.article-body p a, .body-content p a, article p a')) {
      const cs = getComputedStyle(a);
      const r = a.getBoundingClientRect();
      const t = (a.innerText || '').trim();
      if (!r.width || !r.height || !t) continue;
      if (cs.display !== 'inline' || parseFloat(cs.borderTopWidth) > 0 || parseFloat(cs.paddingTop) > 0 || cs.backgroundColor !== 'rgba(0, 0, 0, 0)') continue;
      if (/^(subscribe|sign up|shop|buy|join|watch now|read more|learn more)/i.test(t)) continue;
      a.setAttribute('data-m-mark', 'art-link');
      return;
    }
  }).catch(() => {});
  await S('art-link', q('[data-m-mark="art-link"]'), B4, { group: g, title: 'Inline story link', desc: 'An inline text link inside body copy; measured, never followed. Not every story carries one — this story had only the styled SUBSCRIBE CTA, so the link is a gap rather than a mislabelled button.', sel: 'inline body-copy anchor' }, { dropPrior: true });
  await S('art-pullquote', q('blockquote, [data-theme-key*="pullquote" i], [class*="pullquote" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pull quote', desc: 'A display pull quote inside the story.', sel: 'article blockquote' });
  await S('art-blockhead', q('h2, h3').filter({ hasText: /readers also read|related|more from/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Block heading', desc: 'A mid-story block heading ("readers also read…").', sel: 'article h2 block' });
  await S('art-ad', q('.ad-disclaimer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Ad furniture', desc: 'The "Advertisement - Continue Reading Below" furniture inside the story; the slot below it stays blank because ad requests are aborted.', sel: '.ad-disclaimer' });
  await S('art-related-card', q('main a').filter({ hasText: /Monday with Brad Pitt/ }).filter({ visible: true }).last().locator('xpath=ancestor::*[self::div or self::article][1]'), ['default'], { group: g, title: 'Related card', desc: 'A related-story card in the tail of the article.', sel: 'related card' });
  save();
}

async function essay() {
  if (!(await newPage('essay'))) return;
  await sheetsFor('essay');
  const g = G.article;
  await S('essay-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Essay headline', desc: 'A shorter essay headline — same display treatment as the cover story.', sel: 'essay h1' }, { noScroll: true });
  await S('essay-para', q('.article-body p, article p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Essay paragraph', desc: 'A body paragraph on the shorter essay.', sel: 'essay body p' });
  save();
}

async function offers() {
  if (!(await newPage('offers'))) return;
  await sheetsFor('offers');
  await chrome('offers');
  const g = G.offers;
  await S('offers-h1', q('main').locator('xpath=.//*[contains(normalize-space(.),\"Choose a Plan\")][not(.//*[contains(.,\"Choose a Plan\")])]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Offers heading', desc: '"Choose a Plan" — the display heading over the plan grid.', sel: 'h1/h2 Choose a Plan' });
  const join = q('button[data-theme-key="button-primary"]').filter({ hasText: /join/i }).filter({ visible: true }).first();
  await S('plan-card', join.locator('xpath=ancestor::*[.//text()[contains(., "year") or contains(., "month") or contains(., "$")]][1]'), ['default'], { group: g, title: 'Plan card', desc: 'A membership plan card: plan name, price line, perk list and its Join action.', sel: 'ancestor of Join button' });
  await S('plan-name', q('h3, span, div, p').filter({ hasText: /^\s*(Premium|Print \+ Digital|Digital Only)\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'The plan name ("Premium") heading on a plan card.', sel: 'plan name' });
  // The price the plan charges, not the struck-through list price beside it: on 2026-11-13 the first
  // "$" leaf was the line-through "$75" span. Struck elements are marked and skipped in-page.
  await page.evaluate(() => document.querySelectorAll('main *').forEach((n) => {
    if (getComputedStyle(n).textDecorationLine.includes('line-through') || /^(S|DEL|STRIKE)$/.test(n.tagName)) n.setAttribute('data-m-struck', '1');
  })).catch(() => {});
  await S('plan-price', q('main').locator('xpath=.//*[contains(normalize-space(.),\"$\")][string-length(normalize-space(.))<30][not(.//*[contains(normalize-space(.),\"$\")])][not(ancestor-or-self::*[@data-m-struck])]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'The "$xx/year" price line on a plan card.', sel: 'plan price' });
  await S('plan-perk', q('main').locator('xpath=.//*[contains(translate(normalize-space(.),\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\",\"abcdefghijklmnopqrstuvwxyz\"),\"access to esquire.com\")][not(.//*[contains(.,\"access to esquire.com\")])]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan perk', desc: 'A perk bullet inside a plan card.', sel: 'plan perk li' });
  await S('plan-join', join, B4, { group: g, title: 'Join button', desc: 'The "Join Premium" primary button on a plan card — links to checkout; measured, never followed.', sel: 'button[data-theme-key=button-primary] Join' });
  await S('best-value', q('span, div, p').filter({ hasText: /^\s*best value\s*$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Best Value chip', desc: 'The "Best Value" badge on the featured plan.', sel: 'Best Value' });
  await S('perks-h2', q('h2').filter({ hasText: /membership perks/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Membership Perks heading', desc: 'The "Membership Perks" section heading on the offers page.', sel: 'h2 Membership Perks' });
  await S('faq-h2', q('h2').filter({ hasText: /frequently asked/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ heading', desc: 'The "Frequently Asked Questions" section heading.', sel: 'h2 FAQ' });
  await S('faq-header', q('button[data-theme-key="collapsible-header-button"]').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'FAQ accordion header', desc: 'An FAQ collapsible header ("When will my magazine be delivered?") — a local UI toggle; the opened state was measured after clicking it.', sel: 'collapsible-header-button' });
  // The answer region sits next to the header's heading — aria-controls is
  // absent on this build, so resolve the region by that name first and fall
  // back to the sibling of the header's h-ancestor. Capture it only when the
  // toggled-open region is visible and holds text — a sibling guess saved an
  // empty 1200x4 box before, and a miss must be a gap, not a stale stub.
  await page.evaluate(() => { const b = document.querySelector('button[data-theme-key="collapsible-header-button"]'); if (b && b.getAttribute('aria-expanded') !== 'true') b.click(); }).catch(() => {});
  await page.waitForTimeout(900);
  await page.evaluate(() => {
    const b = document.querySelector('button[data-theme-key="collapsible-header-button"]');
    if (!b) return;
    let region = null;
    const id = b.getAttribute('aria-controls');
    if (id) region = document.getElementById(id);
    if (!region) {
      const head = b.closest('h1,h2,h3,h4,h5,h6');
      region = head && head.nextElementSibling;
    }
    if (region) {
      const r = region.getBoundingClientRect();
      const cs = getComputedStyle(region);
      if (r.height > 8 && cs.visibility !== 'hidden' && cs.display !== 'none' && (region.innerText || '').trim()) region.setAttribute('data-m-mark', 'faq-a');
    }
  }).catch(() => {});
  await S('faq-answer', q('[data-m-mark="faq-a"]'), ['default'], { group: g, title: 'FAQ answer', desc: 'The answer panel revealed by the FAQ header toggle — the region its aria-controls names, or the sibling of the header heading when the attribute is absent; captured only when visible with text.', sel: 'aria-controls region, else header-heading sibling' }, { noScroll: true, noReset: true, dropPrior: true });
  await S('gift-cta', q('a[data-theme-key="button-primary"]').filter({ hasText: /gift/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Gift subscription CTA', desc: 'The "GIVE A GIFT SUBSCRIPTION" ghost action — red text on white at rest, filling red on hover; measured, never followed.', sel: 'a[data-theme-key=button-primary] gift' });
  await S('offers-fine', q('p').filter({ hasText: /cancel anytime|automatically renew/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Renewal fine print', desc: 'The "Cancel anytime…" fine print under the plan grid.', sel: 'renewal fine print' });
  save();
}

async function premium() {
  if (!(await newPage('premium'))) return;
  await sheetsFor('premium');
  const g = G.offers;
  await S('prem-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Premium hub heading', desc: 'The heading on the /esq-premium-exclusive/ hub.', sel: 'premium h1' }, { noScroll: true });
  await S('prem-card', q('main h3, main h2').filter({ visible: true }).first().locator('xpath=ancestor::*[self::a or self::article or self::li or self::div][1]'), ['default'], { group: g, title: 'Premium story card', desc: 'A member-exclusive story card on the premium hub.', sel: 'premium card' });
  save();
}

async function search() {
  if (!(await newPage('search'))) return;
  await sheetsFor('search');
  const g = G.search;
  await S('search-field', q('input.search-input-field, main input[type="search"], main input').filter({ visible: true }).first(), FIELD, { group: g, title: 'Search results field', desc: 'The big search field on the results page (1115x48); focused and typed into then cleared — never submitted.', sel: 'input.search-input-field' }, { fillText: 'suits' });
  await S('search-btn', q('main button[aria-label*="search" i], main form button[data-theme-key="button-primary"]').filter({ visible: true }).first(), B4, { group: g, title: 'Search submit', desc: 'The round red search submit beside the field; measured, never pressed.', sel: 'search submit' });
  await S('search-count', q('main').locator('xpath=.//*[contains(translate(normalize-space(.),\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\",\"abcdefghijklmnopqrstuvwxyz\"),\"results for\")][string-length(normalize-space(.))<80][not(.//*[contains(.,\"results for\")])]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Result count', desc: 'The "N results for keyword <q>" line.', sel: 'result count' });
  await S('search-sort', q('button[data-theme-key="popover-trigger"], button').filter({ hasText: /sort by/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sort control', desc: 'The "Sort By: Relevance" popover trigger; measured, never toggled.', sel: 'Sort By' });
  await S('search-card', q('.custom-item-title, h3').filter({ visible: true }).first().locator('xpath=ancestor::*[self::a or self::article or self::li or self::div][1]'), ['default'], { group: g, title: 'Result card', desc: 'A search-result card: thumbnail, 40px Lausanne title, muted dek.', sel: 'result card' });
  await S('search-title', q('.custom-item-title, h3').filter({ visible: true }).first(), ['default'], { group: g, title: 'Result title', desc: 'A 40px Lausanne result title.', sel: '.custom-item-title' });
  await S('search-more', q('button, a').filter({ hasText: /^\s*see more\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'See More button', desc: 'The "See More" ghost button at the foot of the results — dark #121212 outline, red text; measured, never pressed.', sel: 'See More' });
  save();
}

async function about() {
  if (!(await newPage('about'))) return;
  const g = G.section;
  await S('about-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'About heading', desc: 'The "About Us" page heading.', sel: 'about h1' }, { noScroll: true });
  await S('about-para', page.locator('xpath=//p[string-length(normalize-space(.))>120]').filter({ visible: true }).first(), ['default'], { group: g, title: 'About paragraph', desc: 'A paragraph on the About Us page.', sel: 'about p' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-nav', q(NAV).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile navigation', desc: 'The phone top chrome: red utility strip, hamburger, Esquire wordmark and search icon.', sel: 'nav[data-tracking-id=topNav]' }, { noScroll: true });
  const ham = q('button[aria-label*="Open" i], ' + NAV + ' button[aria-label*="menu" i], ' + NAV + ' button[aria-label*="Sidepanel" i]').filter({ visible: true }).first();
  await S('m-hamburger', ham, [...B4, 'opened'], { group: g, title: 'Hamburger', desc: 'The hamburger button that toggles the side panel — a local UI toggle; the opened state was measured after clicking it.', sel: 'mobile hamburger' }, { noScroll: true, allowLink: true });
  await S('m-drawer', q('.new-sidepanel-menu.visible, nav#sidepanel:not(.hidden)').filter({ visible: true }).first(), ['default'], { group: G.overlay, title: 'Side panel', desc: 'The slide-in side panel the hamburger opens — section links with accordion chevrons; its links were never followed.', sel: 'nav#sidepanel' }, { open: openSidepanel, noScroll: true, noReset: true });
  await S('m-drawer-link', q('.new-sidepanel-menu.visible a, nav#sidepanel:not(.hidden) a').filter({ hasText: /Entertainment/ }).filter({ visible: true }).first(), B4, { group: G.overlay, title: 'Drawer section link', desc: 'A section link inside the side panel; measured, never followed.', sel: 'sidepanel a' }, { open: openSidepanel, noScroll: true, noReset: true });
  await S('m-drawer-close', q('.new-sidepanel-menu.visible button[aria-label*="Close" i], nav#sidepanel:not(.hidden) button[aria-label*="Close" i]').filter({ visible: true }).first(), B4, { group: G.overlay, title: 'Drawer close', desc: 'The "Close Sidepanel" icon button; measured, never pressed.', sel: 'sidepanel close' }, { open: openSidepanel, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await page.evaluate(() => { const b = document.querySelector('.new-sidepanel-menu.visible button[aria-label*="Close" i]'); if (b) b.click(); }).catch(() => {});
  // Same wordmark fix as the desktop nav-logo: mark the nav anchor whose
  // inline svg paints widest rather than first-matching a:has(svg), which
  // caught the Newsletter link's icon.
  await page.evaluate(() => {
    let best = null, w = 0;
    for (const a of document.querySelectorAll('nav[data-tracking-id="topNav"] a')) {
      const r = a.querySelector('svg') && a.querySelector('svg').getBoundingClientRect();
      if (r && r.width > w) { w = r.width; best = a; }
    }
    if (best) best.setAttribute('data-m-mark', 'm-logo');
  }).catch(() => {});
  await S('m-logo', q('[data-m-mark="m-logo"]'), ['default'], { group: g, title: 'Mobile wordmark', desc: 'The Esquire wordmark centred in the phone bar.', sel: 'widest svg inside a nav anchor' }, { noScroll: true });
  await S('m-search', q(NAV + ' a[href*="/search"], ' + NAV + ' a[title*="Search" i], ' + NAV + ' a:has(img[alt="Search"])').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile search link', desc: 'The search icon link in the phone bar; measured, never followed.', sel: 'mobile search a' }, { noScroll: true });
  await S('m-story', q('main h3, main h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile story headline', desc: 'A story headline in the phone feed.', sel: 'mobile h3' });
  await S('m-eyebrow', q('main').locator('xpath=.//*[contains(" NEWS MAN AT HIS BEST STYLE LIFESTYLE WATCHES ENTERTAINMENT FOOD ",concat(" ",translate(normalize-space(.),"abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ")," "))][string-length(normalize-space(.))<30][not(.//*[string-length(normalize-space(.))<30])]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile eyebrow', desc: 'The uppercase eyebrow over a phone headline.', sel: 'mobile eyebrow' });
  await S('m-byline', q('main').locator('xpath=.//*[starts-with(translate(normalize-space(.)," "," "),"By ")][string-length(normalize-space(.))<60][not(.//*[starts-with(translate(normalize-space(.)," "," "),"By ")])]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile byline', desc: 'A "BY <AUTHOR>" byline on the phone feed.', sel: 'mobile byline' });
  await S('m-newsletter', q('form').filter({ hasText: /email/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile newsletter', desc: 'The newsletter band in the phone feed.', sel: 'mobile newsletter form' });
  await S('m-footer', q('nav[data-track-type="footer-menu"]').filter({ visible: true }).last().locator('xpath=ancestor::*[self::footer or self::div][1]'), ['default'], { group: g, title: 'Mobile footer', desc: 'The site footer on the phone.', sel: 'mobile footer' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (the Mobile group at 390 x 844); every captured surface paints the site’s single light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, section, article, essay, offers, premium, search, about, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that animates (the More chevron), so
  // the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.megaMenu button');
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
