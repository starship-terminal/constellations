// PRODUCT (adapt): read the notes of Capy's component gallery (capy://app/design). Each section is an h2 over
// cards of rows, a row being a label and a one-line note on what the specimen beside it shows ("Shape: A rounded
// square, never a circle"); captions sit over free-form specimens. This is the product's own guidance, published in
// the app bundle, and the evidence for components.md's notes and the scorecard's optional C5.
//
//   PORT=9407 node tools/capture/electron/gallery.mjs raw/design-gallery.json
import { connect, disconnect, writeJson } from './cdp.mjs';
import * as P from './product.mjs';

const out = process.argv[2];
if (!out) { console.error('usage: gallery.mjs <out.json>'); process.exit(2); }
const h = await connect(P.WINDOWS.app);
try {
  const { page } = h;
  if (await page.evaluate(() => location.pathname) !== '/design') { await page.goto('capy://app/design'); await page.waitForTimeout(2500); }
  const data = await page.evaluate(() => {
    const clean = s => (s || '').replace(/\s+/g, ' ').trim();
    const sections = [];
    for (const h2 of document.querySelectorAll('section > h2')) {
      const sec = h2.parentElement, notes = [];
      for (const row of sec.querySelectorAll('[data-slot=settings-row]')) {
        const label = row.querySelector('div.text-sm.font-medium'), note = row.querySelector('div.font-normal.text-muted-foreground-2');
        if (label) notes.push({ label: clean(label.textContent), note: note ? clean(note.textContent) : '' });
      }
      for (const cap of sec.querySelectorAll('span.text-xs.text-muted-foreground-2, span.text-2xs.text-muted-foreground-3')) {
        const t = clean(cap.textContent);
        if (t && t.length > 3) notes.push({ caption: t });
      }
      sections.push({ section: clean(h2.textContent), notes });
    }
    const title = document.querySelector('h1'), lede = title && title.parentElement.querySelector('p');
    return { title: clean(title && title.textContent), lede: clean(lede && lede.textContent), sections };
  });
  writeJson(out, { meta: { read: new Date().toISOString().slice(0, 10), url: 'capy://app/design' }, ...data });
  console.log(out, data.sections.length, 'sections', data.sections.reduce((n, s) => n + s.notes.length, 0), 'notes');
} finally {
  await disconnect(h.browser);
}
