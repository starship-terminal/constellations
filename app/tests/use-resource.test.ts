import { describe, expect, it } from "vitest";
import { resourceView } from "@/components/shared";

describe("useResource state", () => {
  const settled = {
    url: "/api/conversations/a",
    data: { id: "a" },
    error: "",
    loading: false,
  };
  it("shows the response for the URL it was fetched for", () => {
    expect(resourceView(settled, "/api/conversations/a")).toEqual({
      data: { id: "a" },
      error: "",
      loading: false,
    });
  });
  it("never shows another URL's data or error after the URL changes", () => {
    expect(resourceView(settled, "/api/conversations/b")).toEqual({
      data: null,
      error: "",
      loading: true,
    });
    expect(
      resourceView(
        { ...settled, data: null, error: "Not found" },
        "/api/conversations/b",
      ),
    ).toEqual({ data: null, error: "", loading: true });
  });
});
