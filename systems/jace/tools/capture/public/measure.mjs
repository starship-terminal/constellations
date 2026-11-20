// Measures jace.ai public components without signing in, paying or submitting.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing blog docs contact signin signup mobile.
// The sales form, app.jace.ai/signin and /signup are boundaries: fields may
// be focused, sample text is typed then deleted, and nothing is submitted.
// Signup Continue is measured at rest and never clicked: it opens a privacy notice whose
// Continue to signup acknowledges it (a consent choice), so the privacy and OAuth cards are a boundary.
// Google, Outlook and SSO buttons are measured, never pressed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, launch, patch, open, closePromo, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: BASE + '/',
  pricing: BASE + '/pricing',
  blog: BASE + '/blog',
  docs: BASE + '/docs/guides-getting-started',
  contact: BASE + '/contact/sales',
  signin: APP + '/signin',
  signup: APP + '/signup',
};
let page, cdp, current, view, context, run;
const touched = new Set();
const listed = new Map();
const opened = new Set();

async function newPage(key, { mobile = false, wait = 2000 } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
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
  if (!(await open(page, URLS[key], { wait }))) { log('  BLOCKED', key); await ctx.close().catch(() => {}); return false; }
  opened.add(key + '|' + view);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await closePromo(page);
  return true;
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(180);
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
  await page.waitForTimeout(250);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(280);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, view, run, url: URLS[current] }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    const prev = c.states[state];
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, loc, `${key}-${state}`, opts.pad ?? 8); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file ?? (prev && prev.crop), via: opts.via, run };
    log('  ', key, state, s.rect.w + 'x' + s.rect.h, s.cropError || '');
  } catch (e) {
    const prev = c.states[state];
    c.states[state] = prev && !prev.error
      ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
      : { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    log('  ! missing', key);
    out.components[key].missing = true;
    return;
  }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (st === 'hover') {
        await loc.hover({ timeout: 4000 }).catch(() => loc.hover({ force: true }));
        await page.waitForTimeout(350);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(loc);
      } else if (st === 'pressed') {
        undo = await forcePseudo(loc, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.focus()));
        await page.waitForTimeout(250);
        via = 'clicked into the field; nothing submitted';
      } else if (st === 'filled') {
        await loc.click({ timeout: 4000 });
        await page.keyboard.type('name@example.com', { delay: 8 });
        await page.waitForTimeout(200);
        undo = async () => {
          await loc.focus();
          await page.keyboard.press('Meta+a');
          await page.keyboard.press('Backspace');
        };
        via = 'typed a sample address, then deleted; nothing submitted';
      } else if (st === 'error') {
        via = opts.via || 'validation state shown by the page';
      } else via = 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 140));
    }
    if (undo) await undo().catch(() => {});
  }
  await reset();
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

const G = {
  shell: 'Shell and navigation',
  home: 'Home',
  pricing: 'Pricing',
  blog: 'Blog',
  docs: 'Docs',
  contact: 'Sales contact (boundary)',
  signin: 'App sign-in (boundary)',
  signup: 'App signup (boundary)',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  const g = G.shell;
  await S('header', q('header').first(), ['default'], { group: g, title: 'Header', desc: 'The sticky marketing header: wordmark, Log In and Get started.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a[href="/"]').first(), ['default', 'hover'], { group: g, title: 'Wordmark', desc: 'The Jace AI home link in the header.', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('nav-login', q('header a').filter({ hasText: /^Log In$/ }).first(), B4, { group: g, title: 'Log In', desc: 'The white pill linking to app.jace.ai/signin. Measured, never followed.', sel: 'header a Log In' }, { noScroll: true });
  await S('nav-cta', q('header a, header button').filter({ hasText: /^Get started$/ }).first(), B4, { group: g, title: 'Header CTA', desc: 'The dark pill linking to signup. Measured, never followed.', sel: 'header Get started' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('h1').first(), ['default'], { group: h, title: 'Hero title', desc: 'The Gelica display headline, 88px light.', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('button').filter({ hasText: /Get started for free/i }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The hero "Get started for free" control. Links toward signup; never followed.', sel: 'button Get started for free' });
  await S('chip', q('button').filter({ hasText: /^Draft e-mails$/ }).first(), B4, { group: h, title: 'Demo chip', desc: 'A white pill that switches the public inbox demo. A local toggle, not a submit.', sel: 'button Draft e-mails' });
  await S('integration-pill', q('a').filter({ hasText: /^Gmail$/ }).first(), B4, { group: h, title: 'Integration pill', desc: 'The Gmail works-with pill. Links to /integrations/gmail.', sel: 'a Gmail' });
  await S('feature-card', q('article, a').filter({ hasText: /Jace for Gmail/ }).first(), ['default', 'hover'], { group: h, title: 'Feature card', desc: 'A product card linking to a public integration page.', sel: 'card Jace for Gmail' });
  await S('section-title', q('h2').first(), ['default'], { group: h, title: 'Section title', desc: 'The first section heading under the hero.', sel: 'h2' });
  await S('page-ground', q('body'), ['default'], { group: h, title: 'Page ground', desc: 'The body fill and type the marketing page paints.', sel: 'body' }, { noScroll: true, crop: false });
  // FAQ-like accordion is not on home; testimonial pager is.
  await S('pager', q('button[aria-label="Next testimonial"]').first(), B4, { group: h, title: 'Pager button', desc: 'The next-testimonial control. A local carousel toggle.', sel: 'button Next testimonial' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1').first(), ['default'], { group: g, title: 'Pricing title', desc: 'The pricing headline in Gelica.', sel: 'h1' }, { noScroll: true });
  await S('billing-yearly', q('button').filter({ hasText: /Bill yearly/ }).first(), B4, { group: g, title: 'Yearly toggle', desc: 'The selected yearly billing control. A local toggle; the monthly sibling is measured separately.', sel: 'button Bill yearly' });
  await S('billing-monthly', q('button').filter({ hasText: /^Bill monthly$/ }).first(), ['default', 'hover', 'pressed'], { group: g, title: 'Monthly toggle', desc: 'The unselected monthly billing control, measured at rest (not switched, so the yearly table stays).', sel: 'button Bill monthly' });
  await S('price-card', q('div').filter({ hasText: /^Plus Plan/ }).first(), ['default'], { group: g, title: 'Plus plan card', desc: 'The Plus plan card on the white pricing surface.', sel: 'div Plus Plan' });
  await S('price-cta', q('button, a').filter({ hasText: /Try Pro/ }).first(), B4, { group: g, title: 'Plan CTA', desc: 'The Pro plan trial button. Links toward signup; never followed.', sel: 'Try Pro' });
  await S('price-secondary', q('a').filter({ hasText: /^Get in touch$/ }).first(), B4, { group: g, title: 'Secondary CTA', desc: 'The white "Get in touch" link to the sales form. Never followed from this measurement.', sel: 'a Get in touch' });
  await S('faq', q('button').filter({ hasText: /How much does Jace AI cost/ }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'FAQ row', desc: 'A closed FAQ accordion trigger.', sel: 'button How much does Jace AI cost' });
  // Open the accordion locally. It does not submit.
  const faq = q('button').filter({ hasText: /How much does Jace AI cost/ }).first();
  if (await faq.count()) {
    await faq.click().catch(() => {});
    await page.waitForTimeout(400);
    await S('faq-open', faq, ['default'], { group: g, title: 'FAQ row, open', desc: 'The same FAQ trigger after its own press, with the answer open.', sel: 'FAQ open' });
  }
  await S('link', q('a').filter({ hasText: /^lawyers$/ }).first(), ['default', 'hover'], { group: g, title: 'Inline link', desc: 'An underlined body link.', sel: 'a lawyers' });
  save();
}

async function blog() {
  if (!(await newPage('blog'))) return;
  const g = G.blog;
  await S('blog-title', q('h1').first(), ['default'], { group: g, title: 'Blog title', desc: 'The blog index headline.', sel: 'h1' }, { noScroll: true });
  await S('blog-nav', q('header a, nav a').filter({ hasText: /^Learn$/ }).first(), B4, { group: g, title: 'Docs nav link', desc: 'A text nav link on the blog header (Learn).', sel: 'a Learn' }, { noScroll: true });
  await S('blog-card', q('a').filter({ hasText: /What happens to your email/ }).first(), ['default', 'hover'], { group: g, title: 'Blog card', desc: 'A published post card. Public marketing content.', sel: 'first blog card' });
  save();
}

async function docs() {
  if (!(await newPage('docs'))) return;
  const g = G.docs;
  await S('docs-title', q('h1').first(), ['default'], { group: g, title: 'Docs title', desc: 'The getting-started headline.', sel: 'h1' });
  await S('docs-nav', q('a').filter({ hasText: /Billing & Plans/ }).first(), ['default', 'hover'], { group: g, title: 'Docs sidebar link', desc: 'A link in the public docs navigation.', sel: 'a Billing & Plans' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  const g = G.contact;
  await S('form-title', q('h1').first(), ['default'], { group: g, title: 'Form title', desc: 'The sales contact heading. The form is a boundary: nothing is submitted.', sel: 'h1' }, { noScroll: true });
  await S('text-field', q('input').first(), ['default', 'hover', 'focus-visible', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'The first sales-form field. Sample text is typed and deleted. Nothing is submitted.', sel: 'input first' });
  await S('text-area', q('textarea').first(), ['default', 'focused'], { group: g, title: 'Text area', desc: 'The message textarea, focused only. Nothing typed that would be sent.', sel: 'textarea' });
  await S('form-submit', q('button').filter({ hasText: /Send a request/ }).first(), ['default', 'hover', 'focus-visible', 'pressed'], { group: g, title: 'Submit button', desc: 'The send button, measured with a forced pressed state. Never clicked, so the form is not submitted.', sel: 'button Send a request' });
  // Empty submit is a click that would POST. Do not click. Record the gap
  // by reading the field's invalid style if the browser paints :invalid on an empty required field.
  const invalid = await page.evaluate(() => {
    const el = document.querySelector('input:invalid, input[required]');
    if (!el) return null;
    el.setAttribute('data-m-invalid', '1');
    return true;
  });
  if (invalid) {
    await S('text-field-invalid', q('[data-m-invalid="1"]'), ['default'], { group: g, title: 'Required field', desc: 'A required field at rest (empty). The form was not submitted, so this is the resting required style, not a posted error.', sel: 'input required' });
  }
  save();
}

async function signin() {
  if (!(await newPage('signin'))) return;
  const g = G.signin;
  await S('signin-title', q('h1').first(), ['default'], { group: g, title: 'Sign-in title', desc: 'The app sign-in headline. Boundary: no OAuth, no SSO, nothing typed.', sel: 'h1' }, { noScroll: true });
  await S('signin-oauth', q('button').filter({ hasText: /Continue with Google/ }).first(), B4, { group: g, title: 'Google button', desc: 'Continue with Google. Measured, never pressed.', sel: 'button Continue with Google' }, { noScroll: true });
  await S('signin-outlook', q('button').filter({ hasText: /Continue with Outlook/ }).first(), ['default', 'hover'], { group: g, title: 'Outlook button', desc: 'Continue with Outlook. Measured, never pressed.', sel: 'button Continue with Outlook' }, { noScroll: true });
  await S('signin-sso', q('a').filter({ hasText: /SSO portal/ }).first(), ['default', 'hover'], { group: g, title: 'SSO link', desc: 'The enterprise SSO link. Never followed.', sel: 'a Launch the SSO portal' }, { noScroll: true });
  await S('signin-signup', q('a').filter({ hasText: /^Sign up$/ }).first(), B4, { group: g, title: 'Sign up link', desc: 'The sign-up link on the sign-in card. Never followed.', sel: 'a Sign up' }, { noScroll: true });
  await S('signin-quote', q('div').filter({ hasText: /true AI assistant/ }).first(), ['default'], { group: g, title: 'Quote card', desc: 'The published testimonial card beside the sign-in form.', sel: 'quote card' }, { noScroll: true });
  save();
}

async function signup() {
  if (!(await newPage('signup'))) return;
  const g = G.signup;
  await S('signup-title', q('h1').first(), ['default'], { group: g, title: 'Signup title', desc: 'The first signup headline (Join +10,000). Boundary: no OAuth.', sel: 'h1' }, { noScroll: true });
  await S('signup-continue', q('button').filter({ hasText: /^Continue$/ }).first(), B4, { group: g, title: 'Signup Continue', desc: 'The landing Continue control; measured, never clicked (it opens a privacy notice).', sel: 'button Continue' }, { noScroll: true });
  // Consent boundary: Continue opens a privacy notice whose "Continue to signup" acknowledges it.
  // Neither is clicked, so the privacy and OAuth cards are not measured.
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header').first(), ['default'], { group: g, title: 'Mobile header', desc: 'The header at 390.', sel: 'header' }, { noScroll: true });
  await S('m-menu', q('button').filter({ hasText: /Open main menu/ }).first(), ['default', 'hover', 'pressed'], { group: g, title: 'Menu button', desc: 'The mobile menu button.', sel: 'button Open main menu' }, { noScroll: true });
  const btn = q('button').filter({ hasText: /Open main menu/ }).first();
  if (await btn.count()) {
    await btn.click().catch(() => {});
    await page.waitForTimeout(600);
    await S('m-menu-open', q('nav, [role="dialog"], header').filter({ hasText: /Pricing/ }).first(), ['default'], { group: g, title: 'Menu open', desc: 'The header after the menu button press.', sel: 'open menu' }, { noScroll: true });
    await S('m-menu-link', q('a').filter({ hasText: /^Pricing$/ }).first(), ['default', 'hover'], { group: g, title: 'Menu link', desc: 'A link in the open mobile menu.', sel: 'a Pricing' }, { noScroll: true });
  }
  await S('m-hero', q('h1').first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The hero headline at 390.', sel: 'h1' });
  save();
}

run = '2026-11-18';
out._meta.read = run;
out._meta.viewport = '1440 x 900 desktop, 390 x 844 mobile; marketing is light; app.jace.ai/signin and /signup are the dark product boundary';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, blog, docs, contact, signin, signup, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) await plan[k]();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length) {
      const cview = c.view || (key.startsWith('m-') ? 'mobile' : 'desktop');
      if (opened.has((c.page || '') + '|' + cview)) delete out.components[key];
    }
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
