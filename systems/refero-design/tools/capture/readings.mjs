// Updates a JSON file of per-page readings in place: each job that succeeds replaces its own key, and
// every other key, from pages this run skipped or failed to read, keeps its saved value. Browser-free
// so it can be tested (test_readings.mjs).
import fs from 'node:fs';
import path from 'node:path';

// jobs: [key, async () => reading] pairs, run one after another. Returns the merged object.
export async function updateReadings(file, jobs, log = console.log) {
  const res = fs.existsSync(file) ? JSON.parse(fs.readFileSync(file, 'utf8')) : {};
  for (const [key, read] of jobs) {
    try {
      res[key] = await read();
      log(key);
    } catch (e) {
      log('failed', key, String(e.message || e).split('\n')[0]);
    }
  }
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, JSON.stringify(res, null, 1) + '\n');
  return res;
}
