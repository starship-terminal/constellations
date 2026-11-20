// Replace a folder's generated files (icons/*.svg and INDEX.tsv) only after the
// whole new set is on disk.
//
// Every new file is first written into a scratch folder beside the target. If a
// write fails there, the target is untouched. Only then are the new files moved
// in (a rename on the same filesystem), old SVGs the new set no longer holds are
// removed, and INDEX.tsv moves last, so it never lists a file that is not there.
import fs from 'node:fs';
import path from 'node:path';

export function replaceSet(dir, files, indexText, { indexName = 'INDEX.tsv', ext = '.svg' } = {}) {
  fs.mkdirSync(dir, { recursive: true });
  const scratch = fs.mkdtempSync(path.join(path.dirname(path.resolve(dir)), `.${path.basename(path.resolve(dir))}-new-`));
  try {
    for (const [name, body] of files) fs.writeFileSync(path.join(scratch, name), body);
    fs.writeFileSync(path.join(scratch, indexName), indexText);
  } catch (e) {
    fs.rmSync(scratch, { recursive: true, force: true });
    throw e;
  }
  const keep = new Set(files.keys ? [...files.keys()] : files.map(([n]) => n));
  for (const name of keep) fs.renameSync(path.join(scratch, name), path.join(dir, name));
  for (const f of fs.readdirSync(dir)) if (f.endsWith(ext) && !keep.has(f)) fs.unlinkSync(path.join(dir, f));
  fs.renameSync(path.join(scratch, indexName), path.join(dir, indexName));
  fs.rmSync(scratch, { recursive: true, force: true });
}
