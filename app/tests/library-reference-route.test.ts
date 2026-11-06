import { expect, test } from "vitest";
import { writeFile } from "node:fs/promises";
import { join } from "node:path";
import { GET } from "@/app/api/library/[source]/[slug]/route";
import { repoFixture } from "./helpers";

const call = (source: string, slug: string) =>
  GET(new Request(`http://localhost/api/library/${source}/${slug}`), {
    params: Promise.resolve({ source, slug }),
  });

test("an unknown source, bad slug or missing reference is a 404", async () => {
  const repo = await repoFixture();
  await writeFile(
    join(repo, "catalog.json"),
    JSON.stringify({ systems: [{ slug: "demo", name: "Demo" }] }),
  );
  const cases: [string, string][] = [
    ["unknown", "demo"],
    ["systems", "missing"],
    ["systems", ".."],
    ["systems", "../refero/x"],
    ["..", "demo"],
    ["systems:demo", "x"],
    ["refero", "-bad"],
    ["", ""],
  ];
  for (const [source, slug] of cases) {
    const response = await call(source, slug);
    expect(response.status, `${source}/${slug}`).toBe(404);
    expect(await response.json()).toEqual({ error: "Reference not found" });
  }
});

test("a known reference is served with its details", async () => {
  const repo = await repoFixture();
  await writeFile(
    join(repo, "catalog.json"),
    JSON.stringify({ systems: [{ slug: "demo", name: "Demo" }] }),
  );
  const response = await call("systems", "demo");
  expect(response.status).toBe(200);
  expect(await response.json()).toMatchObject({
    id: "systems:demo",
    slug: "demo",
  });
});
