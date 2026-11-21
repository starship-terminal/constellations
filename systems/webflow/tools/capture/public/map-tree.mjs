// Deeper public tree: dropdown panels, phone menu, in-page controls, unique paths.
// No form submit, no credential entry, no Google/Apple click.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const OUT = path.join(os.homedir(), '.design-systems', 'webflow', 'site-tree.json');
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

async function collect(page) {
  return page.evaluate(() => {
    const text = (el) => (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 160);
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return r.width > 1 && r.height > 1 && cs.visibility !== 'hidden' && cs.display !== 'none' && Number(cs.opacity) > 0;
    };
    const panels = [...document.querySelectorAll('[id^="dropdown_content_"], [id^="w-nav-overlay"]')].map((el) => ({
      id: el.id,
      hidden: el.getAttribute('aria-hidden'),
      display: getComputedStyle(el).display,
      links: [...el.querySelectorAll('a[href]')].map((a) => ({ text: text(a), href: a.href })),
    }));
    const controls = [...document.querySelectorAll('button, a[aria-haspopup], summary, [role="tab"], [aria-expanded]')].map((el) => ({
      tag: el.tagName.toLowerCase(),
      text: text(el).slice(0, 80),
      expanded: el.getAttribute('aria-expanded'),
      controls: el.getAttribute('aria-controls') || '',
      haspopup: el.getAttribute('aria-haspopup') || '',
      role: el.getAttribute('role') || '',
      href: el.href || '',
      visible: vis(el),
    })).filter((c) => c.text || c.controls);
    const links = [...document.querySelectorAll('a[href]')].map((a) => {
      let u;
      try { u = new URL(a.href); } catch { return null; }
      return { host: u.host, path: u.pathname, text: text(a).slice(0, 80) };
    }).filter(Boolean);
    const tabs = [...document.querySelectorAll('[role="tab"], [role="tablist"] button, .w-tab-link')].map((el) => ({
      text: text(el).slice(0, 80),
      selected: el.getAttribute('aria-selected'),
      visible: vis(el),
    }));
    const dialogs = [...document.querySelectorAll('[role="dialog"], dialog, [aria-modal="true"]')].map((d) => {
      const r = d.getBoundingClientRect();
      const cs = getComputedStyle(d);
      return {
        text: text(d).slice(0, 180),
        visible: r.width > 20 && r.height > 20 && cs.display !== 'none' && cs.visibility !== 'hidden',
        ariaHidden: d.getAttribute('aria-hidden'),
      };
    });
    return {
      url: location.href,
      title: document.title,
      panels,
      controls: controls.slice(0, 250),
      links,
      tabs: tabs.slice(0, 40),
      dialogs,
      theme: {
        dataTheme: document.documentElement.getAttribute('data-theme'),
        colorScheme: getComputedStyle(document.documentElement).colorScheme,
        darkClass: document.documentElement.classList.contains('dark') || document.body.classList.contains('dark'),
      },
    };
  });
}

const browser = await chromium.launch({ headless: true });
const out = { capturedAt: new Date().toISOString() };

const ctx = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
const page = await ctx.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(2000);
out.desktopClosed = await collect(page);

// Open each dropdown by its aria-controls id.
out.dropdowns = [];
for (const id of ['dropdown_content_0', 'dropdown_content_1', 'dropdown_content_2']) {
  const btn = page.locator(`[aria-controls="${id}"]`).first();
  const label = await btn.innerText().catch(() => id);
  log('dropdown', label.trim());
  await btn.click({ timeout: 4000 }).catch((e) => log('click fail', e.message.split('\n')[0]));
  await page.waitForTimeout(500);
  const snap = await collect(page);
  const panel = snap.panels.find((p) => p.id === id);
  out.dropdowns.push({ id, label: label.replace(/\s+/g, ' ').trim(), panel, dialogs: snap.dialogs });
  await page.keyboard.press('Escape').catch(() => {});
  await page.mouse.click(10, 860).catch(() => {});
  await page.waitForTimeout(200);
}

// In-page controls that are not nav.
const home = out.desktopClosed;
out.inPage = home.controls.filter((c) => c.visible && !/Platform|Solutions|Resources|SKIP/.test(c.text)).slice(0, 80);

await ctx.close();

const mctx = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  userAgent: UA_MOBILE,
  isMobile: true,
  hasTouch: true,
  locale: 'en-US',
});
await mctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
const mp = await mctx.newPage();
await mp.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await mp.waitForTimeout(2000);
log('phone menu');
const menuBtn = mp.locator('[aria-label="menu"], button.w-nav-button, .w-nav-button').first();
await menuBtn.click({ timeout: 4000 }).catch((e) => log('menu fail', e.message.split('\n')[0]));
await mp.waitForTimeout(700);
out.phoneMenu = await collect(mp);
out.phoneMenu.overlayOpen = await mp.evaluate(() => {
  const el = document.querySelector('[id^="w-nav-overlay"], .w-nav-overlay');
  if (!el) return null;
  const cs = getComputedStyle(el);
  return { id: el.id, display: cs.display, visibility: cs.visibility, text: (el.innerText || '').replace(/\s+/g, ' ').slice(0, 500) };
});
await mctx.close();

// Unique hosts and webflow.com paths from the closed homepage (footer + nav are in DOM).
const paths = new Map();
const hosts = new Map();
for (const l of home.links) {
  hosts.set(l.host, (hosts.get(l.host) || 0) + 1);
  if (l.host === 'webflow.com' || l.host === 'www.webflow.com') {
    if (!paths.has(l.path)) paths.set(l.path, l.text);
  }
}
out.hosts = [...hosts.entries()].sort((a, b) => b[1] - a[1]);
out.webflowPaths = [...paths.entries()].map(([path, text]) => ({ path, text }));
log('paths', out.webflowPaths.length, 'hosts', out.hosts.length);

fs.writeFileSync(OUT, JSON.stringify(out, null, 2));
log('wrote', OUT);
await browser.close();
