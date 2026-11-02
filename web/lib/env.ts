// Loads the repo's root .env (the same file the Python tools read) into
// process.env for keys not already set — Next only auto-loads web/.env.
// Imported for effect by lib/repo.ts, which everything server-side touches.
import { readFileSync, existsSync } from "node:fs";
import path from "node:path";

const cwd = process.cwd();
const root = path.basename(cwd) === "web" ? path.dirname(cwd) : cwd;
const file = path.join(root, ".env");

try {
  if (existsSync(file)) {
    for (const line of readFileSync(file, "utf8").split("\n")) {
      const m = /^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)\s*$/.exec(line);
      if (!m) continue;
      const [, key, raw] = m;
      const val = raw.replace(/^(['"])(.*)\1$/, "$2");
      if (process.env[key] === undefined) process.env[key] = val;
    }
  }
} catch {
  // a missing or unreadable .env just means env-only configuration
}

export {};
