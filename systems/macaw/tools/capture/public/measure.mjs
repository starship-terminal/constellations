// Measures Macaw's public marketing components, signed out.
// Nothing is submitted, signed into, purchased or consented.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: promo home academy create unit science math history atlas story news mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be re-run)
// and one crop per component and state into components/crops/. raw/measurements.md
// is then built from the JSON by build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or submit button can fire
//   focused        the field clicked into (a text field only)
//   filled         sample text typed into a field, measured, then deleted; Enter is never pressed
//   anything else  a resting state reached by the page itself or by a UI toggle (a tab,
//                  a menu, "Show more", the lesson's own Pause and Settings); nothing that
//                  sends a question, creates a course, signs in or uploads is ever pressed
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, open, closePromo, openStory, styleOf, crop, centre, RAW } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
if (out._meta.storyUrl) out._meta.storyUrl = safeUrl(out._meta.storyUrl);   // an earlier run's, if story is not rerun
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  pricing: '/pricing',
  contact: '/contact-us',
  tool: '/free-tools/blog-title-generator',
  terms: '/terms-and-conditions',
  privacy: '/privacy-policy',
};

let page, cdp, current, context, run;
const touched = new Set();
const listed = new Map(); // component -> the states this run's specs list for it

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 6000 } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, BASE + URLS[key], { wait, promo });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
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

// Clicks a UI toggle (tab, menu, show more). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log in|login|create|generate|upload|send message|get started|start for free|start free|contact our sales team)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = opts.byBox ? (await withBox(target)) : target.filter({ visible: true }).first();
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

const FILL = 'Sample';

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); await opts.open(); }
  const loc = opts.byBox ? await withBox(target) : target.filter({ visible: true }).first();
  if (!(await loc.count())) { log('  ! missing', key); markMissing(key); return; }
  if (opts.byBox) {
    const box = await loc.boundingBox();
    if (!box || box.width < 2 || box.height < 2) { log('  ! missing', key, 'no box'); markMissing(key); return; }
  }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (opts.before?.[st]) via = await opts.before[st](loc);
      if (st === 'hover') {
        const h = (opts.hoverLoc || loc).first();
        await h.hover({ timeout: 5000 }).catch(() => h.hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).first(), ['active', 'hover']);
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

function markMissing(key) {
  out.components[key].missing = true;
  out.components[key].states = {};
}

// Playwright treats Webflow w-nav-link nodes as hidden even when the box is on screen.
async function withBox(loc) {
  const n = await loc.count();
  for (let i = 0; i < n; i++) {
    const item = loc.nth(i);
    const box = await item.boundingBox();
    if (box && box.width > 2 && box.height > 2) return item;
  }
  return loc.first();
}
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

// ---------- Macaw public surfaces ----------
const G = {
  shell: 'Shell and navigation',
  home: 'Home',
  pricing: 'Pricing',
  contact: 'Contact form',
  tool: 'Free tool',
  legal: 'Legal',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  await newPage('home', { wait: 2000 });
  await sheetsFor('home');
  const g = G.shell;
  await S('navbar', q('.navbar_component'), ['default'], { group: g, title: 'Top bar', desc: '80px Webflow nav on the cream page. Frosted fill rgba(255,253,249,0.3), 32px inline padding. Holds Product, Writing examples, Resources, Pricing, affiliate, Log in and Start for free.', sel: '.navbar_component' }, { noScroll: true });
  await S('nav-link', q('.navbar_link, .w-nav-link').filter({ hasText: /^Pricing$/ }), B4, { group: g, title: 'Nav link', desc: '16/600 Inter, ink rgb(29,41,57). A link, so hover and keyboard focus are real. Pressed is forced :active and the link is not followed.', sel: '.navbar_link' }, { noScroll: true });
  await S('button-primary', q('a.button').filter({ hasText: 'Start for free' }).first(), B4, { group: g, title: 'Primary button', desc: 'Coral fill rgb(246,102,88), white 14.8/600 label, 8px radius, 46px tall, 10px 18px padding, a 1px soft shadow. The href is the sign-up wall and was not followed.', sel: 'a.button' }, { noScroll: true });
  // Webflow marks the desktop Log in link w-nav-link, which Playwright treats as hidden.
  // The box is on screen (about 81x46). Match by box, and never follow the href.
  await S('button-secondary', q('a.button-secondary-gray'), B4, { group: g, title: 'Secondary button', desc: 'White fill, ink rgb(52,64,84), 8px radius, 46px tall. The href is the sign-in wall and was not followed. Playwright calls the link hidden; the box is on screen.', sel: 'a.button-secondary-gray' }, { noScroll: true, byBox: true });
  await S('button-google', q('a').filter({ hasText: 'Start free with Google' }).first(), ['default', 'hover'], { group: g, title: 'Google sign-in link', desc: 'Same quiet white button as Log in. The href starts a Google strategy on the app host and was not followed.', sel: 'a[href*="strategy=google"]' });
  await S('display', q('h1').first(), ['default'], { group: G.home, title: 'Display heading', desc: 'Home h1, Inter 53.6/700, ink rgb(16,24,40).', sel: 'h1' }, { noScroll: true });
  await S('body-copy', q('body'), ['default'], { group: G.home, title: 'Page', desc: 'Cream page rgb(255,253,249), body ink rgb(71,84,103), Inter 16/400.', sel: 'body' }, { noScroll: true, crop: false });
  await S('resources-toggle', q('.navbar_dropdown-toggle').first(), ['default', 'hover'], { group: g, title: 'Resources menu toggle', desc: 'Webflow dropdown toggle. Hover opens the menu. The menu items point at # and were not followed.', sel: '.navbar_dropdown-toggle' }, { noScroll: true });
  // The desktop toggle is display:none, so hover never opens this. The page shot was a forced open.
  await S('resources-menu', q('.navbar_menu-dropdown'), [], { group: g, title: 'Resources menu', desc: 'Blog and Documentation rows. Both hrefs are #. The desktop toggle is display:none, so this menu was not opened by hover. The page shot is a forced open.', sel: '.navbar_menu-dropdown' }, { noScroll: true });
  await S('footer-link', q('footer a, .footer_component a, .footer a').filter({ hasText: 'Terms' }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Footer link', desc: 'Footer legal link, ink rgb(51,51,51).', sel: 'footer a' });
  await page.close();
}

async function pricing() {
  await newPage('pricing', { wait: 2000 });
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('pricing-heading', q('h1').first(), ['default'], { group: g, title: 'Pricing heading', desc: 'Inter 53.6/700, ink rgb(29,41,57).', sel: 'h1' }, { noScroll: true });
  await S('plan-starter', q('.pricing07_top-row-content.purple').first(), ['default'], { group: g, title: 'Starter plan card', desc: 'Lavender fill rgb(246,226,255), 12px radius, 40px 0 16px padding. Yearly price at rest.', sel: '.pricing07_top-row-content.purple' });
  await S('plan-pro', q('.pricing07_top-row-content.orange').first(), ['default'], { group: g, title: 'Pro plan card', desc: 'Peach fill rgb(255,232,226), 12px radius.', sel: '.pricing07_top-row-content.orange' });
  await S('plan-scale', q('.pricing07_top-row-content.blue').first(), ['default'], { group: g, title: 'Scale plan card', desc: 'Blue fill rgb(227,238,255), 12px radius.', sel: '.pricing07_top-row-content.blue' });
  await S('billing-yearly', q('.pricing-toggle-button').filter({ hasText: 'Yearly' }).first(), ['default', 'hover'], { group: g, title: 'Yearly billing toggle', desc: 'Selected at rest. A div, so it takes no keyboard focus. Not switched during this reading.', sel: '.pricing-toggle-button' });
  await S('billing-monthly', q('.pricing-toggle-button').filter({ hasText: 'Monthly' }).first(), ['default', 'selected'], { group: g, title: 'Monthly billing toggle', desc: 'Clicked to reveal the monthly price state, then left. No checkout was opened.', sel: '.pricing-toggle-button' }, { before: { selected: async () => { await q('.pricing-toggle-button').filter({ hasText: 'Monthly' }).first().click(); await page.waitForTimeout(400); return 'clicked the Monthly label; no checkout'; } } });
  await S('plan-cta', q('a').filter({ hasText: /^Get started$/ }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Plan call to action', desc: 'Get started links to sign-up. Not followed.', sel: 'a' });
  await S('faq-question', q('.faq01_question').first(), ['default', 'hover', 'expanded'], { group: g, title: 'FAQ question', desc: 'First pricing FAQ row. Expanded by a click that only opens the answer.', sel: '.faq01_question' }, { before: { expanded: async (loc) => { await loc.click(); await page.waitForTimeout(400); return 'clicked the question'; } } });
  await S('faq-answer', q('.faq01_answer').first(), ['default'], { group: g, title: 'FAQ answer', desc: 'The answer under the first question, visible after the row is open or already painted.', sel: '.faq01_answer' });
  await S('sales-link', q('a').filter({ hasText: /Contact our sales team/ }).first(), ['default'], { group: g, title: 'Sales link', desc: 'Custom-plan link. Not followed.', sel: 'a' });
  await page.close();
}

async function contact() {
  await newPage('contact', { wait: 2000 });
  await sheetsFor('contact');
  const g = G.contact;
  await S('field-label', q('.field-label').first(), ['default'], { group: g, title: 'Field label', desc: 'Inter 14/400, ink rgb(52,64,84).', sel: '.field-label' });
  await S('text-field', q('input.form-input').first(), ['default', 'hover', 'focus-visible', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'White field, 8px radius, 44px tall, 8px 14px padding. Autofocus paints a coral ring before any click. Sample text was typed and deleted. The form was not submitted.', sel: 'input.form-input' });
  await S('text-area', q('textarea.form-input').first(), ['default', 'hover', 'focus-visible', 'focused'], { group: g, title: 'Text area', desc: '112px tall, 8px radius, 1px rgb(208,213,221) border, 12px 14px padding. Not submitted.', sel: 'textarea.form-input' }, { fillText: 'A short note' });
  await S('send-button', q('input[type=submit]').first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Send button', desc: 'Webflow submit styled as the coral button. Not pressed. Pressed was not forced, so the form cannot fire.', sel: 'input[type=submit].button' });
  await page.close();
}

async function tool() {
  await newPage('tool', { wait: 2000 });
  await sheetsFor('tool');
  await S('tool-heading', q('h1').first(), ['default'], { group: G.tool, title: 'Tool heading', desc: 'Free Blog Title Generator. The generator form itself did not render signed out (no input on the page).', sel: 'h1' }, { noScroll: true });
  await S('tool-cta', q('a').filter({ hasText: /Try Macaw free/ }).first(), ['default', 'hover'], { group: G.tool, title: 'Tool call to action', desc: 'Try Macaw free. Not followed.', sel: 'a' });
  await page.close();
}

async function legal() {
  await newPage('terms', { wait: 1500 });
  await S('legal-heading', q('h1').first(), ['default'], { group: G.legal, title: 'Legal heading', desc: 'Terms and Conditions, Inter 53.6/700.', sel: 'h1' }, { noScroll: true });
  await page.close();
  await newPage('privacy', { wait: 1500 });
  await S('privacy-heading', q('h1').first(), ['default'], { group: G.legal, title: 'Privacy heading', sel: 'h1' }, { noScroll: true });
  await page.close();
}

async function mobile() {
  const g = G.mobile;
  await newPage('home', { mobile: true, wait: 2000 });
  await S('m-navbar', q('.navbar_component'), ['default'], { group: g, title: 'Mobile top bar', sel: '.navbar_component' }, { noScroll: true });
  await S('m-menu-button', q('.navbar_menu-button, .w-nav-button').first(), ['default'], { group: g, title: 'Mobile menu button', desc: 'Opens the Webflow nav drawer. The drawer shot is in screenshots; this crop is the button at rest.', sel: '.w-nav-button' }, { noScroll: true });
  await S('m-button-primary', q('a.button'), ['default'], { group: g, title: 'Primary button (mobile)', desc: 'Coral Start control in the first phone screen. The href was not followed.', sel: 'a.button' }, { byBox: true });
  await page.close();
  await newPage('pricing', { mobile: true, wait: 2000 });
  await S('m-plan', q('.pricing07_top-row-content').first(), ['default'], { group: g, title: 'Plan card (mobile)', sel: '.pricing07_top-row-content' });
  await page.close();
}

const PAGES = { home, pricing, contact, tool, legal, mobile };
const want = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(PAGES);
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
// the same for states: a state an earlier run recorded that this finished run's spec no longer lists goes
for (const [key, c] of Object.entries(out.components)) {
  if (!done.has(c.run) || !listed.has(key)) continue;
  for (const st of Object.keys(c.states || {})) if (!listed.get(key).has(st)) { delete c.states[st]; log('dropped stale state', key, st); }
}
save();
log('done ->', OUT);
