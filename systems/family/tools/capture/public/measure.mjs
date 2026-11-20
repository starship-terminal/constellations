// Measures family.co's public components in every state reachable without
// signing in, downloading the app or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home blog blogpost changelog support supportart faqs legal docs
// connectkit account login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// family.co paints a single light theme signed out. It is styled-components —
// classes carry the stable styled name (<Name>__<Element>-sc-<hash>-<n>), so
// specs select on the styled name, a role, an aria-label or text. The app
// login (app.family.co, "Aave Account") is a Next.js CSS-modules app. Nothing
// is sent or signed into: the only presses are local UI toggles — the header's
// hover dropdowns, a "Watch the demo" video overlay, a FAQ accordion item and
// a blog filter. Log In, Get Started, Download on iOS and every Watch link are
// measured, never followed; the login and support-search fields are typed into
// and cleared, never submitted. No consent overlay was seen.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', blog: '/blog', blogpost: '/blog/why-family-accounts', changelog: '/changelog', support: '/support', supportart: '/support/import-a-wallet-from-metamask', faqs: '/faqs', legal: '/legal', docs: '/docs', connectkit: '/docs/connectkit', account: '/docs/family-account', login: APP + '/', mobile: '/' };
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
  const loaded = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (!loaded || await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
  // Cosmetic only: hide the text caret during field states. app.family.co's
  // CSP refuses the inline style tag — losing it is fine.
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
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
  const loc = target.and(page.locator(':visible')).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).and(page.locator(':visible')).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via, run };
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
  const loc = target.and(page.locator(':visible')).first();
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
        await (opts.hoverLoc || loc).and(page.locator(':visible')).first().hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).and(page.locator(':visible')).first().hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).and(page.locator(':visible')).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).and(page.locator(':visible')).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc).and(page.locator(':visible')).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).and(page.locator(':visible')).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|download on ios|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|watch the video|watch the demo|learn more)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.and(page.locator(':visible')).first();
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
  shell: 'Header and navigation', home: 'Home', login: 'App login (app.family.co)',
  blog: 'Blog', changelog: 'Changelog', support: 'Help and support', docs: 'Docs pages',
  mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Hover-opens a header dropdown ("Developers" or "Resources") — a local UI
// toggle, never a navigation.
async function openNav(which) {
  const trig = page.locator('header a, header button').filter({ hasText: new RegExp('^\\s*' + which + '\\s*$') }).and(page.locator(':visible')).first();
  if (!(await trig.count())) return 'no ' + which + ' trigger';
  for (let i = 0; i < 3; i++) {
    await trig.hover();
    await page.waitForTimeout(900);
    const shown = await page.locator(M('Nav__DropdownContainer')).and(page.locator(':visible')).first().isVisible().catch(() => false);
    if (shown) return 'hovered "' + which + '" to open the dropdown';
  }
  return 'hovered "' + which + '"; the dropdown did not report open';
}

// Opens a "Watch the demo" video overlay — a local UI toggle; the video is
// left playing and the overlay is measured, never downloaded.
async function openDemo() {
  const t = page.locator('button').filter({ hasText: /Watch the demo/ }).and(page.locator(':visible')).first();
  if (!(await t.count())) return 'no demo button';
  await t.scrollIntoViewIfNeeded();
  await page.waitForTimeout(400);
  await t.click({ timeout: 4000 }).catch(() => t.evaluate((el) => el.click()));
  await page.locator(M('WatchDemo__OverlayContainer')).and(page.locator(':visible')).first().waitFor({ state: 'visible', timeout: 6000 }).catch(() => {});
  await page.waitForTimeout(1500);
  return 'clicked "Watch the demo" to open the video overlay';
}
async function closeDemo() {
  await page.keyboard.press('Escape').catch(() => {});
  const x = page.locator(M('WatchDemo__OverlayContainer') + ' button, ' + M('WatchDemo__OverlayContainer') + ' [class*="Close" i]').and(page.locator(':visible')).first();
  if (await x.count()) await x.evaluate((el) => el.click()).catch(() => {});
  await page.locator(M('WatchDemo__OverlayContainer')).first().waitFor({ state: 'hidden', timeout: 6000 }).catch(() => {});
  await page.waitForTimeout(600);
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Site header', desc: 'The fixed top bar: the Family wordmark, the Developers/Resources hover dropdowns, X (Twitter), Log In and the dark Get Started pill.', sel: 'header' }, { noScroll: true });
  await S('mkt-logo', q('header a[href="/"], header svg').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Logo', desc: 'The Family wordmark at the left of the header.', sel: 'header logo' }, { noScroll: true });
  await S('nav-developers', q('header a').filter({ hasText: /^\s*Developers\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Developers menu', desc: 'The Developers dropdown trigger; hover opens the ConnectKit/Family card menu — measured, never followed.', sel: 'header Developers' }, { noScroll: true });
  await S('nav-dropdown', q(M('Nav__DropdownContainer')).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Nav dropdown', desc: 'The Developers dropdown panel (ConnectKit and Family cards); opened by hovering the trigger.', sel: 'Nav__DropdownContainer' }, { open: () => openNav('Developers'), noScroll: true, noReset: true });
  await S('nav-resources', q('header a').filter({ hasText: /^\s*Resources\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Resources menu', desc: 'The Resources dropdown trigger (Blog / Changelog / Help & Support / FAQs); measured, never followed.', sel: 'header Resources' }, { noScroll: true });
  await S('nav-twitter', q('header a').filter({ hasText: /X \(Twitter\)/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'X (Twitter) link', desc: 'The header social link; measured, never followed.', sel: 'header X (Twitter)' }, { noScroll: true });
  await S('login-btn', q('a.login-button button, a.login-button').and(page.locator(':visible')).first(), B4, { group: g, title: 'Log In button', desc: 'The beige Log In pill in the header, inside a link to app.family.co; measured, never followed.', sel: 'a.login-button' }, { noScroll: true });
  await S('getstarted-btn', q('header button').filter({ hasText: /^\s*Get Started\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Get Started button', desc: 'The near-black Get Started pill; measured, never pressed (it starts the download flow).', sel: 'header Get Started' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Hero headline', desc: '"Your favorite crypto wallet." — the Family display face hero.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('p, div, span').filter({ hasText: /Explore Ethereum with the best wallet for iOS/ }).and(page.locator(':visible')).last(), ['default'], { group: h, title: 'Hero subline', desc: 'The "Explore Ethereum with the best wallet for iOS" subline under the hero.', sel: 'hero subline' }, { noScroll: true });
  await S('download-cta', q('a, button').filter({ hasText: /Download on iOS/ }).and(page.locator(':visible')).first(), B4, { group: h, title: 'Download CTA', desc: 'The "Download on iOS" pill; measured, never followed (it goes to the App Store).', sel: 'Download on iOS' }, { noScroll: true });
  await S('watch-video', q('a, button').filter({ hasText: /Watch the Video/ }).and(page.locator(':visible')).first(), B4, { group: h, title: 'Watch the Video', desc: 'The "Watch the Video" action beside the download pill; measured, never pressed.', sel: 'Watch the Video' });
  await S('feature-h2', q('h1').filter({ hasText: /Explore Ethereum in a whole new way/ }).and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading ("Explore Ethereum in a whole new way.").', sel: 'h1' });
  await S('feature-label', q('h3, h5, div, span').filter({ hasText: /^\s*(Easy|Secure|Fast|Powerful|Fun)\s*$/ }).and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Feature label', desc: 'A feature label in the intro grid (Easy / Secure / Fast / Powerful / Fun).', sel: 'feature label' });
  await S('feature-body', q('p, div').filter({ hasText: /Whether you\u2019re a beginner or seasoned pro/ }).and(page.locator(':visible')).last(), ['default'], { group: h, title: 'Feature body', desc: 'Feature body copy ("Whether you\u2019re a beginner or seasoned pro, Family makes it easy.").', sel: 'feature body' });
  await S('demo-btn', q('button').filter({ hasText: /Watch the demo/ }).and(page.locator(':visible')).first(), B4, { group: h, title: 'Watch-the-demo button', desc: 'A "Watch the demo" button under a feature; opens the video overlay — measured, the press opens a local overlay only.', sel: 'Watch the demo' });
  await S('demo-overlay', q(M('WatchDemo__OverlayContainer')).and(page.locator(':visible')).last(), ['default'], { group: h, title: 'Demo overlay', desc: 'The full-viewport video overlay "Watch the demo" mounts; measured open, then closed.', sel: 'WatchDemo__OverlayContainer' }, { open: openDemo, noScroll: true, noReset: true, crop: true });
  // The overlay is a fixed full-viewport layer with an 80% scrim: close it
  // right after its own measurement and wait for it to hide, or every later
  // crop on this page is shot through it.
  await closeDemo();
  await S('feature-h3', q('h5').filter({ hasText: /^\s*(Send & Receive|Decentralized Swaps|Manage your collectibles|Watching Wallets|Wallet Activity)\s*$/ }).and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Feature tag', desc: 'A feature tag ("Send & Receive", "WalletConnect Enabled") beside a section.', sel: 'h5 feature tag' });
  await S('section-h3', q('h1').filter({ hasText: /Send, receive, swap|The best way to experience NFTs|Relentless protection/ }).and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Feature section heading', desc: 'A feature section heading ("Send, receive, swap. All in one place.").', sel: 'section h1' });
  await S('faq-item', q(M('Item__StyledCollapsableItem')).and(page.locator(':visible')).first(), ['default'], { group: h, title: 'FAQ item', desc: 'A collapsible question/answer item in the home FAQ ("Is Family safe?").', sel: 'Item__StyledCollapsableItem' });
  await S('faq-toggle', q(M('Item__Toggle')).and(page.locator(':visible')).first(), B4, { group: h, title: 'FAQ toggle', desc: 'The 14px collapse toggle on an FAQ item; measured, never pressed.', sel: 'Item__Toggle' });
  // The "Friends of Family" row is a CSS marquee: pause its animation via
  // el.style (CSP-safe — no <style> injection) so hover can hold.
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('[class*="RowContainer"], [class*="Testimonials"]')) {
      el.style.animationPlayState = 'paused';
    }
  }).catch(() => {});
  await S('tweet-card', q('div[class*="Testimonials__Panel"]').and(page.locator(':visible')).first(), B4, { group: h, title: 'Tweet card', desc: 'A "Friends of Family" testimonial card linking to a tweet; measured, never followed.', sel: 'Testimonials__Panel' });
  await S('blog-card', q('a[href^="/blog/"]').and(page.locator(':visible')).first(), B4, { group: h, title: 'Latest-post card', desc: 'A "The latest from Family" post card on the home rail; measured, never followed.', sel: 'a[href^=/blog/]' });
  const f = G.footer;
  await S('site-footer', q('footer').and(page.locator(':visible')).last(), ['default'], { group: f, title: 'Site footer', desc: 'The sitemap footer (Developers / Resources / Company, \u00a9 2026).', sel: 'footer' });
  save();
}

async function blog() {
  if (!(await newPage('blog'))) return;
  await sheetsFor('blog');
  await chrome('blog');
  const g = G.blog;
  await S('blog-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Blog title', desc: 'The "Blog" page title.', sel: 'h1' }, { noScroll: true });
  await S('blog-filter', q('button').filter({ hasText: /^\s*(All|News|Wallet)\s*$/ }).and(page.locator(':visible')).first(), [...B4, 'opened'], { group: g, title: 'Blog filter', desc: 'A topic filter button (All / News / Wallet); "opened" is its selected state — a local filter toggle, never a submission.', sel: 'blog filter button' }, { allowLink: true });
  await S('blog-card', q('a[href^="/blog/"]').and(page.locator(':visible')).first(), B4, { group: g, title: 'Post card', desc: 'A post card on /blog; measured, never followed.', sel: 'a[href^=/blog/]' });
  await S('blog-date', q('p, time').filter({ hasText: /^\s*\d{1,2} \w+, \d{4}/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Post date line', desc: 'The post date/tag meta line on a post card ("13 May, 2025  News, Wallet").', sel: 'post date' });
  save();
}

async function blogpost() {
  if (!(await newPage('blogpost'))) return;
  await sheetsFor('blogpost');
  await chrome('blogpost');
  const g = G.blog;
  await S('post-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Article title', desc: 'The blog article title ("The Crypto Wallet Problem \u2013 Why We Created Family Accounts").', sel: 'article h1' }, { noScroll: true });
  await S('post-h2', q('h2').filter({ hasText: /Seamless Authentication|True Self-Custody/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Article subheading', desc: 'An H2 subheading inside the article.', sel: 'article h2' });
  await S('post-body', q('article p, main p, p').filter({ hasText: /seed phrases|private keys|custodial/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Article body', desc: 'Article body copy.', sel: 'article p' });
  await S('post-back', q('a').filter({ hasText: /back|all posts|blog/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Back link', desc: 'The article\u2019s back/index link if present; measured, never followed.', sel: 'back link' });
  save();
}

async function changelog() {
  if (!(await newPage('changelog'))) return;
  await sheetsFor('changelog');
  await chrome('changelog');
  const g = G.changelog;
  await S('cl-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Changelog title', desc: 'The "Changelog" page title.', sel: 'h1' }, { noScroll: true });
  await S('cl-filter', q('button').filter({ hasText: /^\s*(All|ConnectKit)\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Changelog filter', desc: 'A filter button on /changelog (All / ConnectKit); measured, never pressed.', sel: 'changelog filter button' });
  await S('cl-entry', q('h2').filter({ hasText: /Updated/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Entry heading', desc: 'A changelog entry heading ("Updated").', sel: 'changelog h2' });
  // Scoped to the entry container: a page-wide text match lands in the
  // header's nav dropdown ("Family Dedicated self-custody account."), not
  // the changelog copy.
  await S('cl-entry-body', q('main [class*="ChangelogPost"] p, main [class*="ChangelogPost"] [class*="ListWrapper"]'), ['default'], { group: g, title: 'Entry body', desc: 'Changelog entry copy.', sel: 'changelog entry paragraph' });
  save();
}

async function support() {
  if (!(await newPage('support'))) return;
  await sheetsFor('support');
  await chrome('support');
  const g = G.support;
  await S('sup-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Support title', desc: 'The "Help & Support" page title.', sel: 'h1' }, { noScroll: true });
  await S('sup-search', q('input[placeholder*="Search" i], input').and(page.locator(':visible')).first(), FIELD, { group: g, title: 'Support search', desc: 'The "Search Help & Support" field; typed into then cleared, never submitted.', sel: 'support search input' }, { noScroll: true, fillText: 'recover my wallet' });
  await S('sup-category', q('button, a').filter({ hasText: /^\s*(Ethereum 101|Getting Started with Family|Wallets)\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Category button', desc: 'A help-category button ("Ethereum 101", "Getting Started with Family"); measured, never followed.', sel: 'support category' });
  await S('sup-article-link', q('a[href^="/support/"]').and(page.locator(':visible')).first(), B4, { group: g, title: 'Article link', desc: 'A help-article link; measured, never followed.', sel: 'a[href^=/support/]' });
  save();
}

async function supportart() {
  if (!(await newPage('supportart'))) return;
  await sheetsFor('supportart');
  await chrome('supportart');
  const g = G.support;
  await S('art-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Article title', desc: 'The help-article title ("Import a wallet from MetaMask").', sel: 'article h1' }, { noScroll: true });
  await S('art-h2', q('h2').filter({ hasText: /How to/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Article heading', desc: 'A "How to" section heading inside the help article.', sel: 'article h2' });
  // Scoped to <article>: a page-wide text match lands in the side nav
  // ("Mission Control…"), not the article body.
  await S('art-body', q('article p, article li').filter({ hasText: /Secret Recovery Phrase|MetaMask/i }), ['default'], { group: g, title: 'Article body', desc: 'Help-article body copy.', sel: 'article p/li' });
  await S('art-side-link', q('a[href^="/support/"]').and(page.locator(':visible')).first(), B4, { group: g, title: 'Side-nav link', desc: 'A related-category/article link beside the article; measured, never followed.', sel: 'a[href^=/support/]' });
  save();
}

async function faqs() {
  if (!(await newPage('faqs'))) return;
  await sheetsFor('faqs');
  await chrome('faqs');
  const g = G.support;
  await S('faq-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'FAQs title', desc: 'The "FAQs" page title.', sel: 'h1' }, { noScroll: true });
  await S('faq-item', q(M('Item__StyledCollapsableItem')).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'FAQ item', desc: 'A collapsible question/answer item on /faqs.', sel: 'Item__StyledCollapsableItem' });
  await S('faq-toggle', q(M('Item__Toggle')).and(page.locator(':visible')).first(), B4, { group: g, title: 'FAQ toggle', desc: 'The collapse toggle on an FAQ item; measured, never pressed.', sel: 'Item__Toggle' });
  save();
}

async function legal() {
  if (!(await newPage('legal'))) return;
  await chrome('legal');
  const g = G.docs;
  await S('legal-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Legal title', desc: 'The "Legal" page title.', sel: 'h1' }, { noScroll: true });
  await S('legal-section', q('a, h2, h3, button').filter({ hasText: /Privacy|Terms|Family App|Sweepstakes/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Legal section', desc: 'A legal section link (Family App / Sweepstakes / privacy / terms); measured, never followed.', sel: 'legal section' });
  save();
}

async function docs() {
  if (!(await newPage('docs'))) return;
  await sheetsFor('docs');
  await chrome('docs');
  const g = G.docs;
  await S('docs-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Docs title', desc: 'The "Getting Started" docs title.', sel: 'h1' }, { noScroll: true });
  await S('docs-body', q('p, li, main div').filter({ hasText: /\w{8,}/ }).and(page.locator(':visible')).nth(2), ['default'], { group: g, title: 'Docs body', desc: 'Docs body copy.', sel: 'docs body' });
  save();
}

async function connectkit() {
  if (!(await newPage('connectkit'))) return;
  await sheetsFor('connectkit');
  await chrome('connectkit');
  const g = G.docs;
  await S('ck-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'ConnectKit title', desc: 'The "ConnectKit 1.9.1" docs title.', sel: 'h1' }, { noScroll: true });
  await S('ck-h2', q('h2').filter({ hasText: /Features|Community & Support/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Docs heading', desc: 'A section heading on the ConnectKit doc page.', sel: 'docs h2' });
  await S('ck-cta', q('button, a').filter({ hasText: /Stay Updated|Contact Us/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Docs CTA', desc: 'A docs action button ("Stay Updated" / "Contact Us"); measured, never pressed.', sel: 'docs CTA' });
  save();
}

async function account() {
  if (!(await newPage('account'))) return;
  await chrome('account');
  const g = G.docs;
  await S('acct-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Family doc title', desc: 'The "Family" docs title (the Family account doc).', sel: 'h1' }, { noScroll: true });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000, url: APP + '/' }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  // The card is the smallest container holding both the welcome text and
  // the field: the input's own __inputWrapper ancestor is only the field's
  // transparent shell, not the card.
  await S('login-card', q('div:has(input)').filter({ hasText: /Welcome to Aave Account/ }).last(), ['default'], { group: g, title: 'Login card', desc: 'The Aave Account login card on app.family.co — the container holding the welcome text and the field; at rest, never submitted.', sel: 'login card container' }, { noScroll: true });
  await S('login-h1', q('h1, h2, div, p').filter({ hasText: /Welcome to Aave Account/ }).and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Login title', desc: '"Welcome to Aave Account" — the login heading (Family Accounts is now Aave Account).', sel: 'login h1' }, { noScroll: true });
  await S('login-sub', q('p, div, span').filter({ hasText: /Log in or sign up to get started/ }).and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Login subline', desc: '"Log in or sign up to get started. We\u2019ll create an account if you don\u2019t have one yet."', sel: 'login subline' }, { noScroll: true });
  await S('login-field', q('input#email-or-number, input').and(page.locator(':visible')).first(), FIELD, { group: g, title: 'Email/phone field', desc: 'The "Email or Phone Number" login field; typed into then cleared, never submitted.', sel: '#email-or-number' }, { noScroll: true, fillText: 'name@example.com' });
  await S('login-learn', q('a').filter({ hasText: /Learn More/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Learn More link', desc: 'The "Learn More" link under the rebrand note; measured, never followed.', sel: 'Learn More' }, { noScroll: true });
  await S('login-footer-link', q('a').filter({ hasText: /^\s*(Developers|Privacy|Terms)\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Login footer link', desc: 'A footer link on the login page (Developers / Privacy / Terms); measured, never followed.', sel: 'login footer link' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The phone top bar: wordmark, menu button and the Get Started pill.', sel: 'mobile header' }, { noScroll: true });
  await S('m-menu', q(M('Nav__MenuButton')).and(page.locator(':visible')).first(), B4, { group: g, title: 'Mobile menu button', desc: 'The hamburger that opens the mobile nav drawer; measured, its press is a local toggle.', sel: 'Nav__MenuButton' }, { noScroll: true });
  await S('m-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The phone hero heading.', sel: 'mobile h1' });
  await S('m-download', q('a, button').filter({ hasText: /Download on iOS/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Mobile download CTA', desc: 'The "Download on iOS" pill on the phone hero; measured, never followed.', sel: 'mobile Download on iOS' });
  await S('m-faq-item', q(M('Item__StyledCollapsableItem')).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile FAQ item', desc: 'A collapsible FAQ item at 390 wide.', sel: 'mobile FAQ item' });
  await S('m-footer', q('footer').and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Mobile footer', desc: 'The phone footer.', sel: 'mobile footer' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); family.co and the app.family.co login paint a single light theme signed out';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, blog, blogpost, changelog, support, supportart, faqs, legal, docs, connectkit, account, login, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the Get Started pill),
  // so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header button');
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
