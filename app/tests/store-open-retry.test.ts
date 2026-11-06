import { afterEach, expect, test, vi } from "vitest";
import { mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";

const directories: string[] = [];
afterEach(async () => {
  vi.unstubAllEnvs();
  vi.resetModules();
  for (const dir of directories.splice(0))
    await rm(dir, { recursive: true, force: true });
});

test("getStore retries after a failed open instead of caching the rejection", async () => {
  const parent = await mkdtemp(join(tmpdir(), "research-open-"));
  directories.push(parent);
  // A file where the data directory should be makes mkdir fail.
  const dataDir = join(parent, "data");
  await writeFile(dataDir, "not a directory");
  vi.stubEnv("DESIGN_RESEARCH_DATA_DIR", dataDir);
  vi.resetModules();
  const { getStore } = await import("@/server/db");
  await expect(getStore()).rejects.toThrow();
  await rm(dataDir);
  const store = await getStore();
  try {
    expect(await store.getSettings()).toEqual({});
  } finally {
    store.close();
  }
});
