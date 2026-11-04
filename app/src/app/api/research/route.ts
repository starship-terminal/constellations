import { z } from "zod";
import type { UIMessage } from "ai";
import { getStore } from "@/server/db";
import {
  endpoint,
  mutationGuard,
  readBody,
  identifier,
  referenceIds,
  HttpError,
} from "@/server/research/http";
import { validateReferences } from "@/server/research/references";
import {
  readSettings,
  modelFor,
  supportsToolImages,
} from "@/server/research/settings";
import { streamResearch } from "@/server/research/agent";
export const runtime = "nodejs";
export const maxDuration = 150;
const inFlight = new Set<string>();
const userMessage = z
  .object({
    id: z.string().min(1).max(160),
    role: z.literal("user"),
    parts: z
      .array(
        z
          .object({ type: z.literal("text"), text: z.string().max(30000) })
          .strict(),
      )
      .min(1)
      .max(20),
  })
  .strict();
const bodySchema = z
  .object({
    id: identifier,
    messages: z.array(z.unknown()).min(1).max(300),
    pinnedIds: referenceIds.optional(),
    excludedIds: referenceIds.optional(),
    trigger: z.enum(["submit-message", "regenerate-message"]).optional(),
    messageId: z.string().optional(),
  })
  .strict();
export function POST(request: Request) {
  return endpoint(async () => {
    mutationGuard(request);
    const body = await readBody(request, bodySchema);
    const incoming = userMessage.parse(body.messages.at(-1));
    if (!incoming.parts.some((p) => p.text.trim()))
      throw new HttpError(400, "Write a research question.");
    if (inFlight.has(body.id))
      throw new HttpError(
        409,
        "This conversation already has a research response in progress.",
      );
    inFlight.add(body.id);
    try {
      const store = await getStore();
      let conversation = await store.getConversation(body.id);
      if (!conversation) throw new HttpError(404, "Conversation not found.");
      const pinnedIds = body.pinnedIds ?? conversation.pinnedIds,
        excludedIds = body.excludedIds ?? conversation.excludedIds;
      await validateReferences(pinnedIds, excludedIds);
      if (body.pinnedIds || body.excludedIds)
        await store.updateConversation(body.id, { pinnedIds, excludedIds });
      const duplicate = conversation.messages.findIndex(
        (m) => m.id === incoming.id,
      );
      if (duplicate >= 0 && conversation.messages[duplicate].role !== "user")
        throw new HttpError(409, "Message ID is already in use.");
      const regenerate =
        body.trigger === "regenerate-message" &&
        duplicate >= 0 &&
        conversation.messages
          .slice(duplicate + 1)
          .every((m) => m.role === "assistant");
      if (
        duplicate >= 0 &&
        duplicate !== conversation.messages.length - 1 &&
        !regenerate
      )
        throw new HttpError(
          409,
          "This question already has a response. Start a new question.",
        );
      const messages = regenerate
        ? conversation.messages.slice(0, duplicate + 1)
        : duplicate >= 0
          ? conversation.messages
          : [...conversation.messages, incoming as UIMessage];
      const settings = await readSettings();
      if (settings.configured || !regenerate)
        await store.saveMessages(body.id, messages);
      if (conversation.title === "New research")
        await store.updateConversation(body.id, {
          title: incoming.parts
            .map((p) => p.text)
            .join(" ")
            .slice(0, 100),
        });
      conversation = { ...conversation, messages, pinnedIds, excludedIds };
      if (!settings.configured)
        throw new HttpError(
          503,
          `Set ${settings.provider === "openai" ? "OPENAI_API_KEY" : "ANTHROPIC_API_KEY"} in the server environment, then retry. Your question is saved.`,
          "PROVIDER_NOT_CONFIGURED",
        );
      return await streamResearch({
        model: modelFor(settings),
        supportsImages: supportsToolImages(settings),
        conversation,
        store,
        signal: request.signal,
        onRelease: () => inFlight.delete(body.id),
      });
    } catch (error) {
      inFlight.delete(body.id);
      throw error;
    }
  });
}
