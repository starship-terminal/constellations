// Indexes NotebookLM's icons by role from the page copies and writes icons/INDEX.tsv.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir of page copies> node tools/capture/icons.mjs
//
// NotebookLM draws every icon with a ligature font: a <mat-icon> whose text is the glyph's name
// (`add_2`, `more_vert`), set in Luminous Symbols with Google Symbols and Material Symbols Outlined
// as fallbacks. So an icon is fully named by its ligature, its size and its fill axis, and no
// outline is extracted (Luminous Symbols is not published with a licence; Material Symbols, the
// declared fallback, is Apache 2.0 and draws the same names). Each copy is opened headless and
// every visible mat-icon is read: ligature, rendered size, colour role, and the label of the
// control around it (aria-label, else the visible text of its button, tab or menu item). Rows
// whose text is the owner's own titles (sources, notebooks, outputs) contribute only the icon,
// never the title. One row per ligature, with every role and size it was seen at.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, REF, SNAPS, metaOf, newContext, openSnap } from './signed-in/lib.mjs';

if (!SNAPS) { console.error('SNAPS=<dir of page copies> is required'); process.exit(2); }
const LABELS = fs.readdirSync(SNAPS).filter((f) => f.endsWith('.json')).map((f) => f.slice(0, -5)).filter((l) => fs.existsSync(path.join(SNAPS, `${l}.html`))).sort();
const browser = await chromium.launch();
const seen = new Map();
for (const label of LABELS) {
  const meta = metaOf(label);
  const ctx = await newContext(browser, meta);
  const page = await openSnap(ctx, label);
  const rows = await page.evaluate(() => {
    const clean = (s) => (s || '').replace(/\s+/g, ' ').trim().slice(0, 50);
    const out = [];
    for (const i of document.querySelectorAll('mat-icon')) {
      const r = i.getBoundingClientRect();
      if (r.width < 1 || r.height < 1) continue;
      const cs = getComputedStyle(i);
      if (cs.visibility !== 'visible') continue;
      const name = clean(i.textContent || i.getAttribute('fonticon') || i.getAttribute('data-mat-icon-name'));
      if (!name || !/^[a-z0-9_]+$/.test(name)) continue;
      const host = i.closest('button, a, [role=tab], [role=menuitem], [role=option], [role=radio]');
      const private_ = i.closest('.single-source-container, project-button, .artifact-item-button, tr.mat-mdc-row');
      let role = host ? clean(host.getAttribute('aria-label') || [...host.childNodes].map((n) => (n.nodeType === 3 ? n.nodeValue : n.tagName === 'MAT-ICON' ? '' : n.innerText || '')).join(' ')) : '';
      if (private_ && !(host && host.getAttribute('aria-label') && !/Sample/.test(host.getAttribute('aria-label')))) role = private_.matches('.single-source-container') ? 'source type (row)' : private_.matches('.artifact-item-button') ? 'Studio output type (row)' : 'notebook row';
      if (/Sample/.test(role)) role = '';
      const where = i.closest('section.source-panel') ? 'Sources panel' : i.closest('section.studio-panel') ? 'Studio panel' : i.closest('section.chat-panel') ? 'Chat' : i.closest('[role=dialog]') ? 'dialog' : i.closest('[role=menu]') ? 'menu' : i.closest('page-header, header, .notebook-header') ? 'header' : 'page';
      const fill = (cs.fontVariationSettings.match(/"FILL" ([\d.]+)/) || [])[1] || '0';
      out.push({ name, size: Math.round(r.width) + 'px', role, where, fill, font: cs.fontFamily.split(',')[0].replace(/"/g, '') });
    }
    return out;
  });
  for (const r of rows) {
    const e = seen.get(r.name) || { sizes: new Set(), roles: new Set(), where: new Set(), fills: new Set(), font: r.font, copies: new Set() };
    e.sizes.add(r.size); if (r.role) e.roles.add(r.role); e.where.add(r.where); e.fills.add(r.fill); e.copies.add(label);
    seen.set(r.name, e);
  }
  await ctx.close();
}
await browser.close();
const OUT = path.join(REF, 'icons');
fs.mkdirSync(OUT, { recursive: true });
const lines = ['# ligature\trole (the control it labels)\twhere\tsizes\tfill\tfont\tseen in'];
for (const [name, e] of [...seen].sort((a, b) => a[0].localeCompare(b[0]))) {
  lines.push([name, [...e.roles].slice(0, 4).join('; ') || '(decorative)', [...e.where].join(', '), [...e.sizes].sort().join(', '), [...e.fills].join(', '), e.font, [...e.copies].slice(0, 3).join(', ')].join('\t'));
}
fs.writeFileSync(path.join(OUT, 'INDEX.tsv'), lines.join('\n') + '\n');
console.log('icons', seen.size);
