import type { UIMessage } from "ai";
import type { LibraryDetail, LibraryItem, ReferenceMedia } from "./library";
export interface ConversationSummary {
  id: string;
  title: string;
  archived: boolean;
  createdAt: number;
  updatedAt: number;
}
export interface Conversation extends ConversationSummary {
  messages: UIMessage[];
  pinnedIds: string[];
  excludedIds: string[];
}
export interface Collection {
  id: string;
  name: string;
  notes: string;
  createdAt: number;
  updatedAt: number;
  mediaCount?: number;
  referenceCount?: number;
}
export interface CollectionMediaItem {
  id: string;
  collectionId: string;
  referenceId: string;
  mediaId: string;
  addedAt: number;
  reference: LibraryItem | null;
  name: string;
  media: ReferenceMedia | null;
}
export interface CollectionItem {
  referenceId: string;
  note: string;
  addedAt: number;
  reference: LibraryDetail | null;
}
export type CredentialSource = "stored" | "environment" | null;
export interface ProviderSettings {
  provider: "openai" | "anthropic";
  model: string;
  baseURL: string | null;
  configured: boolean;
  providers: { openai: boolean; anthropic: boolean };
  keySources: { openai: CredentialSource; anthropic: CredentialSource };
}
export interface ResearchCitation {
  id: string;
  title: string;
  url: string | null;
  evidence: "measured" | "interpreted";
  source: "systems" | "refero";
}
export interface SearchOutput {
  kind: "candidates";
  items: LibraryItem[];
  total: number;
}
export interface InspectOutput {
  kind: "inspected";
  /** "image-earlier" exists only in model history: the image went to the
   * model in an earlier turn and is not sent again. */
  visualEvidence?: "image-supplied" | "text-only" | "image-earlier";
  reference: LibraryDetail;
  citation: ResearchCitation;
}
