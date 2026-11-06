import { afterEach, expect, test } from "vitest";
import { promises as fs } from "node:fs";
import os from "node:os";
import path from "node:path";
import { GET as library } from "@/app/api/library/route";
import { GET as screens } from "@/app/api/library/screens/route";
import { parsePagination } from "@/server/sources/pagination";

const originalRepo = process.env.DESIGN_SYSTEMS_REPO;
const dirs: string[] = [];
afterEach(async () => {
  if (originalRepo === undefined) delete process.env.DESIGN_SYSTEMS_REPO;
  else process.env.DESIGN_SYSTEMS_REPO = originalRepo;
  await Promise.all(
    dirs.splice(0).map((dir) => fs.rm(dir, { recursive: true, force: true })),
  );
});
async function fixture() {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), "library-pages-"));
  dirs.push(root);
  process.env.DESIGN_SYSTEMS_REPO = root;
  await fs.writeFile(
    path.join(root, "catalog.json"),
    JSON.stringify({
      systems: ["alpha", "beta", "gamma"].map((slug) => ({
        slug,
        name: slug,
        platform: "web",
      })),
    }),
  );
}
const parse = (query: string) =>
  parsePagination(new URLSearchParams(query), { limit: 60, maxLimit: 200 });

test("one pagination rule: defaults, clamping and invalid values", () => {
  expect(parse("")).toEqual({ limit: 60, offset: 0 });
  expect(parse("limit=500&offset=3")).toEqual({ limit: 200, offset: 3 });
  for (const bad of [
    "limit=",
    "limit=%20",
    "limit=-1",
    "limit=1.5",
    "limit=abc",
    "offset=1e20",
    "limit=1e400",
  ])
    expect(parse(bad), bad).toBeNull();
});

test("library and screens routes answer the same pagination with the same status", async () => {
  await fixture();
  const page = await library(
    new Request("http://localhost/api/library?limit=2&offset=1"),
  );
  expect(page.status).toBe(200);
  const body = await page.json();
  expect(body.total).toBe(3);
  expect(body.items.map((item: { slug: string }) => item.slug)).toEqual([
    "beta",
    "gamma",
  ]);
  for (const query of ["limit=", "offset=1e20", "limit=-1", "limit=2.5"]) {
    const [a, b] = await Promise.all([
      library(new Request(`http://localhost/api/library?${query}`)),
      screens(new Request(`http://localhost/api/library/screens?${query}`)),
    ]);
    expect([a.status, b.status], query).toEqual([400, 400]);
  }
  expect(
    (await library(new Request("http://localhost/api/library?source=web")))
      .status,
  ).toBe(400);
});
