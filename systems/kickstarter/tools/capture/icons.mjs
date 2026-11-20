// Collect inline SVG icons from Kickstarter's public pages.
// PLAYWRIGHT=... node tools/capture/icons.mjs
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launchBrowser, newContext, open } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.resolve(here, '..', '..', 'icons');
fs.mkdirSync(OUT, { recursive: true });

function collect() {
  const rgb = (c) => {
    const m = String(c).match(/rgba?\(([^)]+)\)/);
    return m ? m[1].split(',').slice(0, 3).map((x) => Math.round(parseFloat(x))).join(',') : c;
  };
  return [...document.querySelectorAll('svg')].filter((s) => {
    const r = s.getBoundingClientRect();
    if (r.width < 10 || r.width > 48 || r.height < 10 || r.height > 48) return false;
    if (getComputedStyle(s).visibility === 'hidden' || getComputedStyle(s).display === 'none') return false;
    return true;
  }).slice(0, 80).map((s) => {
    const r = s.getBoundingClientRect();
    const c = s.cloneNode(true);
    c.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    for (const a of ['id', 'class', 'style']) c.removeAttribute(a);
    if (!c.getAttribute('viewBox')) c.setAttribute('viewBox', `0 0 ${Math.round(r.width)} ${Math.round(r.height)}`);
    c.setAttribute('width', '24');
    c.setAttribute('height', '24');
    const holder = s.closest('button, a, [role="button"]');
    const label = (holder?.getAttribute('aria-label') || s.getAttribute('aria-label') || holder?.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40);
    return { html: c.outerHTML, label, w: Math.round(r.width), h: Math.round(r.height) };
  });
}

const seen = new Map();
const browser = await launchBrowser();
const routes = [
  ['/', 'home'],
  ['/discover?ref=nav', 'discover'],
  ['/projects/shirtaloon/hwfwm', 'project'],
  ['/login', 'login'],
];
const failed = [];
for (const [route, tag] of routes) {
  const ctx = await newContext(browser, { dpr: 1 });
  const page = await ctx.newPage();
  let list;
  try {
    if (!(await open(page, BASE + route, { wait: 1200 }))) throw new Error('page did not open (challenge or timeout)');
    list = await page.evaluate(collect);
  } catch (e) {
    console.log(tag, 'FAILED', String(e.message || e).split('\n')[0]);
    failed.push(tag);
    await ctx.close();
    continue;
  }
  let fresh = 0;
  for (const ic of list) {
    const key = crypto.createHash('md5').update(ic.html.replace(/\s(width|height)="[^"]*"/g, '')).digest('hex').slice(0, 8);
    if (seen.has(key)) { seen.get(key).where.add(tag); if (ic.label) seen.get(key).labels.add(ic.label); continue; }
    fresh++;
    seen.set(key, { ...ic, key, where: new Set([tag]), labels: new Set(ic.label ? [ic.label] : []) });
  }
  console.log(tag, list.length, 'svgs', fresh, 'new');
  await ctx.close();
}

await browser.close();

// The old set is replaced only after a complete collection (the kit's rule), so a run that dies
// early or loses a page cannot leave icons/ emptied, stale or out of step with INDEX.tsv.
if (failed.length || !seen.size) {
  console.error(`not replacing icons/: ${failed.length ? 'failed pages: ' + failed.join(', ') : 'no icons collected'}`);
  process.exit(1);
}
// The new set is written into a sibling folder first and swapped in only once it is complete, so
// a write that fails part-way leaves the old icons/ and its INDEX.tsv untouched.
const NEXT = OUT + '.next';
fs.rmSync(NEXT, { recursive: true, force: true });
fs.mkdirSync(NEXT, { recursive: true });

const slug = (s) => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 32) || 'icon';
const used = new Set();
const rows = ['file\trole\twhere'];
let i = 0;
for (const ic of seen.values()) {
  i++;
  const label = [...ic.labels][0] || '';
  let name = slug(label) || ('icon-' + ic.key);
  if (used.has(name)) name = name + '-' + ic.key;
  used.add(name);
  fs.writeFileSync(path.join(NEXT, name + '.svg'), ic.html + '\n');
  rows.push(`${name}.svg\t${label || 'unlabelled'}\t${[...ic.where].join(',')}`);
  if (i >= 40) break;
}
fs.writeFileSync(path.join(NEXT, 'INDEX.tsv'), rows.join('\n') + '\n');
const OLD = OUT + '.old';
fs.rmSync(OLD, { recursive: true, force: true });
fs.renameSync(OUT, OLD);
fs.renameSync(NEXT, OUT);
fs.rmSync(OLD, { recursive: true, force: true });
console.log('wrote', i, 'icons');
