// Measures Leonardo.Ai's public components in every state reachable without
// an account. Marketing (leonardo.ai), the signed-out app shell
// (app.leonardo.ai), docs.leonardo.ai and the OAuth login card. Nothing is
// signed into, submitted, purchased or followed through OAuth. Consent is
// hidden, never answered. Pressed states are forced through CDP so a click
// never fires.
//
//   PLAYWRIGHT=... node measure.mjs [home pricing api learn contact imagegen app blueprints login docs mobile]
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, DOCS, launch, patch, open, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: BASE + '/',
  pricing: BASE + '/pricing',
  api: BASE + '/api',
  learn: BASE + '/learn',
  contact: BASE + '/contact-us',
  imagegen: BASE + '/ai-image-generator',
  app: APP + '/',
  blueprints: APP + '/blueprints',
  login: APP + '/auth/login',
  docs: DOCS + '/docs/getting-started',
  mobile: BASE + '/',
  'mobile-app': APP + '/',
};
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|you have been blocked/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 7000, url = null } = {}) {
  current = key;
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme: 'dark' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', colorScheme: 'dark' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const opened = await open(page, url || URLS[key], { wait }).then(() => true, (e) => { log('  !', key, String(e.message || e).split('\n')[0]); return false; });
  if (!opened || await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  return true;
}

async function chrome(key) {
  const z = await page.evaluate(() => {
    const seen = [];
    for (const el of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(el);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      const r = el.getBoundingClientRect();
      if (r.width < 40 || r.height < 10) continue;
      seen.push({ node: el.tagName.toLowerCase(), z: cs.zIndex, pos: cs.position, rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, text: (el.innerText || '').slice(0, 40).replace(/\n/g, '|') });
    }
    return seen.sort((a, b) => (parseInt(b.z) || 0) - (parseInt(a.z) || 0)).slice(0, 16);
  }).catch(() => []);
  out._meta.chrome ??= {};
  out._meta.chrome[key] = z;
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(200);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el);
    how = 'focus()';
  }
  await page.waitForTimeout(300);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(300);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: URLS[current] }, meta);
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
      try { file = await crop(page, (opts.cropLoc || loc).and(page.locator(':visible')).first(), `${key}-${state}`, opts.pad ?? 8); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
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
  const loc = target.and(page.locator(':visible')).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key);
    if (!has) out.components[key].missing = true;
    else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
    return;
  }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (st === 'hover') {
        await loc.hover({ timeout: 4000 }).catch(() => loc.hover({ timeout: 4000, force: true }));
        await page.waitForTimeout(350);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(loc);
      } else if (st === 'pressed') {
        undo = await forcePseudo(loc, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.focus()));
        await page.waitForTimeout(300);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'a quiet studio portrait', { delay: 8 });
        await page.waitForTimeout(300);
        undo = async () => { await loc.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); };
        via = 'typed sample text, then deleted; nothing sent';
      } else if (st === 'opened') {
        // The kit's guards: never a link, never a submit button, never a
        // control whose label names an action. "Create" is allowed only as a
        // disclosure (aria-expanded or aria-haspopup), which opens a local menu.
        const t = await loc.evaluate((el) => ({
          tag: el.tagName, type: (el.getAttribute('type') || '').toLowerCase(),
          text: (el.innerText || el.getAttribute('aria-label') || '').trim(),
          disclosure: el.hasAttribute('aria-expanded') || el.hasAttribute('aria-haspopup'),
        }));
        const NEVER = /^(send|submit|sign in|sign up|log in|create|generate|upload|share|subscribe|start now|upgrade|buy|checkout|delete|open)$|continue with/i;
        if (t.tag === 'A' || t.type === 'submit' || (NEVER.test(t.text) && !(/^create$/i.test(t.text) && t.disclosure))) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
        await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click()));
        await page.waitForTimeout(700);
        via = 'own toggle, local only';
      } else via = 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prevSt = out.components[key].states[st];
      if (prevSt && prevSt.style) prevSt.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
  }
  await reset();
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];
const G = {
  chrome: 'Marketing chrome',
  hero: 'Marketing hero',
  pricing: 'Pricing',
  app: 'App shell',
  login: 'Login boundary',
  docs: 'Docs',
  mobile: 'Phone',
};

async function home() {
  if (!(await newPage('home'))) return;
  await chrome('home');
  const g = G.chrome;
  await S('mkt-header', q('nav').first(), ['default'], { group: g, title: 'Marketing header', desc: 'The signed-out marketing nav: Create, Industry, Business, Learn, Pricing, Contact, Tutorial, Log in. There is no header element.', sel: 'nav' }, { noScroll: true });
  await S('mkt-nav-pricing', q('a[href="/pricing"]').first(), B4, { group: g, title: 'Pricing nav link', desc: 'A nav text link. Hover and focus measured. The link was not followed.', sel: 'a[href=/pricing]' }, { noScroll: true });
  await S('mkt-login', q('a[href="https://app.leonardo.ai/"]').filter({ hasText: /log in/i }).first(), B4, { group: g, title: 'Log in link', desc: 'The nav Log in control. Measured at rest. It opens the app, which then gates on an account. Never followed.', sel: 'Log in' }, { noScroll: true });
  await S('mkt-menu', q('nav button, button').filter({ hasText: /^create$/i }).first(), [...B4, 'opened'], { group: g, title: 'Create menu', desc: 'A nav disclosure. Opened locally. No destination was followed.', sel: 'button Create' }, { noScroll: true });
  const gh = G.hero;
  await S('mkt-h1', q('h1').first(), ['default'], { group: gh, title: 'Hero display', desc: 'The marketing display heading on the black canvas.', sel: 'h1' }, { noScroll: true });
  await S('mkt-cta', q('a, button').filter({ hasText: /^start now$/i }).first(), B4, { group: gh, title: 'Start now button', desc: 'The primary marketing CTA. States measured through hover, focus and a forced press. Never followed. It lands on the signed-out app, then an account.', sel: 'Start now' }, { noScroll: true });
  await S('mkt-footer', q('footer').last(), ['default'], { group: g, title: 'Marketing footer', desc: 'The sitemap footer: product, company, legal and social links.', sel: 'footer' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await chrome('pricing');
  const g = G.pricing;
  await S('pr-h1', q('h1').first(), ['default'], { group: g, title: 'Pricing heading', desc: 'The pricing page display heading.', sel: 'h1' }, { noScroll: true });
  await S('pr-tab', q('button, a, [role="tab"]').filter({ hasText: /^team$/i }).first(), B4, { group: g, title: 'Plan audience tab', desc: 'Solo / Team / API switch. Measured. A tab click would only change the public price table, so opened is not required for the token.', sel: 'TEAM tab' }, { noScroll: true });
  await S('pr-cycle', q('button, [role="switch"], label').filter({ hasText: /pay yearly|yearly/i }).first(), B4, { group: g, title: 'Billing cycle control', desc: 'Pay Yearly / Pay Monthly. Measured at rest. Not toggled, so no price request is sent.', sel: 'Pay Yearly' }, { noScroll: true });
  await S('pr-card', q('section, article, div').filter({ hasText: /\$0/ }).filter({ hasText: /subscribe/i }).first(), ['default'], { group: g, title: 'Free plan card', desc: 'The Free plan card on the public pricing table.', sel: 'free plan' }, { noScroll: true });
  await S('pr-subscribe', q('a').filter({ hasText: /^subscribe$/i }).first(), B4, { group: g, title: 'Subscribe button', desc: 'A plan Subscribe link to app.leonardo.ai. Measured, never followed. Checkout sits behind an account.', sel: 'Subscribe' }, { noScroll: true });
  save();
}

async function api() {
  if (!(await newPage('api'))) return;
  await chrome('api');
  await S('api-h1', q('h1').first(), ['default'], { group: G.hero, title: 'API hero', desc: 'The public API marketing heading.', sel: 'h1' }, { noScroll: true });
  await S('api-docs', q('a[href*="docs.leonardo.ai"]').first(), B4, { group: G.chrome, title: 'View documentation link', desc: 'A link to the public docs. Measured, not followed from this page.', sel: 'docs link' });
  save();
}

async function learn() {
  if (!(await newPage('learn'))) return;
  await S('learn-h1', q('h1').first(), ['default'], { group: G.hero, title: 'Learn heading', desc: 'The public Learn page heading.', sel: 'h1' }, { noScroll: true });
  await S('learn-card', q('a[href*="/news"], article a, a').filter({ hasText: /.{12,}/ }).nth(4), ['default', 'hover'], { group: G.hero, title: 'Learn card', desc: 'A published article or tutorial card. Hover measured. Not opened.', sel: 'learn card' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  await S('ct-h1', q('h1').first(), ['default'], { group: G.chrome, title: 'Contact heading', desc: 'The public contact page heading. The form itself is a submission boundary and was not filled or sent.', sel: 'h1' }, { noScroll: true });
  save();
}

async function imagegen() {
  if (!(await newPage('imagegen'))) return;
  await S('ig-h1', q('h1').first(), ['default'], { group: G.hero, title: 'Image generator heading', desc: 'A feature marketing page heading.', sel: 'h1' }, { noScroll: true });
  await S('ig-cta', q('a').filter({ hasText: /start now|try/i }).first(), B4, { group: G.hero, title: 'Feature CTA', desc: 'A feature-page CTA into the app. Measured, never followed.', sel: 'feature CTA' });
  save();
}

async function appPage() {
  if (!(await newPage('app', { wait: 7000 }))) return;
  await chrome('app');
  const g = G.app;
  await S('app-sidebar', q('a[href="/"]').filter({ hasText: /home/i }).locator('xpath=ancestor::nav[1]').first(), ['default'], { group: g, title: 'App sidebar', desc: 'The signed-out app nav: Create, Library, Agent, Upscaler, Blueprints and the rest. Library and other account routes redirect to login.', sel: 'nav' }, { noScroll: true });
  await S('app-nav-create', q('a[href*="/generate"], a').filter({ hasText: /^create$/i }).first(), B4, { group: g, title: 'Create nav link', desc: 'The Create item. Measured. Generate itself is a submission boundary.', sel: 'Create' }, { noScroll: true });
  await S('app-signup', q('a').filter({ hasText: /sign up|create free account/i }).first(), B4, { group: g, title: 'Sign up button', desc: 'The signed-out Sign up control. Measured, never followed.', sel: 'Sign up' }, { noScroll: true });
  await S('app-signin', q('a').filter({ hasText: /^sign in$/i }).first(), B4, { group: g, title: 'Sign in button', desc: 'The signed-out Sign in control. Measured, never followed.', sel: 'Sign in' }, { noScroll: true });
  await S('app-h1', q('h1').first(), ['default'], { group: g, title: 'App display heading', desc: 'The signed-out generate shell heading.', sel: 'h1' }, { noScroll: true });
  await S('app-prompt', q('textarea').first(), FIELD, { group: g, title: 'Prompt field', desc: 'The public prompt field. Sample text was typed and cleared. Generate was never pressed.', sel: 'textarea' }, { fillText: 'a quiet studio portrait' });
  await S('app-generate', q('button').filter({ hasText: /^generate$/i }).first(), B4, { group: g, title: 'Generate button', desc: 'The Generate control. States forced through CDP. Never clicked, so no generation ran.', sel: 'Generate' }, { noScroll: true });
  await S('app-ratio', q('button').filter({ hasText: /^1:1$/ }).first(), B4, { group: g, title: 'Aspect chip', desc: 'An aspect-ratio chip on the signed-out composer. Measured at rest. Not selected, so no generation settings were submitted.', sel: '1:1' }, { noScroll: true });
  await S('app-card', q('a, article, button').filter({ hasText: /GPT Image|Seedance|Featured/i }).first(), ['default', 'hover'], { group: g, title: 'Featured model card', desc: 'A published model card on the signed-out home. Hover measured. Not opened.', sel: 'featured card' });
  save();
}

async function blueprints() {
  if (!(await newPage('blueprints', { wait: 6000 }))) return;
  await S('bp-h1', q('h1').first(), ['default'], { group: G.app, title: 'Blueprints heading', desc: 'The public blueprint catalog heading.', sel: 'h1' }, { noScroll: true });
  await S('bp-search', q('input[type="search"], input[placeholder*="earch" i]').first(), FIELD, { group: G.app, title: 'Blueprint search', desc: 'The catalog search field. Typed and cleared. Not submitted.', sel: 'search' }, { noScroll: true, fillText: 'portrait' });
  await S('bp-chip', q('button, a').filter({ hasText: /^all$/i }).first(), B4, { group: G.app, title: 'Category chip', desc: 'A blueprint category chip. Measured at rest.', sel: 'All chip' }, { noScroll: true });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 5000 }))) return;
  const g = G.login;
  await S('li-h1', q('h1').first(), ['default'], { group: g, title: 'Login heading', desc: 'The sign-up or login card. The boundary of the signed-out capture.', sel: 'h1' }, { noScroll: true });
  await S('li-canva', q('button').filter({ hasText: /canva/i }).first(), B4, { group: g, title: 'Continue with Canva', desc: 'An OAuth button. Measured at rest. Never followed.', sel: 'Canva' }, { noScroll: true });
  await S('li-google', q('button').filter({ hasText: /google/i }).first(), B4, { group: g, title: 'Continue with Google', desc: 'An OAuth button. Measured at rest. Never followed.', sel: 'Google' }, { noScroll: true });
  await S('li-email', q('button').filter({ hasText: /continue with email/i }).first(), B4, { group: g, title: 'Continue with Email', desc: 'The email path control. Measured. Not clicked, so the email form was not submitted. A Turnstile widget is present and was not solved.', sel: 'Continue with Email' }, { noScroll: true });
  await S('li-help', q('a[href*="intercom.help"]').first(), B4, { group: g, title: 'Need help link', desc: 'The public login FAQ link. Measured, not followed.', sel: 'Need help' });
  save();
}

async function docs() {
  if (!(await newPage('docs', { wait: 6000 }))) return;
  const g = G.docs;
  await S('docs-h1', q('h1').first(), ['default'], { group: g, title: 'Docs heading', desc: 'The Quick Start heading on the public ReadMe docs.', sel: 'h1' }, { noScroll: true });
  await S('docs-search', q('button').filter({ hasText: /search/i }).first(), B4, { group: g, title: 'Docs search', desc: 'The docs search control. Measured at rest. The search dialog was not opened, so no query was sent.', sel: 'Search' }, { noScroll: true });
  await S('docs-nav', q('nav a, aside a').first(), ['default', 'hover'], { group: g, title: 'Docs nav link', desc: 'A sidebar documentation link. Hover measured. Not followed.', sel: 'docs nav a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  const g = G.mobile;
  await S('m-header', q('nav').first(), ['default'], { group: g, title: 'Phone nav', desc: 'The marketing nav at 390px.', sel: 'nav' }, { noScroll: true });
  await S('m-menu', q('nav button, button').first(), B4, { group: g, title: 'Phone menu button', desc: 'The first nav button at 390px. States measured. The drawer shot is in the screenshot pass.', sel: 'nav button' }, { noScroll: true });
  await S('m-cta', q('a').filter({ hasText: /start now|log in/i }).first(), B4, { group: g, title: 'Phone CTA', desc: 'A phone-width CTA. Measured, never followed.', sel: 'phone CTA' }, { noScroll: true });
  save();
}

async function mobileApp() {
  if (!(await newPage('mobile-app', { mobile: true, url: APP + '/' }))) return;
  await S('m-app-bar', q('nav, header, aside').first(), ['default'], { group: G.mobile, title: 'Phone app chrome', desc: 'The signed-out app chrome at 390px.', sel: 'app chrome' }, { noScroll: true });
  await S('m-app-prompt', q('textarea').first(), ['default'], { group: G.mobile, title: 'Phone prompt', desc: 'The prompt field at 390px, at rest.', sel: 'textarea' });
  save();
}

run = new Date().toLocaleDateString('en-CA'); // the local date of the capture
out._meta.read = run;
out._meta.viewport = '1440 x 900, phone group 390 x 844. Leonardo.Ai public surfaces: marketing, signed-out app shell, docs, login card. One dark theme on each. Account, generation, checkout and OAuth were not entered.';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch({ colorScheme: 'dark' });
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, api, learn, contact, imagegen, app: appPage, blueprints, login, docs, mobile, 'mobile-app': mobileApp };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { await plan[k](); finishedPages.add(k); }
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
