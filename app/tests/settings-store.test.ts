import { expect, test } from "vitest";
import { GET, PATCH } from "@/app/api/settings/route";

// Runs the settings route against the real SQLite store in the temporary
// DESIGN_RESEARCH_DATA_DIR from setup.ts, which starts with no settings row.
function patch(body: unknown) {
  return PATCH(
    new Request("http://localhost:8845/api/settings", {
      method: "PATCH",
      headers: {
        "content-type": "application/json",
        host: "localhost:8845",
        origin: "http://localhost:8845",
      },
      body: JSON.stringify(body),
    }),
  );
}

test("settings saved on a fresh store read back, and a second save merges", async () => {
  const first = await patch({ provider: "anthropic", model: "test-model" });
  expect(first.status).toBe(200);
  expect(await first.json()).toMatchObject({
    provider: "anthropic",
    model: "test-model",
  });
  const read = await GET();
  expect(read.status).toBe(200);
  expect(await read.json()).toMatchObject({
    provider: "anthropic",
    model: "test-model",
  });
  const second = await patch({ model: "second-model" });
  expect(second.status).toBe(200);
  expect(await second.json()).toMatchObject({
    provider: "anthropic",
    model: "second-model",
  });
});
