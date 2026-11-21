// Measures aaply.app's public marketing components in every state reachable
// without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home features value pricing reviews story team figma mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// aaply.app is a Tilda site: every element is a .t396__elem wrapper with a
// data-elem-type (shape/image/button/text) and a .tn-atom child; selectors
// key off data-elem-type and text, not class names. Nothing is sent, bought
// or signed into: the only press is the pricing Monthly/Yearly toggle, a
// local state swap. The auth/demo host go.aaply.app returns "Not found" to
// this client — measured as an unreachable boundary, never submitted.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, open, closePromo, killGeo, domClick, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/',
  features: '/features',
  value: '/value',
  pricing: '/pricing',
  reviews: '/reviews',
  story: '/our-story',
  team: '/team',
  figma: '/figma_plugin',
  early: '/early-program',
  manual: '/manual',
};
let page, cdp, current, context, contextMobile, run, curCtx;
const touched = new Set();

// A bot interstitial or the app host's bare "Not found" body both render a
// minimal page: detect either so a blocked load is skipped, not measured.
async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /something went wrong|performing security verification|verifying you are human|just a moment|^not found$/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 6000 } = {}) {
  current = key;
  // A fresh context per page keeps Tilda's scroll-animated mount state from
  // leaking between routes.
  const b = context.browser();
  const ctx = curCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  page.setDefaultTimeout(8000);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  // Retry transient stalls / error bodies.
  for (let attempt = 0; attempt < 3; attempt++) {
    await open(page, URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { wait, promo });
    if (!(await blocked())) break;
    log('  blocked pass', attempt + 1, '- reloading');
  }
  if (await blocked()) { log('  BLOCKED', key); return false; }
  if (promo === 'close') await killGeo(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  return true;
}

async function closePage() {
  await page?.close().catch(() => {});
  await curCtx?.close().catch(() => {});
  page = cdp = curCtx = null;
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

// Clicks a UI toggle (accordion, menu, drawer). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign up|sign in|log in|create|buy|checkout|pay|purchase|subscribe|share|start free trial|upgrade|open|continue with|accept all|reject all|customize)$/i;
async function toggle(loc) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || t.tag === 'A') throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
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
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  delete out.components[key].missing;
  if (opts.open) { await reset(); await opts.open(); }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
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
// The painted surface of a Tilda elem is the .tn-atom inside it; the
// data-elem-type wrapper itself is transparent. Prefer the atom when present.
const atom = async (m) => ((await q(`[data-m-mark="${m}"] .tn-atom`).count()) ? q(`[data-m-mark="${m}"] .tn-atom`) : q(`[data-m-mark="${m}"]`));
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FILL = 'name@example.com';

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
        if (t || a) transitions.push({ selector: (r.selectorText || '').slice(0, 160), transition: t, animation: a });
      }
    };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin */ } }
    return transitions;
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}
// ---------- page runs ----------
const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  features: 'Features', value: 'Value', reviews: 'Reviews',
  story: 'Our story', team: 'Team', figma: 'Figma plugin',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) { await closePage(); return; }
  await sheetsFor('home');
  const g = G.shell;

  // The floating white nav bar is a [data-elem-type="shape"] atom (1200px,
  // pill radius) holding the logo, links and the two auth buttons.
  const nav = await page.evaluate(() => {
    const y = (n) => n.getBoundingClientRect().top + scrollY;
    const el = [...document.querySelectorAll('[data-elem-type="shape"]')].filter((n) => n.offsetWidth > 1000 && y(n) < 260)[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'nav'); return true;
  });
  await S('nav-bar', nav ? await atom('nav') : q('[data-elem-type="shape"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The floating rounded-white bar: aaply logo left, Features / Value / Pricing / Reviews links centre, Log in ghost button and the black Sign up pill right.', sel: 'shape nav bar' }, { noScroll: true });
  await S('logo', q('a.tn-atom[href="/"], [data-elem-type="image"] .tn-atom').filter({ visible: true }).first(), B4, { group: g, title: 'Logo', desc: 'The aaply wordmark with the lime chevron-roof mark, top-left of the nav bar.', sel: 'logo atom' }, { noScroll: true });
  await S('nav-link', q('a.tn-atom:has-text("Features"), [data-elem-type="button"] a:has-text("Features")').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A text link in the nav bar (Features / Value / Pricing / Reviews), Inter 18px.', sel: 'nav link atom' }, { noScroll: true });
  await S('nav-login', q('a.tn-atom:has-text("Log in")').filter({ visible: true }).first(), B4, { group: g, title: 'Log in button', desc: 'The ghost pill in the nav bar; links to the app host (go.aaply.app). Hovered and focused only — pressing leaves for auth.', sel: 'nav Log in' }, { noScroll: true });
  await S('nav-signup', q('a.tn-atom[href*="signup"]').filter({ visible: true }).first(), B4, { group: g, title: 'Sign up button', desc: 'The black Sign up pill in the nav bar; links to go.aaply.app/signup. Hovered and focused only.', sel: 'nav Sign up' }, { noScroll: true });

  const h = G.home;
  await S('hero-title', await domFind(page, /tool that helps/i, { sel: '.tn-atom', tag: 'ht', minH: 40 }), ['default'], { group: h, title: 'Hero title', desc: 'The Poppins 700 display headline with inline emoji/avatar atoms inside the sentence flow ("Tool that helps teams design mobile apps…").', sel: 'hero text atom' }, { noScroll: true });
  // the inline emoji atoms are duplicated hidden for scroll animation; pick the
  // first painted on-screen one (opacity > 0, inside the viewport, in the hero band)
  await page.evaluate(() => {
    const el = [...document.querySelectorAll('[data-elem-type="image"] .tn-atom')].find((n) => {
      const r = n.getBoundingClientRect(), cs = getComputedStyle(n);
      return r.width > 0 && r.y > 120 && r.y < 460 && r.x > 150 && r.x < 1200 && parseFloat(cs.opacity) > 0;
    });
    if (el) el.setAttribute('data-m-mark', 'he');
  });
  await S('hero-emoji', q('[data-m-mark="he"]').first(), ['default'], { group: h, title: 'Hero inline image', desc: 'One of the inline emoji/squiggle/avatar atoms set inside the headline flow — the design\'s signature move.', sel: 'inline emoji atom' }, { noScroll: true });
  await S('cta-signup-free', q('a.tn-atom:has-text("Sign up fo free"), a.tn-atom:has-text("Sign up to aaply")').filter({ visible: true }).first(), B4, { group: h, title: 'Sign up free CTA', desc: 'The lime "Sign up fo free →" pill (the typo is the product\'s own). Links to go.aaply.app/signup; hovered and focused only.', sel: 'lime hero CTA' }, { noScroll: true });
  await S('cta-demo', q('a.tn-atom:has-text("Try demo project")').filter({ visible: true }).first(), B4, { group: h, title: 'Try demo CTA', desc: 'The black "Try demo project" pill beside the lime CTA. Links to the app host\'s demo workspace; hovered and focused only.', sel: 'black hero CTA' }, { noScroll: true });
  // The product mockup is a browser-chrome-framed image atom — the biggest
  // image on the page.
  const mock = await page.evaluate(() => {
    const imgs = [...document.querySelectorAll('[data-elem-type="image"] .tn-atom, img')].filter(n => n.offsetWidth > 500);
    const big = imgs.sort((a, b) => b.offsetWidth * b.offsetHeight - a.offsetWidth * a.offsetHeight)[0];
    if (!big) return false;
    big.setAttribute('data-m-mark', 'mock'); return true;
  });
  await S('hero-mock', mock ? q('[data-m-mark="mock"]') : q('img').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero product mockup', desc: 'The product canvas inside a browser-chrome frame: the aaply workspace with screen tiles, connection arrows and collaborator cursors.', sel: 'hero mockup' });
  await S('chat-bubble', await domFind(page, /have you seen this|looks nice|i wanna try/i, { sel: '.tn-atom, div', tag: 'cb', minW: 60 }), ['default'], { group: h, title: 'Chat annotation bubble', desc: 'One of the fake-chat bubbles annotating the page (Have you seen this? / Looks nice! / I wanna try too) — rounded white bubbles with avatar stamps.', sel: 'chat bubble atom' });
  await S('step-number', await domFind(page, /^1$/, { sel: '.tn-atom, div, span', tag: 'sn', minW: 30 }), ['default'], { group: h, title: 'Step number', desc: 'The circled step numeral opening the "how it works" sequence.', sel: 'step numeral' });
  // The footer is a full-width black band (shape 1440x1088) at the page end.
  const foot = await page.evaluate(() => {
    const H = document.body.scrollHeight;
    const y = (n) => n.getBoundingClientRect().top + scrollY;
    const el = [...document.querySelectorAll('[data-elem-type="shape"]')].filter((n) => n.offsetWidth > 1200 && n.offsetHeight > 400 && y(n) > H - 1700)[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'foot'); return true;
  });
  await S('footer', foot ? await atom('foot') : await domFind(page, /made remotely|©20\d\d/i, { sel: '.tn-atom, div, footer', tag: 'fo', leaf: false, minW: 200 }), ['default'], { group: g, title: 'Footer', desc: 'The black footer band: "Made remotely with love", a published mail link (address not stored), social icons (Twitter, Medium, LinkedIn, Discord, YouTube, Instagram) and the second nav list.', sel: 'footer band' });
  await S('footer-link', q('a.tn-atom[href*="mailto"]').filter({ visible: true }).first(), B4, { group: g, title: 'Footer mail link', desc: 'The published contact link in the footer. The address is not stored. No crop is kept.', sel: 'footer mailto' });
  await S('social-icon', q('a.tn-atom[href*="twitter.com"], a[href*="discord"], a[href*="linkedin"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social icon', desc: 'One of the social-icon links in the footer.', sel: 'social icon a' });
  await S('early-birds', await domFind(page, /join the early birds/i, { sel: '.tn-atom', tag: 'eb', minH: 40 }), ['default'], { group: g, title: 'Early birds heading', desc: '"Join the early birds" — the Poppins display heading of the pre-footer CTA band ("Be the first to try").', sel: 'early birds heading' });
  await closePage();
}

async function features() {
  if (!(await newPage('features'))) { await closePage(); return; }
  await sheetsFor('features');
  const g = G.features;
  await S('features-title', await domFind(page, /here.?s what|workflow/i, { sel: '.tn-atom', tag: 'ft', minH: 40 }), ['default'], { group: g, title: 'Features title', desc: '"Here\'s what aaply workflow looks like" — Poppins display with an inline squiggle.', sel: 'features title' }, { noScroll: true });
  await S('step-title', await domFind(page, /start your new|add your first/i, { sel: '.tn-atom', tag: 'st2', minH: 30 }), ['default'], { group: g, title: 'Step title', desc: 'A numbered step heading in the workflow sequence ("Start your new mobile app design project").', sel: 'step title' });
  // The step card is a browser-chrome-framed product panel (Recent projects
  // / screen tiles): a 1131x634 image elem below each step heading. Tilda
  // offsetTop is relative to a zero-height wrapper, so rank by client rect.
  const panel = await page.evaluate(() => {
    const y = (n) => n.getBoundingClientRect().top + scrollY;
    const els = [...document.querySelectorAll('[data-elem-type="image"]')].filter((n) => n.offsetWidth > 800 && n.offsetHeight > 500 && y(n) > 300);
    const el = els.sort((a, b) => y(a) - y(b))[0]; if (!el) return false;
    el.setAttribute('data-m-mark', 'panel'); return true;
  });
  await S('step-card', panel ? await atom('panel') : await domFind(page, /let.?s get it started/i, { sel: '.tn-atom, div', tag: 'sc', leaf: false, minW: 200, minH: 80 }), ['default'], { group: g, title: 'Step card', desc: 'A workflow step\'s product panel: the browser-chrome-framed app screenshot beside the chat annotation bubble.', sel: 'step panel' });
  await S('mega-demo-cta', q('a.tn-atom:has-text("Try DEMO project")').filter({ visible: true }).first(), B4, { group: g, title: 'Mega demo CTA', desc: 'The oversized "Try DEMO project →" button (520x96) closing the features page. Links to the demo workspace; hovered and focused only.', sel: 'mega demo cta' });
  await closePage();
}

async function value() {
  if (!(await newPage('value'))) { await closePage(); return; }
  await sheetsFor('value');
  const g = G.value;
  await S('value-title', await domFind(page, /boost your creativity|aaply.?s value/i, { sel: '.tn-atom', tag: 'vt', minH: 40 }), ['default'], { group: g, title: 'Value title', desc: '"Aaply is here to boost your creativity" — the Poppins display heading.', sel: 'value title' }, { noScroll: true });
  // The value grid is square 271x272 shape cells with no inner text — pick by size.
  const vcard = await page.evaluate(() => {
    const el = [...document.querySelectorAll('[data-elem-type="shape"]')].filter((n) => n.offsetWidth > 250 && n.offsetWidth < 300 && n.offsetHeight > 250 && n.offsetHeight < 300)[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'vcard'); return true;
  });
  await S('value-card', vcard ? await atom('vcard') : q('[data-elem-type="shape"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Value card', desc: 'A square value-proposition cell in the Value grid (lime/white rounded shape with icon and caption atoms).', sel: 'value cell' });
  await closePage();
}

async function pricing() {
  if (!(await newPage('pricing'))) { await closePage(); return; }
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('pricing-title', await domFind(page, /^Pricing$/, { sel: '.tn-atom', tag: 'pt', minH: 40 }), ['default'], { group: g, title: 'Pricing title', desc: 'The page heading in Poppins 700.', sel: 'pricing title' }, { noScroll: true });
  const yearly = q('.tn-atom:has-text("Yearly"), [data-elem-type="button"] a:has-text("Yearly"), a:has-text("Yearly")').filter({ visible: true }).first();
  const monthly = q('.tn-atom:has-text("Monthly"), [data-elem-type="button"] a:has-text("Monthly"), a:has-text("Monthly")').filter({ visible: true }).first();
  // The toggle pair sits in a shared container; measure the wrap too.
  const wrap = yearly.locator('xpath=ancestor::*[.//*[contains(.,"Monthly")]][1]');
  await S('billing-toggle', wrap, ['default'], { group: g, title: 'Billing toggle', desc: 'The Monthly / Yearly segment pair: 152x60 pills, the held segment filled lime.', sel: 'billing segment' });
  await S('billing-yearly', yearly, ['default', 'hover', 'pressed'], { group: g, title: 'Yearly option', desc: 'The Yearly segment pill; selected by default.', sel: 'Yearly pill' });
  await S('billing-monthly', monthly, ['default', 'hover'], { group: g, title: 'Monthly option', desc: 'The Monthly segment pill.', sel: 'Monthly pill' });
  if (await monthly.count()) {
    await monthly.click().catch(() => monthly.evaluate((el) => el.click()));
    await page.waitForTimeout(1200);
    if (!(await blocked())) {
      await S('billing-monthly-on', monthly, ['open'], { group: g, title: 'Monthly option (selected)', desc: 'The Monthly segment after pressing it: client-side state swap, nothing posted.', sel: 'Monthly pill on' }, { noScroll: true });
      await S('plan-price-monthly', await domFind(page, /\/month/, { sel: '.tn-atom, div, span', tag: 'pm', minH: 20 }), ['open'], { group: g, title: 'Plan price (monthly)', desc: 'The plan price after switching to Monthly (the price is split across sibling atoms: a "$" atom and a ".1 /month" numeral atom).', sel: 'price monthly' }, { noScroll: true });
      await yearly.click().catch(() => {});
      await page.waitForTimeout(800);
    }
  }
  await S('save-badge', q('.tn-atom:has-text("Save 30%")').filter({ visible: true }).first(), ['default'], { group: g, title: 'Save badge', desc: 'The coral "Save 30%" badge beside the billing toggle.', sel: 'save badge' });
  const free = await domFind(page, /^Free$/, { sel: '.tn-atom', tag: 'fr', minH: 20 });
  const plus = await domFind(page, /^Plus$/, { sel: '.tn-atom', tag: 'pl', minH: 20 });
  // The plan cards are 561x618 shape elems (Free white left, Plus lime right)
  // behind the text atoms — Tilda texts position absolutely over them.
  const cards = await page.evaluate(() => {
    const els = [...document.querySelectorAll('[data-elem-type="shape"]')].filter((n) => n.offsetWidth > 540 && n.offsetWidth < 580 && n.offsetHeight > 590 && n.offsetHeight < 650);
    els.sort((a, b) => a.getBoundingClientRect().left - b.getBoundingClientRect().left);
    if (els[0]) els[0].setAttribute('data-m-mark', 'free');
    if (els[1]) els[1].setAttribute('data-m-mark', 'plus');
    return els.length;
  });
  await S('plan-card-free', cards > 0 ? await atom('free') : free.filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card (Free)', desc: 'The white Free plan card: $0, "Easy start for mobile creators", feature list, 3D character render.', sel: 'free card' });
  await S('plan-card-plus', cards > 1 ? await atom('plus') : plus.filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card (Plus)', desc: 'The lime Plus card: $11.1 /month billed yearly, "Full access for the price of a cup of coffee", 3D character render.', sel: 'plus card' });
  await S('plan-name', free.filter({ visible: true }).first().or(plus.filter({ visible: true }).first()), ['default'], { group: g, title: 'Plan name', desc: 'A plan name (Free / Plus) on the card.', sel: 'plan name' });
  await S('plan-price', await domFind(page, /\$\s*0|\.1\s*\/month|\/month/i, { sel: '.tn-atom, div, span', tag: 'pp', minH: 20 }), ['default'], { group: g, title: 'Plan price', desc: 'The large price numeral with the /month suffix.', sel: 'plan price' });
  await S('plan-cta', q('.tn-atom:has-text("Get started"), a:has-text("Start for free")').filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'The Get started / Start for free button inside a plan card. Hovered and focused only.', sel: 'plan cta' });
  await S('compare-cta', q('.tn-atom:has-text("Compare features"), a:has-text("Compare features")').filter({ visible: true }).first(), B4, { group: g, title: 'Compare features link', desc: 'The "Compare features →" link under the cards.', sel: 'compare link' });
  // The feature-comparison table is a tall 527x1166 shape card.
  const ftable = await page.evaluate(() => {
    const el = [...document.querySelectorAll('[data-elem-type="shape"]')].filter((n) => n.offsetWidth > 500 && n.offsetWidth < 560 && n.offsetHeight > 900)[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'ftable'); return true;
  });
  await S('feature-table', ftable ? await atom('ftable') : await domFind(page, /unlimited|soon|active project/i, { sel: '.tn-atom, td, div', tag: 'fc', minW: 40, minH: 20 }), ['default'], { group: g, title: 'Feature table', desc: 'The feature-comparison table card: rows of features with checkmarks, "+" and "soon" pills.', sel: 'feature table' });
  await closePage();
}

async function reviews() {
  if (!(await newPage('reviews'))) { await closePage(); return; }
  await sheetsFor('reviews');
  const g = G.reviews;
  // The page opens with a wide lime carousel slide (avatar, name, quote,
  // "Try it for free" pill) — measure it as the header, then a grid card.
  const slide = await page.evaluate(() => {
    const el = [...document.querySelectorAll('[data-elem-type="shape"], [data-elem-type="card"]')].filter((n) => n.offsetWidth > 600 && n.offsetHeight > 300 && n.offsetHeight < 600)[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'slide'); return true;
  });
  await S('review-slide', slide ? await atom('slide') : q('[data-elem-type="shape"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Review slide', desc: 'The wide lime featured-review slide at the top: avatar, name and role, the quote in Poppins, a "Try it for free" ghost pill; carousel dots below.', sel: 'review slide' }, { noScroll: true });
  const rcard = await page.evaluate(() => {
    const el = [...document.querySelectorAll('[data-elem-type="shape"], [data-elem-type="card"]')].filter((n) => n.offsetWidth > 340 && n.offsetWidth < 400 && n.offsetHeight > 500 && n.offsetHeight < 650)[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'rcard'); return true;
  });
  await S('review-card', rcard ? await atom('rcard') : q('[data-elem-type="shape"]').filter({ visible: true }).nth(1), ['default'], { group: g, title: 'Review card', desc: 'A testimonial card in the grid (370x580): quote text, an embedded image or chat screenshot.', sel: 'review card' });
  await S('review-text', await domFind(page, /product manager|aaply feels|great product|wireframes/i, { sel: '.tn-atom, [data-elem-type="text"]', tag: 'rt', minH: 60 }), ['default'], { group: g, title: 'Review quote', desc: 'The quote text inside a review card or the featured slide.', sel: 'review text' });
  await closePage();
}

async function story() {
  if (!(await newPage('story'))) { await closePage(); return; }
  await sheetsFor('story');
  const g = G.story;
  await S('story-lead', await domFind(page, /started with a wish|aaply fixes/i, { sel: '.tn-atom, [data-elem-type="text"]', tag: 'sl', minH: 60 }), ['default'], { group: g, title: 'Story lead', desc: '"Our story started with a wish!" — the page\'s opening editorial block.', sel: 'story lead' }, { noScroll: true });
  await S('story-block', await domFind(page, /modern products can|making things happen|app development|henry ford/i, { sel: '.tn-atom, [data-elem-type="text"]', tag: 'sb', minH: 60 }), ['default'], { group: g, title: 'Story paragraph', desc: 'A long-form body paragraph in the story.', sel: 'story text' });
  await closePage();
}

async function team() {
  if (!(await newPage('team'))) { await closePage(); return; }
  await sheetsFor('team');
  const g = G.team;
  await S('team-title', await domFind(page, /^Our Team$|dreamteam/i, { sel: '.tn-atom', tag: 'tt', minH: 40 }), ['default'], { group: g, title: 'Team title', desc: '"Our Team" — the Poppins display heading.', sel: 'team title' }, { noScroll: true });
  // Member cards are 359x479 shapes holding a 320x320 3D avatar image.
  const mcard = await page.evaluate(() => {
    const el = [...document.querySelectorAll('[data-elem-type="shape"], [data-elem-type="card"]')].filter((n) => n.offsetWidth > 330 && n.offsetWidth < 400 && n.offsetHeight > 440 && n.offsetHeight < 520)[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'mcard'); return true;
  });
  await S('member-card', mcard ? await atom('mcard') : q('[data-elem-type="shape"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Member card', desc: 'A team-member card (359x479): 3D character avatar, name, role.', sel: 'member card' });
  await closePage();
}

async function figma() {
  if (!(await newPage('figma'))) { await closePage(); return; }
  await sheetsFor('figma');
  const g = G.figma;
  await S('figma-title', await domFind(page, /aaply figma plugin|figma plugin/i, { sel: '.tn-atom', tag: 'fg', minH: 40 }), ['default'], { group: g, title: 'Figma plugin title', desc: '"Aaply Figma Plugin" display heading.', sel: 'figma title' }, { noScroll: true });
  // The numbered step cards (1 Design your app / 2 Click export / 3 Follow the
  // link) are wide rounded shapes holding text and screenshots.
  const fstep = await page.evaluate(() => {
    const y = (n) => n.getBoundingClientRect().top + scrollY;
    const els = [...document.querySelectorAll('[data-elem-type="shape"], [data-elem-type="card"]')].filter((n) => n.offsetWidth > 500 && n.offsetWidth < 600 && n.offsetHeight > 150 && n.offsetHeight < 420 && y(n) > 400);
    const el = els.sort((a, b) => y(a) - y(b))[0]; if (!el) return false;
    el.setAttribute('data-m-mark', 'fstep'); return true;
  });
  await S('figma-step', fstep ? await atom('fstep') : await domFind(page, /design your app|export button|follow the link/i, { sel: '.tn-atom, div', tag: 'fs', leaf: false, minW: 300 }), ['default'], { group: g, title: 'Export step card', desc: 'A numbered step card in the export instructions (Design your app in Aaply → Click the export button → Follow the link).', sel: 'figma step card' });
  await closePage();
}

async function early() {
  if (!(await newPage('early'))) { await closePage(); return; }
  await sheetsFor('early');
  const g = 'Early program';
  await S('early-title', await domFind(page, /early users program/i, { sel: '.tn-atom', tag: 'et', minH: 30 }), ['default'], { group: g, title: 'Early program title', desc: 'The "Early Users Program" Poppins display heading. The page is in the sitemap and is not linked from nav, footer, or the phone menu.', sel: 'early title' }, { noScroll: true });
  await S('early-step', await domFind(page, /sign up to aaply/i, { sel: '.tn-atom', tag: 'es', minH: 16 }), ['default'], { group: g, title: 'Early program step', desc: 'A numbered step label on the Early Users Program page ("Sign up to Aaply").', sel: 'early step' });
  await S('early-cta', q('a.tn-atom:has-text("Sign up for FREE")').filter({ visible: true }).first(), B4, { group: g, title: 'Early program CTA', desc: 'The lime "Sign up for FREE" pill. Links to go.aaply.app/signup; hovered and focused only, never followed.', sel: 'early cta' });
  await closePage();
}

async function manual() {
  if (!(await newPage('manual'))) { await closePage(); return; }
  await sheetsFor('manual');
  const g = 'Manual';
  await S('manual-title', await domFind(page, /how to get started/i, { sel: '.tn-atom', tag: 'mt', minH: 30 }), ['default'], { group: g, title: 'Manual title', desc: '"How to get started with Aaply?" — the Poppins display heading above an embedded product video. Sitemap-only; no in-page control opens it.', sel: 'manual title' }, { noScroll: true });
  await S('manual-cta', q('a.tn-atom:has-text("Start new project")').filter({ visible: true }).first(), B4, { group: g, title: 'Start new project CTA', desc: 'The "Start new project" pill. Links to https://go.aaply.app/, which is an auth wall (foreign document on the app host). Hovered and focused only.', sel: 'manual cta' });
  await closePage();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) { await closePage(); return; }
  const g = G.mobile;
  await closePromo(page);
  await S('m-nav-bar', q('[data-elem-type="shape"], [data-elem-type="button"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav bar', desc: 'The mobile header: logo left, hamburger right.', sel: 'mobile nav' }, { noScroll: true });
  await S('m-burger', q('a[href="#open-nav"]').filter({ visible: true }).first(), ['default', 'pressed'], { group: g, title: 'Hamburger', desc: 'The mobile menu button at the top right (a[href="#open-nav"]). Opens an in-page overlay; the overlay is m-menu.', sel: 'burger' }, { noScroll: true });
  await page.locator('a[href="#open-nav"]').first().evaluate((el) => el.click()).catch(() => {});
  await page.waitForTimeout(700);
  // The overlay is a full-viewport panel. Mark the painted shape that covers
  // the phone, not the close icon's 24px ancestor.
  const menuMarked = await page.evaluate(() => {
    const panels = [...document.querySelectorAll('[data-elem-type="shape"], div')].filter((n) => {
      const r = n.getBoundingClientRect();
      const cs = getComputedStyle(n);
      return r.width > 300 && r.height > 600 && r.x >= -2 && r.x < 40
        && parseFloat(cs.opacity) > 0.5 && cs.visibility !== 'hidden';
    });
    const el = panels.sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height)[0];
    if (!el) return false;
    el.setAttribute('data-m-mark', 'mmenu');
    return { w: Math.round(el.getBoundingClientRect().width), h: Math.round(el.getBoundingClientRect().height) };
  });
  log('  menu panel', menuMarked);
  await S('m-menu', menuMarked ? q('[data-m-mark="mmenu"]').first() : q('a[href="#close-nav"]').first(), ['default'], { group: g, title: 'Mobile menu', desc: 'The phone overlay opened by the burger: Log in and Sign up pills, then Features, Figma Plugin, Pricing, Reviews, Value, Story, Team, Blog. Close is #close-nav. Auth items were not followed. The whole overlay is also in screenshots/mobile-home-light-menu-open.png.', sel: 'mobile menu panel' }, { noScroll: true });
  // The visible Log in pill (opacity 1, on screen). A duplicate link sits at opacity 0.
  const loginMarked = await page.evaluate(() => {
    const el = [...document.querySelectorAll('a')].find((a) => {
      const r = a.getBoundingClientRect();
      const cs = getComputedStyle(a);
      return /log in/i.test(a.innerText || '') && r.x >= 0 && r.width > 80 && parseFloat(cs.opacity) > 0.5;
    });
    if (!el) return false;
    el.setAttribute('data-m-mark', 'mlogin');
    return true;
  });
  await S('m-menu-login', loginMarked ? q('[data-m-mark="mlogin"]').first() : q('a[href*="go.aaply.app/sign"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu Log in', desc: 'The Log in pill in the open phone menu. Target is https://go.aaply.app/sign, which returns "Not found". Not followed.', sel: 'menu login' }, { noScroll: true });
  await page.locator('a[href="#close-nav"]').first().evaluate((el) => el.click()).catch(() => {});
  await page.waitForTimeout(400);
  // the mobile headline is split into one painted atom per line; the full-text
  // duplicates stay hidden off-viewport for scroll animation — pick the painted line
  await page.evaluate(() => {
    const el = [...document.querySelectorAll('.tn-atom')].find((n) => {
      const r = n.getBoundingClientRect(), cs = getComputedStyle(n);
      return /tool that helps/i.test(n.innerText || '') && r.x >= 0 && r.width > 0 && parseFloat(cs.opacity) > 0;
    });
    if (el) el.setAttribute('data-m-mark', 'mh');
  });
  await S('m-hero-title', q('[data-m-mark="mh"]').first(), ['default'], { group: g, title: 'Mobile hero title', desc: 'The first painted line of the mobile Poppins headline — the mobile title splits one atom per line.', sel: 'mobile hero' }, { noScroll: true });
  await S('m-cta-signup', q('a.tn-atom:has-text("Sign up fo free"), a.tn-atom:has-text("Sign up to aaply")').filter({ visible: true }).first(), ['default', 'pressed'], { group: g, title: 'Mobile sign up CTA', desc: 'The full-width lime pill.', sel: 'mobile lime cta' }, { noScroll: true });
  await S('m-cta-demo', q('a.tn-atom:has-text("Try demo project")').filter({ visible: true }).first(), ['default', 'pressed'], { group: g, title: 'Mobile demo CTA', desc: 'The full-width black pill.', sel: 'mobile black cta' }, { noScroll: true });
  await S('m-step-number', await domFind(page, /^1$/, { sel: '.tn-atom, div, span', tag: 'ms', minW: 20 }), ['default'], { group: g, title: 'Mobile step number', desc: 'The circled step numeral in the mobile how-it-works column.', sel: 'mobile step numeral' });
  await closePage();
}

const RUNNERS = { home, features, value, pricing, reviews, story, team, figma, early, manual, mobile };
run = new Date().toISOString();
out._meta.run = run;
out._meta.product = 'aaply.app';
const wanted = process.argv.slice(2).join(',').split(',').map((s) => s.trim()).filter(Boolean);
try {
({ context } = await launch());
for (const [k, fn] of Object.entries(RUNNERS)) {
  if (wanted.length && !wanted.includes(k)) continue;
  try { await fn(); } catch (e) { log('PAGE FAILED', k, String(e.message).split('\n')[0]); }
  save();
}
} finally {
  await closePage();
  await context?.browser()?.close().catch(() => {});
}
// mark components from this run whose selectors matched nothing; a component
// with recorded states (from an earlier merged run) is covered, not missing
for (const [k, c] of Object.entries(out.components)) {
  if (!touched.has(k)) continue;
  if (Object.keys(c.states || {}).length) delete c.missing;
  else c.missing = true;
}
save();
log('done ->', OUT);
