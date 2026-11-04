import { DocsIndex } from "@/features/knowledge/docs";
export const dynamic = "force-dynamic";
export const metadata = { title: "Library docs" };
export default function Page() {
  return <DocsIndex />;
}
