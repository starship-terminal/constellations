// Writes raw/measurements.md from components-computed.json.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const raw = path.resolve(here, '..', '..', '..', 'raw');
const j = JSON.parse(fs.readFileSync(path.join(raw, 'components-computed.json'), 'utf8'));
const lines = ['# Measurements', '', 'Computed styles from public tilda.cc pages on 2026-11-21. Login and registration fields were not filled.', ''];
for (const [name, c] of Object.entries(j.components)) {
  lines.push(`## ${name}`, '', `Page: ${c.page || ''}`, '');
  for (const [state, s] of Object.entries(c.states || {})) {
    const st = s.style || {};
    lines.push(`- ${state}: ${s.tag} ${st.fontSize || ''} / ${st.fontWeight || ''} ${st.color || ''} on ${st.backgroundColor || ''} radius ${st.borderTopLeftRadius || ''} pad ${st.paddingTop || ''} ${st.paddingRight || ''}`);
  }
  lines.push('');
}
fs.writeFileSync(path.join(raw, 'measurements.md'), lines.join('\n'));
console.log('wrote measurements', Object.keys(j.components).length);
