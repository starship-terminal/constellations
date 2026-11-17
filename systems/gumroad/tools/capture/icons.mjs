// Collects every distinct inline <svg> icon on gumroad.com's public pages into icons/ and writes icons/INDEX.tsv.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node icons.mjs
//
// The icons carry no name in the DOM, so a file is named from icon-names.tsv (geometry hash -> name)
// when the hash is listed there, else from the aria-label or text of the button or link it sits in, else
// from its CSS class, else `icon-<hash>`. Files whose geometry matches are one icon, listed once
// with every page and place it was seen. Colour is kept as `currentColor` wherever the computed fill or
// stroke equals the svg's text colour, so each icon recolours from CSS `color` the way it does on the site.
// Adapted from the gladia package's icons.mjs (itself the Coursera kit's).
//
// ScrollAll walks the document and any inner scrolling panes so icons lower
// on long pages (home, discover, terms) are seen.
import crypto from 'crypto';
import fs from 'fs';
import { M, BASE, chromium, UA, UA_MOBILE, closePromo, patch } from './public/lib.mjs';

const OUT = new URL('../../icons/', import.meta.url).pathname;
fs.mkdirSync(OUT, { recursive: true });
const wait = (p, ms) => p.waitForTimeout(ms);

// Runs in the page: one record per icon-sized svg currently in the DOM.
function collect() {
  const rgb = (c) => { const m = c.match(/rgba?\(([^)]+)\)/); return m ? m[1].split(',').slice(0, 3).map((x) => Math.round(parseFloat(x))).join(',') : c; };
  const hex = (c) => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return c; const [r, g, b] = m[1].split(',').map((x) => Math.round(parseFloat(x))); return '#' + [r, g, b].map((v) => v.toString(16).padStart(2, '0')).join(''); };
  const strip = (c) => String(c).replace(/__[A-Za-z0-9_-]{5,6}$/, '');
  return [...document.querySelectorAll('svg')].filter((s) => {
    const r = s.getBoundingClientRect();
    if (!(r.width >= 10 && r.width <= 64 && r.height >= 10 && r.height <= 64) || s.closest('svg svg')) return false;
    if (s.closest('[class*="canvas_board"], [class*="pgc_playerSurface"], hyperframes-player, .katex')) return false;
    return getComputedStyle(s).visibility !== 'hidden';
  }).map((s) => {
    const r = s.getBoundingClientRect(), col = rgb(getComputedStyle(s).color);
    const c = s.cloneNode(true);
    const shapes = [...s.querySelectorAll('path,circle,rect,line,polyline,polygon,ellipse')], cshapes = [...c.querySelectorAll('path,circle,rect,line,polyline,polygon,ellipse')];
    shapes.forEach((e, i) => {
      const cs = getComputedStyle(e), t = cshapes[i];
      for (const a of ['fill', 'stroke']) if ((t.getAttribute(a) || '').startsWith('var(')) t.setAttribute(a, rgb(cs[a]) === col ? 'currentColor' : hex(cs[a]));
      if (!t.hasAttribute('fill') && cs.fill !== 'none' && !cs.fill.startsWith('url')) t.setAttribute('fill', rgb(cs.fill) === col ? 'currentColor' : hex(cs.fill));
      else if (t.getAttribute('fill') && !['none', 'currentColor'].includes(t.getAttribute('fill')) && !t.getAttribute('fill').startsWith('url') && rgb(cs.fill) === col) t.setAttribute('fill', 'currentColor');
      if (!t.hasAttribute('stroke') && cs.stroke !== 'none') {
        t.setAttribute('stroke', rgb(cs.stroke) === col ? 'currentColor' : hex(cs.stroke));
        t.setAttribute('stroke-width', parseFloat(cs.strokeWidth) || 1);
        if (cs.strokeLinecap !== 'butt') t.setAttribute('stroke-linecap', cs.strokeLinecap);
        if (cs.strokeLinejoin !== 'miter') t.setAttribute('stroke-linejoin', cs.strokeLinejoin);
      }
    });
    c.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    for (const a of ['id', 'class', 'focusable', 'aria-hidden', 'aria-labelledby', 'style', 'data-testid']) c.removeAttribute(a);
    const refs = new Set([...c.outerHTML.matchAll(/url\(#([^)]+)\)/g)].map((m) => m[1].replace(/&quot;|"/g, '')));
    c.querySelectorAll('[id],[class],[style]').forEach((e) => { if (!refs.has(e.id)) e.removeAttribute('id'); e.removeAttribute('class'); if (e.tagName !== 'mask') e.removeAttribute('style'); });
    c.querySelectorAll('image').forEach((e) => e.remove());
    if (!c.hasAttribute('viewBox')) c.setAttribute('viewBox', `0 0 ${c.getAttribute('width') || Math.round(r.width)} ${c.getAttribute('height') || Math.round(r.height)}`.replace(/px/g, ''));
    if (!c.hasAttribute('width') || /%|em/.test(c.getAttribute('width'))) c.setAttribute('width', Math.round(r.width));
    if (!c.hasAttribute('height') || /%|em/.test(c.getAttribute('height'))) c.setAttribute('height', Math.round(r.height));
    const holder = s.closest('button,a,[role=button],[role=tab],[role=switch],label,li');
    const label = (holder?.getAttribute('aria-label') || s.getAttribute('aria-label') || holder?.innerText || s.parentElement?.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40);
    const modCls = [s, s.parentElement, holder].filter(Boolean).flatMap((e) => [...e.classList].map(String)).map(strip).find((x) => /_/.test(x) && !/^x[0-9a-z]+$/.test(x)) || '';
    const place = (holder ? holder.tagName.toLowerCase() : s.parentElement.tagName.toLowerCase()) + (modCls ? ' ' + modCls : '');
    const strokeOnly = shapes.length && shapes.every((e) => getComputedStyle(e).fill === 'none');
    return { w: Math.round(r.width), h: Math.round(r.height), vb: s.getAttribute('viewBox'), html: c.outerHTML, label, modCls, place, strokeOnly, color: col };
  });
}

const seen = new Map();
async function grab(p, tag) {
  const list = await p.evaluate(collect);
  let fresh = 0;
  for (const ic of list) {
    const key = crypto.createHash('md5').update(ic.html.replace(/\s(width|height|id)="[^"]*"/g, '').replace(/<(desc|title)>.*?<\/\1>/g, '').replace(/url\(#[^)]*\)/g, '')).digest('hex').slice(0, 8);
    const hit = seen.get(key);
    if (hit) { hit.where.add(tag); hit.sizes.add(`${ic.w}x${ic.h}`); if (ic.label) hit.labels.add(ic.label); hit.places.add(ic.place); continue; }
    fresh++;
    seen.set(key, { ...ic, key, where: new Set([tag]), sizes: new Set([`${ic.w}x${ic.h}`]), labels: new Set(ic.label ? [ic.label] : []), places: new Set([ic.place]) });
  }
  console.log(' ', tag, list.length, 'svgs,', fresh, 'new');
}
// The article scrolls in its own pane; the document itself stays at 0.
// Both are walked so icons lower in the article or the sidebar are seen.
async function scrollAll(p, tag) {
  const scs = await p.evaluate(() => {
    // gumroad.com scrolls the document; inner panes are appended after it.
    const out = [document.documentElement.scrollHeight];
    for (const el of document.querySelectorAll('div,main,aside,section,nav')) {
      const cs = getComputedStyle(el);
      if ((cs.overflowY === 'auto' || cs.overflowY === 'scroll') && el.scrollHeight > el.clientHeight + 100) out.push(el.scrollHeight);
    }
    return out.slice(0, 3);
  });
  const docH = scs.shift() || 0;
  for (let y = 0; y < docH; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 220); await grab(p, tag);
  }
  for (const h of scs) {
    for (let y = 0; y < h; y += 700) {
      await p.evaluate((y) => { const els = [...document.querySelectorAll('div,main,aside,section,nav')].filter((el) => { const cs = getComputedStyle(el); return (cs.overflowY === 'auto' || cs.overflowY === 'scroll') && el.scrollHeight > el.clientHeight + 100; }); els.forEach((el) => { el.scrollTop = y; }); }, y);
      await wait(p, 220); await grab(p, tag);
    }
  }
  await p.evaluate(() => { [...document.querySelectorAll('div,main,aside,section,nav')].forEach((el) => { el.scrollTop = 0; }); scrollTo(0, 0); });
  await wait(p, 400);
}
async function open(p, path, w = 6500) {
  await p.goto(BASE + path, { waitUntil: 'domcontentloaded', timeout: 90000 }); await wait(p, w);
}
// A page that fails is recorded, and a run with any failure leaves the committed icons alone.
const failed = [];
async function tryDo(label, fn) { try { await fn(); } catch (e) { failed.push(label); console.log('  skip', label, String(e.message).split('\n')[0]); } }

const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
await patch(ctx);
const p = await ctx.newPage();

await open(p, '/');
await closePromo(p);
await scrollAll(p, 'home');
for (const [path, tag] of [
  ['/discover', 'discover'], ['/design', 'category'], ['/features', 'features'],
  ['/pricing', 'pricing'], ['/about', 'about'], ['/help', 'help'],
  ['/login', 'login'], ['/signup', 'signup'], ['/terms', 'terms'],
]) {
  await open(p, path); await closePromo(p); await scrollAll(p, tag);
}
// The public overlays — the phone's nav sheet — are UI toggles: nothing is
// searched, followed or submitted.
await tryDo('mobile nav', async () => {
  await p.setViewportSize({ width: 390, height: 844 });
  await open(p, '/'); await closePromo(p);
  const ham = p.locator('[data-toggle="mobile-menu"], button[aria-label*="menu" i]').filter({ visible: true }).first();
  if (await ham.count()) { await ham.click({ timeout: 5000 }).catch(() => {}); await wait(p, 1400); await grab(p, 'nav (mobile sheet)'); }
  await p.setViewportSize({ width: 1440, height: 900 });
});
// The product page's Share popover is a UI toggle too.
await tryDo('share popover', async () => {
  await p.goto('https://ichigo.gumroad.com/l/ichigo-reader', { waitUntil: 'domcontentloaded', timeout: 90000 }); await wait(p, 10000);
  const share = p.locator('button, a').filter({ hasText: /share/i }).filter({ visible: true }).first();
  if (await share.count()) { await share.click({ timeout: 4000 }).catch(() => {}); await wait(p, 1200); await grab(p, 'product (share popover)'); }
});
// Dark-mode icon variants: gumroad paints dark through prefers-color-scheme —
// emulating it is the product's own mechanism. Same geometries, but any svg
// that hard-codes a light colour would surface as a new hash.
await tryDo('dark theme', async () => {
  await p.emulateMedia({ colorScheme: 'dark' }); await wait(p, 1200);
  await open(p, '/'); await closePromo(p); await scrollAll(p, 'dark');
  await p.emulateMedia({ colorScheme: 'light' });
});
await b.close();

// The old set is replaced only after a complete collection, so a run that dies early or loses a page
// cannot leave icons/ emptied or out of step with INDEX.tsv.
if (failed.length || !seen.size) {
  console.error(`not replacing icons/: ${failed.length ? 'failed pages: ' + failed.join(', ') : 'no icons collected'}`);
  process.exit(1);
}
for (const f of fs.readdirSync(OUT)) if (f.endsWith('.svg')) fs.unlinkSync(OUT + f);

const slug = (s) => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 32);
const names = new Map();
try { for (const l of fs.readFileSync(new URL('./icon-names.tsv', import.meta.url), 'utf8').split('\n')) { const [k, n] = l.split('\t'); if (k && n && k !== 'hash') names.set(k, n); } } catch { /* optional */ }
const all = [...seen.values()].sort((a, b) => b.where.size - a.where.size || a.key.localeCompare(b.key));
const count = new Map();
for (const ic of all) {
  const lab = [...ic.labels][0];
  ic.name = names.get(ic.key) || (lab && lab.length <= 24 ? slug(lab) : ic.modCls ? slug(ic.modCls.split('_').slice(1).join('-')) : 'icon-' + ic.key) || 'icon-' + ic.key;
  count.set(ic.name, (count.get(ic.name) || 0) + 1);
}
const rows = [];
for (const ic of all) {
  ic.file = (count.get(ic.name) > 1 ? `${ic.name}-${ic.key}` : ic.name) + '.svg';
  fs.writeFileSync(OUT + ic.file, ic.html.replace(/></g, '>\n<') + '\n');
  rows.push([ic.file, ic.name, ic.key, [...ic.sizes].sort().join(' '), ic.vb || '', ic.strokeOnly ? 'stroke' : 'fill', [...new Set([...ic.where].map((w) => w.replace(/ \(.*\)/, '')))].join('; '), [...ic.places].slice(0, 3).join('; '), [...ic.labels].slice(0, 3).join(' / ')].map((x) => String(x).replace(/\t/g, ' ')).join('\t'));
}
fs.writeFileSync(OUT + 'INDEX.tsv', ['file\tinferred_name\thash\tsizes\tviewBox\tstyle\tseen_on\tplace\ttext_or_label', ...rows].join('\n') + '\n');
console.log(rows.length, 'icons ->', OUT);
