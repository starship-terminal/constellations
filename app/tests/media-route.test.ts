import { afterEach, beforeEach, describe, expect, it } from "vitest";
import { promises as fs } from "node:fs";
import os from "node:os";
import path from "node:path";
import { GET, HEAD } from "@/app/media/[...path]/route";

const originalRepo = process.env.DESIGN_SYSTEMS_REPO;
let repo = "";
const PNG = Buffer.from(
  "89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c489",
  "hex",
);

async function write(rel: string, body: string | Buffer) {
  const file = path.join(repo, rel);
  await fs.mkdir(path.dirname(file), { recursive: true });
  await fs.writeFile(file, body);
}
function request(parts: string[], headers: Record<string, string> = {}) {
  return [
    new Request(`http://localhost/media/${parts.join("/")}`, { headers }),
    { params: Promise.resolve({ path: parts }) },
  ] as const;
}

beforeEach(async () => {
  repo = await fs.mkdtemp(path.join(os.tmpdir(), "design-media-route-"));
  process.env.DESIGN_SYSTEMS_REPO = repo;
  await write("catalog.json", JSON.stringify({ systems: [{ slug: "demo" }] }));
  await write("systems/demo/screenshots/home.png", PNG);
  await write("systems/demo/raw/full/home.png", PNG);
  await write("systems/demo/screenshots/.hidden/home.png", PNG);
  await write("systems/demo/.cache/home.png", PNG);
  await write("systems/demo/fonts/preview.png", PNG);
  await write(
    "systems/demo/screenshots/pointer.png",
    "version https://git-lfs.github.com/spec/v1\noid sha256:00\nsize 1\n",
  );
});
afterEach(async () => {
  if (originalRepo === undefined) delete process.env.DESIGN_SYSTEMS_REPO;
  else process.env.DESIGN_SYSTEMS_REPO = originalRepo;
  await fs.rm(repo, { recursive: true, force: true });
});

describe("/media route", () => {
  it("serves a package screenshot with validators", async () => {
    const response = await GET(
      ...request(["systems", "demo", "screenshots", "home.png"]),
    );
    expect(response.status).toBe(200);
    expect(response.headers.get("content-type")).toBe("image/png");
    expect(response.headers.get("content-length")).toBe(String(PNG.length));
    expect(Buffer.from(await response.arrayBuffer())).toEqual(PNG);
    const head = await HEAD(
      ...request(["systems", "demo", "screenshots", "home.png"]),
    );
    expect(head.status).toBe(200);
    expect(head.body).toBeNull();
  });
  it("answers ranges, unsatisfiable ranges and conditional requests", async () => {
    const parts = ["systems", "demo", "screenshots", "home.png"];
    const partial = await GET(...request(parts, { range: "bytes=0-3" }));
    expect(partial.status).toBe(206);
    expect(partial.headers.get("content-range")).toBe(
      `bytes 0-3/${PNG.length}`,
    );
    expect(Buffer.from(await partial.arrayBuffer())).toEqual(
      PNG.subarray(0, 4),
    );
    const outside = await GET(...request(parts, { range: "bytes=999-" }));
    expect(outside.status).toBe(416);
    expect(outside.headers.get("content-range")).toBe(`bytes */${PNG.length}`);
    const modified = (await GET(...request(parts))).headers.get(
      "last-modified",
    )!;
    const cached = await GET(
      ...request(parts, { "if-modified-since": modified }),
    );
    expect(cached.status).toBe(304);
  });
  it("refuses raw captures, private folders, dot segments, traversal and LFS pointers", async () => {
    for (const parts of [
      ["systems", "demo", "raw", "full", "home.png"],
      ["systems", "demo", "fonts", "preview.png"],
      ["systems", "demo", "screenshots", ".hidden", "home.png"],
      ["systems", "demo", ".cache", "home.png"],
      ["systems", "demo", "..", "demo", "screenshots", "home.png"],
      ["systems", "demo", "screenshots/..", "screenshots", "home.png"],
      ["systems", "demo", "screenshots", "pointer.png"],
      ["catalog.json"],
    ])
      expect((await GET(...request(parts))).status, parts.join("/")).toBe(404);
  });
});
