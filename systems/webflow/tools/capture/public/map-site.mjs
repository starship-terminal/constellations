// Maps the public webflow.com site tree from the homepage before screenshots.
// Reads the DOM. Opens menus by click, never submits a form, never types,
// never clicks Continue with Google or Apple. Auth URLs are recorded and left.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const OUT = path.join(os.homedir(), '.design-systems', 'webflow', 'site-map.json');
fs.mkdirSync(path.dirname(OUT), { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const AUTH = /webflow\.com\/(login|signup|sign-up|dashboard)(\/|$|\?)/i;
const SOCIAL = /\b(google|apple)\b/i;

async function dump(page) {
  return page.evaluate(() => {
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      if (r.width < 2 || r.height < 2) return false;
      if (cs.visibility === 'hidden' || cs.display === 'none') return false;
      return true;
    };
    const text = (el) => (el.innerText || el.getAttribute('aria-label') || el.getAttribute('title') || '')
      .replace(/\s+/g, ' ').trim().slice(0, 140);
    const nav = document.querySelector('header, nav, [role="banner"]');
    const scope = (root) => root || document;
    const linksOf = (root) => [...scope(root).querySelectorAll('a[href]')].filter(vis).map((a) => ({
      text: text(a),
      href: a.href,
      expanded: a.getAttribute('aria-expanded'),
      haspopup: a.getAttribute('aria-haspopup'),
    }));
    const buttonsOf = (root) => [...scope(root).querySelectorAll('button, [role="button"], summary')].filter(vis).map((b) => ({
      text: text(b),
      aria: b.getAttribute('aria-label') || '',
      expanded: b.getAttribute('aria-expanded'),
      controls: b.getAttribute('aria-controls') || '',
      haspopup: b.getAttribute('aria-haspopup') || '',
    }));
    return {
      url: location.href,
      title: document.title,
      htmlClass: document.documentElement.className.slice(0, 200),
      dataTheme: document.documentElement.getAttribute('data-theme'),
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      navLinks: linksOf(nav).slice(0, 80),
      navButtons: buttonsOf(nav).slice(0, 40),
      allLinkCount: document.querySelectorAll('a[href]').length,
      footerLinks: linksOf(document.querySelector('footer')).slice(0, 80),
      dialogs: [...document.querySelectorAll('[role="dialog"], dialog, [aria-modal="true"]')].map((d) => ({
        text: text(d).slice(0, 240),
        hidden: d.getAttribute('aria-hidden'),
      })),
      inputs: [...document.querySelectorAll('input, textarea, select')].filter(vis).slice(0, 30).map((i) => ({
        tag: i.tagName.toLowerCase(),
        type: i.getAttribute('type') || '',
        name: i.getAttribute('name') || '',
        placeholder: (i.getAttribute('placeholder') || '').slice(0, 80),
        aria: i.getAttribute('aria-label') || '',
      })),
      bodyStart: (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 600),
    };
  });
}

async function openMenus(page, home) {
  const interactions = [];
  const candidates = [];
  for (const b of home.navButtons || []) {
    const label = (b.text || b.aria || '').replace(/\s+/g, ' ').trim();
    if (!label || label.length > 60) continue;
    if (SOCIAL.test(label)) continue;
    candidates.push({ kind: 'button', label });
  }
  for (const a of home.navLinks || []) {
    if (a.haspopup || a.expanded !== null) {
      const label = (a.text || '').slice(0, 60);
      if (label && !SOCIAL.test(label)) candidates.push({ kind: 'link', label, href: a.href });
    }
  }
  const seen = new Set();
  for (const c of candidates) {
    if (seen.has(c.label)) continue;
    seen.add(c.label);
    if (interactions.length >= 14) break;
    log('open', c.kind, c.label);
    const before = page.url();
    try {
      const loc = c.kind === 'button'
        ? page.locator('header button, nav button, [role="banner"] button').filter({ hasText: c.label }).first()
        : page.locator('header a, nav a').filter({ hasText: c.label }).first();
      if (!(await loc.count())) {
        interactions.push({ control: c.label, action: 'not-found' });
        continue;
      }
      await loc.click({ timeout: 4000 });
      await page.waitForTimeout(600);
      const after = page.url();
      if (AUTH.test(after)) {
        interactions.push({ control: c.label, action: 'auth-wall', url: after.split('?')[0] });
        await page.goBack({ waitUntil: 'domcontentloaded', timeout: 20000 }).catch(() => {});
        continue;
      }
      const snap = await dump(page);
      const extra = (snap.navLinks || []).filter((l) => !(home.navLinks || []).some((h) => h.href === l.href)).slice(0, 30);
      interactions.push({
        control: c.label,
        kind: c.kind,
        action: after !== before ? 'navigated' : 'menu-or-dialog',
        url: after.split('?')[0],
        dialogs: snap.dialogs.slice(0, 4),
        revealedLinks: extra.map((l) => ({ text: l.text, href: l.href })),
        expanded: snap.navButtons.filter((b) => b.expanded === 'true').map((b) => b.text || b.aria),
      });
      if (after !== before) {
        await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 30000 });
        await page.waitForTimeout(800);
      } else {
        await page.keyboard.press('Escape').catch(() => {});
        await page.mouse.click(8, 8).catch(() => {});
        await page.waitForTimeout(250);
      }
    } catch (e) {
      interactions.push({ control: c.label, action: 'failed', error: String(e.message).split('\n')[0].slice(0, 180) });
    }
  }
  return interactions;
}

const browser = await chromium.launch({ headless: true });
const tree = { capturedAt: new Date().toISOString(), base: BASE, widths: {} };

for (const [name, mobile] of [['desktop', false], ['phone', true]]) {
  log('width', name);
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: mobile ? 2 : 1,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  const page = await ctx.newPage();
  const record = { viewport: { width: vw, height: vh } };
  try {
    const res = await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 45000 });
    log('home', res && res.status(), page.url());
    await page.waitForTimeout(2500);
    record.measured = await page.evaluate(() => ({
      innerWidth: innerWidth,
      innerHeight: innerHeight,
      dpr: devicePixelRatio,
      vv: visualViewport && { w: visualViewport.width, h: visualViewport.height, scale: visualViewport.scale },
    }));
    record.home = await dump(page);
    log('links', record.home.allLinkCount, 'navButtons', record.home.navButtons.length);
    record.interactions = await openMenus(page, record.home);

    if (!mobile) {
      const login = await ctx.newPage();
      log('login probe');
      const lr = await login.goto('https://webflow.com/login', { waitUntil: 'domcontentloaded', timeout: 45000 });
      await login.waitForTimeout(2000);
      record.loginProbe = await dump(login);
      record.loginProbe.status = lr && lr.status();
      record.loginProbe.frameUrls = login.frames().map((f) => f.url()).filter((u) => u && u !== 'about:blank').slice(0, 8);
      // Do not click Continue with Google. Record that the control exists.
      record.loginProbe.socialControls = await login.evaluate(() =>
        [...document.querySelectorAll('button, a, iframe')].map((el) => (el.innerText || el.getAttribute('aria-label') || el.title || el.src || '').replace(/\s+/g, ' ').trim())
          .filter((t) => /google|apple/i.test(t)).slice(0, 8));
      await login.close();
    }
  } catch (e) {
    record.error = String(e.stack || e.message).split('\n').slice(0, 4).join(' | ');
    log('FAIL', record.error);
  }
  tree.widths[name] = record;
  await ctx.close();
}

fs.writeFileSync(OUT, JSON.stringify(tree, null, 2));
log('wrote', OUT);
await browser.close();
