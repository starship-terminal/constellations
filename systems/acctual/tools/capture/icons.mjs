// Lift the interface SVGs out of acctual.com's public pages into icons/, with
// an INDEX.tsv next to them. Read-only: nothing is clicked except the mobile
// nav trigger on the home pass; no CMP banner renders on the Framer site. SP is a
// scratch dir outside the repository (unused here beyond parity with the
// kit; the outputs go straight into the package).
import crypto from 'crypto';
import fs from 'fs';
import { fileURLToPath } from 'node:url';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const OUT = fileURLToPath(new URL('../../icons/', import.meta.url));
fs.mkdirSync(OUT, { recursive: true });
const ROUTES = ['', 'pricing', 'teams', 'about', 'blog', 'freelancer-invoicing', 'stablecoin-invoicing', 'locations/us-to-japan', 'terms', 'privacy'];
// Slug for the inferred_name column: prefer the link/button label near the icon.
const nameOf = (ctx, cls) => {
  const c = (ctx || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
  const k = (cls || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
  return c || k || 'icon';
};
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
  const p = await ctx.newPage();
  const seen = {};
  for (const path of ROUTES) {
    await p.goto('https://www.acctual.com/' + path, { waitUntil: 'load', timeout: 60000 });
    await p.waitForTimeout(3500);
    // No CMP banner renders on acctual.com; open the mobile nav trigger once on
    // the home pass so its icon is in the DOM (a local disclosure).
    if (path === '') {
      const t = p.locator('[data-framer-name="navtrigger"]').first();
      if (await t.count()) { await t.click().catch(() => {}); await p.waitForTimeout(600); await t.click().catch(() => {}); }
    }
    const icons = await p.evaluate(() => [...document.querySelectorAll('svg')].filter(s => {
      const r = s.getBoundingClientRect();
      return r.width >= 8 && r.width <= 64 && r.height >= 8 && r.height <= 64 && !s.closest('.cky-consent-container, .cky-modal, [class*="cky"]');
    }).map(s => {
      const r = s.getBoundingClientRect();
      const st = getComputedStyle(s);
      const shapes = [...s.querySelectorAll('path,circle,rect,line,polyline,polygon,ellipse')];
      const fills = [...new Set(shapes.map(e => getComputedStyle(e).fill))];
      const strokes = [...new Set(shapes.map(e => getComputedStyle(e).stroke))];
      const sw = [...new Set(shapes.map(e => getComputedStyle(e).strokeWidth))];
      const host = s.closest('a,button');
      const label = (host?.innerText || host?.getAttribute('aria-label') || host?.getAttribute('title') || s.closest('[class*="social"]')?.className || s.parentElement?.innerText || '').trim().slice(0, 60);
      const place = host ? `${host.tagName.toLowerCase()} ${(host.className || '').toString().slice(0, 60)}` : `${s.parentElement?.tagName.toLowerCase() || ''} ${(s.parentElement?.className || '').toString().slice(0, 60)}`;
      const clone = s.cloneNode(true);
      clone.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
      return { w: Math.round(r.width), h: Math.round(r.height), color: st.color, fills, strokes, sw, label, place, vb: s.getAttribute('viewBox'), cls: (s.getAttribute('class') || '').slice(0, 60), html: clone.outerHTML };
    }));
    for (const ic of icons) {
      const h = crypto.createHash('md5').update(ic.html.replace(/class="[^"]*"/g, '')).digest('hex').slice(0, 10);
      if (seen[h]) { seen[h].pages.add(path); continue; }
      seen[h] = { ...ic, pages: new Set([path]), file: h + '.svg' };
      fs.writeFileSync(OUT + h + '.svg', ic.html);
    }
  }
  // Stable inferred names, unique per file.
  const rows = [];
  const used = new Set();
  for (const x of Object.values(seen)) {
    let name = nameOf(x.label, x.cls) || 'icon';
    if (used.has(name)) { let i = 2; while (used.has(`${name}-${i}`)) i++; name = `${name}-${i}`; }
    used.add(name);
    const file = name + '.svg';
    fs.renameSync(OUT + x.file, OUT + file);
    const style = x.strokes.some(s => s !== 'none' && s !== 'rgba(0, 0, 0, 0)') ? 'stroke' : 'fill';
    rows.push([file, name, x.file.replace('.svg', ''), `${x.w}x${x.h}`, x.vb || '', style, [...x.pages].join('; '), x.place.replace(/\t/g, ' '), x.label.replace(/\t/g, ' ').replace(/\n/g, ' ')]);
  }
  rows.sort((a, b) => a[1].localeCompare(b[1]));
  const tsv = ['file\tinferred_name\thash\tsizes\tviewBox\tstyle\tseen_on\tplace\ttext_or_label', ...rows.map(r => r.join('\t'))].join('\n') + '\n';
  fs.writeFileSync(OUT + 'INDEX.tsv', tsv);
  console.log(rows.length, 'icons');
  await b.close();
})();
