import { expect, test } from "vitest";
import { getStore } from "@/server/db";
import { GET, POST } from "@/app/api/collections/route";
import {
  DELETE,
  GET as GET_ONE,
  PATCH,
} from "@/app/api/collections/[id]/route";
import { jsonRequest } from "./helpers";

const context = (id: string) => ({ params: Promise.resolve({ id }) });
const patch = (id: string, payload: unknown, headers = {}) =>
  PATCH(
    jsonRequest(`/api/collections/${id}`, "PATCH", payload, headers),
    context(id),
  );

test("POST creates a collection and validates the name", async () => {
  const created = await POST(
    jsonRequest("/api/collections", "POST", { name: "  Board A  " }),
  );
  expect(created.status).toBe(201);
  expect((await created.json()).name).toBe("Board A");
  for (const payload of [
    {},
    { name: "   " },
    { name: "x".repeat(161) },
    { name: "ok", extra: 1 },
  ]) {
    expect(
      (await POST(jsonRequest("/api/collections", "POST", payload))).status,
    ).toBe(400);
  }
  expect(
    (
      await POST(
        jsonRequest(
          "/api/collections",
          "POST",
          { name: "x" },
          { origin: "https://evil.example" },
        ),
      )
    ).status,
  ).toBe(403);
  const listed = await (await GET()).json();
  expect(listed.collections.map((c: { name: string }) => c.name)).toContain(
    "Board A",
  );
});

test("PATCH renames and sets notes, and rejects bad input", async () => {
  const board = await (await getStore()).createCollection("Before");
  const ok = await patch(board.id, { name: " After ", notes: "memo" });
  expect(ok.status).toBe(200);
  expect(await ok.json()).toMatchObject({ id: board.id, name: "After" });
  expect(
    (await (await getStore()).getCollection(board.id))!.collection.name,
  ).toBe("After");
  for (const payload of [
    { name: "" },
    { name: "x".repeat(161) },
    { notes: "n".repeat(50001) },
    { bogus: 1 },
    { name: 5 },
  ]) {
    expect(
      (await patch(board.id, payload)).status,
      JSON.stringify(payload).slice(0, 40),
    ).toBe(400);
  }
  expect(
    (await patch(board.id, { name: "x" }, { origin: "https://evil.example" }))
      .status,
  ).toBe(403);
  expect(
    (await (await getStore()).getCollection(board.id))!.collection.name,
  ).toBe("After");
});

test("an unknown collection is a 404 and a malformed id a 400", async () => {
  expect((await patch("missing", { name: "x" })).status).toBe(404);
  expect(
    (
      await GET_ONE(
        new Request("http://localhost/api/collections/missing"),
        context("missing"),
      )
    ).status,
  ).toBe(404);
  expect(
    (
      await DELETE(
        jsonRequest("/api/collections/missing", "DELETE"),
        context("missing"),
      )
    ).status,
  ).toBe(404);
  for (const id of ["../x", "-a", "a b"]) {
    expect((await patch(id, { name: "x" })).status, id).toBe(400);
    expect(
      (await DELETE(jsonRequest(`/api/collections/x`, "DELETE"), context(id)))
        .status,
      id,
    ).toBe(400);
  }
});

test("DELETE refuses a foreign origin and leaves the collection", async () => {
  const board = await (await getStore()).createCollection("Keep me");
  const response = await DELETE(
    jsonRequest(`/api/collections/${board.id}`, "DELETE", undefined, {
      origin: "https://evil.example",
    }),
    context(board.id),
  );
  expect(response.status).toBe(403);
  expect(await (await getStore()).getCollection(board.id)).not.toBeNull();
});
