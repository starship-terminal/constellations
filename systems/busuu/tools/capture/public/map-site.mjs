// Maps the public busuu.com tree from the homepage without signing in,
// submitting forms, or following login/signup walls.
//
//   PLAYWRIGHT=... node map-site.mjs
//
// Writes ~/.design-systems/busuu/probe/tree.json
import fs from 'node:fs';
import path from 'node:path';
import { chromium, UA, UA_MOBILE, BASE, patch, clearChallenge, closePromo } from './lib.mjs';

const OUT = process.env.OUT || path.join(process.env.HOME, '.design-systems/busuu/probe');
fs.mkdirSync(OUT, { recursive: true });

const AUTH = /\/(login|register|signup|sign-up|sign-in|onboarding|checkout|subscribe|sso|oauth|auth)\b/i;
const SKIP_HOST = /(facebook|instagram|twitter|x\.com|linkedin|youtube|tiktok|apple\.com|apps\.apple|play\.google|google\.com\/maps)/i;

function norm(href) {
  try {
    const u = new URL(href, BASE);
    u.hash = '';
    if (u.hostname.endsWith('busuu.com')) {
      u.hostname = u.hostname.replace(/^www\./, 'www.');
    }
    return u.toString().replace(/\/$/, '') || u.origin;
  } catch {
    return null;
  }
}

function sameSite(url) {
  try {
    const h = new URL(url).hostname;
    return h === 'www.busuu.com' || h === 'busuu.com' || h === 'app.busuu.com';
  } catch {
    return false;
  }
}

async function snapshotControls(page) {
  return page.evaluate(() => {
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return r.width > 8 && r.height > 8 && cs.visibility !== 'hidden' && cs.display !== 'none' && cs.opacity !== '0';
    };
    const label = (el) => (el.getAttribute('aria-label') || el.innerText || el.getAttribute('title') || el.getAttribute('alt') || '').replace(/\s+/g, ' ').trim().slice(0, 120);
    const items = [];
    const seen = new Set();
    for (const el of document.querySelectorAll('a, button, [role="button"], [role="tab"], [role="menuitem"], summary, select, [aria-haspopup], [aria-expanded]')) {
      if (!vis(el)) continue;
      const text = label(el);
      const href = el.tagName === 'A' ? el.href : (el.getAttribute('href') || '');
      const key = `${el.tagName}|${text}|${href}|${el.getAttribute('aria-expanded') || ''}|${el.getAttribute('aria-controls') || ''}`;
      if (seen.has(key)) continue;
      seen.add(key);
      const r = el.getBoundingClientRect();
      items.push({
        tag: el.tagName.toLowerCase(),
        role: el.getAttribute('role') || '',
        text,
        href: href || '',
        expanded: el.getAttribute('aria-expanded'),
        controls: el.getAttribute('aria-controls') || '',
        haspopup: el.getAttribute('aria-haspopup') || '',
        type: el.getAttribute('type') || '',
        name: el.getAttribute('name') || '',
        cls: String(el.className).slice(0, 80),
        region: r.y < 90 ? 'header' : r.y > window.innerHeight - 80 ? 'sticky' : 'body',
        y: Math.round(r.y),
      });
    }
    return {
      url: location.href,
      title: document.title,
      h1: (document.querySelector('h1')?.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 160),
      items,
    };
  });
}

const browser = await chromium.launch();
const widths = [
  { name: 'desktop', vw: 1440, vh: 900, ua: UA, mobile: false },
  { name: 'phone', vw: 390, vh: 844, ua: UA_MOBILE, mobile: true },
];

const report = { started: new Date().toISOString(), base: BASE, widths: {} };

for (const w of widths) {
  const ctx = await browser.newContext({
    viewport: { width: w.vw, height: w.vh },
    deviceScaleFactor: w.mobile ? 2 : 1,
    userAgent: w.ua,
    isMobile: w.mobile,
    hasTouch: w.mobile,
    locale: 'en-US',
  });
  await patch(ctx);
  const page = await ctx.newPage();
  const pages = [];
  const queue = [BASE + '/'];
  const seen = new Set();
  const walls = [];
  const external = [];
  let hops = 0;
  const MAX = 40;

  while (queue.length && hops < MAX) {
    const url = queue.shift();
    const key = norm(url);
    if (!key || seen.has(key)) continue;
    seen.add(key);
    hops++;
    console.log(w.name, hops, key);
    let status = 0;
    try {
      const res = await page.goto(key, { waitUntil: 'domcontentloaded', timeout: 60000 });
      status = res ? res.status() : 0;
    } catch (e) {
      pages.push({ url: key, error: String(e.message).split('\n')[0] });
      continue;
    }
    const ok = await clearChallenge(page, { tries: 8, step: 1500 });
    await page.waitForTimeout(2500);
    await closePromo(page);
    const finalUrl = page.url();
    const authWall = AUTH.test(finalUrl) || AUTH.test(key);
    const snap = await snapshotControls(page).catch((e) => ({ error: String(e.message), items: [] }));
    const entry = {
      requested: key,
      finalUrl,
      status,
      challenge: !ok,
      authWall,
      title: snap.title,
      h1: snap.h1,
      controlCount: (snap.items || []).length,
      controls: snap.items || [],
    };
    pages.push(entry);
    if (authWall) {
      walls.push({ from: key, finalUrl, title: snap.title });
      continue;
    }
    if (!ok) continue;
    for (const c of snap.items || []) {
      if (!c.href) continue;
      let abs;
      try { abs = new URL(c.href, finalUrl).toString(); } catch { continue; }
      if (SKIP_HOST.test(abs)) {
        external.push({ text: c.text, href: abs.split('?')[0], from: finalUrl });
        continue;
      }
      if (!sameSite(abs)) {
        external.push({ text: c.text, href: abs.split('?')[0], from: finalUrl });
        continue;
      }
      const n = norm(abs);
      if (!n || seen.has(n) || queue.includes(n)) continue;
      if (AUTH.test(n)) {
        walls.push({ text: c.text, href: n, from: finalUrl, stopped: true });
        continue;
      }
      // Stay on www marketing + a few app public shells. Skip query-only variants.
      const u = new URL(n);
      if (u.hostname === 'app.busuu.com') {
        walls.push({ text: c.text, href: n, from: finalUrl, note: 'app host, not followed' });
        continue;
      }
      if (u.pathname.split('/').length > 6) continue;
      queue.push(n);
    }
  }
  report.widths[w.name] = { pages, walls, external: external.slice(0, 80), truncated: queue.length };
  await ctx.close();
}

fs.writeFileSync(path.join(OUT, 'tree.json'), JSON.stringify(report, null, 1));
console.log('wrote', path.join(OUT, 'tree.json'));
await browser.close();
