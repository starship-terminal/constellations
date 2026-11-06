import { ResearchPage } from "@/features/research";
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  return <ResearchPage id={id} />;
}
