import type { UIMessage } from "ai";
import type { LibraryDetail, LibraryItem } from "./library";
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
}
export interface CollectionItem {
  referenceId: string;
  note: string;
  addedAt: number;
  reference: LibraryDetail | null;
}
export interface ProviderSettings {
  provider: "openai" | "anthropic";
  model: string;
  baseURL: string | null;
  configured: boolean;
  providers: { openai: boolean; anthropic: boolean };
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
  visualEvidence?: "image-supplied" | "text-only";
  reference: LibraryDetail;
  citation: ResearchCitation;
}
