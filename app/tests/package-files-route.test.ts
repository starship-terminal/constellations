import { expect, test } from "vitest";
import { mkdir, symlink, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { GET } from "@/app/api/packages/[slug]/files/route";
import { repoFixture, tempDir } from "./helpers";

const SECRET = "TOP-SECRET-OUTSIDE";

// A repo with one package, plus files that must never come back: a sibling
// outside the package, one outside the repo, raw/ and dot paths, a symlink.
async function fixture() {
  const repo = await repoFixture();
  const outside = await tempDir("app-outside-");
  await writeFile(join(outside, "secret.md"), SECRET);
  await writeFile(
    join(repo, "catalog.json"),
    JSON.stringify({ systems: [{ slug: "demo" }, { slug: "other" }] }),
  );
  const pkg = join(repo, "systems/demo");
  await mkdir(join(pkg, "raw"), { recursive: true });
  await mkdir(join(pkg, ".hidden"), { recursive: true });
  await mkdir(join(repo, "systems/other"), { recursive: true });
  await writeFile(join(pkg, "README.md"), "# Demo");
  await writeFile(join(pkg, "raw/reading.json"), `{"s":"${SECRET}"}`);
  await writeFile(join(pkg, ".hidden/x.md"), SECRET);
  await writeFile(join(pkg, ".env.md"), SECRET);
  await writeFile(join(repo, "systems/other/README.md"), SECRET);
  await writeFile(join(repo, "secret.md"), SECRET);
  await symlink(join(outside, "secret.md"), join(pkg, "link.md"));
  return { repo, outside };
}

const call = (slug: string, path?: string) => {
  const url = new URL(
    `http://localhost/api/packages/${encodeURIComponent(slug)}/files`,
  );
  if (path !== undefined) url.searchParams.set("path", path);
  return GET(new Request(url), { params: Promise.resolve({ slug }) });
};
// The raw query string form, as a client that percent-encodes dots would send.
const callRaw = (slug: string, query: string) =>
  GET(new Request(`http://localhost/api/packages/${slug}/files?${query}`), {
    params: Promise.resolve({ slug }),
  });

test("lists a package's documents and reads one", async () => {
  await fixture();
  const list = await (await call("demo")).json();
  expect(list.documents.map((d: { path: string }) => d.path)).toEqual([
    "README.md",
  ]);
  const doc = await call("demo", "README.md");
  expect(doc.status).toBe(200);
  expect((await doc.json()).text).toBe("# Demo");
});

test("path traversal never leaves the package", async () => {
  const { outside } = await fixture();
  const attempts = [
    "../../secret.md",
    "../other/README.md",
    "../../../secret.md",
    "raw/../../other/README.md",
    "./../README.md",
    "..%2f..%2fsecret.md",
    `${outside}/secret.md`,
    "/etc/hosts.md",
    "..\\..\\secret.md",
    "README.md\0.txt",
  ];
  for (const path of attempts) {
    const response = await call("demo", path);
    expect(response.status, path).toBe(404);
    expect(await response.text(), path).not.toContain(SECRET);
  }
  for (const query of [
    "path=%2e%2e/%2e%2e/secret.md",
    "path=%2e%2e%2f%2e%2e%2fsecret.md",
    "path=%2E%2E%2F%2E%2E%2Fsecret.md",
    "path=%252e%252e%252fsecret.md",
  ]) {
    const response = await callRaw("demo", query);
    expect(response.status, query).toBe(404);
    expect(await response.text(), query).not.toContain(SECRET);
  }
});

test("raw/, dot paths and symlinks out of the package are refused", async () => {
  await fixture();
  for (const path of [
    "raw/reading.json",
    ".hidden/x.md",
    ".env.md",
    "link.md",
    "missing.md",
    "README.md/",
    "",
  ]) {
    const response = await call("demo", path);
    expect(response.status, path).toBe(404);
    expect(await response.text(), path).not.toContain(SECRET);
  }
  const list = await (await call("demo")).json();
  expect(JSON.stringify(list)).not.toContain("reading.json");
  expect(JSON.stringify(list)).not.toContain("link.md");
});

test("an unknown or malformed slug yields no documents and a 404", async () => {
  await fixture();
  for (const slug of [
    "nope",
    "..",
    "../other",
    "demo/../other",
    "%2e%2e",
    "demo\0",
    "",
  ]) {
    expect(await (await call(slug)).json(), slug).toEqual({ documents: [] });
    const response = await call(slug, "README.md");
    expect(response.status, slug).toBe(404);
    expect(await response.text(), slug).not.toContain(SECRET);
  }
});
