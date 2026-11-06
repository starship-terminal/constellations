import type { PrepareSendMessagesRequest, UIMessage } from "ai";

/** The server owns complete research history; send only the latest question. */
export const prepareResearchRequest: PrepareSendMessagesRequest<UIMessage> = ({
  id,
  messages,
  trigger,
  messageId,
  body,
}) => {
  const latestUser = messages.findLast((message) => message.role === "user");
  if (!latestUser) throw new Error("Write a research question before sending.");
  const parts = latestUser.parts
    .filter((part) => part.type === "text")
    .map((part) => ({ type: "text" as const, text: part.text }));
  const length = parts.reduce((sum, part) => sum + part.text.length, 0);
  if (!length) throw new Error("Write a research question before sending.");
  if (length > 30_000)
    throw new Error("Keep each research question under 30,000 characters.");
  return {
    body: {
      id,
      messages: [{ id: latestUser.id, role: "user", parts }],
      trigger,
      messageId,
      pinnedIds: body?.pinnedIds,
      excludedIds: body?.excludedIds,
    },
  };
};
