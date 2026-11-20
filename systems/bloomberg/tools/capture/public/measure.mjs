// Measures bloomberg.com's public components in every state reachable without
// signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home markets article quote live subscriptions mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// bloomberg.com's news surface ("phoenix") is a CSS-module React app; classes
// are <Scope>_<name>__<hash>, so M() selects the stable part. The /subscriptions
// offer pages are WordPress blocks — their own class scheme. Nothing is sent,
// bought or signed into: the only presses are local UI toggles — the Sign In
// sheet, the sitemap/edition dropdowns, the mobile Menu and the privacy modal's
// own controls (states only; never a real answer). The privacy modal is
// measured as it arrives, then hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';
import { pageRunner, exitStatus } from './run-pages.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/asia', markets: '/markets', quote: '/quote/SPX:IND', live: '/live', subscriptions: '/subscriptions' };
let page, cdp, current, context, run;
let articleUrl = null;
const touched = new Set();
const listed = new Map();
// Routes PerimeterX gates this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null } = {}) {
  current = key;
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, url || BASE + URLS[key], { wait, promo });
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
  Object.assign(c, { page: current, run, url: current === 'article' ? articleUrl : (URLS[current] && BASE + URLS[current]) }, meta);
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

async function S(key, target, list, meta = {}, opts = {}) {
  // meta is the entry's description only; an option placed here (fillText, cropLoc,
  // noToggle...) would be silently ignored, so refuse it
  for (const k of Object.keys(meta)) if (!['group', 'title', 'desc', 'sel'].includes(k)) throw new Error(`S(${key}): '${k}' is an option; pass it in opts`);
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
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
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

const G = {
  shell: 'Shell and navigation', home: 'Home front', markets: 'Markets',
  article: 'Article (paywalled)', quote: 'Quote page', live: 'Live TV',
  subscriptions: 'Subscription offers', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  // promo:'keep': the privacy modal stays up so it can be measured first,
  // then closePromo hides it for every component after.
  if (!(await newPage('home', { promo: 'keep' }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  // --- the privacy preferences modal, as it arrives (never answered) ---
  const dlg = q('[class*="media-ui-Privacy_wrapper"]').filter({ visible: true });
  await S('privacy-dialog', dlg, ['default'], { group: g, title: 'Privacy preferences modal', desc: 'The consent/preferences card every front page mounts. Measured as it arrives, then hidden; no checkbox or button was ever answered.', sel: '[class*="media-ui-Privacy_wrapper"]' }, { noScroll: true, crop: true });
  await S('privacy-checkbox', dlg.locator('input[type="checkbox"], [class*="Checkbox_input"]').first(), ['default'], { group: g, title: 'Privacy checkbox', sel: 'checkbox inside the privacy modal' }, { noScroll: true });
  await S('privacy-button', dlg.locator('button').first(), B4, { group: g, title: 'Privacy modal button', desc: 'The modal’s own button, states only — a real click would answer the prompt, which never happens.', sel: 'privacy modal button' }, { noScroll: true });
  await closePromo(page);
  // --- chrome ---
  await S('utility-bar', q('nav.bb-that').first(), ['default'], { group: g, title: 'Utility bar', desc: 'The thin top strip: "Bloomberg the Company & Its Products", Terminal demo, Anywhere login, customer support.', sel: 'nav.bb-that' }, { noScroll: true });
  const util = q('button, a').filter({ hasText: /Bloomberg the Company/i }).first();
  await S('utility-toggle', util, B4, { group: g, title: 'Company sitemap toggle', desc: 'Opens the "Bloomberg the Company & Its Products" sitemap dropdown.', sel: 'button:has-text("Bloomberg the Company")' }, { noScroll: true });
  await S('utility-toggle-open', util, ['opened'], { group: g, title: 'Company sitemap, open', desc: 'The toggle after its own press; the dropdown shows in the crop of the opened panel.', sel: 'button:has-text("Bloomberg the Company")' }, { noScroll: true, cropLoc: q('nav.bb-that').first() });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('logo-bar', q('[class*="nav-ui-LogoBar__bar"]').first(), ['default'], { group: g, title: 'Logo bar', desc: 'The black bar: wordmark, Sign In, Subscribe, search.', sel: '[class*="nav-ui-LogoBar__bar"]' }, { noScroll: true });
  await S('logo', q('a[class*="nav-ui-Logo__logo"]').first(), ['default'], { group: g, title: 'Logo', sel: 'a[class*="nav-ui-Logo__logo"]' }, { noScroll: true });
  const signin = q('button[class*="signInButton" i], button').filter({ hasText: /^Sign In$/ }).filter({ visible: true }).first();
  await S('signin-button', signin, B4, { group: g, title: 'Sign In button', desc: 'Opens the sign-in sheet; never a real sign-in.', sel: 'button:has-text("Sign In")' }, { noScroll: true });
  await S('subscribe-nav', q('a[class*="subscribeButton" i]').first(), B4, { group: g, title: 'Subscribe button', desc: 'The white Subscribe CTA in the logo bar. Measured, never followed.', sel: 'a[class*="subscribeButton"]' }, { noScroll: true });
  await S('search-button', q('a[href*="/search"], button[aria-label*="earch" i], [class*="searchButton" i]').first(), B4, { group: g, title: 'Search button', sel: 'nav search control' }, { noScroll: true });
  await S('section-nav', q('[class*="nav-ui-Nav"] nav, [class*="nav-ui-Nav"] [role="list"], [class*="nav-ui-Nav"] ul').first(), ['default'], { group: g, title: 'Section nav', desc: 'The strip under the logo bar: Live TV, Markets, Finance, Economics …', sel: '[class*="nav-ui-Nav"] nav/ul' }, { noScroll: true });
  await S('nav-link', q('[class*="nav-ui-Nav"] a').filter({ hasText: /^Economics$/ }).first(), B4, { group: g, title: 'Section link', sel: 'section nav a:has-text("Economics")' }, { noScroll: true });
  const more = q('[class*="nav-ui-Nav"] button, [class*="styles_nav"] button').filter({ hasText: /More|Markets/i }).filter({ visible: true }).first();
  await S('nav-dropdown', more, B4, { group: g, title: 'Nav dropdown', desc: 'A chevron item in the section nav; opens a subnav list.', sel: 'nav button:has-text("More")' }, { noScroll: true });
  await S('nav-dropdown-open', more, ['opened'], { group: g, title: 'Nav dropdown, open', desc: 'After its own toggle; the opened list shows in the crop.', sel: 'nav button:has-text("More")' }, { noScroll: true, cropLoc: q('[class*="nav-ui-Nav"], [class*="styles_nav"]').first() });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  const ed = q('button, a').filter({ hasText: /Edition$/i }).filter({ visible: true }).first();
  await S('edition-select', ed, B4, { group: g, title: 'Edition selector', sel: 'button:has-text("Edition")' }, { noScroll: true });
  // --- sign-in sheet (mounted by the Sign In button, same-origin iframe) ---
  // The Sign In button only mounts the login iframe (a local UI toggle, never
  // a submit): toggle()'s NEVER list refuses "Sign In" text, so click directly.
  const signinOpen = async () => { const b2 = q('button[class*="signInButton" i], button').filter({ hasText: /^Sign In$/ }).filter({ visible: true }).first(); if (await b2.count()) { await b2.click({ timeout: 5000 }).catch(() => b2.evaluate((el) => el.click())); await page.waitForTimeout(3000); } };
  await S('signin-sheet', q('iframe[src*="/account/iframe/login"], [class*="uverify" i]').first(), ['default'], { group: g, title: 'Sign-in sheet', desc: 'The /account/iframe/login sheet the Sign In button mounts. Opened and left; never used.', sel: 'iframe[src*="/account/iframe/login"]' }, { noScroll: true, open: signinOpen });
  const frame = page.frameLocator('iframe[src*="/account/iframe/login"]');
  await S('signin-email', frame.locator('input[type="email"], input[type="text"], input').first(), ['default', 'focused'], { group: g, title: 'Sign-in email field', desc: 'Inside the sign-in iframe. Focused only; nothing typed.', sel: 'input inside the sign-in iframe' }, { noScroll: true, noToggle: true });
  await S('signin-continue', frame.locator('button, [role="button"]').filter({ hasText: /continue|next|sign|email/i }).first(), ['default'], { group: g, title: 'Sign-in continue', desc: 'The sheet’s submit, measured at rest and never pressed.', sel: 'button inside the sign-in iframe' }, { noScroll: true, noToggle: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(600);
  // --- ticker ---
  const h = G.home;
  await S('ticker-bar', q('[class*="TickerBarWithPill_bar"], [class*="TickerBarWrapper"]').first(), ['default'], { group: h, title: 'Ticker bar', desc: 'The securities strip: Top Securities plus index quotes.', sel: '[class*="TickerBar"]' }, { noScroll: true });
  await S('ticker-item', q('a[class*="TickerBarWithPill_ticker"]').first(), B4, { group: h, title: 'Ticker quote', desc: 'One index in the strip (S&P 500 and its change). Links to the quote page; measured, never followed.', sel: 'a[class*="TickerBarWithPill_ticker"]' }, { noScroll: true });
  await S('ticker-pill', q('[class*="SecurityPill"]').first(), ['default'], { group: h, title: 'Security pill', sel: '[class*="SecurityPill"]' }, { noScroll: true });
  // --- story blocks ---
  await S('hero-story', q('[class*="StoryBlock_storyBlock"]').first(), ['default'], { group: h, title: 'Lead story block', desc: 'The top-story frame on the front page.', sel: '[class*="StoryBlock_storyBlock"]' });
  await S('hero-headline', q('[class*="Headline_phoenix"]').first(), ['default'], { group: h, title: 'Lead headline', desc: 'The big BWHaasGrotesk headline of the lead story.', sel: '[class*="Headline_phoenix"]' });
  await S('story-secondary', q('[class*="StoryBlock_secondaryStory"]').first(), ['default'], { group: h, title: 'Secondary story', desc: 'A smaller story block beside the lead.', sel: '[class*="StoryBlock_secondaryStory"]' });
  await S('story-link', q('a[class*="StoryBlock_storyLink"]').nth(1), B4, { group: h, title: 'Story link', desc: 'A headline link; measured, never followed.', sel: 'a[class*="StoryBlock_storyLink"]' });
  await S('dek', q('[class*="Summary_summary"]').first(), ['default'], { group: h, title: 'Story dek', desc: 'The summary paragraph under a headline.', sel: '[class*="Summary_summary"]' });
  await S('section-title', q('h3[class*="ModuleHeader_title"], [class*="ModuleHeader"] h3').first(), ['default'], { group: h, title: 'Module title', desc: 'A section header on the front (a topic or lane name).', sel: 'h3[class*="ModuleHeader_title"]' });
  await S('subscriber-badge', q('[class*="subscriberOnlyLabel"], [class*="SubscriberOnly"]').first(), ['default'], { group: h, title: 'Subscriber-only badge', desc: 'The caps label marking paywalled stories.', sel: '[class*="subscriberOnlyLabel"]' });
  await S('media-module', q('[class*="LineupContentTopic_primaryStory"], [class*="Media_vodVideo"]').first(), ['default'], { group: h, title: 'Media module', desc: 'A video/story card in a topic lane.', sel: '[class*="LineupContentTopic_primaryStory"]' });
  save();
}

async function markets() {
  if (!(await newPage('markets'))) return;
  await sheetsFor('markets');
  await chrome('markets');
  const g = G.markets;
  await S('markets-title', q('h1, h2').first(), ['default'], { group: g, title: 'Markets title', sel: 'h1' }, { noScroll: true });
  await S('index-card', q('[class*="IndexCard"], [class*="indexCard" i], [class*="MarketCard" i]').first(), ['default'], { group: g, title: 'Index card', desc: 'A market index summary card.', sel: '[class*="IndexCard"]' });
  await S('market-row', q('table tbody tr').nth(1), ['default'], { group: g, title: 'Market row', desc: 'A gainers/losers or index row.', sel: 'table tr / [class*="Mover"]' });
  await S('quote-link', q('a[href*="/quote/"]').first(), B4, { group: g, title: 'Quote link', desc: 'A row linking a security’s quote page; measured, never followed.', sel: 'a[href*="/quote/"]' });
  const tab = q('[role="tab"], button').filter({ hasText: /gainers|losers|movers|americas|emea|asia/i }).filter({ visible: true }).first();
  await S('market-tab', tab, B4, { group: g, title: 'Market tab', sel: 'tab/button naming a market board' });
  save();
}

async function article() {
  // The article URL is discovered on the home front at run time; a blocked
  // discovery load means the article route stays uncaptured too.
  if (!(await newPage('home', { promo: 'close', wait: 6000 }))) { failedPages.add('article'); return; }
  articleUrl = await page.evaluate(() => {
    const a = [...document.querySelectorAll('a[href*="/news/articles/"]')].find((x) => x.offsetParent);
    if (!a) return null;
    const u = new URL(a.getAttribute('href'), location.origin); u.search = ''; return u.toString();
  });
  if (!articleUrl) { log('  no article link'); return; }
  if (!(await newPage('article', { url: articleUrl, wait: 9000 }))) return;
  await sheetsFor('article');
  await chrome('article');
  const g = G.article;
  await S('article-kicker', q('[class*="kicker" i], [class*="Eyebrow"], [class*="eyebrow" i]').first(), ['default'], { group: g, title: 'Kicker', desc: 'The section breadcrumb over the headline (Technology / AI).', sel: '[class*="Eyebrow"]' }, { noScroll: true });
  await S('article-headline', q('h1').first(), ['default'], { group: g, title: 'Article headline', sel: 'h1' }, { noScroll: true });
  await S('byline', q('[class*="Byline"], [class*="byline" i]').first(), ['default'], { group: g, title: 'Byline', sel: '[class*="Byline"]' }, { noScroll: true });
  await S('lede-media', q('[class*="BasicLede"], [class*="lede" i]').first(), ['default'], { group: g, title: 'Lede media', desc: 'The lede image/video frame (the video itself errors headless).', sel: '[class*="BasicLede"]' });
  await S('share-button', q('[class*="share" i] a, [class*="Share"] a, a[href*="facebook" i], a[href*="twitter" i], a[href*="x.com" i]').first(), B4, { group: g, title: 'Share link', sel: 'share/social link' });
  await S('topic-link', q('a').filter({ hasText: /IPO Target|New Fable|Mythos/i }).first(), B4, { group: g, title: 'Topic link', desc: 'A related-topic pill under the nav.', sel: 'a:has-text("IPO Target")' }, { noScroll: true });
  const pay = q('[class*="PaywallAnchor"], [class*="paywall" i], [class*="Paywall"], [class*="Fence" i], [class*="fence" i]').filter({ visible: true });
  // The fence classes differ between article templates; when none match,
  // measure the band that contains the Claim This Offer CTA.
  const payLoc = (await pay.count()) ? pay.first() : q('a, button').filter({ hasText: /Claim This Offer/i }).first().locator('xpath=ancestor::*[self::div or self::section or self::aside][3]');
  await S('paywall', payLoc, ['default'], { group: g, title: 'Paywall fence', desc: 'The "Get unlimited access" band that gates the article body. The boundary of the public capture: nothing past it is public.', sel: '[class*="paywall" i] / Claim-offer band' });
  await S('claim-offer', q('a, button').filter({ hasText: /Claim This Offer/i }).first(), B4, { group: g, title: 'Claim offer CTA', desc: 'The paywall’s action; links to the offers page, measured, never followed.', sel: ':has-text("Claim This Offer")' });
  await S('article-body', q('article p, [class*="body-copy" i] p, [class*="article-body" i] p').filter({ visible: true, hasNotText: /internet connection|refresh the page/i }).first(), ['default'], { group: g, title: 'Body paragraph', desc: 'A body-text paragraph; absent while the paywall holds.', sel: 'article p' });
  save();
}

async function quote() {
  if (!(await newPage('quote'))) return;
  await sheetsFor('quote');
  const g = G.quote;
  await S('quote-title', q('h1').first(), ['default'], { group: g, title: 'Quote title', desc: 'The index name and ticker (S&P 500 INDEX / SPX:IND).', sel: 'h1' }, { noScroll: true });
  await S('follow-button', q('button').filter({ hasText: /^Follow/ }).first(), B4, { group: g, title: 'Follow button', desc: 'The Follow toggle beside the title — a real press would need an account, so it was never pressed.', sel: 'button:has-text("Follow")' }, { noScroll: true });
  await S('quote-price', q('[class*="price" i]:not([class*="icker"]):not([class*="ecurity"]):not([class*="ill"])').filter({ visible: true }).first(), ['default'], { group: g, title: 'Last price', sel: '[class*="price"]:not(ticker/security/pill)' });
  await S('quote-change', q('[class*="change" i]:not([class*="icker"]):not([class*="ecurity"]):not([class*="ill"])').filter({ visible: true }).first(), ['default'], { group: g, title: 'Price change', sel: '[class*="change"]:not(ticker/security/pill)' });
  await S('quote-stat', q('[class*="keyStat" i], dl div, table tbody tr').filter({ visible: true, hasNotText: /as of|updated/i }).first(), ['default'], { group: g, title: 'Key stat', desc: 'A key-statistics row (open, range, market cap).', sel: '[class*="keyStat"] / dl div' });
  save();
}

async function live() {
  if (!(await newPage('live'))) return;
  await sheetsFor('live');
  const g = G.live;
  await S('live-player', q('[class*="Player" i], [class*="player" i], video, [class*="GatedLiveVideo" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Live player', desc: 'The gated live-TV frame; the stream itself needs an account.', sel: '[class*="GatedLiveVideo"]' }, { noScroll: true });
  await S('live-paywall', q('[class*="PaywallAnchor"], [class*="paywall" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Live paywall', sel: '[class*="PaywallAnchor"]' });
  await S('live-schedule', q('[class*="schedule" i] li, [class*="Schedule"] li, [class*="schedule" i] tr, [class*="upcoming" i] li').filter({ visible: true }).first(), ['default'], { group: g, title: 'Schedule row', sel: '[class*="schedule"] li/tr' });
  save();
}

async function subscriptions() {
  if (!(await newPage('subscriptions', { wait: 10000 }))) return;
  await sheetsFor('subscriptions');
  const g = G.subscriptions;
  // the offers page's own header: header/[class*=header] caught the corporate utility bar
  await S('offer-header', q('[class*="offers-page-header"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Offers header', sel: 'header' }, { noScroll: true });
  await S('offer-hero', q('[class*="offers-header-block"]').first(), ['default'], { group: g, title: 'Offer hero', desc: 'The lead WordPress offer block ("Get context beyond the headlines").', sel: '[class*="offers-header-block"]' });
  await S('offer-price', q('[class*="offers-header-block-price"], [class*="price" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Offer price', sel: '[class*="price"]' });
  await S('offer-cta', q('[class*="wp-ga-button"], .wp-block-button a, a.wp-element-button').filter({ hasText: /Continue|Choose|Subscribe/i }).first(), B4, { group: g, title: 'Offer CTA', desc: 'The offer’s own action; links to checkout, measured, never followed.', sel: 'a.wp-ga-button' });
  await S('plan-card', q('[class*="rateplan-option-block"]').first(), ['default'], { group: g, title: 'Plan card', desc: 'A rate-plan option block (billing choices).', sel: '[class*="rateplan-option-block"]' });
  await S('plan-cta', q('a.wp-ga-button, [class*="wp-ga-button"]').filter({ hasText: /Choose/i }).first(), B4, { group: g, title: 'Plan CTA', sel: 'a.wp-ga-button:has-text("Choose")' });
  save();
}

async function footer() {
  if (!(await newPage('footer', { url: BASE + '/asia' }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  const fl = q('footer a, [class*="sitemap" i] a, [class*="footer" i] a').filter({ visible: true }).first();
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', sel: 'footer' }, { noScroll: true });
  await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/asia' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('[class*="LogoBarMobile"], [class*="nav-ui-LogoBar"], header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: '[class*="LogoBarMobile"]' }, { noScroll: true });
  const menu = q('button[class*="menuMobile" i], button').filter({ hasText: /^Menu$/ }).filter({ visible: true }).first();
  await S('m-menu-button', menu, B4, { group: g, title: 'Mobile menu button', sel: 'button:has-text("Menu")' }, { noScroll: true });
  await S('m-menu-open', menu, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The button after its own toggle; the opened drawer shows in the crop.', sel: 'button:has-text("Menu")' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-subscribe', q('a[class*="subscribeButton" i]').first(), B4, { group: g, title: 'Mobile subscribe', sel: 'a[class*="subscribeButton"]' }, { noScroll: true });
  await S('m-headline', q('[class*="Headline_phoenix"]').first(), ['default'], { group: g, title: 'Mobile headline', sel: '[class*="Headline_phoenix"]' });
  await S('m-ticker', q('[class*="TickerBarWithPill_mobileSecurities"], [class*="TickerBar"]').first(), ['default'], { group: g, title: 'Mobile ticker', sel: '[class*="TickerBar"]' }, { noScroll: true });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, markets, article, quote, live, subscriptions, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
// A page counts as finished only when its runner returns without throwing and
// no bot check stopped it: any other throw (a goto timeout, a locator outside
// S()) used to abort the loop, and the finally then pruned every page after it.
// A page that throws is recorded as broken and the run goes on; the exit
// status at the end is nonzero when any page threw (run-pages.mjs).
const { finished, broken, runPage } = pageRunner(() => current, log);
const pageDone = (c) => finished.has(c.page) && !failedPages.has(c.page) && !broken.has(c.page);
try {
  for (const k of order) { if (k !== 'mobile' && k !== 'article') await runPage(plan[k]); }
  if (!pages.length || pages.includes('article')) await runPage(article);
  if (!pages.length || pages.includes('home')) await runPage(footer);
  if (!pages.length || pages.includes('mobile')) await runPage(plan.mobile);
  if (!pages.length || pages.includes('home')) await runPage(reducedMotion, 'home', '[class*="TickerBarWithPill_bar"]');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune only what a finished page no longer produces: a page that was
    // blocked (PerimeterX) or threw keeps its earlier readings under their
    // original provenance instead of being erased and republished.
    if (!touched.has(key)) { if (!pages.length && pageDone(c)) delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want && pageDone(c)) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
process.exitCode = exitStatus(broken);
