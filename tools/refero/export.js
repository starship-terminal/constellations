// Batch-export Refero style artifacts using their own generators.
// Usage: node export.js <jobs.json>
//   jobs.json: [{ "uuid": "...", "slug": "...", "resultPath": "...", "outDir": "..." }]
// Writes variables.css, theme.css, tokens.json, design-system.json into each
// outDir, and appends one line per style to <jobs.json>.artifacts.jsonl holding
// every generated artifact (including raw-result.json and prompt.txt) so the
// caller can store them in the database.
const fs = require('fs');
const path = require('path');
const g = require('./generators.js');

const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = fs.createWriteStream(process.argv[2] + '.artifacts.jsonl');

let ok = 0, failed = 0;
for (const job of jobs) {
  try {
    const result = JSON.parse(fs.readFileSync(job.resultPath, 'utf8'));
    const artifacts = {
      'variables.css': g.generateCssVariables(result, 'compact'),
      'theme.css': g.generateTailwindConfig(result, 'compact'),
      'tokens.json': g.generateTokensJson(result, 'compact'),
      'design-system.json': g.generateDesignJson(result),
      'raw-result.json': g.generateRawResultJson(result),
      'prompt.txt': g.generatePromptSnapshotText(result),
    };
    fs.mkdirSync(job.outDir, { recursive: true });
    for (const [fn, content] of Object.entries(artifacts)) {
      if (fn === 'raw-result.json' || fn === 'prompt.txt') continue; // db-only
      fs.writeFileSync(path.join(job.outDir, fn), content);
    }
    out.write(JSON.stringify({ uuid: job.uuid, slug: job.slug, artifacts }) + '\n');
    ok++;
  } catch (err) {
    out.write(JSON.stringify({ uuid: job.uuid, slug: job.slug, error: String(err) }) + '\n');
    failed++;
  }
}
out.end(() => console.log(`exported ${ok}, failed ${failed}`));
