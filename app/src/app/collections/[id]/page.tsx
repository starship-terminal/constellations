import { CollectionDetailPage } from "@/features/collections";
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  return <CollectionDetailPage id={id} />;
}
