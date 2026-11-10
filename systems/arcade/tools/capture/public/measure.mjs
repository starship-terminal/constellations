// Measures arcade.software's public components in every state reachable without
// signing in, downloading, purchasing or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing demo contact mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// arcade.software is a Webflow build in one light theme; classes are semantic
// (.btn, .nav-btn, .heading-1, .avfaq-trigger, .new-footer-*) so selectors key
// off them, roles or stable text. Nothing is sent, typed into a submit flow or
// followed: the only presses are local UI toggles — a pricing FAQ accordion
// and the mobile menu. "Sign up", "Log in", "Talk to sales" and the plan
// buttons are measured in all states except followed or pressed for real; the
// prompt's send and every form's submit are never pressed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', demo: '/product/interactive-demo', contact: '/contact-sales' };
let page, cdp, current, context, run;
const touched = new Set();
const listed = new Map();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
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
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await closePromo(page);
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

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] }, meta);
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
        if (opts.noToggle) via = 'flyout held open by opts.open';
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
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

// Clicks a UI toggle (accordion, mobile menu). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|start|get started|claim|share|export|select|choose|talk to sales|contact us|play|open arcade|launch video|explore|install|connect|try|view demo plans)$/i;
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

const G = {
  shell: 'Shell and navigation', hero: 'Home', pricing: 'Pricing',
  demo: 'Interactive demo page', contact: 'Contact sales', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home', { wait: 9000 }))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('header', q('.navbar.w-nav').first(), ['default'], { group: g, title: 'Header', desc: 'The fixed top bar: logo, Product/Pricing/Blog/Enterprise links, Log in and Sign up.', sel: '.navbar.w-nav' }, { noScroll: true });
  await S('logo', q('.logo-nav').first(), ['default'], { group: g, title: 'Logo', sel: '.logo-nav' }, { noScroll: true });
  await S('nav-link', q('.navbar .nav-btn').filter({ hasText: /^Pricing$/ }), B4, { group: g, title: 'Nav link', sel: '.nav-btn' }, { noScroll: true });
  await S('nav-login', q('.navbar a.btn.transparent-blend').first(), B4, { group: g, title: 'Log in button', desc: 'The ghost nav action. Measured, never followed.', sel: 'a.btn.transparent-blend' }, { noScroll: true });
  await S('nav-signup', q('.navbar a.btn').filter({ hasText: /^Sign up$/ }).first(), B4, { group: g, title: 'Sign up button', desc: 'The black pill nav action. Measured, never followed.', sel: '.navbar a.btn:has-text("Sign up")' }, { noScroll: true });

  const h = G.hero;
  await S('hero-title', q('h1.heading-1').first(), ['default'], { group: h, title: 'Hero title', desc: 'One of the animated .heading-1 lines.', sel: 'h1.heading-1' }, { noScroll: true });
  await S('hero-subtitle', q('p, div').filter({ hasText: /^Studio quality\. Editor-level control/ }).last(), ['default'], { group: h, title: 'Hero subtitle', sel: 'hero subline' }, { noScroll: true });
  await S('prompt-box', q('.arcade-prompt').first(), ['default'], { group: h, title: 'Prompt box', desc: 'The "describe your video" composer on the hero: textarea, plus and send.', sel: '.arcade-prompt' });
  await S('prompt-field', q('.arcade-prompt textarea').first(), ['default', 'focused'], { group: h, title: 'Prompt field', desc: 'Focused only; nothing was sent.', sel: '.arcade-prompt textarea' });
  await S('prompt-send', q('.arcade-prompt-send').first(), B4, { group: h, title: 'Prompt send', desc: 'The composer submit. Measured, never pressed.', sel: '.arcade-prompt-send' });
  await S('prompt-plus', q('.arcade-prompt-plus').first(), B4, { group: h, title: 'Prompt plus link', desc: '"Open Arcade" beside the composer. Measured, never followed.', sel: '.arcade-prompt-plus' });
  await S('suggestion-chip', q('.arcade-prompt-suggestions button').filter({ visible: true }).first(), B4, { group: h, title: 'Suggestion chip', desc: 'A prompt preset pill under the composer. Tapped in screenshots only; never submitted.', sel: '.arcade-prompt-suggestions button' });
  await S('scatter-card', q('.scatter-card-trigger').filter({ visible: true }).first(), B4, { group: h, title: 'Scatter card', desc: 'A "Play <title>" video card in the Made-to-be-seen wall. Measured, never followed.', sel: '.scatter-card-trigger' });
  await S('spotlight-quote', q('.spotlight-quote').first(), ['default'], { group: h, title: 'Spotlight quote', sel: '.spotlight-quote' });
  await S('spotlight-next', q('.spotlight-next').first(), B4, { group: h, title: 'Spotlight next', desc: 'The quote carousel arrow. Pressed once for the screenshot state.', sel: '.spotlight-next' });
  await S('cta-large', q('a.btn.large').filter({ hasText: /^Get started$/ }).first(), B4, { group: h, title: 'Large CTA', desc: 'The black Get started pill mid-page. Measured, never followed.', sel: 'a.btn.large' });
  await S('cta-secondary', q('a.btn.large.secondary').filter({ hasText: /Talk to sales/ }).first(), B4, { group: h, title: 'Secondary CTA', desc: 'The outlined Talk to sales. Measured, never followed.', sel: 'a.btn.large.secondary' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1').first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1' }, { noScroll: true });
  const card = q('.new-pricing-plan').nth(1);
  await S('plan-card-pro', card, ['default'], { group: g, title: 'Pro plan card', sel: '.new-pricing-plan (Pro)' });
  await S('plan-cta-pro', q('a.btn.new-pricing-btn').filter({ hasText: /Choose Pro/ }).first(), B4, { group: g, title: 'Choose Pro button', desc: 'The primary plan CTA. Measured, never followed.', sel: 'a.btn.new-pricing-btn' });
  await S('plan-cta-neutral', q('a.btn.neutral.new-pricing-btn').filter({ hasText: /Choose Free/ }).first(), B4, { group: g, title: 'Choose Free button', desc: 'The neutral plan CTA. Measured, never followed.', sel: 'a.btn.neutral.new-pricing-btn' });
  await S('plan-price', q('.new-pricing-plan').nth(1).locator('.new-pricing-plan-price').first(), ['default'], { group: g, title: 'Plan price', sel: '.new-pricing-plan-price' });
  const model = q('input[type="radio"][name="avc-model"]').first();
  if (await model.count()) {
    const lab = model.locator('xpath=ancestor::label[1]');
    await S('model-radio', (await lab.count()) ? lab : model, ['default'], { group: g, title: 'Credit calculator radio', desc: 'A model option on the video cost calculator; the input is visually hidden, the label paints it.', sel: 'input[name=avc-model] label' });
  }
  const faq = q('.avfaq-trigger').filter({ visible: true }).first();
  await S('faq-question', faq, B4, { group: g, title: 'FAQ accordion button', sel: '.avfaq-trigger' });
  await S('faq-open', faq, ['opened'], { group: g, title: 'FAQ accordion, open', desc: 'The same item after its own toggle.', sel: '.avfaq-trigger' });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  const ask = q('.ask-ai-btn').filter({ visible: true }).first();
  if (await ask.count()) await S('ask-ai', ask, B4, { group: g, title: 'Ask AI button', desc: 'The icon pill that opens an AI answer for a FAQ. Measured, never pressed.', sel: '.ask-ai-btn' });
  save();
}

async function demo() {
  if (!(await newPage('demo', { wait: 9000 }))) return;
  const g = G.demo;
  await S('demo-title', q('h1, h2').first(), ['default'], { group: g, title: 'Demo title', sel: 'h1' }, { noScroll: true });
  await S('demo-signup', q('a.signup-btn, .button.is-nav-button.signup-btn').first(), B4, { group: g, title: 'Sign up for free', desc: 'The page\'s nav CTA. Measured, never followed.', sel: '.signup-btn' }, { noScroll: true });
  await S('demo-tts', q('a.tts-btn, .button.is-nav-button.tts-btn').first(), B4, { group: g, title: 'Talk to sales', desc: 'The page\'s secondary nav CTA. Measured, never followed.', sel: '.tts-btn' }, { noScroll: true });
  const url = q('.url-to-demo-input').first();
  await S('url-field', url, ['default', 'focused'], { group: g, title: 'URL-to-demo field', desc: 'Focused only; nothing was typed or submitted.', sel: '.url-to-demo-input' });
  await S('url-button', q('.url-to-demo-button').first(), B4, { group: g, title: 'URL-to-demo button', desc: 'The field\'s arrow submit. Measured, never pressed.', sel: '.url-to-demo-button' });
  const card = q('.card-text_wrapper').filter({ visible: true }).first();
  await S('demo-card', card, ['default'], { group: g, title: 'Feature card', sel: '.card-text_wrapper' });
  const nl = q('.text-field.w-input').first();
  if (await nl.count()) await S('newsletter-field', nl, ['default', 'focused'], { group: g, title: 'Newsletter field', desc: 'Focused only; nothing was typed or submitted.', sel: '.text-field.w-input' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  const g = G.contact;
  await S('contact-title', q('h1, h2').first(), ['default'], { group: g, title: 'Contact title', sel: 'h1' }, { noScroll: true });
  await S('form-card', q('.contact-sales-form-card').first(), ['default'], { group: g, title: 'Form card', sel: '.contact-sales-form-card' });
  const first = q('input[name="first_name"]').first();
  await S('field-text', first, ['default', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'One .ds-input (First name). A sample value was typed, measured, then deleted; the form was never submitted.', sel: 'input.ds-input' }, { fillText: 'Jane' });
  const sel = q('select.ds-input').first();
  await S('field-select', sel, ['default', 'focused'], { group: g, title: 'Select', desc: 'Company-size select; focused only, never changed.', sel: 'select.ds-input' });
  const ta = q('textarea.ds-input').first();
  await S('field-textarea', ta, ['default', 'focused'], { group: g, title: 'Textarea', desc: 'Focused only; nothing was typed.', sel: 'textarea.ds-input' });
  await S('form-submit', q('.ds-submit').first(), B4, { group: g, title: 'Submit button', desc: 'The Talk to sales submit. Measured, never pressed.', sel: '.ds-submit' });
  save();
}

async function footer() {
  // The footer is measured on the home page, so home must be the document that
  // is actually open — assigning `current` alone would keep the contact page
  // and mislabel a contact-footer reading as home's.
  if (!(await newPage('home', { wait: 9000 }))) return;
  const g = G.footer;
  const fl = q('.new-footer-link').filter({ hasText: /\w{3,}/ }).first();
  if (await fl.count()) {
    const foot = q('.new-footer-brand').first();
    await S('footer', foot, ['default'], { group: g, title: 'Footer', sel: 'footer band' });
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: '.new-footer-link' });
    await S('footer-social', q('.new-social-link').first(), B4, { group: g, title: 'Footer social icon', sel: '.new-social-link' });
    await S('footer-legal', q('.new-footer-link').filter({ hasText: /Privacy/ }).first(), B4, { group: g, title: 'Legal link', sel: '.new-footer-link:has-text("Privacy")' });
  }
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, wait: 9000 }))) return;
  const g = G.mobile;
  await S('m-header', q('.navbar.w-nav').first(), ['default'], { group: g, title: 'Mobile header', sel: '.navbar.w-nav' }, { noScroll: true });
  const menuBtn = q('.w-nav-button, .menu-button, button[aria-label*="menu" i]').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: '.w-nav-button' }, { noScroll: true });
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The button after its own toggle; the open panel shows in the crop.', sel: '.w-nav-button' });
  // The nav links and Sign up live inside the open menu panel: measure them
  // before dismissing it.
  const mLink = q('a.nav-btn').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first();
  await S('m-nav-link', mLink, ['default'], { group: g, title: 'Mobile nav link', desc: 'Read inside the open menu.', sel: 'a.nav-btn' }, { noScroll: true });
  await S('m-signup', q('a.btn').filter({ hasText: /^Sign up$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile Sign up', desc: 'Read inside the open menu.', sel: 'a.btn' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-prompt', q('.arcade-prompt').first(), ['default'], { group: g, title: 'Mobile prompt box', sel: '.arcade-prompt' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, demo, contact, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length) { delete out.components[key]; continue; }
    if (!Object.keys(c.states || {}).length && !c.missing) delete out.components[key];
  }
  save();
  await context.close().catch(() => {});
  await browser.close().catch(() => {});
}
