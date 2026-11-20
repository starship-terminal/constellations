// Collects every distinct inline <svg> icon on Gauth's public pages into icons/ and writes icons/INDEX.tsv.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node icons.mjs
//
// Gauth's icons carry no name in the DOM, so a file is named from icon-names.tsv (geometry hash -> name)
// when the hash is listed there, else from the aria-label or text of the button or link it sits in, else
// from its CSS-module class, else `icon-<hash>`. Files whose geometry matches are one icon, listed once
// with every page and place it was seen. Colour is kept as `currentColor` wherever the computed fill or
// stroke equals the svg's text colour, so each icon recolours from CSS `color` the way it does on the site.
// Adapted from the Coursera kit's icons.mjs.
// PRODUCT (adapt): name the product here once every part marked PRODUCT (adapt) is rewritten
// for it. While this is null the script stops: the kit's copy is Gauth's example and would
// read or write Gauth's values. KIT_EXAMPLE=1 runs the example as it is.
const ADAPTED_FOR = null;
if (!ADAPTED_FOR && !process.env.KIT_EXAMPLE) {
  console.error('icons.mjs is the kit\'s Gauth example, not adapted: rewrite the parts marked PRODUCT (adapt), then set ADAPTED_FOR');
  process.exit(2);
}
import crypto from 'crypto';
import fs from 'fs';
import { fileURLToPath } from 'url';
import { M, BASE, chromium, UA, closePromo, openStory } from './public/lib.mjs'; // the signed-in route: swap in its own page opener
import { scrubConsole } from './no-query.mjs';
scrubConsole();   // logs are committed: no query, from a locator or a page URL, is printed

const OUT = fileURLToPath(new URL('../../icons/', import.meta.url));
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
    if (s.closest('[class*="canvas_board"], [class*="pgc_playerSurface"], hyperframes-player, .katex')) return false; // lesson content, not UI
    return getComputedStyle(s).visibility !== 'hidden';
  }).map((s) => {
    const r = s.getBoundingClientRect(), col = rgb(getComputedStyle(s).color);
    const c = s.cloneNode(true);
    // The paint a shape takes from a class, a style or var() is written onto its copy as attributes, since
    // the copy keeps neither classes nor styles.
    const SHAPES = 'path,circle,rect,line,polyline,polygon,ellipse';
    // Whether an element itself declares a paint property: as an attribute, in its style, or through a
    // stylesheet rule that matches it. Comparing computed values cannot tell a group that sets the sheet's
    // default fill on purpose from a shape that merely inherits it.
    const rules = [];
    const walk = (list) => { for (const r of list) { if (r.selectorText && r.style) rules.push(r); else if (r.cssRules) walk(r.cssRules); } };
    for (const sh of document.styleSheets) { try { walk(sh.cssRules); } catch { /* a cross-origin sheet */ } }
    const declares = (el, prop) => el.hasAttribute(prop) || !!(el.style && el.style.getPropertyValue(prop))
      || (el.hasAttribute('class') || el.id ? rules.some((r) => { try { return r.style.getPropertyValue(prop) && el.matches(r.selectorText); } catch { return false; } }) : false);
    const paintInto = (src, dst, imported = false) => {
      const shapes = [...src.querySelectorAll(SHAPES)], cshapes = [...dst.querySelectorAll(SHAPES)];
      // Set inside the imported target: by the shape or any group up to the target itself.
      const setInside = (e, prop) => { for (let n = e; n; n = n === src ? null : n.parentElement) if (declares(n, prop)) return true; return false; };
      shapes.forEach((e, i) => {
        // A shape in an imported symbol inherits its paint from the <use> that draws it, unless something
        // inside the target sets it: its own class or style, or a group's (whose class and style the copy
        // loses too). Only then is anything written, or the copy could no longer recolour.
        const cs = getComputedStyle(e), t = cshapes[i];
        // a var() in a paint attribute names a property the standalone file will not have: resolve it first
        for (const a of ['fill', 'stroke']) if ((t.getAttribute(a) || '').startsWith('var(')) t.setAttribute(a, rgb(cs[a]) === col ? 'currentColor' : hex(cs[a]));
        // Each paint property is judged on its own: something inside the target must declare it. A group that
        // sets only a stroke leaves the fill to the <use> (copying the sheet's default black fill would turn an
        // outline into a filled shape), one that sets only a width leaves the stroke colour to the <use>, and
        // one that sets the sheet's default fill on purpose keeps it.
        const set = (prop) => !imported || setInside(e, prop);
        const fillSet = set('fill'), strokeSet = set('stroke'), widthSet = set('stroke-width');
        if (fillSet && !t.hasAttribute('fill') && cs.fill !== 'none' && !cs.fill.startsWith('url')) t.setAttribute('fill', rgb(cs.fill) === col ? 'currentColor' : hex(cs.fill));
        else if (fillSet && imported && !t.hasAttribute('fill') && cs.fill === 'none') t.setAttribute('fill', 'none');   // its style goes below
        // a fill the shape names itself, in the icon's own colour, follows that colour when the icon is recoloured
        // (whatever set the stroke: this is the attribute already on the copy, not inherited paint)
        else if (t.getAttribute('fill') && !['none', 'currentColor'].includes(t.getAttribute('fill')) && !t.getAttribute('fill').startsWith('url') && rgb(cs.fill) === col) t.setAttribute('fill', 'currentColor');
        if (!imported) {   // the icon's own shapes: their whole stroke, as computed
          if (!t.hasAttribute('stroke') && cs.stroke !== 'none') {
            t.setAttribute('stroke', rgb(cs.stroke) === col ? 'currentColor' : hex(cs.stroke));
            t.setAttribute('stroke-width', parseFloat(cs.strokeWidth) || 1);
            if (cs.strokeLinecap !== 'butt') t.setAttribute('stroke-linecap', cs.strokeLinecap);
            if (cs.strokeLinejoin !== 'miter') t.setAttribute('stroke-linejoin', cs.strokeLinejoin);
          }
        } else {   // an imported shape: only what the target itself declares, each part apart
          if (strokeSet && !t.hasAttribute('stroke') && cs.stroke !== 'none') t.setAttribute('stroke', rgb(cs.stroke) === col ? 'currentColor' : hex(cs.stroke));
          if (widthSet && !t.hasAttribute('stroke-width')) t.setAttribute('stroke-width', parseFloat(cs.strokeWidth) || 1);
          if (set('stroke-linecap') && !t.hasAttribute('stroke-linecap')) t.setAttribute('stroke-linecap', cs.strokeLinecap);
          if (set('stroke-linejoin') && !t.hasAttribute('stroke-linejoin')) t.setAttribute('stroke-linejoin', cs.strokeLinejoin);
        }
      });
      // A gradient's stops can take their colour from a class or a style the copy will not keep (both are
      // stripped below), which leaves a stop drawing black: the computed stop-color and stop-opacity are
      // written onto each copied stop, unless its own plain attribute already says it.
      const stops = [...src.querySelectorAll('stop')], cstops = [...dst.querySelectorAll('stop')];
      stops.forEach((e, i) => {
        const t = cstops[i];
        const own = t && t.getAttribute('stop-color');
        if (!t || (own && !own.startsWith('var(') && !e.hasAttribute('class') && !e.hasAttribute('style'))) return;
        const cs = getComputedStyle(e);
        const parts = (cs.stopColor.match(/rgba?\(([^)]+)\)/) || [, ''])[1].split(/[,/\s]+/).filter(Boolean);
        const alpha = parts.length > 3 ? parseFloat(parts[3]) : 1;
        t.setAttribute('stop-color', rgb(cs.stopColor) === col ? 'currentColor' : hex(cs.stopColor));
        const op = parseFloat(cs.stopOpacity) * alpha;
        if (op !== 1) t.setAttribute('stop-opacity', +op.toFixed(3));
        else t.removeAttribute('stop-opacity');
      });
    };
    const shapes = [...s.querySelectorAll(SHAPES)];
    paintInto(s, c);
    c.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    for (const a of ['id', 'class', 'focusable', 'aria-hidden', 'aria-labelledby', 'style', 'data-testid']) c.removeAttribute(a);
    // Every id something in the icon points at is kept: url(#x) (masks, gradients, clip paths) and a <use>'s href.
    const refsOf = (html) => new Set([...html.matchAll(/url\((?:&quot;|["'])?#([^)"'&]+)|\b(?:xlink:)?href="#([^"]+)"/g)].map((m) => m[1] || m[2]));
    // A target defined elsewhere on the page (a sprite sheet's symbol, a shared gradient or mask) would leave
    // the standalone icon drawing nothing, so it is copied into the icon's <defs>, painted like the icon's own
    // shapes, and whatever it points at in turn is followed too (the set stops a cycle).
    const imported = new Set();
    for (const pending = [...refsOf(c.outerHTML)]; pending.length;) {
      const id = pending.shift();
      if (imported.has(id) || c.querySelector(`[id="${CSS.escape(id)}"]`)) continue;
      imported.add(id);
      const t = document.getElementById(id);
      if (!t) continue;
      const copy = t.cloneNode(true);
      paintInto(t, copy, true);
      (c.querySelector('defs') || c.insertBefore(document.createElementNS('http://www.w3.org/2000/svg', 'defs'), c.firstChild)).appendChild(copy);
      pending.push(...refsOf(copy.outerHTML));
    }
    // A <use> that points into another file (href="/icons/sprite.svg#x") draws nothing once the icon is
    // saved on its own, and that file is not fetched: the icon is left out, not saved blank (finding 20-8).
    if ([...c.querySelectorAll('use')].some((u) => !/^#/.test(u.getAttribute('href') || u.getAttribute('xlink:href') || '#'))) return null;
    const refs = refsOf(c.outerHTML);
    c.querySelectorAll('[id],[class],[style]').forEach((e) => { if (!refs.has(e.id)) e.removeAttribute('id'); e.removeAttribute('class'); if (e.tagName !== 'mask') e.removeAttribute('style'); });
    c.querySelectorAll('image').forEach((e) => e.remove());
    if (!c.hasAttribute('viewBox')) c.setAttribute('viewBox', `0 0 ${c.getAttribute('width') || Math.round(r.width)} ${c.getAttribute('height') || Math.round(r.height)}`.replace(/px/g, ''));
    if (!c.hasAttribute('width') || /%|em/.test(c.getAttribute('width'))) c.setAttribute('width', Math.round(r.width));
    if (!c.hasAttribute('height') || /%|em/.test(c.getAttribute('height'))) c.setAttribute('height', Math.round(r.height));
    const holder = s.closest('button,a,[role=button],[role=tab],label,li');
    const label = (holder?.getAttribute('aria-label') || s.getAttribute('aria-label') || holder?.innerText || s.parentElement?.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40);
    const modCls = [s, s.parentElement, holder].filter(Boolean).flatMap((e) => [...e.classList].map(String)).map(strip).find((x) => /_/.test(x) && !/^x[0-9a-z]+$/.test(x)) || '';
    const place = (holder ? holder.tagName.toLowerCase() : s.parentElement.tagName.toLowerCase()) + (modCls ? ' ' + modCls : '');
    const strokeOnly = shapes.length && shapes.every((e) => getComputedStyle(e).fill === 'none');
    return { w: Math.round(r.width), h: Math.round(r.height), vb: s.getAttribute('viewBox'), html: c.outerHTML, label, modCls, place, strokeOnly, color: col };
  });
}

const seen = new Map();
async function grab(p, tag) {
  const all = await p.evaluate(collect);
  const list = all.filter(Boolean);   // an icon drawn from another file's sprite comes back null
  let fresh = 0;
  for (const ic of list) {
    const key = crypto.createHash('md5').update(ic.html.replace(/\s(width|height|id)="[^"]*"/g, '').replace(/<(desc|title)>.*?<\/\1>/g, '').replace(/url\(#[^)]*\)/g, '')).digest('hex').slice(0, 8);
    const hit = seen.get(key);
    if (hit) { hit.where.add(tag); hit.sizes.add(`${ic.w}x${ic.h}`); if (ic.label) hit.labels.add(ic.label); hit.places.add(ic.place); continue; }
    fresh++;
    seen.set(key, { ...ic, key, where: new Set([tag]), sizes: new Set([`${ic.w}x${ic.h}`]), labels: new Set(ic.label ? [ic.label] : []), places: new Set([ic.place]) });
  }
  console.log(' ', tag, list.length, 'svgs,', fresh, 'new' + (all.length > list.length ? `, ${all.length - list.length} drawn from another file's sprite left out` : ''));
}
async function scrollAll(p, tag) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 250); await grab(p, tag); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
}
async function open(p, path, w = 6500) {
  await p.goto(BASE + path, { waitUntil: 'load', timeout: 90000 }); await wait(p, w);
}
// A page that fails is recorded, and a run with any failure leaves the committed icons alone.
const failed = [];
async function tryDo(label, fn) { try { await fn(); } catch (e) { failed.push(label); console.log('  skip', label, String(e.message).split('\n')[0]); } }

const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA });
const p = await ctx.newPage();

await open(p, '/');
await grab(p, 'home (promo dialog)');
await closePromo(p);
await scrollAll(p, 'home');
for (const [path, tag] of [['/course/science', 'academy'], ['/course/math', 'academy'], ['/course/my', 'academy'], ['/news', 'news']]) {
  await open(p, path); await closePromo(p); await scrollAll(p, tag);
}
await tryDo('create dialog', async () => { await open(p, '/course/my'); await closePromo(p); await p.locator(M('catalog_createButton')).first().click(); await wait(p, 2000); await grab(p, 'academy (create dialog)'); });
await open(p, '/course/math/algebra-1?unit=real-numbers-and-sets'); await closePromo(p); await grab(p, 'unit');
await tryDo('science lesson', async () => {
  await open(p, '/course/science/how-things-work-1/learn?entry_source=start&from=science', 7000);
  await grab(p, 'lesson-science (audio dialog)');
  const nn = p.getByRole('button', { name: 'Not now' }); if (await nn.count()) await nn.click();
  await wait(p, 1500); await grab(p, 'lesson-science');
  await p.getByRole('button', { name: 'Settings' }).click(); await wait(p, 1000); await grab(p, 'lesson-science (settings)');
  await p.keyboard.press('Escape');
  const pz = p.getByRole('button', { name: 'Pause' }); if (await pz.count()) await pz.click();
  await p.locator('[aria-label="Ask Tutor"]').first().click(); await wait(p, 1200); await grab(p, 'lesson-science (ask tutor)');
});
await tryDo('math lesson', async () => {
  await open(p, '/course/math/algebra-1/fundamentals-of-set-theory/learn?entry_source=start&return_to=course_detail', 8000);
  const c = p.getByRole('button', { name: 'Continue', exact: true }); if (await c.count()) { await c.click(); await wait(p, 3000); }
  await grab(p, 'lesson-math');
  await p.getByRole('button', { name: 'Open lesson chapters' }).click(); await wait(p, 1000); await grab(p, 'lesson-math (chapters)');
});
await tryDo('history lesson', async () => {
  await open(p, '/course/history/crossing-the-ocean-wall/learn?entry_source=start&from=history', 8000);
  await grab(p, 'lesson-history');
  await p.locator(M('lesson_chapterMenuButton')).first().click(); await wait(p, 1000); await grab(p, 'lesson-history (chapters)');
});
await tryDo('atlas', async () => {
  await open(p, '/atlas'); await closePromo(p); await scrollAll(p, 'atlas');
  await openStory(p); await grab(p, 'atlas story');
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
