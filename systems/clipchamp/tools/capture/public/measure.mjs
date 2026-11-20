// Measures clipchamp.com's public components in every state reachable
// without signing in, paying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing features signin mobile (the footer group also runs
// on home). Writes raw/components-computed.json (merged) and one crop per
// component and state into components/crops/; raw/measurements.md is
// built by build-measurements.mjs.
//
// clipchamp.com is a Microsoft React/Fluent-UI build in one LIGHT theme:
// CSS-modules classes carry semantic suffixes (_Header, _GradientButton,
// _TableWrapper) and nav buttons stable data-testids, so those are the
// selectors used. app.clipchamp.com/login is the product's sign-in
// boundary: its card is measured, never submitted. The only presses are
// local UI toggles — the nav dropdown triggers (href="#"), FAQ <details>
// summaries and the mobile side-bar button. Sign-in/Sign-up/Get-started
// links are measured, never followed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/en/', pricing: '/en/pricing/', features: '/en/features/', signin: 'https://app.clipchamp.com/login' };
let page, cdp, current, view, context, run;
const touched = new Set();
const listed = new Map();
// Page+viewport visits that actually loaded this run (not blocked): readings
// may only be pruned for components of one of these — a blocked mobile visit
// must not erase evidence the desktop visit of the same route kept.
const opened = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || /just a moment/i.test(document.title) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, dsf } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: dsf ?? 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, /^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key], { wait });
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  opened.add(key + '|' + view);
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
  Object.assign(c, { page: current, view, run, url: URLS[current] && new URL(URLS[current], BASE).href }, meta);
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
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    // A failed crop keeps the previous state's image link rather than
    // dropping it; the style reading is fresh, the crop is last good.
    c.states[state] = { ...s, crop: file ?? (prev && prev.crop), via: opts.via, run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed state capture must not erase a previous reading: keep it under
    // its own provenance and record the error beside it.
    const prev = c.states[state];
    c.states[state] = prev && !prev.error
      ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
      : { error: String(e.message || e).slice(0, 200) };
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
        if (opts.noToggle) via = 'menu held open by opts.open';
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      out.components[key].states[st] = prev && !prev.error
        ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
        : { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (nav menu, mobile menu). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|start|get started|claim|share|export|select|continue|book|request)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Marks the shallowest ancestor of a text leaf whose subtree paints a fill of
// colour `want` (Framer draws a button's fill on a sibling layer, so the
// anchor alone reads transparent). `minY` skips same-text copies in the
// header. Falls back to the leaf. Returns whether anything was marked.
const markFillParent = async (textRe, want, attr, { minY = 0 } = {}) => page.evaluate(([src, flags, a, w, miny]) => {
  const re = new RegExp(src, flags);
  const texts = [...document.querySelectorAll('a,button,div,p,span')].filter((n) => {
    const t = (n.innerText || '').trim();
    const r = n.getBoundingClientRect();
    return re.test(t) && t.length < 60 && r.width > 0 && r.y >= miny;
  });
  const leaf = texts.find((n) => !texts.some((o) => o !== n && n.contains(o))) || texts[0];
  if (!leaf) return false;
  const paints = (n) => getComputedStyle(n).backgroundColor === w;
  for (let n = leaf, i = 0; n && i < 8; i++, n = n.parentElement) {
    if (n.getBoundingClientRect().width > 700) break;
    if (paints(n) || [...n.children].some((k) => paints(k) && k.getBoundingClientRect().width >= 80)) {
      n.setAttribute(a, '1');
      return true;
    }
  }
  leaf.setAttribute(a, '1');
  return true;
}, [textRe.source, textRe.flags, attr, want, minY]);

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
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  features: 'Features', signin: 'App sign-in (boundary)',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  // The sticky top bar: Clipchamp wordmark left, Features/Create/For
  // work/Learn dropdown triggers centre, Sign-in outline button and the
  // gradient Try-for-free button right.
  await S('header', q('header[class*="_Header"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The sticky 1440 top nav (position:sticky): logo, four dropdown menus, Sign-in and Try-for-free actions.', sel: 'header[class*=_Header]' }, { noScroll: true });
  await S('logo', q('a[class*="_LogoParent"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Clipchamp wordmark anchor (purple mark + logotype; the mark paints #5a4cdb).', sel: 'a[class*=_LogoParent]' }, { noScroll: true });
  await S('nav-item', q('a[aria-haspopup="true"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav menu trigger', desc: 'The "Features" dropdown trigger — an anchor with role=button/aria-haspopup that opens its submenu locally, never navigates.', sel: 'a[aria-haspopup=true]' }, { noScroll: true });
  // The dropdown opens on trigger hover and closes when the pointer parks,
  // so it must be re-opened inside S()'s own pre-state reset: opts.open runs
  // after reset(), and noReset/noScroll keep it held through the states.
  const trigger = q('a[aria-haspopup="true"]').filter({ visible: true }).first();
  const subPanel = q('[class*="_DesktopNavSubMenuContainer"]').first();
  const subShown = async () => (await subPanel.count()) && (await subPanel.evaluate((e) => getComputedStyle(e).display !== 'none').catch(() => false));
  const openSub = async () => {
    if (!(await trigger.count())) return;
    await trigger.hover({ timeout: 5000 }); await page.waitForTimeout(1200);
    if (!(await subShown())) { await trigger.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(800); }
  };
  await S('nav-submenu', q('[class*="_DesktopNavSubMenuContainer"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav submenu', desc: 'The Features dropdown panel, held open by hovering its trigger (DesktopNavSubMenuContainer).', sel: '[class*=_DesktopNavSubMenuContainer]' }, { noScroll: true, noReset: true, open: openSub });
  // Only default+hover are honest here: keyboard focus or a forced press
  // moves intent off the hover-held menu and the panel closes under the
  // reading, so those states are not measurable on this pattern.
  await S('nav-submenu-link', q('[class*="_SubMenuItem"] a').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Submenu link', desc: 'A link inside the open Features submenu; focus/pressed are unreachable while the panel is hover-held.', sel: '[class*=_SubMenuItem] a' }, { noScroll: true, noReset: true, open: openSub });
  await reset();
  await S('nav-signin', q('a[data-testid="nav-login-button"]').filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in button', desc: 'The outline "Sign in" button (AccentOutlineButton) linking to app.clipchamp.com/login; measured never followed.', sel: 'a[data-testid=nav-login-button]' }, { noScroll: true });
  await S('nav-cta', q('a[data-testid="nav-signup-button"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The "Try for free" button (GradientButton class; paints solid #6453e4 over a 1px same-colour border) linking to app.clipchamp.com/signup; measured never followed.', sel: 'a[data-testid=nav-signup-button]' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('h1[class*="_HeroTitle"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: '"Online video editor" — the hero display headline.', sel: 'h1[class*=_HeroTitle]' }, { noScroll: true });
  await S('hero-subtitle', q('[class*="_HeroSubtitle"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero subtitle', desc: 'The hero subline under the headline.', sel: '[class*=_HeroSubtitle]' }, { noScroll: true });
  await S('hero-cta', q('a[data-testid="heroBannerButton-0"], [class*="_HeroButtonContainer"] a').filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The "Create a video" WhiteButton under the hero copy — a light pill on the purple hero band; links to signup, never followed.', sel: 'a[data-testid=heroBannerButton-0]' }, { noScroll: true });
  await S('cta-secondary', q('main a[class*="_GradientButton"], [class*="_ButtonContainer"] a[class*="_GradientButton"]').filter({ visible: true }).first(), B4, { group: h, title: 'Section CTA', desc: 'A mid-page GradientButton inside a ButtonContainer — the section-level signup CTA, the same solid-purple style as the nav CTA in content context.', sel: 'main a[class*=_GradientButton]' });
  // The dark band sits below the fold and reveals on scroll; bring it into
  // view before measuring its WhiteButton.
  await page.evaluate(() => { const d = document.querySelector('[class*="_ContentBlockDark"]'); if (d) d.scrollIntoView({ block: 'center' }); });
  await page.waitForTimeout(1400);
  await S('cta-white', q('[class*="_AlignedContentWrapper"] a[class*="_WhiteButton"], [class*="_AlignedContent"] a[class*="_WhiteButton"]').filter({ visible: true }).first(), B4, { group: h, title: 'White CTA on dark band', desc: 'The "Create a video" WhiteButton in the dark AlignedContentWrapper promo block — the light-on-dark signup style (the hero\'s WhiteButton is hero-cta).', sel: '[class*=_AlignedContentWrapper] a[class*=_WhiteButton]' });
  await page.evaluate(() => scrollTo(0, 0)); await page.waitForTimeout(400);
  await S('feature-card', q('[class*="_LinkCardStyle"], [class*="_LinkCardInner"]').filter({ visible: true }).first(), B4, { group: h, title: 'Feature link card', desc: 'A feature link card (LinkCardStyle): a GradientButton-labelled card into a feature page, never followed.', sel: '[class*=_LinkCardStyle]' });
  await S('content-block', q('[class*="_ContentBlock"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Content block', desc: 'A content slice (ContentBlock) — copy column beside media.', sel: '[class*=_ContentBlock]' });
  await S('content-block-dark', q('[class*="_ContentBlockDark"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Dark band', desc: 'A dark-background content section — the site\'s dark band inside the single light theme.', sel: '[class*=_ContentBlockDark]' });  // _DarkBackground is also a text variant on headings
  await S('quote', q('[class*="_QuoteWrapper"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Testimonial', desc: 'A customer quote block (QuoteWrapper) with the author line.', sel: '[class*=_QuoteWrapper]' });
  await S('rating', q('[class*="_RatingContainer"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Rating badge', desc: 'The store-rating badge row (RatingContainer: stars + score).', sel: '[class*=_RatingContainer]' });
  await S('section-title', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section title', desc: 'The first section heading under the hero.', sel: 'first h2' });
  await S('page-ground', q('body'), ['default'], { group: h, title: 'Page ground', desc: 'The body element\'s painted fill — the page ground.', sel: 'document.body' }, { noScroll: true, crop: false });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The pricing page headline over the plan comparison table.', sel: 'h1' }, { noScroll: true });
  await S('plan-table', q('[class*="_TableWrapper"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan table', desc: 'The Free/Premium comparison table (TableWrapper): header plan cells + feature rows.', sel: '[class*=_TableWrapper]' }, { noScroll: true });
  await S('plan-head', q('[class*="_HeaderCell"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan header cell', desc: 'A plan header cell (HeaderCell/HeadIcon) carrying the plan name and price.', sel: '[class*=_HeaderCell]' }, { noScroll: true });
  // The comparison table carries no CTA; the plan actions live in the dark
  // hero (WhiteButton "Create videos for free") and the content CTAs below.
  await S('pricing-hero', q('[class*="_DarkHeroTitle"]').filter({ visible: true }).first().locator('xpath=ancestor::*[contains(@class,"_AlignedContentContainer") or contains(@class,"_Hero")][1]'), ['default'], { group: g, title: 'Pricing dark hero', desc: 'The dark hero band over the plan table (DarkHeroTitle + WhiteButton).', sel: 'ancestor band of [class*=_DarkHeroTitle]' }, { noScroll: true });
  await S('pricing-cta', q('[class*="_DarkHeroTitle"] ~ * a[class*="_WhiteButton"], [class*="DarkHero"] a[class*="Button"], a[class*="_WhiteButton"]').filter({ visible: true }).first(), B4, { group: g, title: 'Pricing hero CTA', desc: 'The "Create videos for free" WhiteButton in the dark pricing hero; links to signup, never followed.', sel: 'dark-hero a[class*=_WhiteButton]' }, { noScroll: true });
  await S('feature-row-head', q('[class*="_RowHeadCell"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature row head', desc: 'A feature name cell down the left of the comparison table (RowHeadCell).', sel: '[class*=_RowHeadCell]' });
  await S('feature-cell', q('td[class*="_Cell"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature cell', desc: 'A plan value cell in the table (Cell/CellStyle): check, value or dash.', sel: 'td[class*=_Cell]' });
  await S('feature-tooltip', q('[class*="_CellTooltip"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Tooltip cell', desc: 'A feature cell carrying a tooltip affordance (CellTooltip).', sel: '[class*=_CellTooltip]' });
  // The FAQ accordion — <details>/<summary>; 'opened' presses the summary,
  // a local toggle only.
  await S('faq-item', q('details[class*="_Details"], [class*="_ItemHeaderContainer"]').filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'FAQ item', desc: 'A pricing FAQ accordion item (details/ItemHeaderContainer); opened with its own summary toggle.', sel: 'details[class*=_Details]' }, { noScroll: true });
  await S('inline-link', q('a[class*="_InlineEntryLink"]').filter({ visible: true }).first(), B4, { group: g, title: 'Inline link', desc: 'An inline entry link in the page copy (InlineEntryLink).', sel: 'a[class*=_InlineEntryLink]' });
  save();
}

async function features() {
  if (!(await newPage('features'))) return;
  const g = G.features;
  await S('features-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Features title', desc: 'The features index headline.', sel: 'h1' }, { noScroll: true });
  await S('feature-section', q('[class*="_AlignedContentContainer"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature section', desc: 'An aligned content block on the features index: title, body list of entry links, side media (AlignedContentContainer).', sel: '[class*=_AlignedContentContainer]' });
  await S('feature-heading', q('[class*="_ContentTitle"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature section heading', desc: 'A feature section title inside an aligned content block (ContentTitle/StyledHeading with anchor).', sel: '[class*=_ContentTitle]' });
  await S('feature-link', q('a[class*="_InlineEntryLink"]').filter({ visible: true }).first(), B4, { group: g, title: 'Feature entry link', desc: 'An inline feature link inside a content list (InlineEntryLink); measured never followed.', sel: 'a[class*=_InlineEntryLink]' });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 18000 }))) return;
  const g = G.signin;
  // app.clipchamp.com/login is the product's sign-in surface: the account
  // options and any email field are measured; nothing is typed or sent.
  await S('signin-card', q('main, [class*="login" i], [class*="auth" i], form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The app.clipchamp.com login surface: the sign-in card the SPA paints. Measured at rest, never submitted.', sel: 'main/first visible login container' }, { noScroll: true });
  await S('signin-field', q('input[type="email"], input[type="text"], input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Account field', desc: 'The account/email field on the sign-in card; focused locally, never submitted.', sel: 'first visible input' }, { noScroll: true });
  await S('signin-button', q('button, a[class*="_Button"], a[class*="Button"]').filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'A sign-in/continue control on the card; measured never pressed.', sel: 'first visible button' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home'))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1600);
  await page.evaluate(() => {
    const f = document.querySelector('footer, [class*="_FooterWrapper"], [role="contentinfo"]');
    if (f) f.setAttribute('data-m-footer', '1');
  });
  await S('footer', q('[data-m-footer="1"]'), ['default'], { group: g, title: 'Footer', desc: 'The footer band: link columns, language selector, social icons and the legal subfooter.', sel: 'footer/[class*=_FooterWrapper]' }, { noScroll: true });
  await S('footer-link', q('[data-m-footer="1"] [class*="_LinksWrapper"] a[tabindex="0"], [data-m-footer="1"] [class*="_InfoLinks"] a[tabindex="0"], [data-m-footer="1"] a[tabindex="0"]').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A link in a footer link column. The footer renders duplicate tabindex="-1" clones for the collapsed/mobile variant; only tabindex=0 copies are measured.', sel: 'footer [class*=_LinksWrapper] a[tabindex=0]' }, { noScroll: true });
  await S('footer-social', q('[data-m-footer="1"] [class*="_FooterSocial"] a').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A footer social icon link.', sel: '[class*=_FooterSocial] a' }, { noScroll: true });
  await S('footer-lang', q('[data-m-footer="1"] [class*="_LanguageSelectorWrapper"], [class*="_LanguageSelectorWrapper"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Language selector', desc: 'The footer language selector (LanguageSelectorWrapper).', sel: '[class*=_LanguageSelectorWrapper]' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  // At 390 the nav collapses to the bar plus the side-bar toggle; the drawer
  // opens on the button's own press.
  await S('m-header', q('header[class*="_Header"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile bar', desc: 'The 390 mobile nav bar: logo + menu toggle.', sel: 'header[class*=_Header] at 390' }, { noScroll: true });
  await S('m-menu-button', q('[data-testid="side-bar-nav-button"], [class*="_SideBarNavButton"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Menu button', desc: 'The hamburger (side-bar-nav-button); its own press opens the drawer.', sel: '[data-testid=side-bar-nav-button]' }, { noScroll: true });
  const menuBtn = q('[data-testid="side-bar-nav-button"], [class*="_SideBarNavButton"]').filter({ visible: true }).first();
  if (await menuBtn.count()) {
    try { await menuBtn.evaluate((el) => el.click()); await page.waitForTimeout(1500); } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  }
  await S('m-menu-open', q('[class*="_SideBarDrawer"], [class*="_SideBarContainer"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The side-bar drawer after the hamburger press.', sel: '[class*=_SideBarDrawer] after toggle press' }, { noScroll: true });
  await S('m-menu-link', q('[class*="_SideBarDrawer"] a, [class*="_SideBarListItem"] a, [class*="_SideBarContainer"] a').filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A link row inside the open drawer.', sel: 'first link inside the open side bar' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The hero headline at 390.', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme (app.clipchamp.com/login is the sign-in boundary)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, features, signin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune only components whose page+viewport visit actually opened this
    // run: a blocked route (or a blocked mobile pass of a route the desktop
    // pass captured) keeps its earlier readings. Components saved before the
    // view field existed fall back to the m- prefix for their variant.
    if (!touched.has(key) && !pages.length) {
      const cview = c.view || (key.startsWith('m-') ? 'mobile' : 'desktop');
      if (opened.has(c.page + '|' + cview)) delete out.components[key];
      continue;
    }
    if (!touched.has(key)) continue;
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st) && pages.length) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
