import { afterEach, expect, test } from "vitest";
import { chmod, mkdtemp, readdir, rm, stat } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createClient } from "@libsql/client";
import { pathToFileURL } from "node:url";
import { createResearchStore } from "@/server/db";

const directories: string[] = [];
afterEach(async () => {
  for (const dir of directories.splice(0))
    await rm(dir, { recursive: true, force: true });
});
const mode = async (path: string) => (await stat(path)).mode & 0o777;

test.skipIf(process.platform === "win32")(
  "opening the store makes its directory and database files owner-only",
  async () => {
    const dir = await mkdtemp(join(tmpdir(), "research-perm-"));
    directories.push(dir);
    // An existing, world-readable directory and database, as an older build or
    // a permissive umask leaves them.
    await chmod(dir, 0o755);
    const first = await createResearchStore(dir);
    await first.updateSettings(() => ({ provider: "openai" }));
    first.close();
    for (const name of await readdir(dir)) await chmod(join(dir, name), 0o644);
    await chmod(dir, 0o755);
    const store = await createResearchStore(dir);
    try {
      await store.updateSettings(() => ({ provider: "anthropic" }));
      expect(await mode(dir)).toBe(0o700);
      const files = (await readdir(dir)).filter((name) =>
        name.startsWith("app.db"),
      );
      expect(files).toContain("app.db");
      for (const name of files) expect(await mode(join(dir, name))).toBe(0o600);
    } finally {
      store.close();
    }
  },
);

test.skipIf(process.platform === "win32")(
  "a store that fails to open is still made owner-only",
  async () => {
    const dir = await mkdtemp(join(tmpdir(), "research-perm-"));
    directories.push(dir);
    (await createResearchStore(dir)).close();
    const raw = createClient({ url: pathToFileURL(join(dir, "app.db")).href });
    await raw.execute("PRAGMA user_version = 99");
    raw.close();
    await chmod(join(dir, "app.db"), 0o644);
    await chmod(dir, 0o755);
    await expect(createResearchStore(dir)).rejects.toThrow("newer");
    expect(await mode(dir)).toBe(0o700);
    expect(await mode(join(dir, "app.db"))).toBe(0o600);
  },
);
