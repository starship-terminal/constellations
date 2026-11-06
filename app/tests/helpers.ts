// Shared scaffolding for app tests. Importing this module registers one
// afterEach that undoes everything the helpers below set up for a test.
import { afterEach, vi } from "vitest";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createResearchStore, type ResearchStore } from "@/server/db";
import type { LibraryItem } from "@/contracts/library";

const cleanups: (() => unknown)[] = [];
afterEach(async () => {
  vi.unstubAllEnvs();
  for (const cleanUp of cleanups.splice(0).reverse()) await cleanUp();
});

/** A temporary directory, removed after the current test. */
export async function tempDir(prefix = "app-test-"): Promise<string> {
  const dir = await mkdtemp(join(tmpdir(), prefix));
  cleanups.push(() => rm(dir, { recursive: true, force: true }));
  return dir;
}

/** An empty repository root that source reads use for the current test. */
export async function repoFixture(prefix = "app-repo-"): Promise<string> {
  const dir = await tempDir(prefix);
  vi.stubEnv("DESIGN_SYSTEMS_REPO", dir);
  return dir;
}

/** A fresh research store in its own directory, closed after the test. */
export async function tempStore(
  prefix = "app-store-",
): Promise<{ dir: string; store: ResearchStore }> {
  const dir = await tempDir(prefix);
  const store = await createResearchStore(dir);
  cleanups.push(() => store.close());
  return { dir, store };
}

/** A minimal library item; pass only the fields a test cares about. */
export function libraryItem(
  slug: string,
  extra: Partial<LibraryItem> = {},
): LibraryItem {
  const source = extra.source ?? "systems";
  return {
    id: `${source}:${slug}`,
    source,
    slug,
    name: slug,
    description: "",
    platform: "web",
    themes: [],
    tags: [],
    category: "",
    image: null,
    icon: null,
    video: null,
    evidence: source === "systems" ? "measured" : "interpreted",
    captured: null,
    ...extra,
  };
}

export const appOrigin = "http://localhost:8845";

/** A JSON request from the app's own origin, as the browser sends it. */
export function jsonRequest(
  path: string,
  method: string,
  body?: unknown,
  headers: Record<string, string> = {},
): Request {
  return new Request(`${appOrigin}${path}`, {
    method,
    headers: {
      origin: appOrigin,
      "content-type": "application/json",
      ...headers,
    },
    ...(body === undefined ? {} : { body: JSON.stringify(body) }),
  });
}
