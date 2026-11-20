// Measures Matter's public components in every state reachable without
// signing in, purchasing or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home extension legal words article docs signin mobile.
// Writes raw/components-computed.json and one crop per component and state.
//
// getmatter.com is a Next.js marketing site (CSS modules, --mr-* tokens,
// MR-Camphor) painted near-black. Also measured: a public article on
// words.getmatter.com, the public docs, and the web reader sign-in card.
// Nothing is sent, signed into or submitted. Consent overlays are hidden,
// never clicked. Sign-in, subscribe, OAuth and continue buttons are measured,
// never pressed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, CROPS, REF, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/',
  extension: '/web-extension',
  newsletters: '/newsletters',
  privacy: '/privacy',
  terms: '/terms',
  words: 'https://words.getmatter.com/',
  article: 'https://words.getmatter.com/p/anu-coolhunt-before-sunrise-why-i',
  docs: 'https://docs.getmatter.com/',
  signin: 'https://web.getmatter.com/',
};
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the edge gates this run: components last measured on them keep their
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
  // open() throws on a failed navigation or a challenge that never clears; treat it like BLOCKED.
  const opened = await open(page, url || BASE + URLS[key], { wait, promo })
    .then(() => true, (e) => { log('  OPEN FAILED', key, String(e.message).slice(0, 100)); return false; });
  if (!opened) { failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  Object.assign(c, { page: current, run, url: URLS[current] && new URL(URLS[current], BASE).href }, meta);
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
      } catch (e) {
        s.cropError = String(e.message || e).slice(0, 120);
        // The PNG is saved before post-processing runs: a failed quantize or
        // convert must not unlink an image that landed on disk. Keep the path
        // next to the error so the documents still print the crop.
        const png = path.join(CROPS, `${key}-${state}.png`);
        if (fs.existsSync(png)) file = path.relative(REF, png);
      }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
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
    // Keep earlier evidence under its own provenance: the states stay but the
    // entry keeps its original page/run/url and records the miss, so a re-run
    // never republishes old readings under a new date.
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
      } else if (st === 'selected') {
        if (opts.noToggle) via = 'held selected by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
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

// Clicks a UI toggle (dropdown, menu, radio, day). Refuses a submit button and
// any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|continue|claim this offer|try again|next|confirm|schedule event|i understand|decline)$/i;
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
    await p.goto(BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image (the hero island paints a gradient), or falls back to
// marking a painted descendant: the hero card is a sibling layer, not an
// ancestor, so for it we mark the painted element inside its section instead.
async function markPainted(sel, tag, { maxUp = 8, minW = 100, minH = 60, descend = false } = {}) {
  const ok = await page.evaluate(([s, t, up, w, h, desc]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll(s)].find((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) return false;
    const paints = (cs) => cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none';
    if (!desc) for (let n = el, i = 0; n && i < up; n = n.parentElement, i++) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (r.width >= w && r.height >= h && paints(cs)) { n.setAttribute('data-m-mark', t); return true; }
    }
    if (desc) {
      // The painted layer sits beside the content, not above it: find the
      // biggest painted element under the element's own section.
      const sec = el.closest('section') || el.parentElement;
      const cands = [...(sec || el).querySelectorAll('*')].filter((n) => {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && paints(cs);
      }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
      if (cands[0]) { cands[0].setAttribute('data-m-mark', t); return true; }
    }
    return false;
  }, [sel, tag, maxUp, minW, minH, descend]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

// Marks the widest element matching sel: for repeated media like the hero
// orbit's cover cards, where first-match lands on an edge-on card.
async function markWidest(sel, tag) {
  const ok = await page.evaluate(([s, t]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const els = [...document.querySelectorAll(s)].filter((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!els.length) return false;
    els.sort((a, b) => b.getBoundingClientRect().width - a.getBoundingClientRect().width);
    els[0].setAttribute('data-m-mark', t);
    return true;
  }, [sel, tag]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

const G = {
  shell: 'Shell and navigation',
  hero: 'Home hero',
  home: 'Home sections',
  extension: 'Browser extension',
  legal: 'Legal pages',
  words: 'Words That Matter',
  article: 'Public article',
  docs: 'Docs',
  auth: 'Sign-in card',
  footer: 'Footer',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home', { wait: 5000 }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q(M('Nav_header')), ['default'], { group: g, title: 'Header', desc: 'The 62px near-black top bar: wordmark, Overview, Developer, Words That Matter, X, Sign In and the blurple Get Matter pill.', sel: M('Nav_header') }, { noScroll: true });
  await S('logo', q(M('Nav_logoLockup')), ['default'], { group: g, title: 'Wordmark', desc: 'The Matter lockup in the header.', sel: M('Nav_logoLockup') }, { noScroll: true });
  await S('nav-link', q('header a, nav a').filter({ hasText: /^\s*Overview\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A header text link. Overview is the current item.', sel: 'a "Overview"' }, { noScroll: true });
  await S('nav-signin', q('a[href*="web.getmatter.com"]').filter({ hasText: /Sign In/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in link', desc: 'The header Sign In link to web.getmatter.com. Measured, never followed.', sel: 'a "Sign In"' }, { noScroll: true });
  await S('nav-cta', q(M('GetMatterCTAButton_button')).filter({ visible: true }).first(), B4, { group: g, title: 'Get Matter pill', desc: 'The small blurple App Store pill in the header. Measured, never followed.', sel: M('GetMatterCTAButton_button') }, { noScroll: true });
  const h = G.hero;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The Camphor display headline on the near-black hero.', sel: 'h1' }, { noScroll: true });
  await S('hero-lede', q('p, h2').filter({ hasText: /modern read-later app/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero lede', desc: 'The sentence under the headline.', sel: 'hero lede' });
  await S('hero-cta', q(M('GetMatterCTAButton_l')).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The large blurple Get Matter pill. Measured, never followed (it opens the App Store).', sel: M('GetMatterCTAButton_l') });
  await S('secondary-link', q(M('SecondaryLink_a')).filter({ visible: true }).first(), B4, { group: h, title: 'Secondary link', desc: 'The "Get the browser extension" text link under the hero CTA. Measured, never followed in this reading.', sel: M('SecondaryLink_a') });
  const s = G.home;
  await S('section-h2', q('h2').filter({ hasText: /One place for all your reading/i }).filter({ visible: true }).first(), ['default'], { group: s, title: 'Section heading', desc: 'A Camphor section heading.', sel: 'h2 "One place"' });
  await S('quote', q('h2, p, blockquote').filter({ hasText: /Words are my matter/i }).filter({ visible: true }).first(), ['default'], { group: s, title: 'Footer quote', desc: 'The Ursula K. Le Guin line above the footer CTA.', sel: 'quote' });
  save();
}

async function extension() {
  if (!(await newPage('extension', { wait: 4000 }))) return;
  const g = G.extension;
  await S('ext-h2', q('h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Extension heading', desc: 'The web-extension page heading.', sel: 'h2 on /web-extension' }, { noScroll: true });
  await S('install-button', q(M('BigButton_bigButton')).filter({ visible: true }).first(), B4, { group: g, title: 'Install button', desc: 'An Install-on-Chrome/Safari/Firefox button. Measured, never followed.', sel: M('BigButton_bigButton') });
  save();
}

async function legal() {
  if (!(await newPage('privacy', { wait: 4000 }))) return;
  const g = G.legal;
  await S('legal-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal heading', desc: 'A privacy-policy section heading.', sel: 'h1 on /privacy' }, { noScroll: true });
  await S('legal-body', q('main p, article p, p').filter({ hasText: /privacy is important/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal body', desc: 'A body paragraph on the privacy page.', sel: 'privacy p' });
  save();
}

async function words() {
  if (!(await newPage('words', { wait: 5000, url: URLS.words }))) return;
  const g = G.words;
  // The publication home is a subscribe gate. Measure the gate. Never press Subscribe.
  await S('words-h1', q('h1').filter({ hasText: /Words That Matter/ }).first(), ['default'], { group: g, title: 'Publication title', desc: 'The Words That Matter title on the public Substack subscribe gate. Subscribe was never pressed.', sel: 'h1 on words.getmatter.com' }, { noScroll: true });
  await S('words-subscribe', q('button').filter({ hasText: /^\s*Subscribe\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Subscribe button', desc: 'The publication Subscribe button on the gate. Measured at rest, never pressed (a press opens a sign-up).', sel: 'button "Subscribe"' });
  await S('words-nav', q('button, a').filter({ hasText: /No thanks/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Subscribe dismiss', desc: 'The No thanks control on the subscribe gate. Measured at rest, never pressed.', sel: 'No thanks' });
  save();
}

async function article() {
  if (!(await newPage('article', { wait: 5000, url: URLS.article }))) return;
  const g = G.article;
  await S('article-h1', q('h1').filter({ visible: true }).nth(1), ['default'], { group: g, title: 'Article title', desc: 'The published article headline, loaded signed out.', sel: 'article h1' });
  await S('article-byline', q('a').filter({ hasText: /BEN SPRINGWATER|Ben Springwater/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Byline link', desc: 'The author byline link. Measured, never followed.', sel: 'byline a' });
  await S('article-body', q('article p, .body p, p').filter({ hasText: /.{40,}/ }).filter({ visible: true }).nth(2), ['default'], { group: g, title: 'Article paragraph', desc: 'A body paragraph on the public article.', sel: 'article p' });
  save();
}

async function docs() {
  if (!(await newPage('docs', { wait: 5000, url: URLS.docs }))) return;
  const g = G.docs;
  await S('docs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs heading', desc: 'The Matter Documentation heading on docs.getmatter.com.', sel: 'h1 on docs' }, { noScroll: true });
  await S('docs-tab', q('a').filter({ hasText: /^\s*API\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs tab', desc: 'A top tab (API). Measured, never followed in this reading.', sel: 'a "API"' }, { noScroll: true });
  await S('docs-search', q('button').filter({ hasText: /Search/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs search', desc: 'The Search button. Measured, never opened into a query.', sel: 'button Search' }, { noScroll: true });
  await S('docs-card', q('a[href*="/api"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Docs API link', desc: 'The API card or tab link. Measured, never followed in this reading.', sel: 'a[href*="/api"]' });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 5000, url: URLS.signin }))) return;
  const g = G.auth;
  await S('signin-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in heading', desc: 'The Welcome to Matter heading on the web reader sign-in card. Nothing was submitted.', sel: 'h1 on web.getmatter.com' }, { noScroll: true });
  await S('google-button', q('[class*="g_id_signin"], iframe[title*="Google" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Google button', desc: 'Continue with Google (a Google identity widget). Measured, never pressed.', sel: '.g_id_signin' }, { noScroll: true });
  await S('apple-button', q('button').filter({ hasText: /Continue with Apple/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Apple button', desc: 'Continue with Apple. Measured, never pressed.', sel: 'button "Continue with Apple"' }, { noScroll: true });
  await S('email-field', q('input[placeholder*="Email" i], input[type="email"], input[type="text"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The email field on the sign-in card. Focused only, never filled, never submitted.', sel: 'email input' }, { noScroll: true });
  await S('email-continue', q('button[aria-label], button:has(svg)').filter({ visible: true }).last(), ['default'], { group: g, title: 'Email continue arrow', desc: 'The arrow button beside the email field. Measured at rest, never pressed (a press would submit).', sel: 'email arrow button' }, { noScroll: true });
  await S('legal-link', q('a').filter({ hasText: /Terms of Service/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Legal link', desc: 'The Terms of Service link under the sign-in card.', sel: 'a "Terms of Service"' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 4000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(800);
  await S('footer', q(M('Footer_footer') + ', footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The marketing footer: quote, Get Matter, Terms, Privacy, X, Say hello.', sel: 'Footer_footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /^\s*Privacy\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer text link.', sel: 'footer a "Privacy"' }, { noScroll: true });
  await S('footer-cta', q('footer ' + M('GetMatterCTAButton_button')).filter({ visible: true }).first(), B4, { group: g, title: 'Footer CTA', desc: 'The footer Get Matter pill. Measured, never followed.', sel: 'footer Get Matter' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/', wait: 5000 }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header, [class*="Nav_header"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The header at 390px.', sel: 'header at 390' }, { noScroll: true });
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The hero headline at 390px.', sel: 'h1 at 390' });
  await S('m-cta', q(M('GetMatterCTAButton_l')).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Mobile CTA', desc: 'The large Get Matter pill at 390px. Measured, never followed.', sel: M('GetMatterCTAButton_l') + ' at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the marketing site paints one near-black theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, extension, legal, words, article, docs, signin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
