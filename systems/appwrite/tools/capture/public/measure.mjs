// Measures appwrite.io's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing docs blog signin mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// appwrite.io is a SvelteKit + Tailwind v4 build that pins the dark theme on
// every captured route; components are found by role, aria-label or stable
// text, never by the utility class soup. Nothing is sent, created or signed
// into: the only presses are local UI toggles — the mobile menu, the Products
// nav flyout, a pricing FAQ accordion. Text typed into the email field is
// deleted again; the sign-in form is never submitted.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';
import { pageRunner, exitStatus } from './run-pages.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/',
  pricing: '/pricing',
  docs: '/docs/quick-starts/react',
  blog: '/blog',
  signin: '/sign-in',
};
let page, cdp, current, context, run;
const touched = new Set();
const blockedPages = new Set(); // pages a bot check stopped; their old readings are kept
const listed = new Map(); // component -> the states this run's specs list for it

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|page cannot be found/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

// ---------- helpers ----------

async function newPage(key, { mobile = false, wait = 6000 } = {}) {
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
  await open(page, BASE + URLS[key], { wait });
  if (await blocked()) { log('  BLOCKED', key); blockedPages.add(key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
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

// comp() merges the spec's meta into the entry and marks it touched. The
// page/run/url provenance is only written once the target is found, so a
// re-run whose selector misses keeps the earlier evidence's own page, run and
// url instead of stamping a new date on stale readings (FIELD-NOTES).
function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, meta);
  // the page that owns the entry, even when its element is missing: stale-entry
  // cleanup (pageDone) needs it; found() restamps page/run/url on a real reading
  c.page ??= current;
  touched.add(key);
  c.states ??= {};
  return c;
}

function found(c) {
  delete c.missing;
  delete c.recaptureMissed;
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] });
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

const FILL = 'dev@example.com';

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  const c = comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  if (opts.open) { await reset(); await opts.open(); }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    log('  ! missing', key);
    c.missing = true;
    c.recaptureMissed = run; // earlier states keep their own run's provenance
    return;
  }
  found(c);
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
        // a state that did not receive keyboard focus is not a captured focus
        if (via === 'focus failed') throw new Error('keyboard focus did not land on the element');
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
      } else if (st === 'opened') {
        await toggle(loc);
        await page.waitForTimeout(900);
        via = 'own toggle';
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

// Clicks a UI toggle (nav flyout, menu, accordion). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|generate|upload|start project|sign up|get started|claim|share|export|upgrade|buy|purchase|pay|checkout)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

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

const G = {
  shell: 'Shell and navigation', hero: 'Home', pricing: 'Pricing', docs: 'Docs',
  blog: 'Blog', signin: 'Sign-in gate', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// ---------- pages ----------

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('banner', q('div').filter({ hasText: /thrilled|announce/i }).locator('div:has(> button[aria-label*="ismiss" i])').first(), ['default'], { group: g, title: 'Announcement banner', desc: 'The strip above the header carrying the current announcement and a dismiss button.', sel: 'div:has(> button[aria-label*="ismiss" i])' }, { noScroll: true });
  await S('banner-dismiss', q('button[aria-label*="ismiss" i]'), B4, { group: g, title: 'Banner dismiss button', sel: 'button[aria-label*="ismiss" i]' }, { noScroll: true });
  const header = q('header').first();
  await S('header', header, ['default'], { group: g, title: 'Top bar', desc: 'The fixed glass bar over every marketing page: logo, Products/Solutions flyout buttons, section links, GitHub stars, Sign in/up.', sel: 'header' }, { noScroll: true });
  await S('logo', q('a[aria-label="Appwrite"], a[href="/"]').filter({ visible: true }), ['default'], { group: g, title: 'Logo', sel: 'a[aria-label="Appwrite"]' }, { noScroll: true });
  await S('nav-link', q('header a').filter({ hasText: /^Pricing$/ }), B4, { group: g, title: 'Nav link', desc: 'A top-level destination in the bar: 13px text in a 36px rounded-md row.', sel: 'header a:has-text("Pricing")' }, { noScroll: true });
  const productsBtn = q('header button').filter({ hasText: /^Products$/ });
  await S('nav-menu-button', productsBtn, B4, { group: g, title: 'Nav flyout button', desc: 'Products and Solutions open a flyout; measured at rest, never opened (the flyout is captured in screenshots only when it mounts open).', sel: 'header button:has-text("Products")' }, { noScroll: true });
  await S('nav-menu-open', productsBtn, ['opened'], { group: g, title: 'Nav flyout, open', desc: 'The button after its own flyout toggle: the opened panel underneath (a popover-foreground div the toggle mounts) is what the crop shows.', sel: 'header button:has-text("Products")', }, { noScroll: true, cropLoc: q('div[class*="popover" i]') });
  await page.keyboard.press('Escape'); await page.waitForTimeout(600);
  await S('nav-github', q('header a[aria-label*="GitHub" i], header a[href*="github"]'), B4, { group: g, title: 'GitHub stars link', desc: 'The star-count link to the repo.', sel: 'header a[aria-label*="GitHub" i]' }, { noScroll: true });
  await S('signin-button', q('header a').filter({ hasText: /^Sign in$/ }), B4, { group: g, title: 'Sign in button', desc: 'Ghost-style header action. Measured, never followed.', sel: 'header a:has-text("Sign in")' }, { noScroll: true });
  await S('signup-button', q('header a').filter({ hasText: /^Sign up$/ }), B4, { group: g, title: 'Sign up button', desc: 'The filled header action. Measured, never followed.', sel: 'header a:has-text("Sign up")' }, { noScroll: true });
  await S('skip-link', q('a').filter({ hasText: /^Skip to content$/ }), ['focus-visible'], { group: g, title: 'Skip link', desc: 'The off-screen accessibility link, revealed by keyboard focus.', sel: 'a:has-text("Skip to content")' }, { noScroll: true });

  const h = G.hero;
  await S('announcement-pill', q('a').filter({ hasText: /thrilled to announce/i }), B4, { group: h, title: 'Announcement pill', desc: 'The "Breaking" link pill under the hero.', sel: 'a:has-text("thrilled to announce")' }, { noScroll: true });
  await S('hero-title', q('h1').first(), ['default'], { group: h, title: 'Hero title', desc: 'The 48px Aeonik headline with the brand gradient text.', sel: 'h1' }, { noScroll: true });
  await S('cta-primary', q('a,button').filter({ hasText: /^Start project$/ }), B4, { group: h, title: 'Primary CTA', desc: '"Start project": the main action, brand pink. Measured, never followed.', sel: 'a:has-text("Start project")' }, { noScroll: true });
  await S('cta-secondary', q('a,button').filter({ hasText: /^View docs$/ }), B4, { group: h, title: 'Secondary CTA', desc: '"View docs": the quiet sibling. Measured, never followed.', sel: 'a:has-text("View docs")' }, { noScroll: true });
  await S('framework-icon', q('a[aria-label="React"], button[aria-label="React"]'), B4, { group: h, title: 'Framework icon button', desc: 'One of the 36px round framework icons under the hero strip.', sel: '[aria-label="React"]' });
  const cardLink = q('a[aria-label^="Learn more about"]');
  await S('product-card', cardLink, ['default', 'hover', 'focus-visible'], { group: h, title: 'Product card', desc: 'A services-grid card (Auth/Databases/...): the overlay link covers the whole card, so the card edges are what the crop shows; painted fills come from the ancestors row.', sel: 'a[aria-label^="Learn more about"]' });
  await S('section-title', q('h2').filter({ hasText: /All the services/i }), ['default'], { group: h, title: 'Section headline', desc: 'The 40px Aeonik section title.', sel: 'h2:has-text("All the services")' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h2, h1').filter({ hasText: /Everything your app needs/i }), ['default'], { group: g, title: 'Pricing title', sel: 'h2:has-text("Everything your app needs")' }, { noScroll: true });
  await S('plan-card', q('article').filter({ has: page.locator('h2', { hasText: /^Free$/ }) }).first(), ['default'], { group: g, title: 'Plan card', desc: 'One pricing column: name, price, feature list and its own CTA; an <article> with the muted-tint fill and hairline border.', sel: 'article:has(h2 "Free")' });
  await S('plan-price', q('div,span,p').filter({ hasText: /^\$0$/ }).last(), ['default'], { group: g, title: 'Plan price', sel: 'text "$0"' });
  await S('plan-cta', q('article a, article button').filter({ hasText: /^Start project$/ }), B4, { group: g, title: 'Plan CTA', desc: 'The per-card action. Measured, never followed.', sel: 'article a:has-text("Start project")' });
  await S('plan-cta-contact', q('a,button').filter({ hasText: /^Contact us$/ }).first(), B4, { group: g, title: 'Enterprise CTA', desc: '"Contact us" on the Enterprise card. Measured, never followed.', sel: 'a:has-text("Contact us")' });
  const faqBtn = q('button[aria-expanded]').filter({ visible: true }).last();
  // The accordion item the button belongs to: the nearest ancestor that also
  // holds the answer region, so the open crop shows the question + answer.
  const faqItem = faqBtn.locator('xpath=ancestor::*[.//*[@role="region" or @data-state="open"]][1]');
  await S('faq-question', faqBtn, B4, { group: g, title: 'FAQ accordion button', sel: 'button[aria-expanded]' });
  await S('faq-open', faqBtn, ['opened'], { group: g, title: 'FAQ accordion, open', desc: 'The same item after its own toggle; the answer region shows in the crop.', sel: 'button[aria-expanded]' }, { cropLoc: faqItem });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  await S('compare-link', q('a').filter({ hasText: /^Compare plans$/ }), B4, { group: g, title: 'Compare plans link', desc: 'link-neutral text link.', sel: 'a:has-text("Compare plans")' });
  save();
}

async function docs() {
  if (!(await newPage('docs'))) return;
  const g = G.docs;
  await S('docs-search', q('button').filter({ hasText: /Search documentation/i }), B4, { group: g, title: 'Docs search button', desc: 'The command-K search trigger in the docs header. Measured, never opened.', sel: 'button:has-text("Search documentation")' }, { noScroll: true });
  const sideLink = q('aside a, nav a').filter({ hasText: /^Tutorials$/ }).first();
  await S('docs-nav-link', sideLink, B4, { group: g, title: 'Docs sidebar link', sel: 'aside a:has-text("Tutorials")' }, { noScroll: true });
  const cur = q('[aria-current="page"], [aria-current="true"]').first();
  await S('docs-nav-active', cur, ['default'], { group: g, title: 'Docs sidebar item, current', desc: 'The item the page marks current, if any.', sel: '[aria-current]' }, { noScroll: true });
  const pre = q('main pre, article pre, pre').first();
  await S('code-block', pre, ['default'], { group: g, title: 'Code block', desc: 'The framed snippet on a quick-start page, with --code-* syntax colours.', sel: 'pre' });
  const inline = q('main code, article code').filter({ visible: true }).first();
  await S('code-inline', inline, ['default'], { group: g, title: 'Inline code', sel: 'article code' });
  await S('docs-prose-link', q('main a, article a').filter({ hasText: /\w{4,}/ }).first(), B4, { group: g, title: 'Prose link', sel: 'article a' });
  await S('docs-h1', q('main h1, article h1').first(), ['default'], { group: g, title: 'Docs page title', sel: 'article h1' });
  const stepItem = q('h2, h3').filter({ hasText: /\w/ }).nth(1);
  await S('docs-h2', stepItem, ['default'], { group: g, title: 'Docs section heading', sel: 'article h2/h3' });
  save();
}

async function blog() {
  if (!(await newPage('blog'))) return;
  const g = G.blog;
  await S('blog-title', q('h1').first(), ['default'], { group: g, title: 'Blog title', sel: 'h1' }, { noScroll: true });
  // A story card is the article holding the headline: the bare a.block
  // selector matched only the headline link inside it.
  const card = q('article').filter({ has: q('h2') }).first();
  await S('post-card', card, ['default', 'hover'], { group: g, title: 'Post card', desc: 'A story tile: image, headline, author row.', sel: 'article:has(h2)' });
  await S('post-headline', q('h2').filter({ hasText: /\w{10,}/ }).first(), ['default'], { group: g, title: 'Post headline', sel: 'h2' });
  await S('author-link', q('a').filter({ hasText: /^Eldad Fux$|^Aditya Oberai$/ }).first(), B4, { group: g, title: 'Author link', sel: 'author name link' });
  await S('blog-search', q('button').filter({ hasText: /Search articles/i }), B4, { group: g, title: 'Blog search button', desc: 'Measured, never opened.', sel: 'button:has-text("Search articles")' });
  await S('category-chip', q('a').filter({ hasText: /^Tutorials$/ }).first(), B4, { group: g, title: 'Category link', sel: 'a:has-text("Tutorials")' });
  save();
}

async function signin() {
  if (!(await newPage('signin'))) return;
  const g = G.signin;
  await S('signin-card', q('h1').filter({ hasText: /Welcome back/i }).locator('xpath=ancestor::form[1] | ancestor::div[contains(@class,"rounded") and contains(@class,"border")][1]').first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The centred auth panel.', sel: 'form/card container' }, { noScroll: true });
  await S('signin-title', q('h1').filter({ hasText: /Welcome back/i }), ['default'], { group: g, title: 'Sign-in title', sel: 'h1' }, { noScroll: true });
  await S('oauth-button', q('button').filter({ hasText: /Login with GitHub/i }), B4, { group: g, title: 'OAuth button', desc: '"Login with GitHub": the wide identity-provider row. Measured, never pressed.', sel: 'button:has-text("Login with GitHub")' });
  await S('oauth-icon-button', q('button[aria-label="Login with GitLab"]'), B4, { group: g, title: 'OAuth icon button', desc: 'The square GitLab/Bitbucket identity buttons. Measured, never pressed.', sel: 'button[aria-label="Login with GitLab"]' });
  await S('google-button', q('button').filter({ hasText: /Sign in with Google/i }), B4, { group: g, title: 'Google button', desc: 'Measured, never pressed.', sel: 'button:has-text("Sign in with Google")' });
  await S('passkey-button', q('button').filter({ hasText: /passkey/i }), B4, { group: g, title: 'Passkey button', desc: 'Measured, never pressed.', sel: 'button:has-text("passkey")' });
  const email = q('input[type="email"], input[placeholder*="email" i], input').first();
  await S('email-input', email, ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'Text was typed and deleted; the form was never submitted.', sel: 'input[placeholder="Your email"]' });
  await S('password-input', q('input[type="password"]'), ['default', 'focused'], { group: g, title: 'Password field', desc: 'Focused only; nothing was typed.', sel: 'input[type="password"]' });
  await S('show-password', q('button[aria-label*="password" i], button[aria-label*="Show" i]'), B4, { group: g, title: 'Show-password toggle', desc: 'The eye inside the password field.', sel: 'button[aria-label*="password" i]' });
  await S('forgot-link', q('a').filter({ hasText: /Forgot your password/i }), B4, { group: g, title: 'Forgot-password link', sel: 'a:has-text("Forgot")' });
  await S('login-button', q('button').filter({ hasText: /^Login$/ }), B4, { group: g, title: 'Login button', desc: 'The submit button; measured in every state except a real press — the form was never submitted.', sel: 'button:has-text("Login")' });
  await S('tos-link', q('a').filter({ hasText: /Terms of Service/i }), B4, { group: g, title: 'Legal link', sel: 'a:has-text("Terms of Service")' });
  save();
}

async function footer() {
  // The footer lives on the home page, but a full run ends on /sign-in — an
  // earlier partial run leaves whatever page ran last open. Open home first so
  // the readings are the home footer the page/run/url claim they are.
  if (!page || page.isClosed()) {
    if (!(await newPage('home'))) return;
  } else {
    current = 'home';
    await open(page, BASE + URLS.home, {});
    if (await blocked()) { log('  BLOCKED footer'); blockedPages.add('home'); return; }
  }
  const g = G.footer;
  const fl = q('footer a').filter({ hasText: /\w{3,}/ }).first();
  if (await fl.count()) {
    await S('footer', q('footer'), ['default'], { group: g, title: 'Footer', sel: 'footer' });
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
    await S('footer-social', q('footer a[aria-label], footer a[href*="github" i], footer a[href*="discord" i]').first(), B4, { group: g, title: 'Footer social icon', sel: 'footer a[aria-label]' });
  }
  save();
}

async function mobile() {
  current = 'home';
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header').first(), ['default'], { group: g, title: 'Mobile top bar', sel: 'header' }, { noScroll: true });
  const menuBtn = q('header button[aria-label*="menu" i], header button[aria-expanded], header button:has(svg)').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: 'header button' }, { noScroll: true });
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The button after its own toggle; the open sheet (the data-state=open panel holding the nav links) shows in the crop.', sel: 'header button' }, { noScroll: true, cropLoc: q('div[data-state="open"]:has(a[href])') });
  // The menu sheet m-menu-open left open holds the destination rows.
  const mLink = q('a').filter({ hasText: /^Pricing$/ }).last();
  await S('m-nav-link', mLink, ['default'], { group: g, title: 'Mobile nav link', desc: 'A destination row inside the opened menu sheet.', sel: 'open menu a:has-text("Pricing")' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-cta-primary', q('a,button').filter({ hasText: /^Start project$/ }), B4, { group: g, title: 'Mobile primary CTA', sel: 'a:has-text("Start project")' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), dark theme pinned';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, docs, blog, signin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
// A page counts as finished only when its runner returns without throwing and
// no bot check stopped it. Pruning touches only finished pages: a page that
// threw keeps its unreached components and states instead of losing them.
// A page that throws is recorded as broken and the run goes on; the exit
// status at the end is nonzero when any page threw (run-pages.mjs).
const { finished, broken, runPage } = pageRunner(() => current, log);
const pageDone = (c) => finished.has(c.page) && !broken.has(c.page) && !blockedPages.has(c.page);
try {
  for (const k of order) { if (k !== 'mobile') await runPage(plan[k]); }
  if (!pages.length || pages.includes('home')) await runPage(footer);
  if (!pages.length || pages.includes('mobile')) await runPage(plan.mobile);
} finally {
  // Components whose specs now list a state a run did not touch keep their old
  // evidence; a state that was listed but never written is removed.
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key)) { if (!pages.length && pageDone(c)) delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want && pageDone(c)) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log(broken.size ? 'incomplete ->' : 'done ->', OUT);
process.exitCode = exitStatus(broken);
