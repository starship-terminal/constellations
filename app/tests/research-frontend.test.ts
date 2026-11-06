import { expect, test } from "vitest";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import ReactMarkdown from "react-markdown";
import { DefaultChatTransport, type UIMessage } from "ai";
import type { LibraryDetail } from "@/contracts/library";
import { prepareResearchRequest } from "@/features/research-transport";
import { MarkdownImageAsText } from "@/features/research-markdown";
import { ComparisonValues } from "@/components/reference";

const question: UIMessage = {
  id: "question-two",
  role: "user",
  parts: [{ type: "text", text: "Compare the spacing in these references." }],
};
const oversizedHistory: UIMessage[] = [
  {
    id: "question-one",
    role: "user",
    parts: [{ type: "text", text: "Find references" }],
  },
  {
    id: "inspection",
    role: "assistant",
    parts: [{ type: "text", text: "evidence".repeat(200_000) }],
  },
  question,
];

test("real SDK transport sends a bounded latest-user request despite oversized inspected history", async () => {
  expect(JSON.stringify(oversizedHistory).length).toBeGreaterThan(1_000_000);
  let payload: any;
  const transport = new DefaultChatTransport({
    api: "http://localhost/api/research",
    prepareSendMessagesRequest: prepareResearchRequest,
    fetch: async (_url, init) => {
      payload = JSON.parse(init?.body as string);
      return new Response("data: [DONE]\n\n", {
        headers: { "content-type": "text/event-stream" },
      });
    },
  });
  await transport.sendMessages({
    chatId: "conversation-one",
    trigger: "submit-message",
    messageId: undefined,
    messages: oversizedHistory,
    abortSignal: undefined,
    body: {
      pinnedIds: ["systems:linear"],
      excludedIds: ["refero:example"],
      unwantedHistory: "x".repeat(1_000_001),
    },
  });
  expect(payload.messages).toEqual([question]);
  expect(payload.id).toBe("conversation-one");
  expect(payload.trigger).toBe("submit-message");
  expect(payload.pinnedIds).toEqual(["systems:linear"]);
  expect(payload.excludedIds).toEqual(["refero:example"]);
  expect(payload).not.toHaveProperty("unwantedHistory");
  expect(JSON.stringify(payload).length).toBeLessThan(1_000);
});

test("regeneration keeps the latest user ID and text while omitting following assistant evidence", async () => {
  const response = await prepareResearchRequest({
    id: "conversation-one",
    messages: [
      ...oversizedHistory,
      {
        id: "last-answer",
        role: "assistant",
        parts: [{ type: "text", text: "partial" }],
      },
    ],
    trigger: "regenerate-message",
    messageId: "last-answer",
    api: "/api/research",
    body: { pinnedIds: ["systems:linear"] },
    headers: undefined,
    credentials: undefined,
    requestMetadata: undefined,
  });
  expect(response.body).toMatchObject({
    messages: [question],
    messageId: "last-answer",
    trigger: "regenerate-message",
  });
});

// User and assistant messages share one ReactMarkdown renderer with this img
// override (features/research.tsx Message), so one case covers both roles.
test("Markdown images render only alt text, never remote image requests", () => {
  for (const [source, text] of [
    [
      "A reference: ![A calm layout](https://external.example/track?secret=prompt)",
      "[Image: A calm layout]",
    ],
    ["![](https://external.example/track?secret=prompt)", "[Image omitted]"],
  ]) {
    const markup = renderToStaticMarkup(
      createElement(ReactMarkdown, {
        components: { img: MarkdownImageAsText },
        children: source,
      }),
    );
    expect(markup).toContain(text);
    expect(markup).not.toContain("<img");
    expect(markup).not.toContain("external.example");
    expect(markup).not.toContain("secret=prompt");
  }
});

test("comparison preserves each color, type and spacing value's evidence", () => {
  const detail = {
    colors: [
      { name: "Background", value: "#ffffff", evidence: "measured background" },
    ],
    typography: [{ name: "Body", value: "16px", evidence: "declared type" }],
    spacing: [{ name: "Gap", value: "24px", evidence: "inferred spacing" }],
  } as LibraryDetail;
  const markup = renderToStaticMarkup(
    createElement(ComparisonValues, { detail }),
  );
  for (const text of [
    "Background",
    "#ffffff",
    "measured background",
    "Body",
    "16px",
    "declared type",
    "Gap",
    "24px",
    "inferred spacing",
  ])
    expect(markup).toContain(text);
});
