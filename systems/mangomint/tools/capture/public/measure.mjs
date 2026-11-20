// Measures Mangomint public controls. Nothing is submitted. Walls are not filled.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { launch, open, styleOf, crop, CROPS, RAW, BASE, safeText } from './lib.mjs';

fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const out = {
  _meta: {
    product: 'Mangomint',
    captured: '2026-11-21',
    base: BASE,
    theme: 'light',
    note: 'Public marketing site only. Login, demo and trial are walls. No field was filled and no form was submitted.',
  },
  components: {},
  layout: {},
  foundations: {},
};
const log = (...a) => console.log(...a);

async function record(page, name, state, locator) {
  const n = await locator.count();
  if (!n) { log('  miss', name, state); return null; }
  const el = locator.first();
  const vis = await el.evaluate((node) => {
    const r = node.getBoundingClientRect();
    return r.width > 2 && r.height > 2;
  }).catch(() => false);
  if (!vis) { log('  hidden', name, state); return null; }
  try { await el.scrollIntoViewIfNeeded({ timeout: 3000 }); } catch { /* still measure */ }
  const style = await styleOf(el);
  style.text = safeText(style.text);
  out.components[name] ??= {};
  out.components[name][state] = style;
  const file = path.join(CROPS, `${name}-${state}.png`);
  try {
    await crop(el, file);
    style.crop = `components/crops/${name}-${state}.png`;
    log('  crop', name, state, style.rect.w + 'x' + style.rect.h, style.color, style.backgroundColor);
  } catch (e) {
    style.cropError = String(e.message).split('\n')[0];
    log('  crop failed', name, state, style.cropError);
  }
  return el;
}

async function forcePseudo(page, locator, classes) {
  const cdp = await page.context().newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await locator.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) { await cdp.detach().catch(() => {}); return null; }
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  return async () => {
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
    await cdp.detach().catch(() => {});
  };
}

async function states(page, name, locator) {
  const el = await record(page, name, 'default', locator);
  if (!el) return;
  try {
    await el.hover({ timeout: 2500 });
    await page.waitForTimeout(280);
    await record(page, name, 'hover', locator);
  } catch (e) { log('  hover skip', name, e.message.split('\n')[0]); }
  try {
    await el.focus();
    await page.waitForTimeout(180);
    await record(page, name, 'focus-visible', locator);
  } catch (e) { log('  focus skip', name, e.message.split('\n')[0]); }
  try {
    const release = await forcePseudo(page, locator.first(), ['hover', 'active']);
    if (release) {
      await page.waitForTimeout(120);
      await record(page, name, 'pressed', locator);
      await release();
    } else log('  press skip', name, 'no node id');
  } catch (e) { log('  press skip', name, e.message.split('\n')[0]); }
  await page.mouse.move(8, 8).catch(() => {});
}

async function readFoundations(page) {
  return page.evaluate(() => {
    const pick = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        sel,
        color: s.color,
        backgroundColor: s.backgroundColor,
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing,
        borderRadius: s.borderRadius,
        padding: s.padding,
        border: s.borderTopWidth + ' ' + s.borderTopStyle + ' ' + s.borderTopColor,
        boxShadow: s.boxShadow,
        height: Math.round(r.height),
        text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60),
      };
    };
    const sheets = [];
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { sheets.push({ href: sheet.href, error: 'unreadable' }); continue; }
      let vars = 0;
      if (rules) {
        const walk = (list) => {
          for (const rule of list) {
            if (rule.style) for (const n of rule.style) if (n.startsWith('--')) vars++;
            if (rule.cssRules) walk(rule.cssRules);
          }
        };
        walk(rules);
      }
      sheets.push({ href: sheet.href || 'inline', rules: rules ? rules.length : 0, vars });
    }
    return {
      innerWidth: window.innerWidth,
      innerHeight: window.innerHeight,
      dpr: window.devicePixelRatio,
      visualViewport: window.visualViewport ? {
        width: window.visualViewport.width,
        height: window.visualViewport.height,
        scale: window.visualViewport.scale,
      } : null,
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      body: pick('body'),
      h1: pick('h1'),
      h2: pick('h2'),
      sheets,
    };
  });
}

const { browser, context } = await launch();
const page = await context.newPage();
page.setDefaultTimeout(8000);

log('home');
await open(page, BASE + '/');
out.foundations.home = await readFoundations(page);
out.layout.desktop = {
  innerWidth: out.foundations.home.innerWidth,
  innerHeight: out.foundations.home.innerHeight,
  dpr: out.foundations.home.dpr,
  visualViewport: out.foundations.home.visualViewport,
};

await states(page, 'nav-trigger', page.locator('button.desktopNavbarDropdown-module--link--047eb', { hasText: 'Features' }));
await states(page, 'nav-pricing', page.locator('header a[href="/pricing/"], a[href="/pricing/"]').first());
await states(page, 'nav-login', page.locator('a[href*="app.mangomint.com"]').first());
await states(page, 'button-primary', page.locator('a[href="/trial/"]').first());
await states(page, 'button-secondary', page.locator('header a[href="/demo/"]').first());
await record(page, 'hero-title', 'default', page.locator('h1').first());
await record(page, 'announcement', 'default', page.locator('a[href*="meetmira"]').first());
await record(page, 'logo', 'default', page.locator('header a[href="/"]').first());
await states(page, 'carousel-tab', page.getByRole('button', { name: 'Slide 2' }).first());
await states(page, 'video-tour', page.locator('button.videoSelectionButton').first());

log('menu');
await page.locator('button.desktopNavbarDropdown-module--link--047eb', { hasText: 'Features' }).first().click();
await page.waitForTimeout(450);
const panel = page.locator('[class*="dropdownContent"]').nth(1);
await record(page, 'nav-menu', 'open', panel);
await states(page, 'nav-menu-link', panel.locator('a').first());
await page.keyboard.press('Escape');
await page.mouse.click(12, 500);

log('pricing');
await open(page, BASE + '/pricing/');
out.foundations.pricing = await readFoundations(page);
await record(page, 'pricing-title', 'default', page.locator('h1').first());
await states(page, 'stepper', page.getByRole('button', { name: 'Increase Locations' }));
await record(page, 'price-card', 'default', page.locator('text=Locations').locator('xpath=ancestor::*[contains(@class,"card") or self::div][1]').first());
await states(page, 'trial-cta', page.getByRole('link', { name: /start a free trial/i }).first());

log('login wall, no typing');
await open(page, 'https://app.mangomint.com/login', { wait: 2000 });
out.foundations.login = await readFoundations(page);
await record(page, 'login-email', 'default', page.locator('#login-page-email'));
await record(page, 'login-password', 'default', page.locator('#login-page-password'));
await states(page, 'login-submit', page.getByRole('button', { name: 'Log In' }));
await record(page, 'login-forgot', 'default', page.getByRole('link', { name: /forgot/i }));
const email = page.locator('#login-page-email');
if (await email.count()) {
  await email.focus();
  await page.waitForTimeout(200);
  await record(page, 'login-email', 'focused', email);
}

log('demo wall, no selection');
await open(page, BASE + '/demo/');
await record(page, 'choice-card', 'default', page.getByRole('button', { name: /Haircuts/ }).first());
await states(page, 'choice-card', page.getByRole('button', { name: /Haircuts/ }).first());
await record(page, 'continue', 'default', page.getByRole('button', { name: 'Continue' }));

log('blog card');
await open(page, BASE + '/blog/');
await record(page, 'blog-card', 'default', page.locator('a[href*="/blog/"]').nth(2));

log('footer link, no address');
await open(page, BASE + '/pricing/');
await page.evaluate(() => scrollTo(0, document.body.scrollHeight));
await page.waitForTimeout(500);
await states(page, 'footer-link', page.locator('footer a[href="/blog/"], footer a[href*="blog"]').first());

await page.close();

log('mobile');
const ctxM = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  isMobile: true,
  hasTouch: true,
  userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
  locale: 'en-US',
});
const m = await ctxM.newPage();
await open(m, BASE + '/');
out.layout.mobile = await m.evaluate(() => ({
  innerWidth: window.innerWidth,
  innerHeight: window.innerHeight,
  dpr: window.devicePixelRatio,
  visualViewport: window.visualViewport ? { width: window.visualViewport.width, height: window.visualViewport.height, scale: window.visualViewport.scale } : null,
}));
await states(m, 'm-hamburger', m.getByRole('button', { name: 'Toggle the navigation' }));
await m.getByRole('button', { name: 'Toggle the navigation' }).click();
await m.waitForTimeout(500);
await record(m, 'm-menu-link', 'default', m.getByRole('link', { name: 'Pricing' }).first());
await states(m, 'm-drawer-row', m.getByRole('button', { name: 'Features' }).first());
await m.close();
await ctxM.close();

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 2) + '\n');
log('wrote', Object.keys(out.components).length, 'components');
await browser.close();
