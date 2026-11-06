import { beforeEach, expect, test, vi } from "vitest";

const mocks = vi.hoisted(() => ({
  list: vi.fn(),
  save: vi.fn(),
  remove: vi.fn(),
  media: vi.fn(),
}));
vi.mock("@/server/db", () => ({
  getStore: async () => ({
    listSavedMedia: mocks.list,
    saveMedia: mocks.save,
    removeSavedMedia: mocks.remove,
  }),
}));
vi.mock("@/server/sources", () => ({ getReferenceMedia: mocks.media }));

import { DELETE, GET, POST } from "@/app/api/saved-media/route";
import { jsonRequest } from "./helpers";

const body = { referenceId: "systems:demo", mediaId: "systems/demo/a.png" };
const send = (
  method: "POST" | "DELETE",
  payload: unknown = body,
  headers = {},
) => jsonRequest("/api/saved-media", method, payload, headers);

beforeEach(() => {
  vi.resetAllMocks();
  mocks.media.mockResolvedValue({
    reference: { name: "Demo" },
    media: [{ id: body.mediaId }],
  });
});

test("GET joins saved rows to reference names and media, keeping orphans", async () => {
  mocks.list.mockResolvedValue([
    { referenceId: "systems:demo", mediaId: body.mediaId },
    { referenceId: "systems:demo", mediaId: "systems/demo/gone.png" },
    { referenceId: "systems:ghost", mediaId: "x" },
  ]);
  mocks.media.mockImplementation(async (id: string) =>
    id === "systems:demo"
      ? { reference: { name: "Demo" }, media: [{ id: body.mediaId }] }
      : null,
  );
  const response = await GET();
  expect(response.status).toBe(200);
  const { items } = await response.json();
  expect(items.map((i: { name: string }) => i.name)).toEqual([
    "Demo",
    "Demo",
    "systems:ghost",
  ]);
  expect(items[0].media).toEqual({ id: body.mediaId });
  expect(items[1].media).toBeNull();
  expect(items[2].media).toBeNull();
  expect(mocks.media).toHaveBeenCalledTimes(2);
});

test("POST saves known media and returns saved: true", async () => {
  const response = await POST(send("POST"));
  expect(response.status).toBe(200);
  expect(await response.json()).toEqual({ saved: true });
  expect(mocks.save).toHaveBeenCalledWith(body.referenceId, body.mediaId);
});

test("POST refuses media the reference does not hold", async () => {
  const response = await POST(
    send("POST", { ...body, mediaId: "systems/demo/other.png" }),
  );
  expect(response.status).toBe(404);
  mocks.media.mockResolvedValue(null);
  expect((await POST(send("POST"))).status).toBe(404);
  expect(mocks.save).not.toHaveBeenCalled();
});

test("POST and DELETE validate the body", async () => {
  for (const payload of [
    {},
    { referenceId: "bad id!", mediaId: "x" },
    { ...body, extra: 1 },
    { ...body, mediaId: "" },
  ]) {
    expect((await POST(send("POST", payload))).status).toBe(400);
    expect((await DELETE(send("DELETE", payload))).status).toBe(400);
  }
  const malformed = new Request("http://localhost:8845/api/saved-media", {
    method: "POST",
    headers: {
      origin: "http://localhost:8845",
      "content-type": "application/json",
    },
    body: "{nope",
  });
  expect((await POST(malformed)).status).toBe(400);
  expect(mocks.save).not.toHaveBeenCalled();
  expect(mocks.remove).not.toHaveBeenCalled();
});

test("DELETE removes the selection and returns saved: false", async () => {
  const response = await DELETE(send("DELETE"));
  expect(response.status).toBe(200);
  expect(await response.json()).toEqual({ saved: false });
  expect(mocks.remove).toHaveBeenCalledWith(body.referenceId, body.mediaId);
});

test("mutations refuse a foreign origin, cross-site fetch and non-JSON POST", async () => {
  for (const call of [POST, DELETE]) {
    const method = call === POST ? "POST" : "DELETE";
    expect(
      (await call(send(method, body, { origin: "https://evil.example" })))
        .status,
    ).toBe(403);
    expect(
      (await call(send(method, body, { "sec-fetch-site": "cross-site" })))
        .status,
    ).toBe(403);
    expect(
      (await call(send(method, body, { host: "evil.example" }))).status,
    ).toBe(403);
  }
  expect(
    (await POST(send("POST", body, { "content-type": "text/plain" }))).status,
  ).toBe(415);
  expect(mocks.save).not.toHaveBeenCalled();
  expect(mocks.remove).not.toHaveBeenCalled();
});
