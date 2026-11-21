// Visible-element states. Clicks are cancelled so a link is never followed.
// OAuth providers are measured, never activated. Consent is hidden, never accepted.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const RAW = path.join(PKG, 'raw');
const CROPS = path.join(PKG, 'components', 'crops');
const SHOTS = path.join(os.homedir(), '.design-systems', 'fal', 'raw-shots');
fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(SHOTS, { recursive: true });

const READ = (node) => {
  const s = getComputedStyle(node);
  const r = node.getBoundingClientRect();
  const keys = ['color','backgroundColor','borderTopWidth','borderTopColor','borderRadius','boxShadow','outline','outlineOffset','opacity','fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','paddingTop','paddingRight','paddingBottom','paddingLeft','height','width','textDecorationLine'];
  const o = { text: (node.innerText || node.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80), box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } };
  for (const k of keys) o[k] = s[k];
  return o;
};

async function run(colorScheme, tag) {
  const browser = await chromium.launch({ headless: true });
  const ctx = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    colorScheme,
    locale: 'en-US',
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
  });
  const page = await ctx.newPage();
  await page.addInitScript(() => {
    window.addEventListener('click', (e) => {
      const t = e.target.closest('a, button');
      if (!t) return;
      const label = (t.getAttribute('aria-label') || t.innerText || '');
      if (/theme/i.test(label)) return;
      e.preventDefault();
      e.stopPropagation();
    }, true);
  });
  async function open(url) {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(2500);
    await page.evaluate(() => {
      for (const el of document.querySelectorAll('#onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter')) el.style.setProperty('display', 'none', 'important');
      for (const el of document.querySelectorAll('div, aside')) {
        const t = (el.innerText || '').slice(0, 60);
        const r = el.getBoundingClientRect();
        if (/We Value Your Privacy/i.test(t) && r.width < 560 && r.height < 700) el.style.setProperty('display', 'none', 'important');
      }
    });
  }
  async function pick(sel) {
    const loc = page.locator(sel);
    const n = await loc.count();
    for (let i = 0; i < n; i++) {
      const box = await loc.nth(i).boundingBox();
      if (box && box.width > 8 && box.height > 8 && box.y < 2000) return loc.nth(i);
    }
    return null;
  }
  async function states(sel) {
    const loc = await pick(sel);
    if (!loc) return { missing: true, sel };
    const out = { sel, default: await loc.evaluate(READ) };
    const box = await loc.boundingBox();
    await page.mouse.move(box.x + 8, box.y + 8);
    await page.waitForTimeout(220);
    out.hover = await loc.evaluate(READ);
    await loc.focus().catch(() => {});
    await page.waitForTimeout(100);
    out.focus = await loc.evaluate(READ);
    await page.mouse.move(box.x + 8, box.y + 8);
    await page.mouse.down();
    await page.waitForTimeout(60);
    out.pressed = await loc.evaluate(READ);
    await page.mouse.up();
    await page.mouse.move(2, 2);
    return out;
  }
  async function crop(sel, name) {
    const loc = await pick(sel);
    if (!loc) return;
    const box = await loc.boundingBox();
    const pad = 4;
    await page.screenshot({
      path: path.join(CROPS, name),
      clip: { x: Math.max(0, box.x - pad), y: Math.max(0, box.y - pad), width: box.width + pad * 2, height: box.height + pad * 2 },
    });
  }

  const result = { colorScheme, pages: {} };
  if (tag === 'light') {
    await open('https://fal.ai/');
    result.pages.home = { url: page.url() };
    for (const [id, sel] of [
      ['nav-link', 'a.nav-list-item'],
      ['nav-dropdown', '.dropdown-toggle.w-dropdown-toggle'],
      ['button-sales', 'a.button[href="/contact-sales"]'],
      ['button-start', 'a.button[href="https://fal.ai/dashboard"]'],
      ['hero-h1', 'h1'],
      ['tab', 'a.tab-menu-link'],
      ['footer-link', 'footer a, a.footer-link'],
      ['hero-cta', 'a.button.w-inline-block:not([class*="w-variant"])'],
    ]) {
      result.pages.home[id] = await states(sel);
      const d = result.pages.home[id];
      console.log(tag, id, d.missing ? 'MISS' : `${d.default.text} bg=${d.default.backgroundColor} hover=${d.hover.backgroundColor}`);
      if (!d.missing) await crop(sel, `${id}-default.png`);
    }
    await page.locator('.nav-list-item-dropdown').filter({ hasText: 'Products' }).first().hover();
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(SHOTS, 'home-light-products-menu.png') });
    const item = page.locator('a.dropdown-links-item').first();
    if (await item.count()) {
      result.pages.home['menu-item'] = await states('a.dropdown-links-item');
      await crop('a.dropdown-links-item', 'menu-item-default.png');
    }

    await open('https://fal.ai/login');
    result.pages.login = { url: page.url() };
    for (const [id, sel] of [
      ['oauth-github', 'a[href*="connect/github"]'],
      ['oauth-google', 'a[href*="connect/google"]'],
      ['oauth-microsoft', 'a[href*="connect/microsoft"]'],
      ['sso', 'button:has-text("Use SSO")'],
      ['login-h1', 'h1'],
      ['login-nav', 'a[href="/blog"]'],
    ]) {
      result.pages.login[id] = await states(sel);
      const d = result.pages.login[id];
      console.log(tag, id, d.missing ? 'MISS' : `${d.default.text} bg=${d.default.backgroundColor} hoverBg=${d.hover.backgroundColor} focus=${d.focus.outline} shadow=${(d.focus.boxShadow||'').slice(0,60)}`);
      if (!d.missing) await crop(sel, `${id}-default.png`);
    }
    await page.screenshot({ path: path.join(SHOTS, 'login-light-default.png'), fullPage: false });

    await open('https://fal.ai/explore');
    const search = page.locator('input[aria-label="Search models"]');
    console.log('search count', await search.count());
    if (await search.count()) {
      result.pages.explore = { search: { default: await search.evaluate(READ) } };
      await search.focus();
      await page.waitForTimeout(150);
      result.pages.explore.search.focus = await search.evaluate(READ);
      await search.fill('flux');
      await page.waitForTimeout(500);
      result.pages.explore.search.filled = { valueLength: 4 };
      await page.screenshot({ path: path.join(SHOTS, 'explore-light-search.png') });
      await crop('input[aria-label="Search models"]', 'search-focus.png');
      await search.fill('');
      console.log('search focus shadow', result.pages.explore.search.focus.boxShadow, result.pages.explore.search.focus.outline);
    }
    const theme = await page.evaluate(() => [...document.querySelectorAll('button')].map(b => b.getAttribute('aria-label')).filter(Boolean).slice(0, 30));
    console.log('explore button labels', theme);
  }

  await open('https://fal.ai/docs');
  const html = await page.evaluate(() => document.documentElement.className.slice(0, 160));
  const scheme = await page.evaluate(() => getComputedStyle(document.documentElement).colorScheme + ' ' + getComputedStyle(document.body).backgroundColor);
  console.log(tag, 'docs html', html, 'scheme', scheme);
  const labels = await page.evaluate(() => [...document.querySelectorAll('button')].map(b => b.getAttribute('aria-label') || b.innerText.trim().slice(0, 40)).filter(t => t).slice(0, 20));
  console.log(tag, 'docs buttons', labels);
  await page.screenshot({ path: path.join(SHOTS, `docs-${tag}-default.png`) });

  const dark = page.getByRole('button', { name: /dark theme/i });
  if (tag === 'light' && await dark.count()) {
    await dark.first().click();
    await page.waitForTimeout(700);
    const after = await page.evaluate(() => ({
      html: document.documentElement.className.slice(0, 180),
      bg: getComputedStyle(document.body).backgroundColor,
      color: getComputedStyle(document.body).color,
      scheme: getComputedStyle(document.documentElement).colorScheme,
    }));
    console.log('docs after dark click', after);
    await page.screenshot({ path: path.join(SHOTS, 'docs-dark-default.png') });
    fs.writeFileSync(path.join(RAW, 'docs-dark.json'), JSON.stringify(after, null, 2));
  }

  await browser.close();
  return result;
}

const light = await run('light', 'light');
fs.writeFileSync(path.join(RAW, 'states.json'), JSON.stringify(light, null, 2));
const dark = await run('dark', 'dark');
fs.writeFileSync(path.join(RAW, 'states-dark-scheme.json'), JSON.stringify({ docsNote: 'see log', htmlProbe: true }, null, 2));
console.log('wrote states');
