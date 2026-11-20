// Collects every distinct inline <svg> icon on hitchd.com's public pages
// into icons/ and writes icons/INDEX.tsv.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/icons.mjs
//
// hitchd's own icons are mostly inline SVGs in the Angular apps and a few
// linked SVGs on marketing pages (the wordmark is an <img>). Icons carry no
// name in the DOM, so a file is named from icon-names.tsv (geometry hash ->
// name); unnamed glyphs land in icons/unnamed/ keyed by geometry hash —
// nothing is invented. Linked <img>/<use> URLs are recorded in the TSV, not
// fetched, since asset URLs can carry signed tokens.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { BASE, UA, launch, patch, clearChallenge, closePromo, openRegistry } from './public/lib.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ICONS = path.resolve(HERE, '..', '..', 'icons');
const UNNAMED = path.join(ICONS, 'unnamed');
fs.mkdirSync(UNNAMED, { recursive: true });

const NAMES = {};
const nameFile = path.join(ICONS, 'icon-names.tsv');
if (fs.existsSync(nameFile)) for (const l of fs.readFileSync(nameFile, 'utf8').split('\n')) { const [h, n] = l.split('\t'); if (h && n) NAMES[h] = n; }

const { browser } = await launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA });
await patch(ctx);
const p = await ctx.newPage();
const wait = (ms) => p.waitForTimeout(ms);
const seen = new Map(); // hash -> {name, files}
const rows = [];

async function grab(page, tag) {
  const svgs = await page.evaluate(() => [...document.querySelectorAll('svg')].filter((s) => s.getBoundingClientRect().width > 0).map((s) => ({ html: s.outerHTML, w: +s.getBoundingClientRect().width.toFixed(1), h: +s.getBoundingClientRect().height.toFixed(1), inLink: !!s.closest('a,button'), label: s.closest('a,button')?.getAttribute('aria-label') || s.getAttribute('aria-label') || '' })));
  const imgs = await page.evaluate(() => [...document.querySelectorAll('img[src$=".svg"], img[src*=".svg?"]')].map((i) => i.currentSrc || i.src));
  for (const u of new Set(imgs)) rows.push(['linked', tag, u.split('?')[0]]);
  for (const s of svgs) {
    const hash = crypto.createHash('sha1').update(s.html.replace(/satori|ng-star-inserted|_ng[a-z-]+|class="[^"]*"/g, '')).digest('hex').slice(0, 10);
    if (seen.has(hash)) { seen.get(hash).where.add(tag); continue; }
    const name = NAMES[hash] || null;
    const file = name ? `${name}.svg` : `unnamed/${hash}.svg`;
    fs.writeFileSync(path.join(ICONS, file), s.html + '\n');
    seen.set(hash, { name, file, w: s.w, h: s.h, where: new Set([tag]), label: s.label });
  }
}

const tryDo = async (label, fn) => { try { await fn(); } catch (e) { console.log('FAIL', label, String(e.message).split('\n')[0]); } };

for (const [path_, tag] of [['/', 'home'], ['/blog', 'blog'], ['/blog/what-is-a-honeymoon-registry', 'post'], ['/terms', 'terms'], ['/trips/australia', 'trips'], ['/guides/add-hitchd-to-knot-wedding-webiste', 'guide'], ['/login', 'login'], ['/signup', 'signup'], ['/forgot-password', 'forgot'], ['/zoeandnoah', 'registry'], ['/avaandbenjamin', 'coming-soon']]) {
  await tryDo(tag, async () => {
    await p.goto(BASE + path_, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { console.log('blocked', tag); return; }
    await wait(7000); await closePromo(p);
    await grab(p, tag);
  });
}
// gift modal icons: opened by the card's own tap, read at rest — the same
// painted-wait, tile and hit-target as measure.mjs (a bare div click can land
// on a child that swallows the event), and nothing is saved when the modal
// never opens
await tryDo('gift-modal', async () => {
  if (!(await openRegistry(p))) { console.log('blocked gift-modal: registry never painted'); return; }
  const card = p.locator('ol.gift-list .giftz:visible').filter({ hasText: /Accommodation|Airbnb|Seafood|Dinner|Lessons|Tour|Road Trip/ }).first();
  const target = (await card.count()) ? card : p.locator('ol.gift-list .giftz:visible').first();
  if (!(await target.count())) { console.log('blocked gift-modal: no gift tile'); return; }
  await target.scrollIntoViewIfNeeded();
  await target.locator('.click-space, .view-gift').first().click({ timeout: 8000 }).catch(() => {});
  await wait(5000);
  if (!(await p.locator('.gift-modal:visible, .modalDialog:visible').count())) { console.log('blocked gift-modal: modal did not open'); await p.goBack().catch(() => {}); return; }
  await grab(p, 'gift-modal');
});
await browser.close();

const lines = ['file\tname\tw x h\tseen_on\tcontext'];
for (const [hash, s] of [...seen.entries()].sort((a, b) => (a[1].name || '~' + a[0]).localeCompare(b[1].name || '~' + b[0])))
  lines.push(`${s.file}\t${s.name || ''}\t${s.w} x ${s.h}\t${[...s.where].join(', ')}\t${s.label || ''}`);
for (const r of rows) lines.push(r.join('\t'));
fs.writeFileSync(path.join(ICONS, 'INDEX.tsv'), lines.join('\n') + '\n');
console.log(`icons: ${seen.size} distinct (${[...seen.values()].filter((s) => s.name).length} named), ${rows.length} linked svg refs`);
