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
import {
  HISTORY_IMAGES,
  modelHistory,
  researchTools,
} from "@/server/research/agent";
import type { UIMessage } from "ai";

const execution = { toolCallId: "call", messages: [], context: {} };
const image = { data: new Uint8Array([1, 2, 3]), mediaType: "image/png" };
beforeEach(() => {
  vi.clearAllMocks();
  mocks.readReferenceImage.mockResolvedValue(image);
  mocks.readLocalImage.mockResolvedValue(image);
});

test("inspecting a reference reads its image once and stores a bounded reference", async () => {
  const tools = researchTools({ excludedIds: [] });
  const output = (await tools.inspectReference.execute!(
    { referenceId: "systems:test" },
    execution,
  )) as InspectOutput;
  const model = await tools.inspectReference.toModelOutput!({
    toolCallId: "call",
    input: { referenceId: "systems:test" },
    output,
  });
  expect(mocks.readReferenceImage).toHaveBeenCalledTimes(1);
  expect(JSON.stringify(model)).toContain('"data":"AQID"');
  expect(output.visualEvidence).toBe("image-supplied");
  // The stored output keeps the evidence the model reads again, not the
  // package README, exports or related styles.
  expect(output.reference).not.toHaveProperty("measured");
  expect(output.reference.colors).toHaveLength(100);
  expect(output.reference.exports).toEqual({});
  expect(output.reference.related).toEqual([]);
  expect(output.reference.name).toBe("Test");
  expect(JSON.stringify(output).length).toBeLessThan(20_000);
});

test("viewing media reads the file once across execute and model output", async () => {
  const tools = researchTools({ excludedIds: [] });
  const input = {
    referenceId: "systems:test",
    mediaId: "systems/test/screenshots/home.png",
  };
  const output = await tools.viewReferenceMedia.execute!(input, execution);
  if (!("media" in output)) throw new Error("Expected viewed media");
  const model = await tools.viewReferenceMedia.toModelOutput!({
    toolCallId: "call",
    input,
    output,
  });
  expect(mocks.readLocalImage).toHaveBeenCalledTimes(1);
  expect(JSON.stringify(model)).toContain('"type":"file"');
});

test("a text-only model never reads image files", async () => {
  const tools = researchTools({ excludedIds: [] }, false);
  const output = (await tools.inspectReference.execute!(
    { referenceId: "systems:test" },
    execution,
  )) as InspectOutput;
  expect(output.visualEvidence).toBe("text-only");
  expect(mocks.readReferenceImage).not.toHaveBeenCalled();
});

test("inspecting a reference and then viewing its screenshot reads the file once", async () => {
  // Behave like the real reader: pick the first image through the caller's read.
  mocks.readReferenceImage.mockImplementation(
    (reference: typeof mocks.reference, read: (url: string) => unknown) =>
      read(reference.media[0].url),
  );
  const tools = researchTools({ excludedIds: [] });
  const inspected = (await tools.inspectReference.execute!(
    { referenceId: "systems:test" },
    execution,
  )) as InspectOutput;
  const first = await tools.inspectReference.toModelOutput!({
    toolCallId: "call",
    input: { referenceId: "systems:test" },
    output: inspected,
  });
  const input = {
    referenceId: "systems:test",
    mediaId: "systems/test/screenshots/home.png",
  };
  const viewed = await tools.viewReferenceMedia.execute!(input, execution);
  if (!("media" in viewed)) throw new Error("Expected viewed media");
  const second = await tools.viewReferenceMedia.toModelOutput!({
    toolCallId: "call",
    input,
    output: viewed,
  });
  expect(mocks.readLocalImage).toHaveBeenCalledTimes(1);
  expect(JSON.stringify(first)).toContain('"data":"AQID"');
  expect(JSON.stringify(second)).toContain('"data":"AQID"');
});

test("only the most recent history images go back to the model", async () => {
  const inspected = (id: string) => ({
    type: "tool-inspectReference",
    toolCallId: id,
    state: "output-available",
    input: { referenceId: "systems:test" },
    output: { kind: "inspected", visualEvidence: "image-supplied" },
  });
  const messages = ["a", "b", "c"].map(
    (id) =>
      ({
        id,
        role: "assistant",
        parts: [inspected(id)],
      }) as unknown as UIMessage,
  );
  const evidence = modelHistory(messages, []).map(
    (message) =>
      (message.parts[0] as unknown as { output: { visualEvidence: string } })
        .output.visualEvidence,
  );
  expect(HISTORY_IMAGES).toBe(2);
  expect(evidence).toEqual([
    "image-earlier",
    "image-supplied",
    "image-supplied",
  ]);
  // The stored messages are not touched.
  expect(
    (messages[0].parts[0] as unknown as { output: { visualEvidence: string } })
      .output.visualEvidence,
  ).toBe("image-supplied");
  // An earlier image is described, not read and attached again.
  const tools = researchTools({ excludedIds: [] });
  const output = (await tools.inspectReference.execute!(
    { referenceId: "systems:test" },
    execution,
  )) as InspectOutput;
  vi.clearAllMocks();
  const model = await tools.inspectReference.toModelOutput!({
    toolCallId: "call",
    input: { referenceId: "systems:test" },
    output: { ...output, visualEvidence: "image-earlier" },
  });
  expect(mocks.readReferenceImage).not.toHaveBeenCalled();
  expect(JSON.stringify(model)).not.toContain('"type":"file"');
  expect(JSON.stringify(model)).toContain("earlier turn");
});
