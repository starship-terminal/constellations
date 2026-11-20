import { beforeEach, expect, test, vi } from "vitest";
import type { InspectOutput } from "@/contracts/research";
const mocks = vi.hoisted(() => ({
  reference: {
    id: "systems:test",
    source: "systems",
    slug: "test",
    name: "Test",
    description: "A test package",
    platform: "web",
    themes: [],
    tags: [],
    category: "app",
    image: null,
    icon: null,
    video: null,
    evidence: "measured",
    captured: null,
    sourceUrl: null,
    media: [
      {
        id: "systems/test/screenshots/home.png",
        kind: "screenshot",
        name: "home",
        url: "/media/systems/test/screenshots/home.png",
        type: "image",
        group: "screenshots",
        tags: [],
      },
    ],
    colors: Array.from({ length: 500 }, (_, i) => ({
      name: `core.color.${i}`,
      value: "#000000",
    })),
    typography: [],
    spacing: [],
    radii: [],
    descriptionLong: "A recorded design",
    guidelines: [],
    exports: { "DESIGN.md": "/api/library/systems/test/export" },
    related: [{ id: "systems:other" }],
    measured: { readme: "x".repeat(200_000), documents: [] },
  },
  readReferenceImage: vi.fn(),
  readLocalImage: vi.fn(),
}));
vi.mock("@/server/sources", () => ({
  listLibrary: async () => [],
  getReference: async (id: string) =>
    id === "systems:test" ? mocks.reference : null,
  readReferenceImage: mocks.readReferenceImage,
}));
vi.mock("@/server/sources/files", () => ({
  readLocalImage: mocks.readLocalImage,
}));
vi.mock("@/server/research/evidence", () => ({
  allowedReference: async () => mocks.reference,
  packageDocuments: vi.fn(),
  packageDocument: vi.fn(),
  packageTokens: vi.fn(),
  handoffPrompt: vi.fn(),
}));
import { handleBatch, toolSpecs } from "@/server/mcp";

const image = { data: new Uint8Array([1, 2, 3]), mediaType: "image/png" };
beforeEach(() => {
  vi.clearAllMocks();
  mocks.readReferenceImage.mockImplementation(
    (reference: typeof mocks.reference, read: (url: string) => unknown) =>
      read(reference.media[0].url),
  );
  mocks.readLocalImage.mockResolvedValue(image);
});
async function call(name: string, args: Record<string, unknown>) {
  return (await handleBatch({
    jsonrpc: "2.0",
    id: 1,
    method: "tools/call",
    params: { name, arguments: args },
  })) as {
    result: { content: { type: string; data?: string; mimeType?: string }[] };
  };
}

test("an MCP media view reads its image once and returns it as an image block", async () => {
  const reply = await call("viewReferenceMedia", {
    referenceId: "systems:test",
    mediaId: "systems/test/screenshots/home.png",
  });
  expect(mocks.readLocalImage).toHaveBeenCalledTimes(1);
  expect(reply.result.content[1]).toEqual({
    type: "image",
    data: "AQID",
    mimeType: "image/png",
  });
});

test("an MCP inspect reads the reference image once and returns it", async () => {
  const reply = await call("inspectReference", { referenceId: "systems:test" });
  expect(mocks.readReferenceImage).toHaveBeenCalledTimes(1);
  expect(mocks.readLocalImage).toHaveBeenCalledTimes(1);
  expect(reply.result.content[1]).toMatchObject({
    type: "image",
    data: "AQID",
  });
});

test("a text-only result has no image block", async () => {
  mocks.readLocalImage.mockResolvedValue(null);
  const reply = await call("viewReferenceMedia", {
    referenceId: "systems:test",
    mediaId: "systems/test/screenshots/home.png",
  });
  expect(reply.result.content).toHaveLength(1);
});

test("tool schemas are built once and shared", async () => {
  expect(await toolSpecs()).toBe(await toolSpecs());
});
