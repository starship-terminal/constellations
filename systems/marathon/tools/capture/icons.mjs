// Collects distinct inline SVGs on Marathon's public pages into icons/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/icons.mjs
//
// Public signed-out only. Nothing is submitted. Sign-in and register redirect home.
import crypto from 'crypto';
import fs from 'fs';
import { BASE, UA, chromium, hideConsent } from './public/lib.mjs';
import { fragmentRefs } from './svg_refs.mjs';

const OUT = new URL('../../icons/', import.meta.url).pathname;
fs.mkdirSync(OUT, { recursive: true });
const wait = (p, ms) => p.waitForTimeout(ms);

// `fragmentRefs` is svg_refs.mjs's function, passed in as source by grab() below.
function collect(fragmentRefs) {
  const rgb = (c) => { const m = String(c).match(/rgba?\(([^)]+)\)/); return m ? m[1].split(',').slice(0, 3).map((x) => Math.round(parseFloat(x))).join(',') : c; };
  const hex = (c) => { const m = String(c).match(/rgba?\(([^)]+)\)/); if (!m) return c; const [r, g, b] = m[1].split(',').map((x) => Math.round(parseFloat(x))); return '#' + [r, g, b].map((v) => v.toString(16).padStart(2, '0')).join(''); };
  return [...document.querySelectorAll('svg')].filter((s) => {
    const r = s.getBoundingClientRect();
    if (!(r.width >= 8 && r.width <= 80 && r.height >= 8 && r.height <= 80) || s.closest('svg svg')) return false;
    return getComputedStyle(s).visibility !== 'hidden' && r.width > 0;
  }).map((s) => {
    const r = s.getBoundingClientRect(), col = rgb(getComputedStyle(s).color);
    const c = s.cloneNode(true);
    const shapes = [...s.querySelectorAll('path,circle,rect,line,polyline,polygon,ellipse')], cshapes = [...c.querySelectorAll('path,circle,rect,line,polyline,polygon,ellipse')];
    shapes.forEach((e, i) => {
      const cs = getComputedStyle(e), t = cshapes[i];
      for (const a of ['fill', 'stroke']) if ((t.getAttribute(a) || '').startsWith('var(')) t.setAttribute(a, rgb(cs[a]) === col ? 'currentColor' : hex(cs[a]));
      if (!t.hasAttribute('fill') && cs.fill !== 'none' && !String(cs.fill).startsWith('url')) t.setAttribute('fill', rgb(cs.fill) === col ? 'currentColor' : hex(cs.fill));
    });
    c.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    for (const a of ['id', 'class', 'focusable', 'aria-hidden', 'aria-labelledby', 'style', 'data-testid']) c.removeAttribute(a);
    // The kit's child sanitiser: ids nothing references, classes, inline styles and raster <image>
    // go, and so do scripts, event handlers and any href or src that is not a fragment.
    // Kept ids are those url(#id), href="#id" or xlink:href="#id" name, so <use> keeps its target.
    const refs = fragmentRefs(c.outerHTML);
    c.querySelectorAll('[id],[class],[style]').forEach((e) => { if (!refs.has(e.id)) e.removeAttribute('id'); e.removeAttribute('class'); if (e.tagName !== 'mask') e.removeAttribute('style'); });
    c.querySelectorAll('image, script, foreignObject').forEach((e) => e.remove());
    for (const e of [c, ...c.querySelectorAll('*')]) {
      for (const a of [...e.attributes]) {
        if (/^on/i.test(a.name) || (/^(href|xlink:href|src)$/i.test(a.name) && !a.value.startsWith('#'))) e.removeAttribute(a.name);
      }
    }
    if (!c.hasAttribute('viewBox')) c.setAttribute('viewBox', `0 0 ${Math.round(r.width)} ${Math.round(r.height)}`);
    c.setAttribute('width', Math.round(r.width));
    c.setAttribute('height', Math.round(r.height));
    const holder = s.closest('button,a,[role=button],header');
    const inHeader = !!s.closest('header');
    const label = inHeader ? 'wordmark' : (holder?.getAttribute('aria-label') || s.getAttribute('aria-label') || holder?.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40);
    return { w: Math.round(r.width), h: Math.round(r.height), vb: s.getAttribute('viewBox'), html: c.outerHTML, label, place: holder ? holder.tagName.toLowerCase() : 'svg' };
  });
}

const seen = new Map();
async function grab(p, tag) {
  // One string expression, so the page gets collect and fragmentRefs together without eval.
  const list = await p.evaluate(`(${collect})(${fragmentRefs})`);
  let fresh = 0;
  for (const ic of list) {
    const key = crypto.createHash('md5').update(ic.html.replace(/\s(width|height)="[^"]*"/g, '')).digest('hex').slice(0, 8);
    const hit = seen.get(key);
    if (hit) { hit.where.add(tag); hit.sizes.add(`${ic.w}x${ic.h}`); if (ic.label) hit.labels.add(ic.label); continue; }
    fresh++;
    seen.set(key, { ...ic, key, where: new Set([tag]), sizes: new Set([`${ic.w}x${ic.h}`]), labels: new Set(ic.label ? [ic.label] : []) });
  }
  console.log(' ', tag, list.length, 'svgs,', fresh, 'new');
}

const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA });
const p = await ctx.newPage();
// A page that fails to load throws here, before icons/ is touched: the old set is replaced only
// after every page was collected.
for (const path of ['/', '/for-agencies', '/pricing', '/demo', '/curated']) {
  await p.goto(BASE + path, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await hideConsent(p);
  await wait(p, 1500);
  await grab(p, path);
}
await b.close();

if (!seen.size) {
  console.error('no icons collected');
  process.exit(1);
}
for (const f of fs.readdirSync(OUT)) if (f.endsWith('.svg')) fs.unlinkSync(OUT + f);

const slug = (s) => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 32) || 'icon';
const all = [...seen.values()].sort((a, b) => a.key.localeCompare(b.key));
const count = new Map();
for (const ic of all) {
  const lab = [...ic.labels][0];
  ic.name = lab ? slug(lab) : 'icon-' + ic.key;
  count.set(ic.name, (count.get(ic.name) || 0) + 1);
}
const rows = [];
for (const ic of all) {
  ic.file = (count.get(ic.name) > 1 ? `${ic.name}-${ic.key}` : ic.name) + '.svg';
  fs.writeFileSync(OUT + ic.file, ic.html.replace(/></g, '>\n<') + '\n');
  rows.push([ic.file, ic.name, ic.key, [...ic.sizes].join(' '), ic.vb || '', [...ic.where].join('; '), [...ic.labels].join(' / ')].join('\t'));
}
fs.writeFileSync(OUT + 'INDEX.tsv', ['file\tinferred_name\thash\tsizes\tviewBox\tseen_on\ttext_or_label', ...rows].join('\n') + '\n');
console.log(rows.length, 'icons ->', OUT);
