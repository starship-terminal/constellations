// Turns raw/components-computed.json into raw/measurements.md.
import fs from 'node:fs';
import path from 'node:path';
import { RAW } from './lib.mjs';

const src = path.join(RAW, 'components-computed.json');
const data = JSON.parse(fs.readFileSync(src, 'utf8'));
const lines = [];
const W = (s) => lines.push(s);
W('# Component measurements');
W('');
W('Hello Klean, measured from helloklean.com on ' + (data.captured || '').slice(0, 10) + '.');
W('Public signed-out pages only. Hover is a real mouse move. Focus is a real focus. Pressed states were not forced. Nothing was submitted or bought.');
W('');
W('## Pages');
W('');
for (const [name, page] of Object.entries(data.pages || {})) W(`- ${name}: ${page.title} (${page.url})`);
W('');
W('## Components');
W('');
for (const [name, comp] of Object.entries(data.components || {})) {
  W(`### ${name}`);
  W('');
  if (comp.missing) { W(`Not present in the measured DOM: ${comp.reason}.`); W(''); continue; }
  const d = comp.states?.default;
  if (!d) { W('No default reading.'); W(''); continue; }
  const s = d.style || {};
  W(`- page: ${comp.page}`);
  W(`- text: ${(d.text || '').replace(/\|/g, '/')}`);
  W(`- size: ${d.rect?.w} x ${d.rect?.h}`);
  W(`- font: ${s.fontFamily} ${s.fontSize} / ${s.lineHeight} weight ${s.fontWeight}`);
  W(`- color: ${s.color} on ${s.backgroundColor}`);
  W(`- radius: ${s.borderTopLeftRadius}`);
  W(`- padding: ${s.paddingTop} ${s.paddingRight} ${s.paddingBottom} ${s.paddingLeft}`);
  const h = comp.states.hover?.style;
  if (h && (h.backgroundColor !== s.backgroundColor || h.color !== s.color)) W(`- hover: ${h.color} on ${h.backgroundColor}`);
  W('');
}
fs.writeFileSync(path.join(RAW, 'measurements.md'), lines.join('\n'));
console.log('wrote measurements.md', lines.length, 'lines');
